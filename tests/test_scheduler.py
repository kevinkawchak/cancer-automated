"""Tests for the non-stop commit scheduler.

LICENSE: MIT
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from conftest import load_module


def test_plan_slot_count_and_interval():
    sched = load_module("commit_scheduler", "scheduler/commit_scheduler.py")
    scheduler = sched.CommitScheduler(commits_per_day=24)
    assert scheduler.interval_seconds == 3600.0
    slots = scheduler.plan(start=datetime(2026, 5, 21, tzinfo=timezone.utc), days=2)
    assert len(slots) == 48
    assert slots[0].label == "deliverable-0001"
    assert slots[-1].label == "deliverable-0048"


def test_slots_are_evenly_spaced():
    sched = load_module("commit_scheduler", "scheduler/commit_scheduler.py")
    scheduler = sched.CommitScheduler(commits_per_day=24)
    start = datetime(2026, 5, 21, tzinfo=timezone.utc)
    slots = scheduler.plan(start=start, days=1)
    first = datetime.fromisoformat(slots[0].scheduled_at)
    second = datetime.fromisoformat(slots[1].scheduled_at)
    assert second - first == timedelta(hours=1)


def test_next_slot_returns_future_slot():
    sched = load_module("commit_scheduler", "scheduler/commit_scheduler.py")
    scheduler = sched.CommitScheduler(commits_per_day=24)
    start = datetime(2026, 5, 21, 0, 0, tzinfo=timezone.utc)
    now = datetime(2026, 5, 21, 3, 30, tzinfo=timezone.utc)
    slot = scheduler.next_slot(now=now, start=start, days=1)
    assert slot is not None
    assert datetime.fromisoformat(slot.scheduled_at) >= now


def test_scheduler_rejects_zero_cadence():
    sched = load_module("commit_scheduler", "scheduler/commit_scheduler.py")
    try:
        sched.CommitScheduler(commits_per_day=0)
    except ValueError:
        return
    raise AssertionError("expected ValueError for commits_per_day=0")
