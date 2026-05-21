"""Example: run a project three times with distinct seeds.

Run from the repository root:
    python simulation/examples-simulation/01_triple_run.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

SIM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SIM_DIR)

from triple_runner import TripleRunner  # noqa: E402


def project(seed: int) -> dict:
    # A small, deterministic project: metrics vary slightly with the seed.
    jitter = (seed % 5) * 0.002
    return {"acceleration_factor": 2.5 + jitter, "automated_days": 12.0 - jitter}


def main() -> None:
    runs = TripleRunner(n_runs=3).run(project)
    for run in runs:
        print(f"run {run.run_index} seed={run.seed} metrics={run.metrics}")


if __name__ == "__main__":
    main()
