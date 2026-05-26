"""Deterministic intent-to-command compiler (thesis core, VVUQ 04).

Compiles high-level phase-level intents into per-hand commands conforming to
``schemas/h2_command.schema.json``: a Cartesian fingertip-frame target plus 20
per-finger joint targets plus the grasp state. The compiler is deterministic and
seed-stable so the same intents always yield the same commands.

VVUQ 04 measures phase-step concordance between the compiled plan and the
annotated reference plan.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

from src.autonomy.llm_intent import Intent

# Per-grasp 20-DOF finger joint targets (radians), 5 fingers x 4 joints in the
# order [mcp_abduction, mcp_flexion, pip_flexion, dip_flexion] per finger.
GRASP_FINGER_TARGETS: dict[str, list[float]] = {
    "open": [0.0] * 20,
    "pinch": [
        0.0,
        0.6,
        0.5,
        0.3,
        0.0,
        0.7,
        0.6,
        0.4,
        0.0,
        0.1,
        0.0,
        0.0,
        0.0,
        0.1,
        0.0,
        0.0,
        0.0,
        0.1,
        0.0,
        0.0,
    ],
    "tripod": [
        0.0,
        0.6,
        0.5,
        0.3,
        0.0,
        0.7,
        0.6,
        0.4,
        0.0,
        0.7,
        0.6,
        0.4,
        0.0,
        0.2,
        0.1,
        0.0,
        0.0,
        0.2,
        0.1,
        0.0,
    ],
    "power": [
        0.2,
        1.0,
        1.0,
        0.8,
        0.1,
        1.1,
        1.0,
        0.8,
        0.1,
        1.1,
        1.0,
        0.8,
        0.1,
        1.1,
        1.0,
        0.8,
        0.1,
        1.1,
        1.0,
        0.8,
    ],
    "needle_driver": [
        0.0,
        0.8,
        0.7,
        0.5,
        0.0,
        0.9,
        0.8,
        0.5,
        0.0,
        0.9,
        0.8,
        0.5,
        0.0,
        0.3,
        0.2,
        0.1,
        0.0,
        0.3,
        0.2,
        0.1,
    ],
}

DEFAULT_FORCE_SOFT_CAP_N = 2.5


@dataclass
class Command:
    """One compiled per-hand command (conforms to h2_command.schema.json)."""

    tick: int
    hand_id: str
    phase: int
    tip_target: tuple[float, float, float]
    tip_orientation: tuple[float, float, float, float]
    finger_target: list[float]
    grasp_state: str
    velocity_scale: float = 1.0
    force_soft_cap_n: float = DEFAULT_FORCE_SOFT_CAP_N
    intent_id: str = ""

    def as_dict(self) -> dict:
        """Serialize to a schema-conformant dict."""
        return {
            "tick": self.tick,
            "hand_id": self.hand_id,
            "phase": self.phase,
            "tip_target": list(self.tip_target),
            "tip_orientation": list(self.tip_orientation),
            "finger_target": list(self.finger_target),
            "grasp_state": self.grasp_state,
            "velocity_scale": self.velocity_scale,
            "force_soft_cap_n": self.force_soft_cap_n,
            "intent_id": self.intent_id,
        }


def compile_intent(intent: Intent, tick: int = 0) -> Command:
    """Compile a single intent into a single deterministic command."""
    finger_target = list(GRASP_FINGER_TARGETS.get(intent.grasp, GRASP_FINGER_TARGETS["open"]))
    return Command(
        tick=tick,
        hand_id=intent.hand_id,
        phase=intent.phase,
        tip_target=intent.tip_target,
        tip_orientation=(0.0, 0.0, 0.0, 1.0),
        finger_target=finger_target,
        grasp_state=intent.grasp,
        velocity_scale=1.0,
        force_soft_cap_n=DEFAULT_FORCE_SOFT_CAP_N,
        intent_id=intent.intent_id,
    )


def compile_intents(intents: list[Intent], tick: int = 0) -> list[Command]:
    """Compile a list of intents into commands, preserving order."""
    return [compile_intent(intent, tick) for intent in intents]


def _within_tolerance(a: tuple[float, ...], b: tuple[float, ...], tol_mm: float) -> bool:
    """True when two tip targets agree within a Euclidean tolerance in mm."""
    return sum((ai - bi) ** 2 for ai, bi in zip(a, b, strict=False)) ** 0.5 <= tol_mm


def phase_step_concordance(
    compiled: list[Command],
    reference: list[Intent],
    tip_target_tolerance_mm: float = 2.0,
) -> float:
    """Fraction of reference intents matched by a compiled command.

    A match requires the same phase, hand, and grasp, and a tip target within the
    tolerance. This is the validation metric for VVUQ 04.
    """
    if not reference:
        return 1.0
    matched = 0
    for ref in reference:
        for cmd in compiled:
            if (
                cmd.phase == ref.phase
                and cmd.hand_id == ref.hand_id
                and cmd.grasp_state == ref.grasp
                and _within_tolerance(cmd.tip_target, ref.tip_target, tip_target_tolerance_mm)
            ):
                matched += 1
                break
    return matched / len(reference)
