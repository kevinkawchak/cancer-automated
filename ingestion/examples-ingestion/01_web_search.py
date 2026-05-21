"""Example: robust web search with retry and offline fallback.

Run from the repository root:
    python ingestion/examples-ingestion/01_web_search.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

INGEST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, INGEST_DIR)

from web_search import WebSearchClient  # noqa: E402


def main() -> None:
    client = WebSearchClient(max_attempts=4, base_delay_s=0.0)
    response = client.search("physical AI oncology trial automation", max_results=3)
    print("query:", response.query)
    print("online:", response.online, "attempts:", response.attempts)
    for result in response.results:
        print(f"  - {result.title} ({result.source})")


if __name__ == "__main__":
    main()
