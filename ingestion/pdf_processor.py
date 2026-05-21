"""Robust PDF processing for the ingestion stage.

The processor extracts text from a PDF when ``pypdf`` is available, and otherwise
reports a clear, non-fatal status. It also exposes a chunk-count estimate so the
ingestion stage can hand oversized documents to the chunking module (200K cap).
The ``pypdf`` dependency is imported through a guard.

LICENSE: MIT
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass, field

try:  # optional PDF dependency, guarded
    import pypdf
except ImportError:  # pragma: no cover - exercised only when the package is absent
    pypdf = None

DEFAULT_CHUNK_CAP_BYTES = 200_000


@dataclass
class PDFExtract:
    """The outcome of a PDF extraction."""

    path: str
    text: str = ""
    pages: int = 0
    ok: bool = False
    status: str = ""
    chunks_needed: int = 1


class PDFProcessor:
    """Extract text from PDFs with a guarded optional backend."""

    def __init__(self, chunk_cap_bytes: int = DEFAULT_CHUNK_CAP_BYTES) -> None:
        self.chunk_cap_bytes = chunk_cap_bytes

    def extract(self, path: str) -> PDFExtract:
        """Extract text from ``path``, degrading gracefully when unavailable."""
        if not os.path.exists(path):
            return PDFExtract(path=path, ok=False, status="file not found")
        if pypdf is None:
            return PDFExtract(path=path, ok=False, status="pypdf not installed; install to extract text")

        try:  # pragma: no cover - requires pypdf and a real PDF
            reader = pypdf.PdfReader(path)
            text = "\n".join((page.extract_text() or "") for page in reader.pages)
            return PDFExtract(
                path=path,
                text=text,
                pages=len(reader.pages),
                ok=True,
                status="extracted",
                chunks_needed=self.chunks_needed(text),
            )
        except Exception as exc:  # noqa: BLE001 - report any extraction failure, do not abort
            return PDFExtract(path=path, ok=False, status=f"extraction failed: {exc}")

    def chunks_needed(self, text: str) -> int:
        """Number of 200K chunks required to hold ``text``."""
        size = len(text.encode("utf-8"))
        if size == 0:
            return 1
        return max(1, math.ceil(size / self.chunk_cap_bytes))
