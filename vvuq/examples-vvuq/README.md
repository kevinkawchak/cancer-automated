# examples-vvuq/

Runnable examples for the VVUQ pillars and the gate. Each script adds the
`vvuq/` directory to `sys.path` and runs from the repository root.

| Script | Shows |
|--------|-------|
| `01_verification_checks.py` | Run verification over a small deliverable-like object |
| `02_validation_against_reference.py` | Compare observed metrics to a reference |
| `03_uncertainty_budget.py` | Quantify dispersion across three runs and apply the gate |

```bash
python vvuq/examples-vvuq/01_verification_checks.py
python vvuq/examples-vvuq/02_validation_against_reference.py
python vvuq/examples-vvuq/03_uncertainty_budget.py
```
