"""Tests for the VVUQ framework and gate.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field

from conftest import load_module


@dataclass
class FakeArtifact:
    name: str
    content: str

    @property
    def size_bytes(self) -> int:
        return len(self.content.encode("utf-8"))


@dataclass
class FakeDeliverable:
    complete: bool = True
    artifacts: list = field(default_factory=list)

    def all_artifacts(self):
        return self.artifacts


def _good_deliverable():
    return FakeDeliverable(
        complete=True,
        artifacts=[FakeArtifact("instructions.md", "step\n"), FakeArtifact("paper.md", "# Title\n")],
    )


def test_verification_passes_for_good_deliverable():
    verification = load_module("verification", "vvuq/verification.py")
    result = verification.verify(_good_deliverable())
    assert result.all_passed
    assert result.fraction_passed == 1.0


def test_verification_flags_oversize_file():
    verification = load_module("verification", "vvuq/verification.py")
    big = FakeArtifact("big.txt", "x" * 5)
    deliverable = FakeDeliverable(complete=True, artifacts=[big])
    result = verification.verify(deliverable, per_file_cap_bytes=1)
    assert not result.all_passed
    assert any("within_file_cap" in failure for failure in result.failures())


def test_validation_perfect_agreement():
    validation = load_module("validation", "vvuq/validation.py")
    ref = {"a": 2.5, "b": 12.0}
    result = validation.validate(ref, ref, human_review=True)
    assert result.agreement == 1.0
    assert result.max_relative_error == 0.0


def test_validation_detects_disagreement():
    validation = load_module("validation", "vvuq/validation.py")
    result = validation.validate({"a": 3.0}, {"a": 2.5}, max_relative_error=0.05)
    assert result.agreement == 0.0
    assert result.max_relative_error > 0.05


def test_uncertainty_zero_cv_for_identical_runs():
    uncertainty = load_module("uncertainty", "vvuq/uncertainty.py")
    runs = [{"x": 2.5}, {"x": 2.5}, {"x": 2.5}]
    result = uncertainty.quantify(runs)
    assert result.n_runs == 3
    assert result.max_cv == 0.0


def test_gate_accepts_clean_deliverable():
    gate_mod = load_module("vvuq_gate", "vvuq/vvuq_gate.py")
    gate = gate_mod.VVUQGate()
    runs = [{"acceleration_factor": 2.5}, {"acceleration_factor": 2.5}, {"acceleration_factor": 2.5}]
    decision = gate.evaluate(
        _good_deliverable(),
        runs=runs,
        observed={"acceleration_factor": 2.5},
        reference={"acceleration_factor": 2.5},
        human_review=True,
    )
    assert decision.accepted
    assert decision.reasons == []


def test_gate_blocks_without_human_review():
    gate_mod = load_module("vvuq_gate", "vvuq/vvuq_gate.py")
    gate = gate_mod.VVUQGate()
    runs = [{"acceleration_factor": 2.5}, {"acceleration_factor": 2.5}, {"acceleration_factor": 2.5}]
    decision = gate.evaluate(
        _good_deliverable(),
        runs=runs,
        observed={"acceleration_factor": 2.5},
        reference={"acceleration_factor": 2.5},
        human_review=False,
    )
    assert decision.blocked
    assert any("human review" in reason for reason in decision.reasons)


def test_gate_blocks_and_escalates_on_divergence():
    gate_mod = load_module("vvuq_gate", "vvuq/vvuq_gate.py")
    gate = gate_mod.VVUQGate()
    runs = [{"acceleration_factor": 2.5}, {"acceleration_factor": 5.0}, {"acceleration_factor": 1.0}]
    decision = gate.evaluate(
        _good_deliverable(),
        runs=runs,
        observed={"acceleration_factor": 2.5},
        reference={"acceleration_factor": 2.5},
        human_review=True,
    )
    assert decision.blocked
    assert decision.escalate
