# Section 02: Pipeline Execution (Five Established Methods, One Daily Deliverable)

This section executes the heart of the platform: the daily-deliverable pipeline
in `pipeline/`. It is emphasized in the project because it packages the five
established methods (instruction generation, code generation, code execution,
and paper assembly, orchestrated end to end) into one repeatable run. Every
example here was executed on the foundation host from Section 01.

## The five established methods, as executed

The orchestrator in `pipeline/orchestrator.py` runs four producing stages in
strict order and threads a single `Deliverable` object through them. A fifth
method, the VVUQ gate, is an optional callable invoked after the paper stage and
is exercised in Section 03.

```
  Deliverable(id, title, topic)
        |
        v
  +----------------------+   instructions.md (instructions kind)
  | 1. InstructionStage  | -----------------------------> records artifact
  +----------------------+
        |   reads instructions
        v
  +----------------------+   generated_deliverable.py (code kind)
  | 2. CodegenStage      | -----------------------------> records artifact
  +----------------------+
        |   reads code
        v
  +----------------------+   execution_log.txt (execution_log kind)
  | 3. ExecutionStage    | -----------------------------> records artifact
  +----------------------+   parses key=value into metadata
        |   reads execution log + results
        v
  +----------------------+   paper.md (paper kind)
  | 4. PaperStage        | -----------------------------> records artifact
  +----------------------+
        |
        v
  optional gate(deliverable)  -> Section 03 VVUQ
        |
        v
  Deliverable.complete == True
```

## Example 1: single deliverable end to end

Command:

```bash
python pipeline/examples-pipeline/01_single_deliverable.py
```

Verbatim output:

```text
complete: True
statuses: {'instruction': 'complete', 'codegen': 'complete', 'execution': 'complete', 'paper': 'complete'}
{
  "deliverable_id": "DAILY-0001",
  "title": "Automated trial acceleration estimate",
  "topic": "Physical AI oncology trial throughput",
  "created_at": "2026-05-23T04:20:54.159230+00:00",
  "complete": true,
  "stages": {
    "instruction": {
      "status": "complete",
      "artifacts": ["instructions.md"],
      "bytes": 963
    },
    "codegen": {
      "status": "complete",
      "artifacts": ["generated_deliverable.py"],
      "bytes": 735
    },
    "execution": {
      "status": "complete",
      "artifacts": ["execution_log.txt"],
      "bytes": 95
    },
    "paper": {
      "status": "complete",
      "artifacts": ["paper.md"],
      "bytes": 1000
    }
  }
}
```

All four stages reached `complete` and the deliverable reported
`complete: True`. The four artifacts produced are saved verbatim in the
`artifacts/` subdirectory next to this file (the Python artifact is reproduced
below in a fenced block rather than as a `.py` file, to keep it out of the lint
surface).

## Example 2: stage by stage walkthrough

Command:

```bash
python pipeline/examples-pipeline/02_instruction_to_paper.py
```

This runs each stage object directly and previews the first lines of every
artifact. Verbatim output:

```text
--- instructions.md (instructions, 909 bytes) ---
# Instruction Set: Stage by stage walkthrough

Deliverable ID: DAILY-0002
Topic: Established methods

## Inputs

--- generated_deliverable.py (code, 724 bytes) ---
"""Generated deliverable script. Authored by the codegen stage."""


def compute_metrics(runs):
    baseline_days = 30.0
    automated_days = baseline_days / (1.0 + runs * 0.5)

--- execution_log.txt (execution_log, 84 bytes) ---
title=Stage by stage walkthrough
runs=3
automated_days=12.0
acceleration_factor=2.5

--- paper.md (paper, 960 bytes) ---
# Stage by stage walkthrough

Deliverable ID: DAILY-0002
Topic: Established methods
Generated: 2026-05-23T04:20:54.194975+00:00
```

The `---` prefixes in that output are the example script's own artifact
separators, printed verbatim, not Markdown rules. The artifact byte counts
differ from Example 1 because the title and topic strings differ, which changes
the substituted text length.

## Example 3: small daily batch (non-stop cadence at small scale)

Command:

```bash
python pipeline/examples-pipeline/03_full_daily_run.py
```

