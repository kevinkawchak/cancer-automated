"""Grasp execution and slip detection (VVUQ 05).

Models grasping a human-designed instrument with one of the taxonomy grasps and
detects slip from a Coulomb friction condition: slip occurs when the tangential
load exceeds the available friction (mu times the summed normal grasp force).
Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

TAXONOMY = ("pinch", "tripod", "power", "needle_driver")

# Nominal number of contacting fingertips and a grasp-quality prior per grasp.
_GRASP_CONTACTS = {"pinch": 2, "tripod": 3, "power": 5, "needle_driver": 3}
_GRASP_QUALITY_PRIOR = {"pinch": 0.85, "tripod": 0.92, "power": 0.97, "needle_driver": 0.95}


@dataclass
class GraspResult:
    """The outcome of one grasp attempt."""

    taxonomy: str
    success: bool
    slip_detected: bool
    grasp_quality: float
    normal_force_n: float
    tangential_load_n: float
    friction_capacity_n: float


def grasp(
    taxonomy: str,
    normal_force_per_contact_n: float,
    tangential_load_n: float,
    friction_coefficient: float = 0.6,
) -> GraspResult:
    """Execute a grasp and report success and slip.

    Args:
        taxonomy: one of pinch, tripod, power, needle_driver.
        normal_force_per_contact_n: normal force at each contacting fingertip.
        tangential_load_n: tangential load the instrument imposes.
        friction_coefficient: Coulomb friction coefficient at the contact.

    Returns:
        A ``GraspResult`` with the slip decision and grasp quality.
    """
    if taxonomy not in TAXONOMY:
        raise ValueError(f"unknown grasp taxonomy: {taxonomy}")
    contacts = _GRASP_CONTACTS[taxonomy]
    normal_total = max(0.0, normal_force_per_contact_n) * contacts
    friction_capacity = friction_coefficient * normal_total
    slip = tangential_load_n > friction_capacity
    quality = _GRASP_QUALITY_PRIOR[taxonomy]
    if friction_capacity > 0:
        margin_ratio = min(1.0, max(0.0, 1.0 - tangential_load_n / friction_capacity))
        quality = round(quality * (0.5 + 0.5 * margin_ratio), 4)
    else:
        quality = 0.0
    return GraspResult(
        taxonomy=taxonomy,
        success=(not slip) and quality >= 0.5,
        slip_detected=slip,
        grasp_quality=quality,
        normal_force_n=round(normal_total, 4),
        tangential_load_n=round(tangential_load_n, 4),
        friction_capacity_n=round(friction_capacity, 4),
    )
