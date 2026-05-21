"""Example: quantify uncertainty across three runs and apply the gate.

Run from the repository root:
    python vvuq/examples-vvuq/03_uncertainty_budget.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field

VVUQ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VVUQ_DIR)

from uncertainty import quantify  # noqa: E402
from vvuq_gate import VVUQGate  # noqa: E402


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
    runs = [
        {"acceleration_factor": 2.50, "automated_days": 12.0},
        {"acceleration_factor": 2.52, "automated_days": 12.1},
        {"acceleration_factor": 2.49, "automated_days": 11.9},
    ]
    uncertainty = quantify(runs)
    print("n_runs:", uncertainty.n_runs, "max_cv:", round(uncertainty.max_cv, 4))

    deliverable = FakeDeliverable(artifacts=[FakeArtifact("paper.md", "# Title\n")])
    gate = VVUQGate()
    decision = gate.evaluate(
        deliverable,
        runs=runs,
        observed={"acceleration_factor": 2.50, "automated_days": 12.0},
        reference={"acceleration_factor": 2.50, "automated_days": 12.0},
        human_review=True,
    )
    print("accepted:", decision.accepted)
    print("reasons:", decision.reasons)
    print("scores:", {k: round(v, 4) if isinstance(v, float) else v for k, v in decision.scores.items()})


if __name__ == "__main__":
    main()
