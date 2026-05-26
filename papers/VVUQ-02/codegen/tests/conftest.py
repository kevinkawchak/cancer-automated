"""Shared fixtures for the VVUQ-02 test suite.

Adds the codegen root to ``sys.path`` so ``from src.<pkg> import ...`` resolves
when pytest runs from this directory, and seeds the standard-library RNG for
deterministic tests.

LICENSE: MIT
"""

from __future__ import annotations

import random
import sys
from pathlib import Path

import pytest

CODEGEN_ROOT = Path(__file__).resolve().parent.parent
if str(CODEGEN_ROOT) not in sys.path:
    sys.path.insert(0, str(CODEGEN_ROOT))


@pytest.fixture(autouse=True)
def _seed_rng():
    """Seed the standard-library RNG for deterministic tests."""
    random.seed(20260525)
    yield
