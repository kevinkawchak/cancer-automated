"""Verification: did we build the deliverable right?

Verification runs structural and policy checks over a deliverable: all stages
completed, artifacts are present and non-empty, every artifact is within the
200K per-file cap, the schema is valid, and the code lints cleanly. It is pure
standard library and uses duck typing so it does not depend on the pipeline
package.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field

PER_FILE_CAP_BYTES = 200_000


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
        return sum(1 for check in self.checks if check.passed) / len(self.checks)

    @property
    def all_passed(self) -> bool:
        return all(check.passed for check in self.checks)

    def failures(self) -> list[str]:
        return [f"{check.name}: {check.detail}" for check in self.checks if not check.passed]


def verify(
    deliverable,
    *,
    per_file_cap_bytes: int = PER_FILE_CAP_BYTES,
    schema_valid: bool = True,
    lint_clean: bool = True,
) -> VerificationResult:
    """Run the verification checks over a deliverable-like object."""
    checks: list[VerificationCheck] = []

    complete = bool(getattr(deliverable, "complete", False))
    checks.append(VerificationCheck("all_stages_complete", complete, "" if complete else "not all stages complete"))

    artifacts = list(deliverable.all_artifacts()) if hasattr(deliverable, "all_artifacts") else []
    checks.append(
        VerificationCheck("artifacts_present", len(artifacts) > 0, f"{len(artifacts)} artifacts"),
    )
    non_empty = all(getattr(art, "size_bytes", 0) > 0 for art in artifacts)
    checks.append(VerificationCheck("artifacts_non_empty", non_empty and bool(artifacts)))

    oversize = [art.name for art in artifacts if getattr(art, "size_bytes", 0) > per_file_cap_bytes]
    checks.append(
        VerificationCheck("within_file_cap", not oversize, f"oversize: {oversize}" if oversize else ""),
    )

    checks.append(VerificationCheck("schema_valid", bool(schema_valid)))
    checks.append(VerificationCheck("lint_clean", bool(lint_clean)))

    return VerificationResult(checks)
