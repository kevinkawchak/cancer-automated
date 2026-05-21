# scheduler/ - Non-Stop Commit Schedules

Stage 1 calls for non-stop commit schedules: an autonomous, evenly spaced
cadence that produces daily deliverables without manual triggers. A cadence of
24 commits per day maps to one deliverable increment per hour.

```
  start (T0)
    |--- slot 0 ---|--- slot 1 ---|--- slot 2 ---| ...  (interval = 1 day / N)
    v              v              v              v
  deliverable-0001 deliverable-0002 deliverable-0003 ...
```

## Module

| File | Responsibility |
|------|----------------|
| `commit_scheduler.py` | Plan an evenly spaced, non-stop commit cadence |

## Usage

```python
import os, sys
from datetime import datetime, timezone
sys.path.insert(0, os.path.abspath("scheduler"))
from commit_scheduler import CommitScheduler

scheduler = CommitScheduler(commits_per_day=24)
slots = scheduler.plan(start=datetime(2026, 5, 21, tzinfo=timezone.utc), days=1)
print(len(slots), scheduler.interval_seconds)
```

The scheduler only plans the slots. The caller or CI performs the commits, and
every commit still passes through the VVUQ gate before it ships.

See `examples-scheduler/` for a runnable example.
