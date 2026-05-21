"""Stage 2: code runs physical AI in lights-off factories.

A lights-off factory runs autonomously with no humans on the floor. This module
is a reference controller that gates an autonomous run behind safety interlocks,
distributes tasks across cells, and emergency-stops the line when cumulative
faults exceed the budget. It is a simulation and planning reference, disabled by
default in ``configs/pipeline_config.yaml``; any real deployment must pass the
VVUQ gate and your institution's safety validation first. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable


class FactoryState(str, Enum):
    """Lifecycle state of the lights-off line."""

    DARK = "dark"  # lights off, no humans on the floor, idle
    READY = "ready"
    RUNNING = "running"
    FAULT = "fault"
    ESTOP = "estop"


@dataclass
class Interlock:
    """A safety interlock that must be satisfied before an autonomous run."""

    name: str
    satisfied: bool
    detail: str = ""


def default_interlocks() -> list[Interlock]:
    """The interlocks that must hold before a lights-off run begins."""
    return [
        Interlock("estop_armed", True),
        Interlock("perimeter_clear", True),
        Interlock("vvuq_gate_online", True),
        Interlock("human_oversight_remote", True),
    ]


@dataclass
class RunReport:
    """The outcome of an autonomous batch run."""

    state: str
    blocked: bool
    faults: int = 0
    unsatisfied: list = field(default_factory=list)
    per_cell: dict = field(default_factory=dict)


class LightsOffFactory:
    """Autonomous, safety-gated controller for a lights-off factory line."""

    def __init__(
        self,
        cell_ids: list[str],
        interlocks: list[Interlock] | None = None,
        max_cumulative_faults: int = 1,
    ) -> None:
        if not cell_ids:
            raise ValueError("at least one cell is required")
        self.cell_ids = list(cell_ids)
        self.interlocks = interlocks if interlocks is not None else default_interlocks()
        self.max_cumulative_faults = max_cumulative_faults
        self.state = FactoryState.DARK

    def unsatisfied(self) -> list[str]:
        return [lock.name for lock in self.interlocks if not lock.satisfied]

    def ready(self) -> bool:
        return not self.unsatisfied()

    def run_batch(self, tasks: list, executor: Callable[[str, object], bool]) -> RunReport:
        """Run a batch of tasks autonomously across the cells.

        Args:
            tasks: the work items to execute.
            executor: callable ``(cell_id, task) -> bool`` that returns True on
                a successful task and False on a fault.
        """
        if not self.ready():
            self.state = FactoryState.FAULT
            return RunReport(state=self.state.value, blocked=True, unsatisfied=self.unsatisfied())

        self.state = FactoryState.RUNNING
        per_cell = {cell: {"completed": 0, "faulted": 0} for cell in self.cell_ids}
        faults = 0
        for index, task in enumerate(tasks):
            cell = self.cell_ids[index % len(self.cell_ids)]
            if executor(cell, task):
                per_cell[cell]["completed"] += 1
            else:
                per_cell[cell]["faulted"] += 1
                faults += 1
                if faults > self.max_cumulative_faults:
                    self.state = FactoryState.ESTOP
                    break

        if self.state != FactoryState.ESTOP:
            self.state = FactoryState.DARK
        return RunReport(state=self.state.value, blocked=False, faults=faults, per_cell=per_cell)
