"""Example: chunk a document and generate its reconstruction README.

Run from the repository root:
    python chunking/examples-chunking/02_chunk_with_readme.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

CHUNK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CHUNK_DIR)

from chunker import Chunker  # noqa: E402
from readme_generator import generate_readme  # noqa: E402


def main() -> None:
    document = "".join(f"section {i}\n" for i in range(5000))
    chunks = Chunker(cap_bytes=20_000, stem="document").chunk_text(document)
    readme = generate_readme("big_document.md", chunks, extension=".md")
    print(readme)


if __name__ == "__main__":
    main()