Verbatim output:

```text
DAILY-0001: complete=True acceleration_factor=2.5
DAILY-0002: complete=True acceleration_factor=2.5
DAILY-0003: complete=True acceleration_factor=2.5
completed 3/3 deliverables
```

Three deliverables on three different topics all completed and all reported the
same acceleration factor of 2.5, because the codegen template is deterministic
in the number of simulation runs (3), not in the topic string. This determinism
is intentional: it is what lets the uncertainty check in Section 03 measure a
coefficient of variation of zero across identical runs.

## The four generated artifacts in full (DAILY-0001)

The instruction, execution log, and paper artifacts are saved as real files in
`artifacts/`. The generated code is reproduced here in full.

### artifacts/instructions.md (963 bytes)

The instruction stage ran on its deterministic template backend (no
`ANTHROPIC_API_KEY` and no `anthropic` package), producing a bracketed
instruction set with Inputs, Ordered Steps, Production Constraints, and
Acceptance Criteria. See `artifacts/instructions.md`.

### generated_deliverable.py (735 bytes)

```python
"""Generated deliverable script. Authored by the codegen stage."""


def compute_metrics(runs):
    baseline_days = 30.0
    automated_days = baseline_days / (1.0 + runs * 0.5)
    acceleration = baseline_days / automated_days
    return {
        "runs": runs,
        "baseline_days": baseline_days,
        "automated_days": round(automated_days, 3),
        "acceleration_factor": round(acceleration, 3),
    }


def main():
    metrics = compute_metrics(3)
    print("title=Automated trial acceleration estimate")
    print("runs=" + str(metrics["runs"]))
    print("automated_days=" + str(metrics["automated_days"]))
    print("acceleration_factor=" + str(metrics["acceleration_factor"]))


if __name__ == "__main__":
    main()
```

The arithmetic the generated code performs: with `runs = 3`, the automated
timeline is `30.0 / (1.0 + 3 * 0.5) = 30.0 / 2.5 = 12.0` days, and the
acceleration factor is `30.0 / 12.0 = 2.5`. This is the source of the 2.5 and
12.0 values seen throughout this run.

### artifacts/execution_log.txt (95 bytes)

The execution stage compiled the generated code (a syntax-level verification),
executed it in an isolated namespace while capturing stdout, and parsed the
`key=value` lines into structured results. See `artifacts/execution_log.txt`.

### artifacts/paper.md (1000 bytes)

The paper stage tabulated the four parsed result rows into a Markdown paper with
Abstract, Methods, Results, and Conclusion sections. See `artifacts/paper.md`.

## Stage logs and timing (DAILY-0001)

The per-stage logs and wall-clock durations captured from the orchestrator run:

| Stage | Status | Duration (s) | Log |
|-------|--------|--------------|-----|
| instruction | complete | 0.000010 | instructions generated via template backend (963 bytes) |
| codegen | complete | 0.000008 | code generated (735 bytes, 3 simulation runs) |
| execution | complete | 0.000197 | execution complete |
| paper | complete | 0.000010 | paper assembled (1000 bytes, 4 result rows) |

The execution stage is the slowest of the four because it compiles and runs the
generated code; even so the entire deliverable was produced in well under a
millisecond of stage time. Every artifact is far under the 200000 byte per-file
cap.

## Parsed execution results (DAILY-0001)

```json
{
  "title": "Automated trial acceleration estimate",
  "runs": "3",
  "automated_days": "12.0",
  "acceleration_factor": "2.5"
}
```

## Outcome

| Item | Result |
|------|--------|
| Examples run | 3 of 3, all exit 0 |
| Deliverables completed | 5 deliverable runs total (example 1 ran 1, example 2 ran 1, example 3 ran 3) over IDs DAILY-0001 to DAILY-0003 |
| Stages completed per deliverable | 4 of 4 (instruction, codegen, execution, paper) |
| Backend used | deterministic template (no agentic API key present) |
| Largest artifact | paper.md at 1000 bytes, far under the 200000 byte cap |
| Acceleration factor | 2.5 (30 baseline days to 12 automated days) |

The pipeline section is fully green. The deliverable that this section produced
is the input to the VVUQ gate exercised in Section 03.
