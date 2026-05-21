# pipeline/ - Five Established Methods, One Daily Deliverable

The pipeline packages the established methods that prior projects proved into a
single repeatable engine. Every daily deliverable flows through the same four
producing stages, in order, and is then cleared by the VVUQ gate.

```
  instruction_stage    codegen_stage      execution_stage     paper_stage
  +---------------+    +---------------+   +---------------+   +-------------+
  | Method 1      | -> | Method 2      |-> | Method 3      |-> | Method 4    |
  | generate      |    | generate code |   | execute code, |   | assemble a  |
  | instructions  |    | from the      |   | capture and   |   | paper from  |
  | (bracketed)   |    | instructions  |   | parse outputs |   | the results |
  +---------------+    +---------------+   +---------------+   +-------------+
        |                    |                   |                   |
        +--------------------+---------+---------+-------------------+
                                       v
                              +--------------------+
                              | orchestrator.py    |
                              | runs all stages,   |
                              | invokes VVUQ gate  |
                              +--------------------+
```

## Modules

| File | Method | Responsibility |
|------|--------|----------------|
| `deliverable.py` | data model | `Stage`, `StageStatus`, `Artifact`, `StageResult`, `Deliverable` |
| `instruction_stage.py` | 1 | Generate the bracketed instruction set |
| `codegen_stage.py` | 2 | Generate an executable script from the instructions |
| `execution_stage.py` | 3 | Compile, run, and parse the generated code outputs |
| `paper_stage.py` | 4 | Assemble a Markdown paper from the results |
| `orchestrator.py` | all | Run every stage in order and invoke the optional VVUQ gate |

## Usage

```python
import os, sys
sys.path.insert(0, os.path.abspath("pipeline"))
from orchestrator import PipelineOrchestrator

orchestrator = PipelineOrchestrator(simulate_runs=3)
deliverable = orchestrator.run_deliverable(
    deliverable_id="DAILY-0001",
    title="Automated trial acceleration estimate",
    topic="Physical AI oncology trial throughput",
    sources=["national-platform paper", "four-simulation paper"],
)
print(deliverable.complete)
print(deliverable.summary())
```

## Design Notes

- The core engine is pure standard library. Agentic backends (Anthropic) are
  imported through try/except guards so the modules stay importable offline.
- The execution stage runs generated code in-process for deterministic CI. The
  code it runs is produced by the codegen template in this repository. Production
  deployments must sandbox code execution.
- See `examples-pipeline/` for runnable examples.
