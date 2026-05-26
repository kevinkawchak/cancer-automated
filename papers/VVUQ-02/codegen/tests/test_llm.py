"""Tests for the 4-entrant comparison tournament.

LICENSE: MIT
"""

from __future__ import annotations

from src.llm.compare_agent import (
    ENTRANT_TARGETS,
    STRUCTURAL_CAVEAT,
    WEIGHTS,
    composite,
    render_report,
    run_tournament,
)


def test_four_entrants():
    assert set(ENTRANT_TARGETS) == {
        "H2_Surgical_1_0",
        "PancreSpeed_1_0",
        "da_Vinci_successor_2030",
        "Dutch_human_baseline",
    }


def test_weights_sum_to_one():
    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9


def test_composite_orders_entrants():
    assert composite("H2_Surgical_1_0") > composite("Dutch_human_baseline")


def test_tournament_leaderboard():
    result = run_tournament(iterations=32, seed=20260525)
    assert len(result["leaderboard"]) == 4
    leader = result["leaderboard"][0]["entrant"]
    assert leader in {"H2_Surgical_1_0", "PancreSpeed_1_0"}


def test_round3_carries_time_caveat():
    result = run_tournament(iterations=1, seed=20260525)
    round3 = next(r for r in result["iterations"][0]["rounds"] if r["round"] == 3)
    assert STRUCTURAL_CAVEAT in round3["caveats"]


def test_report_renders():
    report = render_report(run_tournament(iterations=2, seed=20260525))
    assert "Leaderboard" in report
    assert "simulation against simulation" in report


def test_tournament_deterministic():
    a = run_tournament(iterations=4, seed=20260525)["leaderboard"]
    b = run_tournament(iterations=4, seed=20260525)["leaderboard"]
    assert a == b
