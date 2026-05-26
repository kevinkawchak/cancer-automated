"""Tests for the Zenodo L0 pointer patcher.

LICENSE: MIT
"""

from __future__ import annotations

import json

from src.zenodo.patch_pointers import sha256_file, write_manifest, write_pointer


def test_sha256_file(tmp_path):
    f = tmp_path / "x.bin"
    f.write_bytes(b"abc")
    digest = sha256_file(f)
    assert digest == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def test_write_pointer_missing_file_uses_zero_sha(tmp_path):
    pointer_path = write_pointer(3, tmp_path / "absent.parquet", tmp_path)
    data = json.loads(pointer_path.read_text(encoding="utf-8"))
    assert data["iteration_id"] == 3
    assert data["file_sha256"] == "0" * 64
    assert data["file_size_bytes"] == 0
    assert pointer_path.name == "run_00003_L0_raw.zenodo_pointer.json"


def test_write_pointer_real_file(tmp_path):
    raw = tmp_path / "run_00000_L0_raw.parquet"
    raw.write_bytes(b"raw-l0-data")
    pointer_path = write_pointer(0, raw, tmp_path)
    data = json.loads(pointer_path.read_text(encoding="utf-8"))
    assert data["file_size_bytes"] == len(b"raw-l0-data")
    assert data["file_sha256"] != "0" * 64


def test_write_manifest(tmp_path):
    p0 = write_pointer(0, tmp_path / "a.parquet", tmp_path)
    p1 = write_pointer(1, tmp_path / "b.parquet", tmp_path)
    manifest_path = tmp_path / "manifest.json"
    write_manifest("v0.1.0", "2026-05-26", [p0, p1], manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["release_version"] == "v0.1.0"
    assert len(manifest["iterations"]) == 2
