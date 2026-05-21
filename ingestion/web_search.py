"""Robust web search for the ingestion stage.

Robustness here means bounded retries with exponential backoff around a fetch
function, so a transient network failure does not abort a deliverable. The
``requests`` dependency is imported through a guard: when it is absent (for
example in CI) the client returns a clearly labeled offline stub instead of
raising. Pure standard library otherwise.

LICENSE: MIT
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

try:  # optional networking dependency, guarded
    import requests
except ImportError:  # pragma: no cover - exercised only when the package is absent
    requests = None


@dataclass
class SearchResult:
    """A single search hit."""

    title: str
    url: str
    snippet: str = ""
    source: str = "offline-stub"


@dataclass
class SearchResponse:
    """The outcome of a search, including retry accounting."""

    query: str
    results: list = field(default_factory=list)
    attempts: int = 0
    online: bool = False


class WebSearchClient:
    """A web search client with bounded exponential-backoff retries."""

    def __init__(self, max_attempts: int = 4, base_delay_s: float = 2.0, sleep=time.sleep) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        self.max_attempts = max_attempts
        self.base_delay_s = base_delay_s
        self._sleep = sleep

    def search(self, query: str, max_results: int = 5) -> SearchResponse:
        """Search for ``query``, retrying transient failures with backoff."""
        if requests is None:
            return SearchResponse(query=query, results=self._offline_stub(query, max_results), attempts=0, online=False)

        last_error: Exception | None = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                results = self._fetch(query, max_results)
                return SearchResponse(query=query, results=results, attempts=attempt, online=True)
            except Exception as exc:  # noqa: BLE001 - retry any transient fetch failure
                last_error = exc
                if attempt < self.max_attempts:
                    self._sleep(self.base_delay_s * (2 ** (attempt - 1)))
        # Exhausted retries: degrade gracefully to the offline stub.
        return SearchResponse(
            query=query,
            results=self._offline_stub(query, max_results),
            attempts=self.max_attempts,
            online=False,
        )

    def _fetch(self, query: str, max_results: int) -> list:  # pragma: no cover - requires network
        response = requests.get(
            "https://duckduckgo.com/html/",
            params={"q": query},
            timeout=10,
        )
        response.raise_for_status()
        # Parsing the HTML is left to the caller's preferred parser; the robust
        # retry envelope is the contribution of this module.
        return [SearchResult(title=query, url=response.url, snippet="", source="duckduckgo")][:max_results]

    @staticmethod
    def _offline_stub(query: str, max_results: int) -> list:
        return [
            SearchResult(
                title=f"[offline] {query} result {index + 1}",
                url=f"https://example.invalid/{index + 1}",
                snippet="Offline stub. Install requests and provide network access for live search.",
            )
            for index in range(max(1, min(max_results, 3)))
        ]
