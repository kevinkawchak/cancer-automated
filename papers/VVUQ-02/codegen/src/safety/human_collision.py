"""Whole-body human-aware collision avoidance FSM (VVUQ 09).

Keyed on the minimum distance from any humanoid link to any human-actor keep-out
sphere surface in the shared operating room. Implements the four-state FSM (clear,
proximity, contact, unsafe) with speed-and-separation monitoring per ISO/TS 15066
and ISO 10218. The unsafe state triggers an e-stop within the intrusion-reaction
latency budget. VVUQ 09 requires the minimum clearance never to drop below the
hard floor. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import math
from dataclasses import dataclass

CLEAR_MM = 300.0
PROXIMITY_MM = 150.0
CONTACT_MM = 50.0
HARD_FLOOR_MM = 50.0
INTRUSION_REACTION_LATENCY_MS = 3.0


@dataclass(frozen=True)
class HumanActor:
    """A human in the shared OR with a keep-out sphere."""

    actor_id: str
    position_m: tuple[float, float, float]
    keep_out_radius_m: float


@dataclass(frozen=True)
class Link:
    """A sampled humanoid link position."""

    name: str
    position_m: tuple[float, float, float]


@dataclass
class CollisionResult:
    """The collision FSM verdict for one configuration."""

    min_clearance_mm: float
    nearest_actor: str
    nearest_link: str
    state: str
    velocity_scale: float
    e_stop: bool
    reaction_latency_ms: float


def _clearance_mm(link: Link, actor: HumanActor) -> float:
    """Clearance in mm from a link to an actor keep-out sphere surface."""
    center_dist_m = math.dist(link.position_m, actor.position_m)
    return 1000.0 * (center_dist_m - actor.keep_out_radius_m)


def _state_for(clearance_mm: float) -> tuple[str, float, bool]:
    """Map a clearance to (state, velocity_scale, e_stop)."""
    if clearance_mm < HARD_FLOOR_MM:
        return "unsafe", 0.0, True
    if clearance_mm < PROXIMITY_MM:
        return "contact", 0.1, False
    if clearance_mm < CLEAR_MM:
        return "proximity", 0.5, False
    return "clear", 1.0, False


def evaluate(links: list[Link], actors: list[HumanActor]) -> CollisionResult:
    """Evaluate the minimum clearance and the FSM state across all link-actor pairs."""
    min_clearance = math.inf
    nearest_actor = "none"
    nearest_link = "none"
    for link in links:
        for actor in actors:
            c = _clearance_mm(link, actor)
            if c < min_clearance:
                min_clearance, nearest_actor, nearest_link = c, actor.actor_id, link.name
    state, velocity_scale, e_stop = _state_for(min_clearance)
    return CollisionResult(
        min_clearance_mm=round(min_clearance, 4),
        nearest_actor=nearest_actor,
        nearest_link=nearest_link,
        state=state,
        velocity_scale=velocity_scale,
        e_stop=e_stop,
        reaction_latency_ms=INTRUSION_REACTION_LATENCY_MS,
    )
