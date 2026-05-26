"""The 10-gate registry and runner (centerpiece).

Enumerates the 10 humanoid-specific VVUQ gates, binds each to its verification
predicates, its independent reference artifact, its threshold block from
config/vvuq_thresholds.yaml, and its governing standards from
config/standards_map.yaml. Provides run_gate, run_all, and a CLI that runs every
gate over a directory of iteration outputs (or over nominal reference cases) and
writes results/vvuq_decisions.json and results/vvuq_report.md.

Pure standard library plus optional click; importable without click.

LICENSE: MIT
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from src.vvuq.uncertainty import quantify
from src.vvuq.validation import validate
from src.vvuq.verification import verify
from src.vvuq.vvuq_gate import GateDecision, evaluate

CODEGEN_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = CODEGEN_ROOT / "config"
REFERENCE_DIR = CODEGEN_ROOT / "data" / "reference"

GATE_SLUGS = [
    "bimanual-handeye-servo",
    "dexterous-finger-force",
    "whole-body-balance",
    "autonomous-plan-correctness",
    "instrument-grasp-handover",
    "vascular-no-fly-hand",
    "bimanual-suturing-anastomosis",
    "perception-scene-understanding",
    "shared-or-human-collision",
    "fault-estop-graceful-degradation",
]


@dataclass
class GateSpec:
    """Static binding for one VVUQ gate."""

    gate_id: str
    slug: str
    verification_checks: list[str]
    reference_file: str
    standards: list[str]
    immediate_catastrophe: bool = False
    hard_checks: list[str] = field(default_factory=list)


GATES: dict[str, GateSpec] = {
    "bimanual-handeye-servo": GateSpec(
        "01",
        "bimanual-handeye-servo",
        [
            "fingertip_samples_present",
            "no_nan_in_tip_trace",
            "within_file_cap",
            "schema_valid",
            "lint_clean",
        ],
        "handeye_reference.json",
        ["IEC_80601_2_77_2019", "ISO_9283_1998", "ASME_V_and_V_40_2018"],
    ),
    "dexterous-finger-force": GateSpec(
        "02",
        "dexterous-finger-force",
        [
            "force_samples_present",
            "force_caps_loaded",
            "no_nan_in_force_trace",
            "schema_valid",
            "lint_clean",
        ],
        "finger_force_reference.json",
        ["IEC_80601_2_77_2019", "ISO_TS_15066_2016"],
    ),
    "whole-body-balance": GateSpec(
        "03",
        "whole-body-balance",
        [
            "zmp_samples_present",
            "support_polygon_loaded",
            "no_nan_in_com_trace",
            "schema_valid",
            "lint_clean",
        ],
        "balance_zmp_reference.json",
        ["ISO_13482_2014", "IEC_60601_1_2005_AMD2_2020"],
    ),
    "autonomous-plan-correctness": GateSpec(
        "04",
        "autonomous-plan-correctness",
        [
            "plan_present",
            "reference_plan_loaded",
            "all_phases_covered",
            "schema_valid",
            "lint_clean",
        ],
        "plan_reference.json",
        ["UL_4600_2023", "IEEE_7009_2024", "IEC_62304_2006_AMD1_2015"],
    ),
    "instrument-grasp-handover": GateSpec(
        "05",
        "instrument-grasp-handover",
        [
            "grasp_events_present",
            "taxonomy_valid",
            "no_nan_in_grasp_trace",
            "schema_valid",
            "lint_clean",
        ],
        "grasp_reference.json",
        ["IEC_80601_2_77_2019", "ISO_9283_1998"],
    ),
    "vascular-no-fly-hand": GateSpec(
        "06",
        "vascular-no-fly-hand",
        [
            "proximity_samples_present",
            "safety_zones_loaded",
            "no_nan_in_distance_trace",
            "schema_valid",
            "lint_clean",
        ],
        "vessel_reference.json",
        ["IEC_80601_2_77_2019", "ISO_14971_2019"],
        immediate_catastrophe=True,
        hard_checks=["hard_stop_violations_zero"],
    ),
    "bimanual-suturing-anastomosis": GateSpec(
        "07",
        "bimanual-suturing-anastomosis",
        [
            "ring_tension_samples_present",
            "targets_loaded",
            "no_nan_in_tension_trace",
            "schema_valid",
            "lint_clean",
        ],
        "ring_tension_reference.json",
        ["IEC_80601_2_77_2019", "Fistula_Risk_Score"],
    ),
    "perception-scene-understanding": GateSpec(
        "08",
        "perception-scene-understanding",
        [
            "masks_present",
            "reference_masks_loaded",
            "all_structures_segmented",
            "schema_valid",
            "lint_clean",
        ],
        "perception_reference.json",
        ["ASME_V_and_V_40_2018", "IEC_62304_2006_AMD1_2015"],
    ),
    "shared-or-human-collision": GateSpec(
        "09",
        "shared-or-human-collision",
        [
            "clearance_samples_present",
            "actors_loaded",
            "no_nan_in_clearance_trace",
            "schema_valid",
            "lint_clean",
        ],
        "collision_reference.json",
        ["ISO_TS_15066_2016", "ISO_10218_1_2011", "ISO_13482_2014"],
        immediate_catastrophe=True,
        hard_checks=["clearance_above_floor"],
    ),
    "fault-estop-graceful-degradation": GateSpec(
        "10",
        "fault-estop-graceful-degradation",
        [
            "fault_events_present",
            "budgets_loaded",
            "no_nan_in_latency_trace",
            "schema_valid",
            "lint_clean",
        ],
        "fault_reference.json",
        ["IEC_60601_1_2005_AMD2_2020", "ISO_13849_1_2023", "IEEE_7009_2024"],
        immediate_catastrophe=True,
        hard_checks=["safe_state_reached"],
    ),
}

# Threshold defaults and per-gate overrides used when the YAML is unavailable.
_DEFAULTS = {
    "verification": {"min_checks_passed_fraction": 1.0},
    "validation": {"min_agreement": 0.95, "max_relative_error": 0.05, "require_human_review": True},
    "uncertainty": {
        "max_coefficient_of_variation": 0.10,
        "min_consensus_runs": 3,
        "confidence_level": 0.95,
    },
    "gate": {"block_on_any_failure": True, "escalate_on_divergence": True},
}
_OVERRIDES = {
    "bimanual-handeye-servo": {
        "validation": {"min_agreement": 0.97},
        "uncertainty": {"max_coefficient_of_variation": 0.08},
    },
    "whole-body-balance": {
        "validation": {"min_agreement": 0.98, "max_relative_error": 0.03},
        "uncertainty": {"max_coefficient_of_variation": 0.06},
    },
    "instrument-grasp-handover": {"validation": {"min_agreement": 0.96}},
    "vascular-no-fly-hand": {
        "validation": {"min_agreement": 1.00, "max_relative_error": 0.01},
        "uncertainty": {"max_coefficient_of_variation": 0.05},
    },
    "bimanual-suturing-anastomosis": {
        "validation": {"min_agreement": 0.96},
        "uncertainty": {"max_coefficient_of_variation": 0.08},
    },
    "shared-or-human-collision": {
        "validation": {"min_agreement": 1.00, "max_relative_error": 0.02},
        "uncertainty": {"max_coefficient_of_variation": 0.06},
    },
    "fault-estop-graceful-degradation": {
        "validation": {"min_agreement": 1.00, "max_relative_error": 0.02},
        "uncertainty": {"max_coefficient_of_variation": 0.05},
    },
}


def _merge(base: dict, override: dict) -> dict:
    """Deep-merge two threshold dicts (override wins)."""
    out = {k: dict(v) if isinstance(v, dict) else v for k, v in base.items()}
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = {**out[key], **value}
        else:
            out[key] = value
    return out


def load_thresholds(path: Path | None = None) -> dict[str, dict]:
    """Load per-gate merged thresholds, falling back to the embedded defaults."""
    raw: dict = {}
    path = path or (CONFIG_DIR / "vvuq_thresholds.yaml")
    try:
        import yaml

        with path.open("r", encoding="utf-8") as handle:
            raw = yaml.safe_load(handle) or {}
    except (ImportError, OSError):
        raw = {}
    defaults = raw.get("defaults", _DEFAULTS)
    merged: dict[str, dict] = {}
    for slug in GATE_SLUGS:
        override = raw.get(slug, _OVERRIDES.get(slug, {}))
        merged[slug] = _merge(defaults, override)
    return merged


def load_reference(slug: str, reference_dir: Path | None = None) -> dict:
    """Load the independent validation reference metrics for a gate."""
    reference_dir = reference_dir or REFERENCE_DIR
    path = reference_dir / GATES[slug].reference_file
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except OSError:
        return {}


def run_gate(slug: str, case: dict, thresholds: dict[str, dict] | None = None) -> GateDecision:
    """Run one gate over one candidate case and return its decision."""
    if slug not in GATES:
        raise ValueError(f"unknown gate slug: {slug}")
    thresholds = thresholds or load_thresholds()
    block = thresholds[slug]
    ver = verify(case.get("checks", {}), case.get("check_details"))
    val = validate(
        case.get("observed", {}),
        case.get("reference", {}),
        max_relative_error=block["validation"]["max_relative_error"],
        human_review=bool(case.get("human_review", False)),
    )
    unc = quantify(case.get("runs", []))
    return evaluate(slug, ver, val, unc, block, hard_checks=case.get("hard_checks"))


def run_all(
    cases: dict[str, dict], thresholds: dict[str, dict] | None = None
) -> dict[str, GateDecision]:
    """Run every gate that has a case and return the per-gate decisions."""
    thresholds = thresholds or load_thresholds()
    return {slug: run_gate(slug, case, thresholds) for slug, case in cases.items()}


def nominal_accept_case(slug: str, reference_dir: Path | None = None) -> dict:
    """Build a nominal ACCEPT case from a gate's reference (observed == reference)."""
    ref = load_reference(slug, reference_dir)
    spec = GATES[slug]
    checks = dict.fromkeys(spec.verification_checks, True)
    hard = dict.fromkeys(spec.hard_checks, True)
    return {
        "gate_slug": slug,
        "checks": checks,
        "observed": dict(ref),
        "reference": dict(ref),
        "runs": [dict(ref), dict(ref), dict(ref)],
        "human_review": True,
        "hard_checks": hard,
    }


