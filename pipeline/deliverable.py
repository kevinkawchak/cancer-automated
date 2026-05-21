"""Core data model for a daily deliverable flowing through the pipeline.

A ``Deliverable`` carries the artifacts produced by each of the five established
methods (instruction generation, code generation, code execution, paper
assembly) and the per-stage results. The model is pure standard library so it
imports and tests cleanly without any heavy dependency.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional


class Stage(str, Enum):
    """The ordered stages of the daily-deliverable pipeline."""

    INSTRUCTION = "instruction"
    CODEGEN = "codegen"
    EXECUTION = "execution"
    PAPER = "paper"


class StageStatus(str, Enum):
    """Lifecycle status of a single stage."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"
    BLOCKED = "blocked"


# Canonical execution order for the established methods.
STAGE_ORDER: list[Stage] = [Stage.INSTRUCTION, Stage.CODEGEN, Stage.EXECUTION, Stage.PAPER]


@dataclass
class Artifact:
    """A single produced file-like artifact (instructions, code, log, paper)."""

    name: str
    kind: str
    content: str

    @property
    def size_bytes(self) -> int:
        return len(self.content.encode("utf-8"))


@dataclass
class StageResult:
    """The outcome of running one stage."""

    stage: Stage
    status: StageStatus
    artifacts: list[Artifact] = field(default_factory=list)
    log: str = ""
    duration_s: float = 0.0

    @property
    def ok(self) -> bool:
        return self.status == StageStatus.COMPLETE


@dataclass
class Deliverable:
    """A daily deliverable and the results of every stage that produced it."""

    deliverable_id: str
    title: str
    topic: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    results: dict[Stage, StageResult] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def record(self, result: StageResult) -> None:
        """Store the result of a stage, keyed by stage."""
        self.results[result.stage] = result

    def artifact(self, kind: str) -> Optional[Artifact]:
        """Return the first artifact of a given kind, or None."""
        for result in self.results.values():
            for art in result.artifacts:
                if art.kind == kind:
                    return art
        return None

    def all_artifacts(self) -> list[Artifact]:
        """Return every artifact across every stage."""
        collected: list[Artifact] = []
        for result in self.results.values():
            collected.extend(result.artifacts)
        return collected

    @property
    def complete(self) -> bool:
        """True only when all four established methods completed successfully."""
        return all(stage in self.results and self.results[stage].ok for stage in STAGE_ORDER)

    def summary(self) -> dict[str, Any]:
        """Return a compact, serializable summary of the deliverable."""
        return {
            "deliverable_id": self.deliverable_id,
            "title": self.title,
            "topic": self.topic,
            "created_at": self.created_at,
            "complete": self.complete,
            "stages": {
                stage.value: {
                    "status": self.results[stage].status.value,
                    "artifacts": [art.name for art in self.results[stage].artifacts],
                    "bytes": sum(art.size_bytes for art in self.results[stage].artifacts),
                }
                for stage in STAGE_ORDER
                if stage in self.results
            },
        }
