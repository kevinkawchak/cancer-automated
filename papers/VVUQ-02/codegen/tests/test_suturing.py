"""Tests for ring-tension control and bimanual suturing (VVUQ 07).

LICENSE: MIT
"""

from __future__ import annotations

import pytest

from src.suturing.bimanual_suture import GRADE_TAXONOMY, suture_anastomosis
from src.suturing.ring_tension import (
    RING_TENSION_TARGETS_N,
    in_band_fraction,
    restore,
    ring_tension_rmse,
    within_band,
)


def test_targets():
    assert RING_TENSION_TARGETS_N["pancreaticojejunostomy"] == 0.45
    assert RING_TENSION_TARGETS_N["hepaticojejunostomy"] == 0.50
    assert RING_TENSION_TARGETS_N["gastrojejunostomy"] == 0.60


def test_within_band():
    assert within_band(0.46, 0.45)
    assert within_band(0.40, 0.45)
    assert not within_band(0.55, 0.45)


def test_restore_opposing_deltas():
    cmd = restore("pancreaticojejunostomy", 0.40)
    assert cmd.suturing_hand_delta_n == pytest.approx(-cmd.presenting_hand_delta_n)
    assert cmd.suturing_hand_delta_n > 0  # tension below target, pull up


def test_ring_tension_rmse_perfect_is_zero():
    assert ring_tension_rmse(0.45, [0.45, 0.45, 0.45]) == 0.0


def test_ring_tension_rmse_positive_for_offset():
    assert ring_tension_rmse(0.45, [0.55, 0.55]) == pytest.approx(0.10, abs=1e-6)


def test_in_band_fraction():
    assert in_band_fraction(0.45, [0.45, 0.46, 0.60]) == pytest.approx(2 / 3)


def test_suture_pj_low_drift_grade_a():
    result = suture_anastomosis("pancreaticojejunostomy", drift_amplitude_n=0.005)
    assert result.realized_grade == "A"
    assert result.in_band_fraction == 1.0
    assert result.n_stitches == 16


def test_suture_pj_high_drift_worse_grade():
    result = suture_anastomosis("pancreaticojejunostomy", drift_amplitude_n=0.2)
    assert result.realized_grade in {"B", "C"}
    assert result.ring_tension_rmse_n > 0.02


def test_suture_deterministic():
    a = suture_anastomosis("hepaticojejunostomy", drift_amplitude_n=0.01)
    b = suture_anastomosis("hepaticojejunostomy", drift_amplitude_n=0.01)
    assert a == b


def test_suture_unknown_raises():
    with pytest.raises(ValueError):
        suture_anastomosis("colostomy")


def test_grade_taxonomy():
    assert GRADE_TAXONOMY["pancreaticojejunostomy"] == ("A", "B", "C")
    assert GRADE_TAXONOMY["hepaticojejunostomy"] == ("absent", "present")
    assert GRADE_TAXONOMY["gastrojejunostomy"] == ("patent", "delayed")
