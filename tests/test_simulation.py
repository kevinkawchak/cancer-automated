"""Tests for triple simulation and consensus.

LICENSE: MIT
"""

from __future__ import annotations

from conftest import load_module


def test_triple_runner_runs_three_times_with_distinct_seeds():
    triple = load_module("triple_runner", "simulation/triple_runner.py")
    seeds = []

    def project(seed):
        seeds.append(seed)
        return {"value": float(seed)}

    runs = triple.TripleRunner(n_runs=3, base_seed=100).run(project)
    assert len(runs) == 3
    assert [run.seed for run in runs] == [100, 101, 102]
    assert len(set(seeds)) == 3


def test_consensus_converges_for_low_variance():
    consensus = load_module("consensus", "simulation/consensus.py")
    runs = [{"x": 2.50}, {"x": 2.51}, {"x": 2.49}]
    result = consensus.summarize(runs, max_cv=0.10)
    assert result.n_runs == 3
    assert result.converged
    assert abs(result.mean["x"] - 2.50) < 1e-6


def test_consensus_flags_divergence_for_high_variance():
    consensus = load_module("consensus", "simulation/consensus.py")
    runs = [{"x": 1.0}, {"x": 5.0}, {"x": 2.0}]
    result = consensus.summarize(runs, max_cv=0.10)
    assert not result.converged
    assert "x" in result.divergent


def test_triple_runner_rejects_zero_runs():
    triple = load_module("triple_runner", "simulation/triple_runner.py")
    try:
        triple.TripleRunner(n_runs=0)
    except ValueError:
        return
    raise AssertionError("expected ValueError for n_runs=0")
