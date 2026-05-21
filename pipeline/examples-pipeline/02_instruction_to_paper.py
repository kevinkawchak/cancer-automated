"""Example: run each pipeline stage individually and inspect the artifacts.

Run from the repository root:
    python pipeline/examples-pipeline/02_instruction_to_paper.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

PIPELINE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PIPELINE_DIR)

from codegen_stage import CodegenStage  # noqa: E402
from deliverable import Deliverable  # noqa: E402
from execution_stage import ExecutionStage  # noqa: E402
from instruction_stage import InstructionStage  # noqa: E402
from paper_stage import PaperStage  # noqa: E402


def main() -> None:
    deliverable = Deliverable(
        deliverable_id="DAILY-0002",
        title="Stage by stage walkthrough",
        topic="Established methods",
    )

    InstructionStage().run(deliverable, sources=["humanoid demo workflow"])
    CodegenStage(simulate_runs=3).run(deliverable)
    ExecutionStage().run(deliverable)
    PaperStage().run(deliverable)

    for artifact in deliverable.all_artifacts():
        print(f"--- {artifact.name} ({artifact.kind}, {artifact.size_bytes} bytes) ---")
        preview = artifact.content.strip().splitlines()[:6]
        for line in preview:
            print(line)
        print()


if __name__ == "__main__":
    main()