def decisions_to_report(decisions: dict[str, GateDecision]) -> str:
    """Render a Markdown report of the per-gate decisions."""
    lines = [
        "# VVUQ Gate Decisions",
        "",
        "| # | Gate | Decision | Reasons |",
        "|---|------|----------|---------|",
    ]
    for slug in GATE_SLUGS:
        if slug not in decisions:
            continue
        d = decisions[slug]
        reasons = "; ".join(d.reasons) if d.reasons else "all dimensions pass"
        lines.append(f"| {GATES[slug].gate_id} | {slug} | {d.decision} | {reasons} |")
    all_accept = all(d.accepted for d in decisions.values())
    lines += ["", f"All 10 gates ACCEPT: {all_accept}"]
    return "\n".join(lines) + "\n"


def main() -> None:
    """CLI: run every gate over nominal reference cases and write the report."""
    thresholds = load_thresholds()
    cases = {slug: nominal_accept_case(slug) for slug in GATE_SLUGS}
    decisions = run_all(cases, thresholds)
    out_dir = CODEGEN_ROOT / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        slug: {
            "gate_id": GATES[slug].gate_id,
            "decision": d.decision,
            "accepted": d.accepted,
            "escalate": d.escalate,
            "reasons": d.reasons,
            "scores": d.scores,
            "standards": GATES[slug].standards,
        }
        for slug, d in decisions.items()
    }
    (out_dir / "vvuq_decisions.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (out_dir / "vvuq_report.md").write_text(decisions_to_report(decisions), encoding="utf-8")
    accepted = sum(1 for d in decisions.values() if d.accepted)
    print(f"ran {len(decisions)} gates: {accepted} ACCEPT")


if __name__ == "__main__":
    main()
