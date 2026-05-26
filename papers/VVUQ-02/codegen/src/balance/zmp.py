"""Zero-moment-point stability margin (VVUQ 03).

Computes the ZMP from the centre-of-mass state using the linear inverted-pendulum
(cart-table) model and the signed distance from the ZMP to the support-polygon
edge. A standing humanoid can fall over where a fixed coelomic arm cannot, so this
margin is safety-critical, grounded in ISO 13482 stability and fall prevention.
Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import math

GRAVITY = 9.81

# Default double-support polygon corners in metres (x forward, y left), from
# config/balance_model.yaml.
DEFAULT_SUPPORT_POLYGON = [
    (0.13, 0.175),
    (0.13, -0.175),
    (-0.13, -0.175),
    (-0.13, 0.175),
]

Point = tuple[float, float]


def compute_zmp(
    com_xy: Point,
    com_z: float,
    com_accel_xy: Point,
    g: float = GRAVITY,
) -> Point:
    """ZMP from the cart-table model: zmp = com - (com_z / g) * com_accel."""
    zx = com_xy[0] - (com_z / g) * com_accel_xy[0]
    zy = com_xy[1] - (com_z / g) * com_accel_xy[1]
    return (zx, zy)


def support_polygon_margin_mm(point: Point, polygon: list[Point] | None = None) -> float:
    """Signed distance (mm) from a point to the support polygon edge.

    Positive when the point is inside the convex polygon (distance to the nearest
    edge), negative when outside.
    """
    poly = polygon or DEFAULT_SUPPORT_POLYGON
    n = len(poly)
    area2 = sum(
        poly[i][0] * poly[(i + 1) % n][1] - poly[(i + 1) % n][0] * poly[i][1] for i in range(n)
    )
    ccw = area2 > 0.0
    inside = True
    min_dist = math.inf
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        ex, ey = x2 - x1, y2 - y1
        px, py = point[0] - x1, point[1] - y1
        cross = ex * py - ey * px
        signed = cross if ccw else -cross
        if signed < 0.0:
            inside = False
        edge_len = math.hypot(ex, ey)
        dist = abs(cross) / edge_len if edge_len > 0 else math.inf
        min_dist = min(min_dist, dist)
    margin_m = min_dist if inside else -min_dist
    return round(margin_m * 1000.0, 4)


def zmp_margin(
    com_xy: Point,
    com_z: float,
    com_accel_xy: Point,
    polygon: list[Point] | None = None,
    g: float = GRAVITY,
) -> float:
    """ZMP stability margin in mm for a centre-of-mass state."""
    zmp = compute_zmp(com_xy, com_z, com_accel_xy, g)
    return support_polygon_margin_mm(zmp, polygon)
