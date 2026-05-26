"""Humanoid sensor record ingest for the H2-Surgical 1.0.

Synthesizes and serializes per-tick per-hand sensor records that conform to
``schemas/h2_sensor_record.schema.json``. The humanoid record extends the 8-arm
baseline with 20 per-finger joint channels, 5 per-fingertip force channels, and
the whole-body balance channels (centre of mass, zero-moment point, support
polygon margin, ankle and hip torques). Deterministic: the same seed and tick
yield the same record across platforms.

Pure standard library plus the optional ``click`` CLI; importable without click.

LICENSE: MIT
"""

from __future__ import annotations

import csv
import json
import math
import random
from dataclasses import dataclass, field
from pathlib import Path

ROOT_SEED = 20260525
HANDS = ("L", "R")
FINGERS_PER_HAND = 5
FINGER_JOINTS = 4
FINGER_CHANNELS = FINGERS_PER_HAND * FINGER_JOINTS  # 20
COMMAND_RATE_HZ = 10_000
FORCE_RATE_HZ = 100_000
SUPPORT_POLYGON_MARGIN_FLOOR_MM = 8.0

PHASE_BOUNDARIES_S = [
    (1, 0.000, 6.000),
    (2, 6.000, 16.000),
    (3, 16.000, 24.000),
    (4, 24.000, 32.000),
    (5, 32.000, 42.000),
    (6, 42.000, 48.000),
    (7, 48.000, 54.000),
    (8, 54.000, 60.000),
]


def phase_for_time(t_s: float) -> int:
    """Map a time in seconds to its 1-based phase index over the 60 s timeline."""
    if t_s >= 60.0:
        return 8
    for phase_id, start_s, end_s in PHASE_BOUNDARIES_S:
        if start_s <= t_s < end_s:
            return phase_id
    return 1


@dataclass
class H2SensorRecord:
    """A single per-hand per-tick humanoid sensor record."""

    tick: int
    hand_id: str
    phase: int
    q_arm: list[float] = field(default_factory=list)
    finger_q: list[float] = field(default_factory=list)
    finger_force: list[float] = field(default_factory=list)
    ee_pos: list[float] = field(default_factory=list)
    fingertip_pos: list[float] = field(default_factory=list)
    grasp_state: str = "open"
    vessel_proximity: float = 0.0
    ring_tension: float = 0.0
    support_polygon_margin: float = 0.0
    balance_state: str = "stable"
    tip_force_scalar: float = 0.0
    bimanual_cumulative_force: float = 0.0
    estop_state: str = "armed"
    collision_state: str = "clear"

    def flat_row(self) -> dict[str, float | int | str]:
        """Flatten the record to a single CSV-friendly row of scalar columns."""
        row: dict[str, float | int | str] = {
            "tick": self.tick,
            "hand_id": self.hand_id,
            "phase": self.phase,
            "grasp_state": self.grasp_state,
            "vessel_proximity": self.vessel_proximity,
            "ring_tension": self.ring_tension,
            "support_polygon_margin": self.support_polygon_margin,
            "balance_state": self.balance_state,
            "tip_force_scalar": self.tip_force_scalar,
            "bimanual_cumulative_force": self.bimanual_cumulative_force,
            "estop_state": self.estop_state,
            "collision_state": self.collision_state,
        }
        for i, v in enumerate(self.q_arm):
            row[f"q_arm_{i + 1}"] = v
        for i, v in enumerate(self.finger_force):
            row[f"finger_force_{i + 1}"] = v
        for i, v in enumerate(self.ee_pos):
            row[f"ee_pos_{'xyz'[i]}"] = v
        return row


