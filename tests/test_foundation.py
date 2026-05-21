"""Foundation tests: repository invariants and configuration integrity.

These tests use only the standard library so they pass on the minimal CI
install (pytest plus pyyaml).

LICENSE: MIT
"""

from __future__ import annotations

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CITATION.cff",
    "requirements.txt",
    "ruff.toml",
    ".github/workflows/ci.yml",
    "configs/pipeline_config.yaml",
    "configs/vvuq_thresholds.yaml",
    "scripts/verify_installation.py",
]


@pytest.mark.parametrize("relative", REQUIRED_FILES)
def test_required_file_exists(relative):
    assert (PROJECT_ROOT / relative).is_file(), f"missing required file: {relative}"


def test_pipeline_config_parses():
    yaml = pytest.importorskip("yaml")
    path = PROJECT_ROOT / "configs/pipeline_config.yaml"
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    assert config["project"] == "cancer-automated"
    stage_names = [stage["name"] for stage in config["stages"]]
    assert stage_names == ["instruction", "codegen", "execution", "paper"]
    assert config["automation"]["simulate_runs"] == 3
    assert config["chunking"]["per_file_cap_bytes"] == 200000


def test_vvuq_thresholds_parse():
    yaml = pytest.importorskip("yaml")
    path = PROJECT_ROOT / "configs/vvuq_thresholds.yaml"
    with path.open("r", encoding="utf-8") as handle:
        thresholds = yaml.safe_load(handle)
    assert thresholds["uncertainty"]["min_consensus_runs"] == 3
    assert thresholds["gate"]["block_on_any_failure"] is True


def test_verify_installation_importable():
    from conftest import load_module

    module = load_module("verify_installation", "scripts/verify_installation.py")
    assert hasattr(module, "main")
    assert module.CORE_PACKAGES == ["numpy", "yaml"]
