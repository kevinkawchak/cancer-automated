"""Tests for ZMP margin and the posture controller (VVUQ 03).

LICENSE: MIT
"""

from __future__ import annotations

import pytest

from src.balance.posture_controller import STABILITY_FLOOR_MM, stabilize
from src.balance.zmp import compute_zmp, support_polygon_margin_mm, zmp_margin


def test_zmp_equals_com_at_zero_accel():
    zmp = compute_zmp((0.05, -0.02), 0.78, (0.0, 0.0))
    assert zmp == (0.05, -0.02)


def test_zmp_shifts_against_acceleration():
    zmp = compute_zmp((0.0, 0.0), 0.78, (1.0, 0.0))
    assert zmp[0] < 0.0


def test_center_is_inside_polygon():
    margin = support_polygon_margin_mm((0.0, 0.0))
    assert margin == pytest.approx(130.0, abs=0.5)


def test_far_point_is_outside():
    assert support_polygon_margin_mm((1.0, 0.0)) < 0.0


def test_zmp_margin_positive_for_small_accel():
    margin = zmp_margin((0.0, 0.0), 0.78, (0.2, 0.0))
    assert 0.0 < margin < 130.0


def test_stabilize_stable_at_rest():
    cmd = stabilize((0.0, 0.0), (0.0, 0.0))
    assert cmd.balance_state == "stable"
    assert cmd.admitted_force_scale == 1.0
    assert not cmd.estop


def test_stabilize_recovers_large_push():
    cmd = stabilize((0.0, 0.0), (300.0, 0.0))
    assert cmd.admitted_force_scale < 1.0
    assert cmd.corrected_margin_mm >= STABILITY_FLOOR_MM
    assert not cmd.estop


def test_stabilize_falls_when_com_outside():
    cmd = stabilize((0.2, 0.0), (0.0, 0.0))
    assert cmd.balance_state == "fall"
    assert cmd.estop
