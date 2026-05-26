"""Unit tests for the VVUQ framework (verify, validate, quantify, gate).

LICENSE: MIT
"""

from __future__ import annotations

from src.vvuq.gate_registry import GATE_SLUGS, load_thresholds, nominal_accept_case
from src.vvuq.uncertainty import quantify
from src.vvuq.validation import validate
from src.vvuq.verification import verify
from src.vvuq.vvuq_gate import evaluate


def test_verify_all_pass():
    result = verify({"a": True, "b": True})
    assert result.fraction_passed == 1.0
    assert result.all_passed


def test_verify_one_fail():
    result = verify({"a": True, "b": False}, {"b": "missing artifact"})
    assert result.fraction_passed == 0.5
    assert not result.all_passed
    assert any("b" in f for f in result.failures())


def test_validate_perfect_agreement():
    ref = {"x": 0.05, "y": 45.0}
    result = validate(ref, ref, human_review=True)
    assert result.agreement == 1.0
    assert result.max_relative_error == 0.0


def test_validate_detects_disagreement():
    result = validate({"x": 0.10}, {"x": 0.05}, max_relative_error=0.05)
    assert result.agreement == 0.0
    assert result.max_relative_error > 0.05


def test_quantify_zero_cv_for_identical_runs():
    result = quantify([{"m": 45.0}, {"m": 45.0}, {"m": 45.0}])
    assert result.n_runs == 3
    assert result.max_cv == 0.0


def test_quantify_high_cv_for_divergent_runs():
    result = quantify([{"m": 45.0}, {"m": 63.0}, {"m": 27.0}])
    assert result.max_cv > 0.10


def test_evaluate_accepts_clean_case():
    thresholds = load_thresholds()
    case = nominal_accept_case("whole-body-balance")
    ver = verify(case["checks"])
    val = validate(case["observed"], case["reference"], max_relative_error=0.03, human_review=True)
    unc = quantify(case["runs"])
    decision = evaluate(
        "whole-body-balance", ver, val, unc, thresholds["whole-body-balance"], case["hard_checks"]
    )
    assert decision.decision == "ACCEPT"
    assert decision.accepted


def test_load_thresholds_merges_overrides():
    thresholds = load_thresholds()
    assert set(thresholds.keys()) == set(GATE_SLUGS)
    # vascular gate tightens validation and uncertainty relative to defaults.
    vasc = thresholds["vascular-no-fly-hand"]
    assert vasc["validation"]["min_agreement"] == 1.0
    assert vasc["validation"]["max_relative_error"] == 0.01
    assert vasc["uncertainty"]["max_coefficient_of_variation"] == 0.05
    # a non-overridden gate keeps the defaults.
    ff = thresholds["dexterous-finger-force"]
    assert ff["validation"]["min_agreement"] == 0.95
    assert ff["uncertainty"]["max_coefficient_of_variation"] == 0.10


def test_nominal_accept_case_shape():
    case = nominal_accept_case("vascular-no-fly-hand")
    assert case["observed"] == case["reference"]
    assert len(case["runs"]) == 3
    assert case["human_review"] is True
    assert case["hard_checks"]["hard_stop_violations_zero"] is True
