"""Example: run a small daily batch of deliverables.

Demonstrates the non-stop cadence at small scale by producing several
deliverables in one pass. Run from the repository root:
    python pipeline/examples-pipeline/03_full_daily_run.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

PIPELINE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PIPELINE_DIR)

from orchestrator import PipelineOrchestrator  # noqa: E402

TOPICS = [
    "Trial throughput acceleration",
    "Multi-site enrollment forecast",
    "Robotic resection timing study",
]


def main() -> None:
    orchestrator = PipelineOrchestrator(simulate_runs=3)
    completed = 0
    for index, topic in enumerate(TOPICS, start=1):
        deliverable = orchestrator.run_deliverable(
            deliverable_id=f"DAILY-{index:04d}",
            title=f"Daily deliverable {index}",
            topic=topic,
        )
        results = deliverable.metadata.get("execution_results", {})
        accel = results.get("acceleration_factor", "n/a")
        print(f"{deliverable.deliverable_id}: complete={deliverable.complete} acceleration_factor={accel}")
        completed += int(deliverable.complete)
    print(f"completed {completed}/{len(TOPICS)} deliverables")


if __name__ == "__main__":
    main()
