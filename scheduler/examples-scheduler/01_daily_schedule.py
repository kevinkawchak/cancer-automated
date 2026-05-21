"""Example: plan a one-day, 24-slot non-stop commit cadence.

Run from the repository root:
    python scheduler/examples-scheduler/01_daily_schedule.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone

SCHED_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCHED_DIR)

from commit_scheduler import CommitScheduler  # noqa: E402


def main() -> None:
    scheduler = CommitScheduler(commits_per_day=24)
    start = datetime(2026, 5, 21, 0, 0, tzinfo=timezone.utc)
    slots = scheduler.plan(start=start, days=1)
    print(f"planned {len(slots)} slots, interval {scheduler.interval_seconds:.0f} seconds")
    for slot in slots[:5]:
        print(f"  {slot.label} at {slot.scheduled_at}")
    print("  ...")


if __name__ == "__main__":
    main()
