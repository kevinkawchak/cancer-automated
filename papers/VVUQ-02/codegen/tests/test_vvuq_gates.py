"""Decision-surface tests for all 10 VVUQ gates.

For every gate this exercises one ACCEPT case and several distinct BLOCK and
ESCALATE cases, mirroring the VVUQ-01 six-case decision surface. With 10 gates
the parametrized scenarios produce well over 60 gate-level test items, so the
suite is comparable in coverage to the VVUQ-01 gate tests.

LICENSE: MIT
"""

from __future__ import annotations

import copy

import pytest

from src.vvuq.gate_registry import (
    GATE_SLUGS,
    GATES,
    load_thresholds,
    nominal_accept_case,
    run_gate,
)

THRESHOLDS = load_thresholds()
HARD_CHECK_GATES = [slug for slug in GATE_SLUGS if GATES[slug].hard_checks]


def _disagree(ref: dict) -> dict:
    """Push every observed metric far outside any per-gate tolerance."""
    return {k: v + (abs(v) if v != 0 else 1.0) + 1.0 for k, v in ref.items()}


def _divergent_runs(ref: dict) -> list[dict]:
    """Three runs whose nonzero metrics diverge well above any CV bound."""
    return [dict(ref), {k: v * 1.4 for k, v in ref.items()}, {k: v * 0.6 for k, v in ref.items()}]


@pytest.mark.parametrize("slug", GATE_SLUGS)
def test_gate_accepts_nominal_case(slug):
    decision = run_gate(slug, nominal_accept_case(slug), THRESHOLDS)
    assert decision.decision == "ACCEPT", f"{slug}: {decision.reasons}"
    assert decision.accepted


@pytest.mark.parametrize("slug", GATE_SLUGS)
def test_gate_blocks_on_verification_failure(slug):
    case = copy.deepcopy(nominal_accept_case(slug))
    first_check = next(iter(case["checks"]))
    case["checks"][first_check] = False
    decision = run_gate(slug, case, THRESHOLDS)
    assert decision.blocked
    assert any("verification" in r for r in decision.reasons)


@pytest.mark.parametrize("slug", GATE_SLUGS)
def test_gate_blocks_on_validation_disagreement(slug):
    case = copy.deepcopy(nominal_accept_case(slug))
    case["observed"] = _disagree(case["reference"])
    decision = run_gate(slug, case, THRESHOLDS)
    assert decision.blocked
    assert any("agreement" in r or "relative error" in r for r in decision.reasons)


@pytest.mark.parametrize("slug", GATE_SLUGS)
def test_gate_blocks_on_missing_human_review(slug):
    case = copy.deepcopy(nominal_accept_case(slug))
    case["human_review"] = False
    decision = run_gate(slug, case, THRESHOLDS)
    assert decision.blocked
    assert any("human review" in r for r in decision.reasons)


@pytest.mark.parametrize("slug", GATE_SLUGS)
def test_gate_blocks_on_insufficient_runs(slug):
    case = copy.deepcopy(nominal_accept_case(slug))
    case["runs"] = [dict(case["reference"])]
    decision = run_gate(slug, case, THRESHOLDS)
    assert decision.blocked
    assert any("runs" in r for r in decision.reasons)


@pytest.mark.parametrize("slug", GATE_SLUGS)
def test_gate_escalates_on_uncertainty_divergence(slug):
    case = copy.deepcopy(nominal_accept_case(slug))
    case["runs"] = _divergent_runs(case["reference"])
    decision = run_gate(slug, case, THRESHOLDS)
    assert decision.escalate
    assert decision.decision == "ESCALATE"
    assert any("cv" in r for r in decision.reasons)


@pytest.mark.parametrize("slug", HARD_CHECK_GATES)
def test_immediate_catastrophe_gate_blocks_on_hard_check(slug):
    case = copy.deepcopy(nominal_accept_case(slug))
    hard_name = next(iter(case["hard_checks"]))
    case["hard_checks"][hard_name] = False
    decision = run_gate(slug, case, THRESHOLDS)
    assert decision.blocked
    assert any("hard check" in r for r in decision.reasons)


def test_all_ten_gates_present():
    assert len(GATE_SLUGS) == 10
    assert len(HARD_CHECK_GATES) == 3
