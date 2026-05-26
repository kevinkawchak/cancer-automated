"""Validation: did we build the right deliverable? (ASME V&V 40 section 9).

Compares observed metrics against a trusted reference that is produced
independently of the run under test (the artifacts in data/reference/ are derived
from standard-defined nominal values and analytic models, not from the same
stochastic simulation). Reports the fraction of metrics that agree within
tolerance, the worst relative error, and whether a human review has been recorded
(ISO 14971 risk control verification). Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """The outcome of validating observed metrics against a reference."""

    agreement: float
    max_relative_error: float
    human_review: bool
    per_key: dict = field(default_factory=dict)
    compared_keys: list[str] = field(default_factory=list)


def relative_error(observed: float, reference: float) -> float:
    """Relative error with a guard for a zero reference."""
    denom = abs(reference) if reference != 0 else 1.0
    return abs(observed - reference) / denom


def validate(
    observed: dict,
    reference: dict,
    *,
    max_relative_error: float = 0.05,
    human_review: bool = False,
) -> ValidationResult:
    """Compare observed metrics to an independent reference and summarize agreement."""
    keys = [k for k in reference if k in observed]
    per_key: dict = {}
    agree = 0
    worst = 0.0
    for key in keys:
        try:
            obs = float(observed[key])
            ref = float(reference[key])
        except (TypeError, ValueError):
            continue
        err = relative_error(obs, ref)
        per_key[key] = err
        worst = max(worst, err)
        if err <= max_relative_error:
            agree += 1
    compared = list(per_key.keys())
    agreement = (agree / len(compared)) if compared else 0.0
    return ValidationResult(
        agreement=agreement,
        max_relative_error=worst,
        human_review=human_review,
        per_key=per_key,
        compared_keys=compared,
    )
