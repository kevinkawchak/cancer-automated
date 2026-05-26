"""Bimanual suturing that realizes the anastomosis ring-tension targets (VVUQ 07).

Drives a per-stitch ring-tension series toward the target with the ring-tension
controller and reports the realized RMS error, the in-band fraction, and the
realized anastomosis grade. The grade taxonomy follows the PDAC baseline: PJ
grades A (subclinical), B (clinically relevant), C (severe); HJ leak absent or
present; GJ patency patent or delayed. Grounded in IEC 80601-2-77 and the Callery
Fistula Risk Score. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from src.suturing.ring_tension import (
    RING_TENSION_TARGETS_N,
    in_band_fraction,
    restore,
    ring_tension_rmse,
)

SUTURE_COUNTS = {
    "pancreaticojejunostomy": 16,
    "hepaticojejunostomy": 12,
    "gastrojejunostomy": 9,
}

GRADE_TAXONOMY = {
    "pancreaticojejunostomy": ("A", "B", "C"),
    "hepaticojejunostomy": ("absent", "present"),
    "gastrojejunostomy": ("patent", "delayed"),
}


@dataclass
class SutureResult:
    """The outcome of suturing one anastomosis."""

    anastomosis_id: str
    n_stitches: int
    ring_tension_rmse_n: float
    in_band_fraction: float
    realized_grade: str


def _realized_grade(anastomosis_id: str, rmse_n: float) -> str:
    """Map the ring-tension RMS error to the realized grade taxonomy."""
    grades = GRADE_TAXONOMY[anastomosis_id]
    if anastomosis_id == "pancreaticojejunostomy":
        if rmse_n <= 0.02:
            return grades[0]
        if rmse_n <= 0.05:
            return grades[1]
        return grades[2]
    # Two-grade anastomoses: the good grade unless the band is clearly missed.
    return grades[0] if rmse_n <= 0.05 else grades[1]


def suture_anastomosis(
    anastomosis_id: str,
    drift_amplitude_n: float = 0.01,
    seed: int = 20260525,
) -> SutureResult:
    """Suture one anastomosis under a ring-tension drift and report the outcome.

    Args:
        anastomosis_id: pancreaticojejunostomy, hepaticojejunostomy, or
            gastrojejunostomy.
        drift_amplitude_n: amplitude of the per-stitch ring-tension drift, one of
            the five sweep free parameters.
        seed: deterministic seed.

    Returns:
        A ``SutureResult`` with the realized RMS error, in-band fraction, and grade.
    """
    if anastomosis_id not in RING_TENSION_TARGETS_N:
        raise ValueError(f"unknown anastomosis: {anastomosis_id}")
    target = RING_TENSION_TARGETS_N[anastomosis_id]
    n = SUTURE_COUNTS[anastomosis_id]
    rng = random.Random((seed << 6) ^ hash(anastomosis_id) & 0xFFFFFF)
    measured: list[float] = []
    tension = target
    for _ in range(n):
        tension = tension + drift_amplitude_n * (rng.random() - 0.5) * 2.0
        cmd = restore(anastomosis_id, tension)
        # Apply the restoring delta toward the target for the next stitch.
        tension = tension + cmd.suturing_hand_delta_n
        measured.append(round(tension, 6))
    rmse = ring_tension_rmse(target, measured)
    return SutureResult(
        anastomosis_id=anastomosis_id,
        n_stitches=n,
        ring_tension_rmse_n=rmse,
        in_band_fraction=round(in_band_fraction(target, measured), 4),
        realized_grade=_realized_grade(anastomosis_id, rmse),
    )
