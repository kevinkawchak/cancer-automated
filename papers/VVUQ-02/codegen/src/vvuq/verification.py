"""Verification: did we build the deliverable right? (ASME V&V 40 section 8).

Generalizes the VVUQ-01 6-check pattern so each of the 10 gates supplies its own
structural and policy predicates (for example: ZMP samples present for all ticks,
no NaN in the centre-of-mass trace, output file under the size cap, schema valid,
lint clean). The gate requires the pass fraction to equal 1.0. Pure standard
library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VerificationCheck:
    """A single named verification check."""

    name: str
    passed: bool
    detail: str = ""


@dataclass
class VerificationResult:
    """The collected outcome of every verification check."""

    checks: list[VerificationCheck] = field(default_factory=list)

    @property
    def fraction_passed(self) -> float:
        if not self.checks:
            return 0.0
        return sum(1 for c in self.checks if c.passed) / len(self.checks)

    @property
    def all_passed(self) -> bool:
        return bool(self.checks) and all(c.passed for c in self.checks)

    def failures(self) -> list[str]:
        return [f"{c.name}: {c.detail}" for c in self.checks if not c.passed]


def verify(checks: dict[str, bool], details: dict[str, str] | None = None) -> VerificationResult:
    """Build a VerificationResult from a gate's evaluated predicate results.

    Args:
        checks: mapping of predicate name to whether it passed.
        details: optional mapping of predicate name to a failure detail string.

    Returns:
        The ``VerificationResult`` whose ``fraction_passed`` the gate compares
        against ``min_checks_passed_fraction`` (1.0 for all gates).
    """
    details = details or {}
    return VerificationResult(
        checks=[
            VerificationCheck(name, bool(passed), details.get(name, ""))
            for name, passed in checks.items()
        ]
    )
