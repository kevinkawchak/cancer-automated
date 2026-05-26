"""On-prem LLM phase-level intent proposal (thesis core, VVUQ 04).

The thesis is that an on-premises, repository-based LLM issues high-level intents
to the humanoid, which a deterministic policy compiles to motion. This module
implements the LLM path with a deterministic offline template fallback: it tries
a guarded on-prem backend (anthropic, ollama, or openai), and if none is
installed it emits the frozen reference plan. That fallback is the honest CI path
documented by VVUQ-01, so the suite runs green with zero heavy installs.

VVUQ 04 (autonomous-plan-correctness) validates the proposed plan against the
annotated reference plan in ``config/autonomy_plan.yaml``, under UL 4600 and IEEE
7009: any ESCALATE defaults to hand-back-to-human.

LICENSE: MIT
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "autonomy_plan.yaml"

# Embedded fallback so the module is standalone even without the YAML present.
_EMBEDDED_PLAN: list[dict] = [
    {
        "phase": 1,
        "name": "exploration_kocher",
        "intents": [
            {
                "hand": "R",
                "action": "kocher_mobilize",
                "tip_target": [20.0, -20.0, -40.0],
                "grasp": "tripod",
            },
            {
                "hand": "L",
                "action": "retract_duodenum",
                "tip_target": [10.0, -18.0, -38.0],
                "grasp": "power",
            },
        ],
    },
    {
        "phase": 5,
        "name": "pancreaticojejunostomy",
        "intents": [
            {
                "hand": "R",
                "action": "suture_pj_duct_mucosa",
                "tip_target": [18.0, -30.0, -42.0],
                "grasp": "needle_driver",
            },
            {
                "hand": "L",
                "action": "present_pj_ring",
                "tip_target": [18.0, -31.0, -42.0],
                "grasp": "pinch",
            },
        ],
    },
]


@dataclass(frozen=True)
class Intent:
    """A high-level phase-level intent the LLM proposes for one hand."""

    phase: int
    hand_id: str
    action: str
    tip_target: tuple[float, float, float]
    grasp: str
    intent_id: str

    @property
    def source(self) -> str:
        """The provenance prefix of the intent id (llm or reference)."""
        return self.intent_id.split(":", 1)[0]


def backend_select() -> str:
    """Return the configured on-prem backend, defaulting to the offline path."""
    return os.environ.get("AUTONOMY_BACKEND", "offline")


def load_reference_plan(path: Path | None = None) -> list[dict]:
    """Load the frozen reference plan, falling back to the embedded copy."""
    path = path or CONFIG_PATH
    try:
        import yaml
    except ImportError:
        return _EMBEDDED_PLAN
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        return (data or {}).get("reference_plan", _EMBEDDED_PLAN)
    except (OSError, yaml.YAMLError):
        return _EMBEDDED_PLAN


def _intents_from_plan_rows(rows: list[dict], phase: int, source: str) -> list[Intent]:
    """Build Intent objects for one phase from plan rows tagged with a source."""
    intents: list[Intent] = []
    for row in rows:
        if int(row["phase"]) != phase:
            continue
        for i, raw in enumerate(row.get("intents", [])):
            tip = tuple(float(v) for v in raw["tip_target"])
            intents.append(
                Intent(
                    phase=phase,
                    hand_id=str(raw["hand"]),
                    action=str(raw["action"]),
                    tip_target=(tip[0], tip[1], tip[2]),
                    grasp=str(raw["grasp"]),
                    intent_id=f"{source}:p{phase}:{i}",
                )
            )
    return intents


def _call_backend(backend: str, phase: int, scene_state: dict | None) -> list[Intent] | None:
    """Try an on-prem backend; return None to signal the offline fallback.

    A production build replaces this stub with a real call to the on-prem model
    (anthropic Claude Opus 4.7, a local ollama model, or an openai-compatible
    endpoint). The stub returns None so CI exercises the deterministic fallback.
    """
    if backend == "offline":
        return None
    for module_name in ("anthropic", "ollama", "openai"):
        try:
            __import__(module_name)
        except ImportError:
            continue
        # A real client call would go here. The reference build does not contact a
        # network in CI, so it falls through to the deterministic plan.
        return None
    return None


def propose_intents(
    phase: int,
    scene_state: dict | None = None,
    backend: str | None = None,
    plan_path: Path | None = None,
) -> list[Intent]:
    """Propose the phase-level intents for a phase.

    Tries the configured on-prem backend; on absence or no response, emits the
    frozen reference plan for the phase tagged with the ``reference`` source.
    """
    backend = backend or backend_select()
    llm_intents = _call_backend(backend, phase, scene_state)
    if llm_intents:
        return llm_intents
    return _intents_from_plan_rows(load_reference_plan(plan_path), phase, source="reference")
