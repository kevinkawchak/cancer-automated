"""Stage 2: hybrid surgery and medicine first pilot.

This module models a hybrid pilot that combines a robotic surgical procedure
with an adjuvant medicine regimen into a single planned timeline, analogous to
the 2030 PDAC 60-second robotic Whipple plus Daraxonrasib simulation in the
robotic-surgeries repository. It is a planning and simulation reference only.
Any real pilot requires VVUQ clearance, human oversight, IRB approval, and
regulatory authorization. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SurgeryPlan:
    """The robotic surgical phase of the pilot."""

    name: str
    duration_s: float
    arms: int


@dataclass
class MedicinePlan:
    """The adjuvant medicine phase of the pilot."""

    name: str
    cycles: int
    cycle_days: int


@dataclass
class PhaseEvent:
    """One event on the combined pilot timeline."""

    day: int
    phase: str
    description: str


@dataclass
class HybridPilot:
    """A hybrid surgery and medicine pilot timeline and summary."""

    surgery: SurgeryPlan
    medicine: MedicinePlan
    requires_human_oversight: bool = True

    def timeline(self) -> list:
        """Return the ordered timeline: surgery on day 0, then medicine cycles."""
        events: list = [
            PhaseEvent(
                day=0,
                phase="surgery",
                description=f"{self.surgery.name}: {self.surgery.arms}-arm procedure, {self.surgery.duration_s:.0f} s",
            )
        ]
        for cycle in range(1, self.medicine.cycles + 1):
            events.append(
                PhaseEvent(
                    day=cycle * self.medicine.cycle_days,
                    phase="medicine",
                    description=f"{self.medicine.name}: adjuvant cycle {cycle}",
                )
            )
        return events

    @property
    def regimen_days(self) -> int:
        return self.medicine.cycles * self.medicine.cycle_days

    def summary(self) -> dict:
        return {
            "surgery": self.surgery.name,
            "surgery_seconds": self.surgery.duration_s,
            "surgery_arms": self.surgery.arms,
            "medicine": self.medicine.name,
            "regimen_days": self.regimen_days,
            "events": len(self.timeline()),
            "requires_human_oversight": self.requires_human_oversight,
        }


def default_pilot() -> HybridPilot:
    """A reference pilot analogous to the 2030 PDAC Whipple plus Daraxonrasib case."""
    return HybridPilot(
        surgery=SurgeryPlan(name="Robotic Whipple (60 second)", duration_s=60.0, arms=8),
        medicine=MedicinePlan(name="Daraxonrasib (adjuvant)", cycles=6, cycle_days=28),
    )
