"""Forward kinematics for the 2 x 7-DOF H2-Surgical 1.0 arms.

Pure standard library (uses ``math`` only) so the core runs with zero heavy
installs. Uses the standard Denavit-Hartenberg convention. The fingertip and
hand-reference tip pose produced here is the input to VVUQ 01
(bimanual-handeye-servo), which validates closed-loop placement against an
independent optical-tracker reference.

LICENSE: MIT
"""

from __future__ import annotations

import math
from dataclasses import dataclass

Matrix = list[list[float]]
Vec3 = tuple[float, float, float]


@dataclass(frozen=True)
class DHRow:
    """One Denavit-Hartenberg row for one joint."""

    a: float
    alpha: float
    d: float
    theta_offset: float
    q_min: float
    q_max: float


def identity4() -> Matrix:
    """Return a 4x4 identity matrix."""
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def matmul4(a: Matrix, b: Matrix) -> Matrix:
    """Multiply two 4x4 matrices."""
    out = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            out[i][j] = sum(a[i][k] * b[k][j] for k in range(4))
    return out


def dh_transform(row: DHRow, q: float) -> Matrix:
    """Build the 4x4 homogeneous transform for a single DH joint at angle q."""
    theta = q + row.theta_offset
    ct, st = math.cos(theta), math.sin(theta)
    ca, sa = math.cos(row.alpha), math.sin(row.alpha)
    return [
        [ct, -st * ca, st * sa, row.a * ct],
        [st, ct * ca, -ct * sa, row.a * st],
        [0.0, sa, ca, row.d],
        [0.0, 0.0, 0.0, 1.0],
    ]


def clamp_to_limits(q: list[float], dh: list[DHRow]) -> list[float]:
    """Clamp each joint angle to its configured limits."""
    return [min(max(qi, row.q_min), row.q_max) for qi, row in zip(q, dh, strict=False)]


def forward_kinematics(
    q: list[float],
    dh: list[DHRow],
    base_offset_m: Vec3 = (0.0, 0.0, 0.0),
) -> tuple[Vec3, Matrix]:
    """Compute the tip position (metres) and 3x3 rotation for an arm chain.

    Args:
        q: joint angles in radians, one per DH row.
        dh: the DH rows for the chain.
        base_offset_m: translation of the arm base in the world frame.

    Returns:
        A tuple of the tip position (x, y, z) in metres and the 3x3 rotation
        matrix of the tip frame.
    """
    if len(q) != len(dh):
        raise ValueError(f"q has {len(q)} angles but chain has {len(dh)} joints")
    t = identity4()
    for row, qi in zip(dh, q, strict=False):
        t = matmul4(t, dh_transform(row, qi))
    pos = (
        t[0][3] + base_offset_m[0],
        t[1][3] + base_offset_m[1],
        t[2][3] + base_offset_m[2],
    )
    rot = [[t[i][j] for j in range(3)] for i in range(3)]
    return pos, rot


def rows_from_config(dh_dicts: list[dict]) -> list[DHRow]:
    """Build DHRow objects from the list-of-dicts in config/h2_kinematics.yaml."""
    return [
        DHRow(
            a=float(d["a"]),
            alpha=float(d["alpha"]),
            d=float(d["d"]),
            theta_offset=float(d["theta_offset"]),
            q_min=float(d["q_min"]),
            q_max=float(d["q_max"]),
        )
        for d in dh_dicts
    ]


def euclidean_distance_mm(a: Vec3, b: Vec3) -> float:
    """Euclidean distance between two points given in metres, returned in mm."""
    return 1000.0 * math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b, strict=False)))
