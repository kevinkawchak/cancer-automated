"""Tests for the composite score and the 10-gate gating overlay.

LICENSE: MIT
"""

from __future__ import annotations

import math

from src.metrics.compute import WEIGHTS, composite_score, gated_composite

_COMPONENTS = {
    "quality": 95.0,
    "time": 100.0,
    "cost": 80.0,
    "safety": 96.0,
    "patient_experience": 92.0,
    "anastomosis_quality": 95.0,
}


def test_weights_sum_to_one():
    assert math.isclose(sum(WEIGHTS.values()), 1.0, abs_tol=1e-9)


def test_composite_score_value():
    assert composite_score(_COMPONENTS) == 93.75


def test_gated_composite_reports_when_all_accept():
    rollup = dict.fromkeys(
        [f"gate_{i}" for i in range(10)],
        "ACCEPT",
    )
    result = gated_composite(_COMPONENTS, rollup)
    assert result.gates_all_accepted
    assert result.composite_reported
    assert result.composite_score == 93.75


def test_gated_composite_withholds_on_block():
    rollup = {"gate_0": "ACCEPT", "gate_1": "BLOCK"}
    result = gated_composite(_COMPONENTS, rollup)
    assert not result.gates_all_accepted
    assert not result.composite_reported
    assert result.composite_score is None


def test_gated_composite_withholds_on_escalate():
    rollup = {"gate_0": "ACCEPT", "gate_1": "ESCALATE"}
    result = gated_composite(_COMPONENTS, rollup)
    assert result.composite_score is None
