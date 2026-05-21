"""Tests for the daily-deliverable pipeline (the five established methods).

Modules are loaded by file path through the conftest ``load_module`` helper, so
the hyphen-free ``pipeline/`` modules import cleanly without packaging.

LICENSE: MIT
"""

from __future__ import annotations

from conftest import load_module


def _orchestrator_module():
    return load_module("orchestrator", "pipeline/orchestrator.py")


def test_pipeline_runs_all_four_methods():
    orch = _orchestrator_module()
    pipeline = orch.PipelineOrchestrator(simulate_runs=3)
    deliverable = pipeline.run_deliverable(
        deliverable_id="T-0001",
        title="Test deliverable",
        topic="unit test",
        sources=["reference paper"],
    )
    assert deliverable.complete
    assert deliverable.artifact("instructions") is not None
    assert deliverable.artifact("code") is not None
    assert deliverable.artifact("execution_log") is not None
    assert deliverable.artifact("paper") is not None


def test_execution_results_have_acceleration():
    orch = _orchestrator_module()
    pipeline = orch.PipelineOrchestrator(simulate_runs=3)
    deliverable = pipeline.run_deliverable("T-0002", "Metrics", "unit test")
    results = deliverable.metadata["execution_results"]
    assert "acceleration_factor" in results
    assert float(results["acceleration_factor"]) > 1.0


def test_codegen_is_blocked_without_instructions():
    orch = _orchestrator_module()
    deliverable = orch.Deliverable(deliverable_id="T-0003", title="No instructions")
    result = orch.CodegenStage().run(deliverable)
    assert result.status == orch.StageStatus.BLOCKED
    assert not result.ok


def test_paper_tabulates_results():
    orch = _orchestrator_module()
    pipeline = orch.PipelineOrchestrator(simulate_runs=3)
    deliverable = pipeline.run_deliverable("T-0004", "Paper check", "unit test")
    paper = deliverable.artifact("paper")
    assert paper is not None
    assert "acceleration_factor" in paper.content
    assert "## Results" in paper.content


def test_gate_callable_is_invoked():
    orch = _orchestrator_module()
    pipeline = orch.PipelineOrchestrator(simulate_runs=3)
    seen = {}

    def gate(deliverable):
        seen["called"] = True
        return {"accepted": deliverable.complete}

    deliverable = pipeline.run_deliverable("T-0005", "Gated", "unit test", gate=gate)
    assert seen.get("called") is True
    assert deliverable.metadata["gate_result"] == {"accepted": True}
