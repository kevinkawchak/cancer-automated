"""Example: aggregate three runs into a consensus report.

Run from the repository root:
    python simulation/examples-simulation/02_consensus_report.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

SIM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SIM_DIR)

from consensus import summarize  # noqa: E402
from triple_runner import TripleRunner  # noqa: E402


def project(seed: int) -> dict:
    jitter = (seed % 5) * 0.002
    return {"acceleration_factor": 2.5 + jitter, "automated_days": 12.0 - jitter}


def main() -> None:
    runs = TripleRunner(n_runs=3).run(project)
    consensus = summarize(runs)
    print("n_runs:", consensus.n_runs)
    print("converged:", consensus.converged)
    for key in consensus.mean:
        print(f"  {key}: mean={consensus.mean[key]:.4f} cv={consensus.cv[key]:.4f}")
    print("divergent:", consensus.divergent)


if __name__ == "__main__":
    main()
