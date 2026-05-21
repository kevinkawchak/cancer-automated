"""Example: chunk a large document under the 200K cap.

Run from the repository root:
    python chunking/examples-chunking/01_chunk_document.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

CHUNK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CHUNK_DIR)

from chunker import Chunker  # noqa: E402


def main() -> None:
    # Build a document larger than a small demo cap.
    document = "".join(f"line {i}: physical AI oncology trial deliverable content\n" for i in range(2000))
    chunker = Chunker(cap_bytes=20_000, stem="document")
    chunks = chunker.chunk_text(document)
    print(f"document bytes: {len(document.encode('utf-8'))}")
    print(f"chunks: {len(chunks)} (cap {chunker.cap_bytes} bytes)")
    for chunk in chunks:
        print(f"  {chunk.name}: {chunk.size_bytes} bytes")


if __name__ == "__main__":
    main()
