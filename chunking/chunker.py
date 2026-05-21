"""Autochunk code and documents under the 200K per-file cap.

The chunker splits text on line boundaries so that every chunk stays at or under
the configured byte cap (200K by default). A single line longer than the cap is
hard-split by bytes. The chunker pairs with ``readme_generator`` to emit a
reconstruction README alongside the chunks. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field

DEFAULT_CAP_BYTES = 200_000


@dataclass
class Chunk:
    """A single chunk of a larger file."""

    index: int
    name: str
    content: str

    @property
    def size_bytes(self) -> int:
        return len(self.content.encode("utf-8"))


def _byte_len(text: str) -> int:
    return len(text.encode("utf-8"))


def _hard_split_line(line: str, cap_bytes: int) -> list[str]:
    """Split a single oversized line into byte-bounded pieces."""
    encoded = line.encode("utf-8")
    pieces: list[str] = []
    start = 0
    while start < len(encoded):
        end = start + cap_bytes
        # Step back to avoid splitting a multi-byte character.
        piece = encoded[start:end]
        while piece and (piece[-1] & 0xC0) == 0x80 and len(piece) > 1:
            end -= 1
            piece = encoded[start:end]
        pieces.append(piece.decode("utf-8", errors="ignore"))
        start = end
    return pieces


class Chunker:
    """Split text into chunks that each stay within the byte cap."""

    def __init__(self, cap_bytes: int = DEFAULT_CAP_BYTES, stem: str = "chunk") -> None:
        if cap_bytes < 1:
            raise ValueError("cap_bytes must be positive")
        self.cap_bytes = cap_bytes
        self.stem = stem

    def chunk_text(self, text: str) -> list[Chunk]:
        """Chunk ``text`` on line boundaries within the byte cap."""
        if _byte_len(text) <= self.cap_bytes:
            return [Chunk(index=0, name=self._name(0), content=text)]

        chunks: list[Chunk] = []
        current: list[str] = []
        current_bytes = 0

        def flush() -> None:
            nonlocal current, current_bytes
            if current:
                chunks.append(Chunk(index=len(chunks), name=self._name(len(chunks)), content="".join(current)))
                current = []
                current_bytes = 0

        for raw_line in text.splitlines(keepends=True):
            for line in self._fit_line(raw_line):
                line_bytes = _byte_len(line)
                if current_bytes + line_bytes > self.cap_bytes and current:
                    flush()
                current.append(line)
                current_bytes += line_bytes
        flush()
        return chunks

    def _fit_line(self, line: str) -> list[str]:
        if _byte_len(line) <= self.cap_bytes:
            return [line]
        return _hard_split_line(line, self.cap_bytes)

    def _name(self, index: int) -> str:
        return f"{self.stem}_{index + 1:03d}"
