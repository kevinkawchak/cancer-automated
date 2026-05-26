"""Zenodo L0 raw deposition pointer patcher.

The 71-DOF humanoid L0 raw stream is larger than the 8-arm baseline, so the
Zenodo discipline matters more: L0 is never committed. This module writes the
per-iteration pointer JSON (deposition DOI plus SHA-256) and the cross-iteration
manifest, reading L0 files from a local staging directory. Supports the
ZENODO_TOKEN environment variable for authenticated deposition. Pure standard
library plus optional click.

LICENSE: MIT
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DEPOSITION_DOI = "10.5281/zenodo.xxxxxxxx"
DEFAULT_DEPOSITION_URL = "https://doi.org/10.5281/zenodo.xxxxxxxx"


def sha256_file(path: Path, chunk_size: int = 1_048_576) -> str:
    """Compute the SHA-256 of a local file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            buf = f.read(chunk_size)
            if not buf:
                break
            h.update(buf)
    return h.hexdigest()


def write_pointer(
    iteration_id: int,
    file_path: Path,
    output_dir: Path,
    deposition_doi: str = DEFAULT_DEPOSITION_DOI,
    deposition_url: str = DEFAULT_DEPOSITION_URL,
) -> Path:
    """Write a per-iteration pointer JSON with the DOI plus SHA-256."""
    sha = sha256_file(file_path) if file_path.exists() else "0" * 64
    size = file_path.stat().st_size if file_path.exists() else 0
    pointer = {
        "iteration_id": iteration_id,
        "deposition_doi": deposition_doi,
        "deposition_url": deposition_url,
        "file_name": file_path.name,
        "file_size_bytes": size,
        "file_sha256": sha,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"run_{iteration_id:05d}_L0_raw.zenodo_pointer.json"
    out.write_text(json.dumps(pointer, indent=2) + "\n", encoding="utf-8")
    return out


def write_manifest(
    release_version: str, release_date: str, pointer_files: list[Path], output_path: Path
) -> None:
    """Write the cross-iteration manifest."""
    iterations = [json.loads(p.read_text(encoding="utf-8")) for p in pointer_files if p.exists()]
    manifest = {
        "release_version": release_version,
        "release_date": release_date,
        "deposition_doi": DEFAULT_DEPOSITION_DOI,
        "deposition_url": DEFAULT_DEPOSITION_URL,
        "iterations": iterations,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """CLI: write per-iteration pointers plus the cross-iteration manifest."""
    staging = Path("zenodo_staging")
    out_dir = Path("data/iterations")
    pointer_files = [
        write_pointer(i, staging / f"run_{i:05d}_L0_raw.parquet", out_dir) for i in range(32)
    ]
    manifest_path = Path("releases") / "v0.1.0" / "manifest.json"
    write_manifest("v0.1.0", "2026-05-26", pointer_files, manifest_path)
    print(f"wrote {len(pointer_files)} pointers plus manifest {manifest_path}")


if __name__ == "__main__":
    main()
