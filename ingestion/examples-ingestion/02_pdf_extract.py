"""Example: report PDF extraction status and the 200K chunk estimate.

Run from the repository root:
    python ingestion/examples-ingestion/02_pdf_extract.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

INGEST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, INGEST_DIR)

from pdf_processor import PDFProcessor  # noqa: E402


def main() -> None:
    processor = PDFProcessor()
    extract = processor.extract("nonexistent_reference.pdf")
    print("path:", extract.path)
    print("ok:", extract.ok)
    print("status:", extract.status)

    # The chunk estimate works on any text, independent of the PDF backend.
    sample = "x" * 450_000
    print("chunks needed for a 450K document:", processor.chunks_needed(sample))


if __name__ == "__main__":
    main()
