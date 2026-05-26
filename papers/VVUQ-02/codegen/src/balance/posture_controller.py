"""Posture controller that holds the ZMP margin above the floor (VVUQ 03).

Given a centre-of-mass state and an external reaction wrench from the surgical
hands, the controller computes the induced ZMP margin and, when the margin falls
below the 8 mm floor, applies an ankle-strategy correction that scales the
admitted reaction force to recover. Reports the resulting balance state. Pure
standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

from src.balance.zmp import zmp_margin

STABILITY_FLOOR_MM = 8.0
WARNING_MM = 15.0
DEFAULT_MASS_KG = 47.0
DEFAULT_COM_Z_M = 0.78


@dataclass
class PostureCommand:
    """The posture correction and the resulting balance assessment."""

    margin_mm: float
    corrected_margin_mm: float
    admitted_force_scale: float
    balance_state: str
    estop: bool


def _state_for_margin(margin_mm: float) -> str:
    """Map a margin to a balance state."""
    if margin_mm < 0.0:
        return "fall"
    if margin_mm < STABILITY_FLOOR_MM:
        return "recovering"
    if margin_mm < WARNING_MM:
        return "warning"
    return "stable"


def stabilize(
    com_xy: tuple[float, float],
    external_force_xy: tuple[float, float],
    com_z: float = DEFAULT_COM_Z_M,
    mass_kg: float = DEFAULT_MASS_KG,
    polygon=None,
) -> PostureCommand:
    """Compute the ZMP margin under an external force and recover if needed.

    The external force induces a centre-of-mass acceleration ``F / m``. If the
    resulting ZMP margin is below the floor, the controller reduces the admitted
    reaction force in proportion to the shortfall (an ankle-strategy analogue)
    and recomputes the margin. A margin that stays negative triggers an e-stop.
    """
    accel = (external_force_xy[0] / mass_kg, external_force_xy[1] / mass_kg)
    margin = zmp_margin(com_xy, com_z, accel, polygon)

    scale = 1.0
    corrected = margin
    if margin < STABILITY_FLOOR_MM:
        # Reduce admitted force until the projected margin reaches the floor.
        for trial in (0.75, 0.5, 0.25, 0.1, 0.0):
            scaled_accel = (accel[0] * trial, accel[1] * trial)
            corrected = zmp_margin(com_xy, com_z, scaled_accel, polygon)
            scale = trial
            if corrected >= STABILITY_FLOOR_MM:
                break

    state = _state_for_margin(corrected)
    return PostureCommand(
        margin_mm=margin,
        corrected_margin_mm=corrected,
        admitted_force_scale=scale,
        balance_state=state,
        estop=corrected < 0.0,
    )
