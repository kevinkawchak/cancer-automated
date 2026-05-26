"""Tests for the H2-Surgical forward kinematics (VVUQ 01 input).

LICENSE: MIT
"""

from __future__ import annotations

import math

from src.kinematics.forward_kinematics import (
    DHRow,
    clamp_to_limits,
    dh_transform,
    euclidean_distance_mm,
    forward_kinematics,
    identity4,
    matmul4,
    rows_from_config,
)


def _row(a=0.0, alpha=0.0, d=0.0, theta_offset=0.0, q_min=-3.15, q_max=3.15):
    return DHRow(a=a, alpha=alpha, d=d, theta_offset=theta_offset, q_min=q_min, q_max=q_max)


def test_identity_is_neutral():
    ident = identity4()
    other = dh_transform(_row(a=0.4), 0.0)
    assert matmul4(ident, other) == other


def test_single_prismatic_offset_along_x():
    pos, _rot = forward_kinematics([0.0], [_row(a=0.5)])
    assert math.isclose(pos[0], 0.5, abs_tol=1e-9)
    assert math.isclose(pos[1], 0.0, abs_tol=1e-9)
    assert math.isclose(pos[2], 0.0, abs_tol=1e-9)


def test_single_offset_along_z():
    pos, _rot = forward_kinematics([0.0], [_row(d=0.3)])
    assert math.isclose(pos[2], 0.3, abs_tol=1e-9)


def test_base_offset_applied():
    pos, _rot = forward_kinematics([0.0], [_row(d=0.3)], base_offset_m=(0.0, 0.18, 1.25))
    assert math.isclose(pos[1], 0.18, abs_tol=1e-9)
    assert math.isclose(pos[2], 1.55, abs_tol=1e-9)


def test_length_mismatch_raises():
    try:
        forward_kinematics([0.0, 0.0], [_row()])
    except ValueError:
        return
    raise AssertionError("expected ValueError for joint count mismatch")


def test_clamp_to_limits():
    dh = [_row(q_min=-1.0, q_max=1.0), _row(q_min=0.0, q_max=2.0)]
    assert clamp_to_limits([5.0, -5.0], dh) == [1.0, 0.0]


def test_rows_from_config_roundtrip():
    cfg = [
        {"a": 0.0, "alpha": 1.5708, "d": 0.3, "theta_offset": 0.0, "q_min": -3.14, "q_max": 3.14}
    ]
    rows = rows_from_config(cfg)
    assert len(rows) == 1
    assert math.isclose(rows[0].d, 0.3)


def test_seven_dof_chain_deterministic_and_bounded():
    dh = [
        _row(alpha=1.5708),
        _row(alpha=-1.5708),
        _row(alpha=1.5708, d=0.30),
        _row(alpha=-1.5708),
        _row(alpha=1.5708, d=0.28),
        _row(alpha=-1.5708),
        _row(d=0.10),
    ]
    q = [0.1, -0.2, 0.3, -0.4, 0.5, -0.6, 0.7]
    p1, _ = forward_kinematics(q, dh)
    p2, _ = forward_kinematics(q, dh)
    assert p1 == p2
    reach = 0.30 + 0.28 + 0.10
    assert math.sqrt(sum(c * c for c in p1)) <= reach + 1e-9


def test_euclidean_distance_mm():
    assert math.isclose(
        euclidean_distance_mm((0.0, 0.0, 0.0), (0.001, 0.0, 0.0)), 1.0, abs_tol=1e-9
    )
