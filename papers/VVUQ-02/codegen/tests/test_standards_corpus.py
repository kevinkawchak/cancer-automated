"""Tests that the real standards input corpus is wired into the gate registry.

The corpus is loaded from papers/VVUQ-02/inputs/standards/manifest.yaml via
PyYAML. The harness degrades gracefully when PyYAML is absent (the corpus loader
returns an empty mapping and gate standards fall back to their keys), so these
tests skip rather than fail when PyYAML or the manifest are unavailable, matching
the VVUQ-01 dependency-skip pattern.

LICENSE: MIT
"""

from __future__ import annotations

import pytest

from src.vvuq.gate_registry import (
    GATE_SLUGS,
    GATES,
    gate_standards,
    load_standards_corpus,
)

_CORPUS = load_standards_corpus()
pytestmark = pytest.mark.skipif(
    not _CORPUS, reason="PyYAML or the standards manifest is unavailable"
)


def test_corpus_loads():
    assert _CORPUS["ASME_V_and_V_40_2018"] == "ASME V&V 40-2018"
    assert _CORPUS["IEC_80601_2_77_2019"] == "IEC 80601-2-77:2019"


def test_every_gate_standard_resolves_in_corpus():
    known = set(_CORPUS.keys()) | {"Fistula_Risk_Score"}
    for slug in GATE_SLUGS:
        for key in GATES[slug].standards:
            assert key in known, f"{slug} references unknown standard key {key}"


def test_gate_standards_returns_designations():
    designations = gate_standards("vascular-no-fly-hand", _CORPUS)
    assert "IEC 80601-2-77:2019" in designations
    assert "ISO 14971:2019" in designations
