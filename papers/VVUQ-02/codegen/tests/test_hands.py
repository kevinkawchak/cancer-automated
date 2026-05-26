"""Tests for finger force control, grasp, and handover (VVUQ 02 and 05).

LICENSE: MIT
"""

from __future__ import annotations

import pytest

from src.hands.finger_force import (
    BIMANUAL_HARD_N,
    PER_FINGERTIP_HARD_N,
    PER_FINGERTIP_SOFT_N,
    bimanual_check,
    force_tracking_error,
    track_force,
)
from src.hands.grasp import grasp
from src.hands.handover import SWAP_TIME_MS, handover


def test_track_force_moves_toward_target():
    cmd = track_force(target_n=1.5, measured_n=1.0)
    assert 1.0 < cmd.commanded_n <= 1.5
    assert not cmd.estop
    assert not cmd.soft_exceeded


def test_track_force_estop_at_hard_cap():
    cmd = track_force(target_n=2.0, measured_n=PER_FINGERTIP_HARD_N)
    assert cmd.estop
    assert "hard cap" in cmd.reason


def test_track_force_clamps_above_hard():
    cmd = track_force(target_n=10.0, measured_n=2.9)
    assert cmd.commanded_n <= PER_FINGERTIP_HARD_N


def test_track_force_flags_soft_exceedance():
    cmd = track_force(target_n=2.9, measured_n=2.8)
    assert cmd.commanded_n > PER_FINGERTIP_SOFT_N
    assert cmd.soft_exceeded
    assert not cmd.estop


def test_bimanual_check_bands():
    within = bimanual_check([1.0, 1.0, 1.0])
    assert within.within_soft and within.within_hard and not within.estop
    over = bimanual_check([2.0, 2.0, 2.5])
    assert over.cumulative_n > BIMANUAL_HARD_N
    assert over.estop


def test_force_tracking_error():
    assert force_tracking_error(2.5, 2.45) == pytest.approx(0.05)


def test_grasp_stable_no_slip():
    result = grasp("tripod", normal_force_per_contact_n=2.0, tangential_load_n=1.0)
    assert result.success
    assert not result.slip_detected
    assert result.grasp_quality >= 0.5


def test_grasp_slips_when_load_exceeds_friction():
    result = grasp("pinch", normal_force_per_contact_n=0.5, tangential_load_n=5.0)
    assert result.slip_detected
    assert not result.success


def test_grasp_unknown_taxonomy_raises():
    with pytest.raises(ValueError):
        grasp("claw", 2.0, 1.0)


def test_handover_success_and_duration():
    result = handover("needle_driver_handle", "R", "L")
    assert result.duration_ms == SWAP_TIME_MS
    assert result.success
    assert not result.slip_detected


def test_handover_same_hand_raises():
    with pytest.raises(ValueError):
        handover("scalpel", "L", "L")
