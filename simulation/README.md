# simulation/ - Auto-Simulate Every Project Three Times

Running three times is a Stage 1 requirement. A single run hides run to run
variance; three runs expose it and feed both the consensus aggregator and the
VVUQ uncertainty check.

```
   project_fn(seed)
        |
        v
  +-------------------------------------------+
  | TripleRunner (n_runs = 3)                 |
  | seed+0 -> metrics   run 1                 |
  | seed+1 -> metrics   run 2                 |
  | seed+2 -> metrics   run 3                 |
  +-------------------------------------------+
        |
        v
  +-------------------------------------------+
  | consensus.summarize                       |
  | mean per metric, cv per metric,           |
  | divergent metrics flagged (cv > 0.10)     |
  +-------------------------------------------+
```

## Modules

| File | Responsibility |
|------|----------------|
| `triple_runner.py` | Run a project callable three times with distinct seeds |
| `consensus.py` | Aggregate runs into a mean and flag divergent metrics |

## Usage

```python
import os, sys
sys.path.insert(0, os.path.abspath("simulation"))
from triple_runner import TripleRunner
from consensus import summarize

def project(seed):
    return {"acceleration_factor": 2.5 + (seed % 3) * 0.001}

runs = TripleRunner(n_runs=3).run(project)
consensus = summarize(runs)
print(consensus.mean, consensus.converged)
```

See `examples-simulation/` for runnable examples.
