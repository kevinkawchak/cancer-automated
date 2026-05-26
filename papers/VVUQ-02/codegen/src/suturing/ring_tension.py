"""Anastomosis ring-tension control (VVUQ 07).

Holds the anastomosis ring tension at the PJ, HJ, and GJ targets within a plus or
minus 0.05 N band. When the tension drifts outside the band, the controller
commands the suturing hand and the presenting hand in opposite directions to
restore the target, the bimanual analogue of the PDAC arm-pair coordination.
Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import math
from dataclasses import dataclass

RING_TENSION_TARGETS_N = {
    "pancreaticojejunostomy": 0.45,
    "hepaticojejunostomy": 0.50,
    "gastrojejunostomy": 0.60,
}
RING_TENSION_TOLERANCE_N = 0.05
_RESTORE_GAIN = 0.5


@dataclass
class RingTensionCommand:
    """A bimanual ring-tension restoring command."""

    target_n: float
    measured_n: float
    in_band: bool
    suturing_hand_delta_n: float
    presenting_hand_delta_n: float


def within_band(
    measured_n: float, target_n: float, tolerance_n: float = RING_TENSION_TOLERANCE_N
) -> bool:
    """True when the measured ring tension is inside the tolerance band."""
    return abs(measured_n - target_n) <= tolerance_n


def restore(anastomosis_id: str, measured_n: float) -> RingTensionCommand:
    """Command opposing hand deltas to restore the target ring tension."""
    target = RING_TENSION_TARGETS_N[anastomosis_id]
    error = target - measured_n
    delta = _RESTORE_GAIN * error
    return RingTensionCommand(
        target_n=target,
        measured_n=measured_n,
        in_band=within_band(measured_n, target),
        suturing_hand_delta_n=round(delta, 4),
        presenting_hand_delta_n=round(-delta, 4),
    )


def ring_tension_rmse(target_n: float, measured_series: list[float]) -> float:
    """Root-mean-square error of a ring-tension series against the target."""
    if not measured_series:
        return 0.0
    sq = sum((m - target_n) ** 2 for m in measured_series)
    return round(math.sqrt(sq / len(measured_series)), 6)


def in_band_fraction(
    target_n: float, measured_series: list[float], tolerance_n: float = RING_TENSION_TOLERANCE_N
) -> float:
    """Fraction of a ring-tension series that stays inside the band."""
    if not measured_series:
        return 1.0
    inside = sum(1 for m in measured_series if within_band(m, target_n, tolerance_n))
    return inside / len(measured_series)
