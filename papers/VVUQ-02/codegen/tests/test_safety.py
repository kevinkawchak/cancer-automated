"""Tests for the three immediate-catastrophe safety gates (VVUQ 06, 09, 10).

LICENSE: MIT
"""

from __future__ import annotations

from src.safety.estop import monitor
from src.safety.human_collision import HumanActor, Link, evaluate
from src.safety.vessel_gate import count_hard_stop_violations, gate


def test_vessel_gate_clear_far_away():
    result = gate((100.0, 100.0, 100.0), phase=2)
    assert result.action == "clear"
    assert result.velocity_scale == 1.0
    assert not result.e_stop


def test_vessel_gate_hard_stop_inside_smv_phase2():
    result = gate((15.0, -45.0, -50.0), phase=2)
    assert result.action == "hard_stop"
    assert result.e_stop
    assert result.vessel == "superior_mesenteric_vein"


def test_vessel_gate_inactive_phase_is_clear():
    # SMA and celiac are active only in phases 3, 4, 8; in phase 1 nothing is active.
    result = gate((0.0, -50.0, -57.0), phase=1)
    assert result.action == "clear"


def test_vessel_gate_no_fly_band():
    # About 5 mm from the SMV centerline (radii 2/4/6) lands in the no-fly band.
    result = gate((20.0, -45.0, -50.0), phase=2)
    assert result.action in {"no_fly", "soft_warning"}
    assert not result.e_stop


def test_count_hard_stop_violations():
    safe_path = [(100.0, 100.0, 100.0), (90.0, 90.0, 90.0)]
    assert count_hard_stop_violations(safe_path, phase=2) == 0
    breach_path = [(15.0, -45.0, -50.0)]
    assert count_hard_stop_violations(breach_path, phase=2) == 1


def _actors():
    return [HumanActor("scrub_nurse", (0.55, 0.45, 0.95), 0.30)]


def test_collision_clear_when_far():
    links = [Link("head", (0.0, -1.0, 1.3))]
    result = evaluate(links, _actors())
    assert result.state == "clear"
    assert not result.e_stop


def test_collision_unsafe_when_inside_keepout():
    links = [Link("left_hand", (0.55, 0.45, 0.95))]
    result = evaluate(links, _actors())
    assert result.state == "unsafe"
    assert result.e_stop
    assert result.min_clearance_mm < 50.0


def test_collision_proximity_band():
    # 0.50 m centre distance minus the 0.30 m keep-out radius is 200 mm clearance.
    links = [Link("left_hand", (0.55, -0.05, 0.95))]
    result = evaluate(links, _actors())
    assert result.state == "proximity"
    assert not result.e_stop


def test_estop_no_fault():
    response = monitor({"balance_margin_mm": 40.0, "vision_confidence": 0.9})
    assert not response.fault_detected
    assert response.action == "none"


def test_estop_balance_loss_safe_parks():
    response = monitor({"balance_margin_mm": 3.0})
    assert response.fault_detected
    assert response.fault_type == "balance_loss"
    assert response.action == "safe_park"
    assert response.safe_state_reached
    assert not response.escalate


def test_estop_vision_dropout_hands_back_and_escalates():
    response = monitor({"vision_confidence": 0.2})
    assert response.fault_type == "vision_dropout"
    assert response.action == "hand_back"
    assert response.escalate


def test_estop_multiple_faults_escalate():
    response = monitor({"balance_margin_mm": 3.0, "vision_confidence": 0.2})
    assert response.action == "hand_back"
    assert response.escalate
