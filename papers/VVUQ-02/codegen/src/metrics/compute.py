"""6-component composite score with the 10-gate gating overlay.

The composite reuses the PDAC frozen weights (Quality 0.30, Time 0.20, Cost 0.15,
Safety 0.15, Patient experience 0.05, Anastomosis quality 0.15). The VVUQ overlay
makes the assurance layer decisive: the composite is reported only when all 10
gates ACCEPT; otherwise the report shows the BLOCK or ESCALATE roll-up and the
composite is withheld. This operationalizes the thesis that assurance, not the
score, is the decision-bearing part. Pure standard library plus optional click.

LICENSE: MIT
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

WEIGHTS = {
    "quality": 0.30,
    "time": 0.20,
    "cost": 0.15,
    "safety": 0.15,
    "patient_experience": 0.05,
    "anastomosis_quality": 0.15,
}


@dataclass
class GatedComposite:
    """The composite score with the gate roll-up overlay."""

    components: dict
    composite_score: float | None
    gates_all_accepted: bool
    composite_reported: bool
    gate_rollup: dict = field(default_factory=dict)


def composite_score(components: dict) -> float:
    """Apply the frozen composite weights and return a 0 to 100 scalar."""
    return round(sum(WEIGHTS[k] * float(components[k]) for k in WEIGHTS), 3)


def gated_composite(components: dict, gate_rollup: dict) -> GatedComposite:
    """Report the composite only when every gate decision is ACCEPT.

    Args:
        components: the six component scores.
        gate_rollup: mapping of gate slug to ACCEPT / BLOCK / ESCALATE.

    Returns:
        A ``GatedComposite``; ``composite_score`` is None when any gate is not
        ACCEPT, so the assurance layer gates the headline number.
    """
    all_accepted = bool(gate_rollup) and all(v == "ACCEPT" for v in gate_rollup.values())
    score = composite_score(components) if all_accepted else None
    return GatedComposite(
        components=dict(components),
        composite_score=score,
        gates_all_accepted=all_accepted,
        composite_reported=all_accepted,
        gate_rollup=dict(gate_rollup),
    )


def main() -> None:
    """CLI: read the iteration index and emit gated composite records."""
    index_path = Path("data/iterations/index.jsonl")
    out_path = Path("outputs/metrics/composite_scores.jsonl")
    if not index_path.exists():
        print(f"index not found at {index_path}; run iterate first")
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with (
        index_path.open("r", encoding="utf-8") as f_in,
        out_path.open("w", encoding="utf-8") as f_out,
    ):
        for line in f_in:
            row = json.loads(line)
            f_out.write(
                json.dumps(
                    {
                        "iteration_id": row["iteration_id"],
                        "composite_score": row.get("composite_score"),
                        "gates_all_accepted": row.get("gates_all_accepted"),
                    },
                    separators=(",", ":"),
                )
            )
            f_out.write("\n")
            n += 1
    print(f"wrote {n} gated composite records to {out_path}")


if __name__ == "__main__":
    main()