def synth_record(tick: int, hand_id: str, seed: int = ROOT_SEED) -> H2SensorRecord:
    """Synthesize one deterministic sensor record for a hand at a command tick."""
    rng = random.Random((seed << 8) ^ (tick << 1) ^ (1 if hand_id == "R" else 0))
    t_s = tick / COMMAND_RATE_HZ
    phase = phase_for_time(t_s)
    q_arm = [round(0.1 * j + 0.01 * rng.random(), 5) for j in range(7)]
    finger_q = [
        round(0.05 * (k % FINGER_JOINTS) + 0.005 * rng.random(), 5) for k in range(FINGER_CHANNELS)
    ]
    finger_force = [round(0.4 + 0.3 * rng.random(), 4) for _ in range(FINGERS_PER_HAND)]
    tip_force = round(math.fsum(finger_force), 4)
    ee_pos = [
        round(15.0 + 2.0 * rng.random(), 3),
        round(-30.0 + 2.0 * rng.random(), 3),
        round(-42.0 + 2.0 * rng.random(), 3),
    ]
    fingertip_pos = [round(ee_pos[i % 3] + 0.5 * rng.random(), 3) for i in range(15)]
    margin = round(SUPPORT_POLYGON_MARGIN_FLOOR_MM + 30.0 + 5.0 * rng.random(), 3)
    ring = round(0.45 + 0.01 * (rng.random() - 0.5), 4) if phase in (5, 6, 7) else 0.0
    return H2SensorRecord(
        tick=tick,
        hand_id=hand_id,
        phase=phase,
        q_arm=q_arm,
        finger_q=finger_q,
        finger_force=finger_force,
        ee_pos=ee_pos,
        fingertip_pos=fingertip_pos,
        grasp_state="needle_driver" if phase in (5, 6, 7) else "tripod",
        vessel_proximity=round(6.0 + 4.0 * rng.random(), 3),
        ring_tension=ring,
        support_polygon_margin=margin,
        balance_state="stable",
        tip_force_scalar=tip_force,
        bimanual_cumulative_force=round(2.0 * tip_force, 4),
        estop_state="armed",
        collision_state="clear",
    )


def sample_rows(n_ticks: int = 500, seed: int = ROOT_SEED) -> list[dict[str, float | int | str]]:
    """Build a publication sample of flattened rows across both hands."""
    rows: list[dict[str, float | int | str]] = []
    for tick in range(n_ticks):
        for hand_id in HANDS:
            rows.append(synth_record(tick, hand_id, seed).flat_row())
    return rows


def write_sample_csv(path: Path, n_ticks: int = 500, seed: int = ROOT_SEED) -> int:
    """Write the publication sample CSV; return the number of rows written."""
    rows = sample_rows(n_ticks, seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def write_sample_jsonl(path: Path, n_ticks: int = 500, seed: int = ROOT_SEED) -> int:
    """Write the publication sample JSONL; return the number of rows written."""
    rows = sample_rows(n_ticks, seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, separators=(",", ":")))
            f.write("\n")
    return len(rows)


def main() -> None:
    """CLI entry point: emit the publication sample CSV and JSONL."""
    try:
        import click
    except ImportError:
        n = write_sample_csv(Path("data/sample_h2_sensor.csv"))
        write_sample_jsonl(Path("data/sample_h2_sensor.jsonl"))
        print(f"wrote {n} sample rows (click not installed, used defaults)")
        return

    @click.command()
    @click.option("--ticks", type=int, default=500)
    @click.option("--seed", type=int, default=ROOT_SEED)
    @click.option(
        "--out-csv", type=click.Path(path_type=Path), default=Path("data/sample_h2_sensor.csv")
    )
    @click.option(
        "--out-jsonl", type=click.Path(path_type=Path), default=Path("data/sample_h2_sensor.jsonl")
    )
    def _cli(ticks: int, seed: int, out_csv: Path, out_jsonl: Path) -> None:
        n = write_sample_csv(out_csv, ticks, seed)
        write_sample_jsonl(out_jsonl, ticks, seed)
        click.echo(f"wrote {n} sample rows to {out_csv} and {out_jsonl}")

    _cli()


if __name__ == "__main__":
    main()
