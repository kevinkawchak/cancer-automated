"""The VVUQ gate: composes the three dimensions into one decision.

Mirrors the VVUQ-01 control flow: block on any dimension failure; set escalate
when the maximum coefficient of variation exceeds the bound (divergence). Adds
per-gate hard predicates (for example hard_stop_violations == 0 for the vascular
gate) that must also pass. The decision is ACCEPT, BLOCK, or ESCALATE. Any
ESCALATE defaults the autonomy and fault paths to hand-back-to-human (UL 4600,
IEEE 7009). Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.vvuq.uncertainty import UncertaintyResult
from src.vvuq.validation import ValidationResult
from src.vvuq.verification import VerificationResult


@dataclass
class GateDecision:
    """The gate verdict for one candidate behavior."""

    gate_slug: str
    accepted: bool
    escalate: bool
    reasons: list[str] = field(default_factory=list)
    scores: dict = field(default_factory=dict)

    @property
    def blocked(self) -> bool:
        return not self.accepted

    @property
    def decision(self) -> str:
        if self.accepted:
            return "ACCEPT"
        return "ESCALATE" if self.escalate else "BLOCK"


def evaluate(
    gate_slug: str,
    verification: VerificationResult,
    validation: ValidationResult,
    uncertainty: UncertaintyResult,
    thresholds: dict,
    hard_checks: dict[str, bool] | None = None,
) -> GateDecision:
    """Combine the three dimensions and the hard predicates into a decision."""
    ver_t = thresholds["verification"]
    val_t = thresholds["validation"]
    unc_t = thresholds["uncertainty"]
    gate_t = thresholds.get("gate", {})
    hard_checks = hard_checks or {}

    reasons: list[str] = []

    if verification.fraction_passed < ver_t["min_checks_passed_fraction"]:
        reasons.append(
            f"verification fraction {verification.fraction_passed:.2f} below "
            f"{ver_t['min_checks_passed_fraction']}: {verification.failures()}"
        )
    if validation.agreement < val_t["min_agreement"]:
        reasons.append(
            f"validation agreement {validation.agreement:.2f} below {val_t['min_agreement']}"
        )
    if validation.max_relative_error > val_t["max_relative_error"]:
        reasons.append(
            f"max relative error {validation.max_relative_error:.3f} above {val_t['max_relative_error']}"
        )
    if val_t.get("require_human_review", False) and not validation.human_review:
        reasons.append("human review not recorded")
    if uncertainty.n_runs < unc_t["min_consensus_runs"]:
        reasons.append(f"only {uncertainty.n_runs} runs, need {unc_t['min_consensus_runs']}")

    diverged = uncertainty.max_cv > unc_t["max_coefficient_of_variation"]
    if diverged:
        reasons.append(
            f"max cv {uncertainty.max_cv:.3f} above {unc_t['max_coefficient_of_variation']}"
        )

    for name, passed in hard_checks.items():
        if not passed:
            reasons.append(f"hard check failed: {name}")

    escalate = diverged and gate_t.get("escalate_on_divergence", True)
    accepted = len(reasons) == 0
    scores = {
        "verification_fraction": round(verification.fraction_passed, 4),
        "validation_agreement": round(validation.agreement, 4),
        "max_relative_error": round(validation.max_relative_error, 4),
        "max_cv": round(uncertainty.max_cv, 4),
        "n_runs": uncertainty.n_runs,
    }
    return GateDecision(
        gate_slug=gate_slug,
        accepted=accepted,
        escalate=escalate,
        reasons=reasons,
        scores=scores,
    )
