# vvuq/ - Verification, Validation, Uncertainty Quantification

A central Stage 1 principle is that VVUQ is more robust than code generation.
Code generation produces a candidate deliverable. The VVUQ gate decides whether
that candidate is allowed to ship.

```
   Candidate deliverable + three simulation runs + reference metrics
                                   |
            +----------------------+----------------------+
            v                      v                      v
   +-----------------+   +-------------------+   +-------------------+
   | verification    |   | validation        |   | uncertainty       |
   | did we build it |   | did we build the  |   | dispersion across |
   | right? checks,  |   | right thing? vs   |   | the 3 runs, cv    |
   | schema, lint,   |   | reference metrics |   | per metric        |
   | 200K file cap   |   | + human review    |   |                   |
   +-----------------+   +-------------------+   +-------------------+
            |                      |                      |
            +----------------------+----------------------+
                                   v
                         +-------------------+
                         | vvuq_gate         |
                         | accept or block,  |
                         | escalate on       |
                         | divergence        |
                         +-------------------+
```

## Modules

| File | Pillar | Responsibility |
|------|--------|----------------|
| `verification.py` | V | Structural, schema, lint, and 200K file-cap checks |
| `validation.py` | V | Agreement and relative error against a reference, human review |
| `uncertainty.py` | UQ | Mean, standard deviation, and coefficient of variation across runs |
| `vvuq_gate.py` | gate | Combine all three against `configs/vvuq_thresholds.yaml` |

## Thresholds

The gate loads `configs/vvuq_thresholds.yaml` when PyYAML is available and falls
back to the built-in defaults otherwise. By default the gate requires:

- verification: all checks pass (fraction 1.0).
- validation: agreement at or above 0.95, max relative error at or below 0.05, human review recorded.
- uncertainty: at least 3 runs, coefficient of variation at or below 0.10.

The gate blocks on any failure and escalates divergent uncertainty to a human.

## Usage

```python
import os, sys
sys.path.insert(0, os.path.abspath("vvuq"))
from vvuq_gate import VVUQGate

gate = VVUQGate()
decision = gate.evaluate(
    deliverable,
    runs=[{"acceleration_factor": 2.5}, {"acceleration_factor": 2.5}, {"acceleration_factor": 2.5}],
    observed={"acceleration_factor": 2.5},
    reference={"acceleration_factor": 2.5},
    human_review=True,
)
print(decision.accepted, decision.reasons)
```

See `examples-vvuq/` for runnable examples.
