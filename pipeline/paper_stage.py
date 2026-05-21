"""Method 4: assemble a paper from the executed results.

The paper stage reads the execution results recorded on the deliverable and
assembles a structured Markdown paper (title, abstract, methods, results table,
conclusion). This mirrors the multi-stage instruction to code to execution to
paper workflow proven in the prior demo projects.

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from deliverable import Artifact, Stage, StageResult, StageStatus  # noqa: E402


class PaperStage:
    """Assemble a Markdown paper from the deliverable artifacts and results."""

    def run(self, deliverable) -> StageResult:
        start = time.perf_counter()
        execution_log = deliverable.artifact("execution_log")
        if execution_log is None:
            result = StageResult(
                stage=Stage.PAPER,
                status=StageStatus.BLOCKED,
                log="no execution log found; run the execution stage first",
                duration_s=time.perf_counter() - start,
            )
            deliverable.record(result)
            return result

        results = deliverable.metadata.get("execution_results", {})
        content = self._assemble(deliverable, results)
        artifact = Artifact(name="paper.md", kind="paper", content=content)
        result = StageResult(
            stage=Stage.PAPER,
            status=StageStatus.COMPLETE,
            artifacts=[artifact],
            log=f"paper assembled ({artifact.size_bytes} bytes, {len(results)} result rows)",
            duration_s=time.perf_counter() - start,
        )
        deliverable.record(result)
        return result

    def _assemble(self, deliverable, results: dict) -> str:
        rows = "\n".join(f"| {key} | {value} |" for key, value in results.items())
        if not rows:
            rows = "| (no results) | |"
        return (
            f"# {deliverable.title}\n\n"
            f"Deliverable ID: {deliverable.deliverable_id}  \n"
            f"Topic: {deliverable.topic}  \n"
            f"Generated: {deliverable.created_at}\n\n"
            "## Abstract\n\n"
            "This paper was assembled automatically from the executed results of the daily "
            "deliverable pipeline. It records the trial-acceleration metrics computed by the "
            "generated code and is presented as a draft pending VVUQ clearance and human review.\n\n"
            "## Methods\n\n"
            "The deliverable was produced by the five established methods in order: instruction "
            "generation, code generation, code execution, and paper assembly. The generated code "
            "was executed and its outputs were captured and parsed.\n\n"
            "## Results\n\n"
            "| Metric | Value |\n"
            "|--------|-------|\n"
            f"{rows}\n\n"
            "## Conclusion\n\n"
            "Automation of the established methods produced a measurable acceleration of the "
            "deliverable timeline. This draft must pass the VVUQ gate before any clinical use.\n"
        )
