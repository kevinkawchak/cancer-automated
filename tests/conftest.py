"""Shared fixtures and helpers for the cancer-automated test suite.

Several source modules live in directories with hyphens (for example
``physical-ai/``) which cannot be imported with a normal ``import`` statement.
The ``load_module`` helper uses ``importlib.util`` to load any source file by
path. When a module depends on a package that is not installed (for example
anthropic, requests, pypdf, mujoco) the test is skipped rather than errored,
which keeps CI green when only core dependencies are available.

LICENSE: MIT
"""

from __future__ import annotations

import importlib.util
import random
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_module(name: str, relative_path: str):
    """Load a Python module by file path from the project root.

    Args:
        name: Module name to register in ``sys.modules``.
        relative_path: Path relative to the project root.

    Returns:
        The loaded module object, or skips the test if a dependency is missing.
    """
    if name in sys.modules:
        return sys.modules[name]

    filepath = PROJECT_ROOT / relative_path
    if not filepath.exists():
        pytest.skip(f"Source file not found: {relative_path}")

    spec = importlib.util.spec_from_file_location(name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except ImportError as exc:
        sys.modules.pop(name, None)
        pytest.skip(f"Module {name!r} requires a dependency not installed here: {exc}")
    return module


@pytest.fixture(autouse=True)
def _seed_rng():
    """Seed the standard-library RNG for deterministic tests."""
    random.seed(42)
    yield
