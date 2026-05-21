"""Example: run verification over a small deliverable-like object.

Run from the repository root:
    python vvuq/examples-vvuq/01_verification_checks.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field

VVUQ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VVUQ_DIR)

from verification import verify  # noqa: E402


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


def main() -> None:
    deliverable = FakeDeliverable(
        complete=True,
        artifacts=[FakeArtifact("instructions.md", "step 1\nstep 2\n"), FakeArtifact("paper.md", "# Title\n")],
    )
    result = verify(deliverable)
    print("fraction_passed:", result.fraction_passed)
    print("all_passed:", result.all_passed)
    for check in result.checks:
        print(f"  [{'ok' if check.passed else '--'}] {check.name} {check.detail}")


if __name__ == "__main__":
    main()
