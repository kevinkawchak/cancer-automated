"""Instrument pick, place, and bimanual handover (VVUQ 05).

Models swapping a human-designed instrument between the two hands. The swap-time
analogue is 200 ms, matching the PDAC tool-changer swap. A handover succeeds when
the receiving grasp is stable and no slip is detected during the transfer.
Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

from src.hands.grasp import GraspResult, grasp

SWAP_TIME_MS = 200.0


@dataclass
class HandoverResult:
    """The outcome of an instrument handover."""

    instrument: str
    from_hand: str
    to_hand: str
    duration_ms: float
    success: bool
    slip_detected: bool
    receiving_grasp_quality: float


def handover(
    instrument: str,
    from_hand: str,
    to_hand: str,
    receiving_taxonomy: str = "tripod",
    normal_force_per_contact_n: float = 2.0,
    tangential_load_n: float = 1.0,
    swap_time_ms: float = SWAP_TIME_MS,
) -> HandoverResult:
    """Transfer an instrument from one hand to the other and report the outcome."""
    if from_hand == to_hand:
        raise ValueError("from_hand and to_hand must differ")
    receiving: GraspResult = grasp(
        receiving_taxonomy, normal_force_per_contact_n, tangential_load_n
    )
    return HandoverResult(
        instrument=instrument,
        from_hand=from_hand,
        to_hand=to_hand,
        duration_ms=swap_time_ms,
        success=receiving.success,
        slip_detected=receiving.slip_detected,
        receiving_grasp_quality=receiving.grasp_quality,
    )
