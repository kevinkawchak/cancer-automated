# examples-pipeline/

Runnable examples for the daily-deliverable pipeline. Each script is
self-contained and adds the `pipeline/` directory to `sys.path` before importing
the orchestrator, so it runs from the repository root with no installation.

| Script | Shows |
|--------|-------|
| `01_single_deliverable.py` | Run one deliverable end to end and print its summary |
| `02_instruction_to_paper.py` | Run each stage individually and inspect the artifacts |
| `03_full_daily_run.py` | Run a small daily batch of deliverables |

```bash
python pipeline/examples-pipeline/01_single_deliverable.py
python pipeline/examples-pipeline/02_instruction_to_paper.py
python pipeline/examples-pipeline/03_full_daily_run.py
```
