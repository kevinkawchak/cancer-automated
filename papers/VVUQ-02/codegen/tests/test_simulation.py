"""Tests for the 32-iteration deterministic sweep.

LICENSE: MIT
"""

from __future__ import annotations

import json

from src.simulation.iterate import (
    FREE_PARAMS,
    ITERATIONS,
    ROOT_SEED,
    build_iteration_params,
    latin_hypercube_samples,
    run_sweep,
    simulate_iteration,
)


def test_constants():
    assert ROOT_SEED == 20260525
    assert ITERATIONS == 32
    assert len(FREE_PARAMS) == 5


def test_latin_hypercube_deterministic():
    a = latin_hypercube_samples(32, 5, ROOT_SEED)
    b = latin_hypercube_samples(32, 5, ROOT_SEED)
    assert a == b
    assert len(a) == 32
    assert len(a[0]) == 5


def test_build_iteration_params_in_range():
    samples = latin_hypercube_samples(32, 5, ROOT_SEED)
    params = build_iteration_params(0, samples[0])
    assert params.seed == ROOT_SEED
    assert 0.0 <= params.fingertip_placement_noise_mm <= 0.05
    assert 0.0 <= params.perception_occlusion_fraction <= 0.30


def test_simulate_iteration_clears_all_gates():
    samples = latin_hypercube_samples(32, 5, ROOT_SEED)
    record = simulate_iteration(build_iteration_params(0, samples[0]))
    assert len(record["gate_rollup"]) == 10
    assert record["gates_all_accepted"]
    assert all(d == "ACCEPT" for d in record["gate_rollup"].values())
    assert record["composite_score"] is not None


def test_run_sweep_writes_index(tmp_path):
    records = run_sweep(iterations=32, seed=ROOT_SEED, out_dir=tmp_path)
    assert len(records) == 32
    index = (tmp_path / "index.jsonl").read_text(encoding="utf-8").strip().splitlines()
    assert len(index) == 32
    first = json.loads(index[0])
    assert first["iteration_id"] == 0
    assert (tmp_path / "run_00000_vvuq.csv").exists()
    assert (tmp_path / "run_00000_L0_raw.zenodo_pointer.json").exists()


def test_sweep_deterministic(tmp_path):
    r1 = run_sweep(iterations=8, seed=ROOT_SEED, out_dir=tmp_path / "a")
    r2 = run_sweep(iterations=8, seed=ROOT_SEED, out_dir=tmp_path / "b")
    assert [r["composite_score"] for r in r1] == [r["composite_score"] for r in r2]
