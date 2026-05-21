"""Tests for the Stage 2 deployment references.

LICENSE: MIT
"""

from __future__ import annotations

from conftest import load_module


def _factory_module():
    return load_module("lights_off_factory", "physical-ai/lights_off_factory.py")


def test_factory_is_ready_by_default_and_completes_clean_run():
    factory_mod = _factory_module()
    factory = factory_mod.LightsOffFactory(cell_ids=["a", "b"])
    assert factory.ready()
    report = factory.run_batch(tasks=list(range(6)), executor=lambda cell, task: True)
    assert not report.blocked
    assert report.faults == 0
    assert report.state == "dark"
    completed = sum(cell["completed"] for cell in report.per_cell.values())
    assert completed == 6


def test_factory_blocks_when_interlock_unsatisfied():
    factory_mod = _factory_module()
    interlocks = [factory_mod.Interlock("perimeter_clear", False, "person detected")]
    factory = factory_mod.LightsOffFactory(cell_ids=["a"], interlocks=interlocks)
    report = factory.run_batch(tasks=[1, 2], executor=lambda cell, task: True)
    assert report.blocked
    assert "perimeter_clear" in report.unsatisfied


def test_factory_emergency_stops_past_fault_budget():
    factory_mod = _factory_module()
    factory = factory_mod.LightsOffFactory(cell_ids=["a"], max_cumulative_faults=1)
    report = factory.run_batch(tasks=list(range(6)), executor=lambda cell, task: False)
    assert report.state == "estop"
    assert report.faults == 2


def test_factory_requires_at_least_one_cell():
    factory_mod = _factory_module()
    try:
        factory_mod.LightsOffFactory(cell_ids=[])
    except ValueError:
        return
    raise AssertionError("expected ValueError for empty cell list")


def test_hybrid_pilot_timeline_and_summary():
    pilot_mod = load_module("hybrid_surgery_medicine", "physical-ai/hybrid_surgery_medicine.py")
    pilot = pilot_mod.default_pilot()
    summary = pilot.summary()
    assert summary["surgery_arms"] == 8
    assert summary["regimen_days"] == 168
    assert summary["requires_human_oversight"] is True

    timeline = pilot.timeline()
    assert timeline[0].day == 0
    assert timeline[0].phase == "surgery"
    assert timeline[-1].day == 168
