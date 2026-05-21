"""Non-stop commit schedules.

The scheduler plans an autonomous, evenly spaced commit cadence so daily
deliverables flow without manual triggers. A cadence of 24 commits per day maps
to one deliverable increment per hour. The scheduler only plans slots; the
caller (or CI) performs the commits. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

DEFAULT_COMMITS_PER_DAY = 24


@dataclass
class CommitSlot:
    """A single planned commit slot."""

    index: int
    scheduled_at: str
    label: str


class CommitScheduler:
    """Plan an evenly spaced, non-stop commit cadence."""

    def __init__(self, commits_per_day: int = DEFAULT_COMMITS_PER_DAY) -> None:
        if commits_per_day < 1:
            raise ValueError("commits_per_day must be at least 1")
        self.commits_per_day = commits_per_day
        self.interval = timedelta(days=1) / commits_per_day

    @property
    def interval_seconds(self) -> float:
        return self.interval.total_seconds()

    def plan(self, start: datetime | None = None, days: int = 1) -> list[CommitSlot]:
        """Plan ``commits_per_day * days`` evenly spaced commit slots."""
        if days < 1:
            raise ValueError("days must be at least 1")
        start = start or datetime.now(timezone.utc)
        total = self.commits_per_day * days
        slots: list[CommitSlot] = []
        for index in range(total):
            moment = start + self.interval * index
            slots.append(
                CommitSlot(
                    index=index,
                    scheduled_at=moment.isoformat(),
                    label=f"deliverable-{index + 1:04d}",
                )
            )
        return slots

    def next_slot(self, now: datetime, start: datetime, days: int = 1) -> CommitSlot | None:
        """Return the first planned slot at or after ``now``, or None if past the horizon."""
        for slot in self.plan(start=start, days=days):
            if datetime.fromisoformat(slot.scheduled_at) >= now:
                return slot
        return None
