#!/usr/bin/env python3
"""Verify the cancer-automated environment.

Reports which core and optional dependencies are available and confirms that
the pipeline configuration files are present and parseable. Heavy and optional
packages are probed through try/except so this script runs on a bare Python
install and never fails the lint-and-format or test CI jobs.

Usage:
    python scripts/verify_installation.py

LICENSE: MIT
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

CORE_PACKAGES = ["numpy", "yaml"]

OPTIONAL_PACKAGES = [
    "anthropic",
    "openai",
    "mcp",
    "requests",
    "pypdf",
    "bs4",
    "mujoco",
    "tqdm",
]

CONFIG_FILES = [
    "configs/pipeline_config.yaml",
    "configs/vvuq_thresholds.yaml",
]


def is_available(module_name: str) -> bool:
    """Return True when a module can be located without importing it."""
    try:
        return importlib.util.find_spec(module_name) is not None
    except (ImportError, ValueError):
        return False


def check_packages(title: str, names: list[str]) -> int:
    """Print availability for a list of packages and return the count present."""
    print(title)
    present = 0
    for name in names:
        available = is_available(name)
        marker = "ok" if available else "--"
        status = "available" if available else "not installed"
        print(f"  [{marker}] {name}: {status}")
        present += int(available)
    return present


def check_configs() -> int:
    """Confirm the pipeline configuration files exist and parse cleanly."""
    print("Configuration files")
    present = 0
    yaml_spec = is_available("yaml")
    for relative in CONFIG_FILES:
        path = REPO_ROOT / relative
        if not path.exists():
            print(f"  [--] {relative}: missing")
            continue
        if yaml_spec:
            import yaml

            try:
                with path.open("r", encoding="utf-8") as handle:
                    yaml.safe_load(handle)
                print(f"  [ok] {relative}: present and parseable")
                present += 1
            except yaml.YAMLError as exc:
                print(f"  [--] {relative}: parse error: {exc}")
        else:
            print(f"  [ok] {relative}: present (install pyyaml to validate parsing)")
            present += 1
    return present


def main() -> None:
    print("=" * 64)
    print("cancer-automated environment verification")
    print("=" * 64)

    core_present = check_packages("Core packages", CORE_PACKAGES)
    print()
    optional_present = check_packages("Optional packages (guarded at import)", OPTIONAL_PACKAGES)
    print()
    configs_present = check_configs()
    print()

    print("Summary")
    print(f"  core packages present:     {core_present}/{len(CORE_PACKAGES)}")
    print(f"  optional packages present: {optional_present}/{len(OPTIONAL_PACKAGES)}")
    print(f"  config files present:      {configs_present}/{len(CONFIG_FILES)}")
    print()
    if core_present < len(CORE_PACKAGES):
        print("Install core dependencies with: pip install -r requirements.txt")
    else:
        print("Core environment is ready.")


if __name__ == "__main__":
    main()
