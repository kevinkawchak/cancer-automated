"""End-to-end orchestration of the five established methods.

The orchestrator runs the four producing stages in order (instruction, codegen,
execution, paper) for a single deliverable. An optional ``gate`` callable (for
example the VVUQ gate) is invoked after the paper stage; if it returns a falsy
or blocking result the deliverable is marked accordingly. The orchestrator keeps
no hard dependency on the VVUQ package so the pipeline can be used on its own.

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
from typing import Callable, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from codegen_stage import CodegenStage  # noqa: E402
from deliverable import STAGE_ORDER, Deliverable, Stage, StageStatus  # noqa: E402
from execution_stage import ExecutionStage  # noqa: E402
from instruction_stage import InstructionStage  # noqa: E402
from paper_stage import PaperStage  # noqa: E402


class PipelineOrchestrator:
    """Run the daily-deliverable pipeline for one deliverable."""

    def __init__(self, simulate_runs: int = 3, use_llm: bool = False) -> None:
        self.instruction_stage = InstructionStage(use_llm=use_llm)
        self.codegen_stage = CodegenStage(simulate_runs=simulate_runs)
        self.execution_stage = ExecutionStage()
        self.paper_stage = PaperStage()

    def run_deliverable(
        self,
        deliverable_id: str,
        title: str,
        topic: str = "",
        sources: Optional[list[str]] = None,
        gate: Optional[Callable[[Deliverable], object]] = None,
    ) -> Deliverable:
        """Run all stages in order and return the completed deliverable."""
        deliverable = Deliverable(deliverable_id=deliverable_id, title=title, topic=topic)

        instruction_result = self.instruction_stage.run(deliverable, sources=sources)
        if not instruction_result.ok:
            return deliverable

        codegen_result = self.codegen_stage.run(deliverable)
        if not codegen_result.ok:
            return deliverable

        execution_result = self.execution_stage.run(deliverable)
        if not execution_result.ok:
            return deliverable

        self.paper_stage.run(deliverable)

        if gate is not None:
            deliverable.metadata["gate_result"] = gate(deliverable)

        return deliverable

    def stage_statuses(self, deliverable: Deliverable) -> dict[str, str]:
        """Return the status of each stage for quick inspection."""
        return {
            stage.value: (deliverable.results[stage].status.value if stage in deliverable.results else "pending")
            for stage in STAGE_ORDER
        }
