"""Tests for autochunking and reconstruction READMEs.

LICENSE: MIT
"""

from __future__ import annotations

from conftest import load_module


def test_small_text_is_a_single_chunk():
    chunker_mod = load_module("chunker", "chunking/chunker.py")
    chunks = chunker_mod.Chunker(cap_bytes=200_000).chunk_text("short content\n")
    assert len(chunks) == 1


def test_large_text_splits_within_cap_and_reconstructs():
    chunker_mod = load_module("chunker", "chunking/chunker.py")
    text = "".join(f"line {i}\n" for i in range(10_000))
    chunker = chunker_mod.Chunker(cap_bytes=5_000, stem="part")
    chunks = chunker.chunk_text(text)
    assert len(chunks) > 1
    assert all(chunk.size_bytes <= 5_000 for chunk in chunks)
    assert "".join(chunk.content for chunk in chunks) == text


def test_oversized_single_line_is_hard_split():
    chunker_mod = load_module("chunker", "chunking/chunker.py")
    text = "x" * 12_000
    chunks = chunker_mod.Chunker(cap_bytes=5_000).chunk_text(text)
    assert len(chunks) >= 3
    assert all(chunk.size_bytes <= 5_000 for chunk in chunks)
    assert "".join(chunk.content for chunk in chunks) == text


def test_readme_generator_lists_chunks_and_cat_command():
    chunker_mod = load_module("chunker", "chunking/chunker.py")
    readme_mod = load_module("readme_generator", "chunking/readme_generator.py")
    text = "".join(f"row {i}\n" for i in range(4_000))
    chunks = chunker_mod.Chunker(cap_bytes=5_000, stem="part").chunk_text(text)
    readme = readme_mod.generate_readme("big.md", chunks, extension=".md")
    assert "cat " in readme
    assert "> big.md" in readme
    assert f"{len(chunks)} pieces" in readme
