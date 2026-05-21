"""The VVUQ gate: held to a higher standard than code generation.

Code generation produces a candidate deliverable. The VVUQ gate decides whether
that candidate is allowed to ship. It combines verification, validation, and
uncertainty quantification and compares each against the thresholds in
``configs/vvuq_thresholds.yaml``. The gate blocks on any failure and escalates
divergent uncertainty to a human.

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from uncertainty import quantify  # noqa: E402
from validation import validate  # noqa: E402
from verification import verify  # noqa: E402

DEFAULT_THRESHOLDS = {
    "verification": {
        "min_checks_passed_fraction": 1.0,
        "require_schema_valid": True,
        "require_lint_clean": True,
    },
    "validation": {
        "min_agreement_with_reference": 0.95,
        "max_relative_error": 0.05,
        "require_human_review": True,
    },
    "uncertainty": {
        "max_coefficient_of_variation": 0.10,
        "min_consensus_runs": 3,
        "confidence_level": 0.95,
    },
    "gate": {
        "block_on_any_failure": True,
        "escalate_to_human_on_divergence": True,
    },
}


def load_thresholds(path: str | None = None) -> dict:
    """Load gate thresholds from YAML, falling back to built-in defaults."""
    try:
        import yaml
    except ImportError:
        return {key: dict(value) for key, value in DEFAULT_THRESHOLDS.items()}

    if path is None:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(repo_root, "configs", "vvuq_thresholds.yaml")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        return data or {key: dict(value) for key, value in DEFAULT_THRESHOLDS.items()}
    except (OSError, yaml.YAMLError):
        return {key: dict(value) for key, value in DEFAULT_THRESHOLDS.items()}


@dataclass
class GateDecision:
    """The gate verdict for a deliverable."""

    accepted: bool
    reasons: list[str] = field(default_factory=list)
    scores: dict = field(default_factory=dict)
    escalate: bool = False

    @property
    def blocked(self) -> bool:
        return not self.accepted


class VVUQGate:
    """Combine verification, validation, and uncertainty into one decision."""

    def __init__(self, thresholds: dict | None = None) -> None:
        self.thresholds = thresholds or load_thresholds()

    def evaluate(
        self,
        deliverable,
        runs: list[dict],
        observed: dict,
        reference: dict,
        *,
        schema_valid: bool = True,
        lint_clean: bool = True,
        human_review: bool = False,
    ) -> GateDecision:
        ver_t = self.thresholds["verification"]
        val_t = self.thresholds["validation"]
        unc_t = self.thresholds["uncertainty"]

        ver = verify(deliverable, schema_valid=schema_valid, lint_clean=lint_clean)
        val = validate(observed, reference, max_relative_error=val_t["max_relative_error"], human_review=human_review)
        unc = quantify(runs)

        reasons: list[str] = []

        if ver.fraction_passed < ver_t["min_checks_passed_fraction"]:
            reasons.append(f"verification fraction {ver.fraction_passed:.2f} below {ver_t['min_checks_passed_fraction']}")
        if val.agreement < val_t["min_agreement_with_reference"]:
            reasons.append(f"validation agreement {val.agreement:.2f} below {val_t['min_agreement_with_reference']}")
        if val.max_relative_error > val_t["max_relative_error"]:
            reasons.append(f"max relative error {val.max_relative_error:.3f} above {val_t['max_relative_error']}")
        if val_t.get("require_human_review", False) and not human_review:
            reasons.append("human review not recorded")
        if unc.n_runs < unc_t["min_consensus_runs"]:
            reasons.append(f"only {unc.n_runs} runs, need {unc_t['min_consensus_runs']}")
        if unc.max_cv > unc_t["max_coefficient_of_variation"]:
            reasons.append(f"max cv {unc.max_cv:.3f} above {unc_t['max_coefficient_of_variation']}")

        escalate = unc.max_cv > unc_t["max_coefficient_of_variation"] and self.thresholds["gate"].get(
            "escalate_to_human_on_divergence", False
        )
        accepted = len(reasons) == 0
        scores = {
            "verification_fraction": ver.fraction_passed,
            "validation_agreement": val.agreement,
            "max_relative_error": val.max_relative_error,
            "max_cv": unc.max_cv,
            "n_runs": unc.n_runs,
        }
        return GateDecision(accepted=accepted, reasons=reasons, scores=scores, escalate=escalate)
