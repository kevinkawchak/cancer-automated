"""Example: run an autonomous lights-off batch and trigger an emergency stop.

Run from the repository root:
    python physical-ai/examples-physical-ai/01_lights_off_cell.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

PAI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PAI_DIR)

from lights_off_factory import LightsOffFactory  # noqa: E402


def main() -> None:
    factory = LightsOffFactory(cell_ids=["cell-a", "cell-b"], max_cumulative_faults=1)

    clean = factory.run_batch(tasks=list(range(6)), executor=lambda cell, task: True)
    print("clean run state:", clean.state, "per_cell:", clean.per_cell)

    # Force faults on every third task to exercise the emergency stop.
    def flaky(cell, task):
        return task % 3 != 0

    faulted = factory.run_batch(tasks=list(range(9)), executor=flaky)
    print("faulted run state:", faulted.state, "faults:", faulted.faults)


if __name__ == "__main__":
    main()
