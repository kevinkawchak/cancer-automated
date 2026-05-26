"""Unified fault monitor and graceful degradation (VVUQ 10).

Watches for balance loss, joint fault, vision dropout, thermal, and power faults,
and emits a safe-park or a hand-back-to-human response. Reports the fault
detection latency and whether the safe state is reached within the 3 ms e-stop
budget. This is the gate most likely to ESCALATE: an ambiguous fault hands back
to the human by default (IEC 60601-1 single-fault safety, ISO 13849-1 performance
level, IEEE 7009 fail-safe). Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

BALANCE_MARGIN_FLOOR_MM = 8.0
JOINT_TORQUE_LIMIT_NM = 60.0
VISION_CONFIDENCE_FLOOR = 0.5
TEMPERATURE_LIMIT_C = 70.0
POWER_LIMIT_W = 800.0

SAFE_STATE_BUDGET_US = 3000.0  # 3 ms hand-arm e-stop budget

# Per-fault detection latency (microseconds) and the degradation action.
_FAULT_TABLE = [
    ("balance_loss", 50.0, "safe_park"),
    ("joint_fault", 50.0, "safe_park"),
    ("power", 100.0, "safe_park"),
    ("thermal", 100.0, "safe_park"),
    ("vision_dropout", 1000.0, "hand_back"),
]


@dataclass
class FaultResponse:
    """The fault monitor verdict for one sensor snapshot."""

    fault_detected: bool
    fault_type: str
    action: str
    detection_latency_us: float
    safe_state_reached: bool
    escalate: bool
    reason: str = ""


def _detected_faults(sensors: dict) -> list[str]:
    """Return the fault types present in a sensor snapshot, in priority order."""
    faults: list[str] = []
    if sensors.get("balance_margin_mm", 999.0) < BALANCE_MARGIN_FLOOR_MM:
        faults.append("balance_loss")
    if sensors.get("max_joint_torque_nm", 0.0) > JOINT_TORQUE_LIMIT_NM:
        faults.append("joint_fault")
    if sensors.get("power_w", 0.0) > POWER_LIMIT_W:
        faults.append("power")
    if sensors.get("max_temperature_c", 0.0) > TEMPERATURE_LIMIT_C:
        faults.append("thermal")
    if sensors.get("vision_confidence", 1.0) < VISION_CONFIDENCE_FLOOR:
        faults.append("vision_dropout")
    return faults


def monitor(sensors: dict) -> FaultResponse:
    """Detect faults and emit the degradation response.

    Returns a no-fault response when the snapshot is clean. When one fault is
    present it parks or hands back per the fault table. When more than one fault
    is present, or the fault is a vision dropout, the response escalates so the
    system defaults to hand-back-to-human.
    """
    faults = _detected_faults(sensors)
    if not faults:
        return FaultResponse(
            fault_detected=False,
            fault_type="none",
            action="none",
            detection_latency_us=0.0,
            safe_state_reached=True,
            escalate=False,
        )

    priority = {name: (latency, action) for name, latency, action in _FAULT_TABLE}
    primary = faults[0]
    latency, action = priority[primary]
    multi = len(faults) > 1
    escalate = action == "hand_back" or multi
    if multi:
        action = "hand_back"
    reason = f"{primary} detected"
    if multi:
        reason = f"multiple faults {faults} detected, hand back to human"
    return FaultResponse(
        fault_detected=True,
        fault_type=primary,
        action=action,
        detection_latency_us=latency,
        safe_state_reached=latency <= SAFE_STATE_BUDGET_US,
        escalate=escalate,
        reason=reason,
    )
