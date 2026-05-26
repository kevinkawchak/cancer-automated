"""Per-finger force control and force limiting (VVUQ 02).

Tracks a commanded fingertip force toward a target while enforcing the IEC
80601-2-77 derived caps: per-fingertip soft 2.5 N and hard 3.0 N, and bimanual
cumulative soft 5.0 N and hard 6.0 N. Breaching a hard cap triggers an e-stop.
Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

PER_FINGERTIP_SOFT_N = 2.5
PER_FINGERTIP_HARD_N = 3.0
BIMANUAL_SOFT_N = 5.0
BIMANUAL_HARD_N = 6.0

_TRACK_GAIN = 0.6


@dataclass
class FingerForceCmd:
    """The force-control command for one fingertip at one tick."""

    target_n: float
    measured_n: float
    commanded_n: float
    clamped: bool
    soft_exceeded: bool
    estop: bool
    reason: str = ""


def track_force(target_n: float, measured_n: float) -> FingerForceCmd:
    """Drive the measured fingertip force toward a target under the force caps.

    A proportional step moves the command from the measured value toward the
    target. The command is clamped at the hard cap; a measured value at or above
    the hard cap triggers an e-stop.
    """
    estop = measured_n >= PER_FINGERTIP_HARD_N
    raw = measured_n + _TRACK_GAIN * (target_n - measured_n)
    commanded = min(max(raw, 0.0), PER_FINGERTIP_HARD_N)
    clamped = raw > PER_FINGERTIP_HARD_N
    soft_exceeded = commanded > PER_FINGERTIP_SOFT_N
    reason = ""
    if estop:
        reason = f"fingertip force {measured_n:.3f} N at or above hard cap {PER_FINGERTIP_HARD_N} N"
    elif clamped:
        reason = f"command clamped to hard cap {PER_FINGERTIP_HARD_N} N"
    elif soft_exceeded:
        reason = f"command {commanded:.3f} N above soft cap {PER_FINGERTIP_SOFT_N} N"
    return FingerForceCmd(
        target_n=target_n,
        measured_n=measured_n,
        commanded_n=round(commanded, 4),
        clamped=clamped,
        soft_exceeded=soft_exceeded,
        estop=estop,
        reason=reason,
    )


@dataclass
class BimanualForceCheck:
    """The cumulative cross-hand force check."""

    cumulative_n: float
    within_soft: bool
    within_hard: bool
    estop: bool


def bimanual_check(fingertip_forces: list[float]) -> BimanualForceCheck:
    """Check the summed cross-hand fingertip force against the bimanual caps."""
    cumulative = round(sum(max(0.0, f) for f in fingertip_forces), 4)
    return BimanualForceCheck(
        cumulative_n=cumulative,
        within_soft=cumulative <= BIMANUAL_SOFT_N,
        within_hard=cumulative <= BIMANUAL_HARD_N,
        estop=cumulative > BIMANUAL_HARD_N,
    )


def force_tracking_error(target_n: float, achieved_n: float) -> float:
    """Absolute force tracking error in newtons (VVUQ 02 validation metric)."""
    return abs(achieved_n - target_n)
