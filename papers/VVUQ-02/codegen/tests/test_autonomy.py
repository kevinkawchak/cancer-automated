"""Tests for the autonomy intent and plan compiler (VVUQ 04 core).

LICENSE: MIT
"""

from __future__ import annotations

from src.autonomy.llm_intent import (
    Intent,
    backend_select,
    load_reference_plan,
    propose_intents,
)
from src.autonomy.plan_compiler import (
    GRASP_FINGER_TARGETS,
    compile_intents,
    phase_step_concordance,
)


def test_backend_defaults_to_offline(monkeypatch):
    monkeypatch.delenv("AUTONOMY_BACKEND", raising=False)
    assert backend_select() == "offline"


def test_reference_plan_loads_eight_phases():
    plan = load_reference_plan()
    phases = sorted(row["phase"] for row in plan)
    assert phases[0] == 1
    assert 5 in phases


def test_propose_intents_phase5_reference():
    intents = propose_intents(phase=5)
    assert len(intents) == 2
    assert all(isinstance(i, Intent) for i in intents)
    assert all(i.phase == 5 for i in intents)
    assert all(i.source == "reference" for i in intents)
    suturing = [i for i in intents if i.grasp == "needle_driver"]
    assert len(suturing) == 1


def test_compile_produces_20_finger_targets():
    intents = propose_intents(phase=5)
    commands = compile_intents(intents, tick=320_000)
    assert len(commands) == 2
    for cmd in commands:
        assert len(cmd.finger_target) == 20
        assert cmd.tick == 320_000
        assert cmd.velocity_scale == 1.0
        assert cmd.force_soft_cap_n == 2.5


def test_command_as_dict_schema_keys():
    cmd = compile_intents(propose_intents(phase=1))[0]
    d = cmd.as_dict()
    for key in (
        "tick",
        "hand_id",
        "phase",
        "tip_target",
        "tip_orientation",
        "finger_target",
        "grasp_state",
        "velocity_scale",
        "force_soft_cap_n",
    ):
        assert key in d
    assert len(d["tip_target"]) == 3
    assert len(d["tip_orientation"]) == 4


def test_concordance_perfect_for_reference_roundtrip():
    intents = propose_intents(phase=5)
    commands = compile_intents(intents)
    assert phase_step_concordance(commands, intents) == 1.0


def test_concordance_drops_on_target_drift():
    intents = propose_intents(phase=5)
    commands = compile_intents(intents)
    drifted = [
        Intent(
            phase=i.phase,
            hand_id=i.hand_id,
            action=i.action,
            tip_target=(i.tip_target[0] + 10.0, i.tip_target[1], i.tip_target[2]),
            grasp=i.grasp,
            intent_id=i.intent_id,
        )
        for i in intents
    ]
    assert phase_step_concordance(commands, drifted) == 0.0


def test_grasp_targets_cover_taxonomy():
    for grasp in ("open", "pinch", "tripod", "power", "needle_driver"):
        assert len(GRASP_FINGER_TARGETS[grasp]) == 20
