"""Tests for the humanoid sensor ingest.

LICENSE: MIT
"""

from __future__ import annotations

import json

from src.sensors.ingest_h2 import (
    FINGER_CHANNELS,
    FINGERS_PER_HAND,
    HANDS,
    ROOT_SEED,
    phase_for_time,
    sample_rows,
    synth_record,
    write_sample_csv,
    write_sample_jsonl,
)


def test_root_seed_and_constants():
    assert ROOT_SEED == 20260525
    assert HANDS == ("L", "R")
    assert FINGERS_PER_HAND == 5
    assert FINGER_CHANNELS == 20


def test_phase_for_time_boundaries():
    assert phase_for_time(0.0) == 1
    assert phase_for_time(5.999) == 1
    assert phase_for_time(6.0) == 2
    assert phase_for_time(16.0) == 3
    assert phase_for_time(32.0) == 5
    assert phase_for_time(42.0) == 6
    assert phase_for_time(48.0) == 7
    assert phase_for_time(54.0) == 8
    assert phase_for_time(59.999) == 8
    assert phase_for_time(60.0) == 8


def test_synth_record_deterministic():
    a = synth_record(1234, "L")
    b = synth_record(1234, "L")
    assert a == b
    assert synth_record(1234, "R") != a


def test_record_shape():
    rec = synth_record(320_000, "L")
    assert len(rec.q_arm) == 7
    assert len(rec.finger_q) == 20
    assert len(rec.finger_force) == 5
    assert len(rec.fingertip_pos) == 15
    assert rec.phase == 5
    assert rec.grasp_state == "needle_driver"
    assert rec.ring_tension > 0.0


def test_flat_row_columns():
    row = synth_record(0, "L").flat_row()
    assert row["tick"] == 0
    assert row["hand_id"] == "L"
    assert "q_arm_7" in row
    assert "finger_force_5" in row
    assert "ee_pos_z" in row


def test_sample_rows_count():
    rows = sample_rows(n_ticks=10)
    assert len(rows) == 20


def test_write_sample_csv_and_jsonl(tmp_path):
    csv_path = tmp_path / "s.csv"
    jsonl_path = tmp_path / "s.jsonl"
    n_csv = write_sample_csv(csv_path, n_ticks=5)
    n_jsonl = write_sample_jsonl(jsonl_path, n_ticks=5)
    assert n_csv == 10
    assert n_jsonl == 10
    lines = jsonl_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 10
    first = json.loads(lines[0])
    assert first["hand_id"] == "L"
