"""Example: run one deliverable end to end through the orchestrator.

Run from the repository root:
    python pipeline/examples-pipeline/01_single_deliverable.py

LICENSE: MIT
"""

from __future__ import annotations

import json
import os
import sys

PIPELINE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PIPELINE_DIR)

from orchestrator import PipelineOrchestrator  # noqa: E402


def main() -> None:
    orchestrator = PipelineOrchestrator(simulate_runs=3)
    deliverable = orchestrator.run_deliverable(
        deliverable_id="DAILY-0001",
        title="Automated trial acceleration estimate",
        topic="Physical AI oncology trial throughput",
        sources=["national-platform paper", "four-simulation paper"],
    )
    print("complete:", deliverable.complete)
    print("statuses:", orchestrator.stage_statuses(deliverable))
    print(json.dumps(deliverable.summary(), indent=2))


if __name__ == "__main__":
    main()
