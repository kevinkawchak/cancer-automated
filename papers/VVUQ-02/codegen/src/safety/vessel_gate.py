"""Vascular no-fly gate for fingertip and instrument tips (VVUQ 06).

Ported from the PDAC 8-arm safety zone gate. Reads the per-hand tip position and
applies the five vessel safety zone gate per phase: clear, no-fly (50 percent
velocity), soft-warning (10 percent velocity), hard-stop (e-stop). Defends in
depth behind the 100 kHz vessel proximity sensor, which triggers the one-tick
(10 microsecond) hard-stop e-stop. VVUQ 06 requires zero hard-stop volume
breaches and is grounded in IEC 80601-2-77 and ISO 14971. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import math
from dataclasses import dataclass

Vec3 = tuple[float, float, float]

VESSELS = [
    {
        "name": "superior_mesenteric_vein",
        "start": (15.0, -25.0, -45.0),
        "end": (15.0, -65.0, -55.0),
        "hard_stop_r": 2.0,
        "soft_warning_r": 4.0,
        "no_fly_r": 6.0,
        "active_phases": {2, 4, 5, 8},
    },
    {
        "name": "portal_vein",
        "start": (5.0, -55.0, -55.0),
        "end": (5.0, -75.0, -50.0),
        "hard_stop_r": 2.0,
        "soft_warning_r": 4.0,
        "no_fly_r": 6.0,
        "active_phases": {2, 4, 5, 8},
    },
    {
        "name": "hepatic_artery_common",
        "start": (5.0, -60.0, -50.0),
        "end": (20.0, -65.0, -55.0),
        "hard_stop_r": 1.5,
        "soft_warning_r": 3.0,
        "no_fly_r": 5.0,
        "active_phases": {2, 4, 6, 8},
    },
    {
        "name": "celiac_axis",
        "start": (0.0, -65.0, -60.0),
        "end": (5.0, -70.0, -55.0),
        "hard_stop_r": 1.5,
        "soft_warning_r": 3.0,
        "no_fly_r": 5.0,
        "active_phases": {3, 4, 8},
    },
    {
        "name": "superior_mesenteric_artery",
        "start": (0.0, -35.0, -55.0),
        "end": (5.0, -65.0, -60.0),
        "hard_stop_r": 1.5,
        "soft_warning_r": 3.0,
        "no_fly_r": 5.0,
        "active_phases": {3, 4, 8},
    },
]

ACTIONS = {
    "clear": {"velocity_scale": 1.0, "force_soft_cap_n": 3.0, "e_stop": False},
    "no_fly": {"velocity_scale": 0.5, "force_soft_cap_n": 2.5, "e_stop": False},
    "soft_warning": {"velocity_scale": 0.1, "force_soft_cap_n": 1.5, "e_stop": False},
    "hard_stop": {"velocity_scale": 0.0, "force_soft_cap_n": 0.0, "e_stop": True},
}

HARD_STOP_E_STOP_LATENCY_US = 10.0


@dataclass
class GateResult:
    """The vessel gate verdict for one tip position."""

    vessel: str
    distance_mm: float
    action: str
    velocity_scale: float
    force_soft_cap_n: float
    e_stop: bool


def _distance_to_segment(p: Vec3, a: Vec3, b: Vec3) -> float:
    """Euclidean distance from a point to a line segment in 3D."""
    ax, ay, az = a
    bx, by, bz = b
    px, py, pz = p
    abx, aby, abz = bx - ax, by - ay, bz - az
    apx, apy, apz = px - ax, py - ay, pz - az
    ab2 = abx * abx + aby * aby + abz * abz
    if ab2 == 0.0:
        return math.dist(p, a)
    t = max(0.0, min(1.0, (apx * abx + apy * aby + apz * abz) / ab2))
    closest = (ax + t * abx, ay + t * aby, az + t * abz)
    return math.dist(p, closest)


def gate(tip_pos: Vec3, phase: int) -> GateResult:
    """Compute the safety zone action for a tip position in a given phase."""
    nearest_action = "clear"
    nearest_vessel = "none"
    nearest_distance = math.inf
    for v in VESSELS:
        if phase not in v["active_phases"]:
            continue
        d = _distance_to_segment(tip_pos, v["start"], v["end"])
        if d <= v["hard_stop_r"]:
            a = ACTIONS["hard_stop"]
            return GateResult(
                v["name"],
                round(d, 4),
                "hard_stop",
                a["velocity_scale"],
                a["force_soft_cap_n"],
                a["e_stop"],
            )
        if d <= v["soft_warning_r"] and nearest_action != "soft_warning":
            nearest_action, nearest_vessel, nearest_distance = "soft_warning", v["name"], d
        elif d <= v["no_fly_r"] and nearest_action == "clear":
            nearest_action, nearest_vessel, nearest_distance = "no_fly", v["name"], d
        elif d < nearest_distance and nearest_action == "clear":
            nearest_distance, nearest_vessel = d, v["name"]
    a = ACTIONS[nearest_action]
    dist = nearest_distance if nearest_distance != math.inf else -1.0
    return GateResult(
        nearest_vessel,
        round(dist, 4),
        nearest_action,
        a["velocity_scale"],
        a["force_soft_cap_n"],
        a["e_stop"],
    )


def count_hard_stop_violations(path: list[Vec3], phase: int) -> int:
    """Count tip positions on a path that breach a hard-stop volume (must be 0)."""
    return sum(1 for p in path if gate(p, phase).action == "hard_stop")
