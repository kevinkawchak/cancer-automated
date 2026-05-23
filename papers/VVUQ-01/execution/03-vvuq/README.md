# Section 03: VVUQ Execution (Held Higher Than Code Generation)

This section executes the `vvuq/` package, the part of the platform the study
emphasizes most. The central principle is that verification, validation, and
uncertainty quantification (VVUQ) is a more substantial process than the code
generation it gates. Code generation produces a candidate deliverable. The VVUQ
gate decides whether that candidate is allowed to ship, and it is intentionally
strict: any single failing dimension blocks the deliverable.

This section first runs the three shipped examples (the accept path), then
exercises the gate across the block and escalate paths with a dedicated capture
so the full decision surface is documented, not just the happy path.

## The three dimensions, as executed

```
  candidate deliverable (from the pipeline, Section 02)
        |
        v
  +-----------------------------+
  | Verification                |  did we build it right?
  | verify(deliverable)         |  6 structural and policy checks
  +-----------------------------+
        |
        v
  +-----------------------------+
  | Validation                  |  did we build the right thing?
  | validate(observed, ref)     |  agreement vs reference, max rel error,
  +-----------------------------+  human review recorded
        |
        v
  +-----------------------------+
  | Uncertainty quantification  |  how dispersed are the 3 runs?
  | quantify(runs)              |  coefficient of variation per metric
  +-----------------------------+
        |
        v
  +-----------------------------+
  | VVUQGate.evaluate(...)      |  block on any failure;
  |                             |  escalate to human on divergence
  +-----------------------------+
        |
        +--> ACCEPT  (all dimensions pass)
        +--> BLOCK   (any dimension fails)
        +--> ESCALATE (uncertainty divergence)
```

## Loaded thresholds

The gate loaded its thresholds from `configs/vvuq_thresholds.yaml` (it falls
back to built-in defaults only if PyYAML or the file are absent; here the file
was read).

| Dimension | Threshold | Value |
|-----------|-----------|-------|
| Verification | min checks passed fraction | 1.0 (all checks) |
| Verification | require schema valid | true |
| Verification | require lint clean | true |
| Validation | min agreement with reference | 0.95 |
| Validation | max relative error | 0.05 |
| Validation | require human review | true |
| Uncertainty | max coefficient of variation | 0.10 |
| Uncertainty | min consensus runs | 3 |
| Uncertainty | confidence level | 0.95 |
| Gate | block on any failure | true |
| Gate | escalate to human on divergence | true |

## Example 1: verification checks

```bash
python vvuq/examples-vvuq/01_verification_checks.py
```

```text
fraction_passed: 1.0
all_passed: True
  [ok] all_stages_complete
  [ok] artifacts_present 2 artifacts
  [ok] artifacts_non_empty
  [ok] within_file_cap
  [ok] schema_valid
  [ok] lint_clean
```

All six verification checks passed for a complete deliverable with two non-empty
artifacts under the cap. Verification answers "did we build the deliverable
right?" with structural and policy checks only; it does not look at numeric
correctness, which is validation's job.

## Example 2: validation against a reference

```bash
python vvuq/examples-vvuq/02_validation_against_reference.py
```

```text
agreement: 1.0
max_relative_error: 0.033
human_review: True
  acceleration_factor: relative_error=0.020
  automated_days: relative_error=0.033
```

Both observed metrics fell within the 0.05 relative-error tolerance
(0.020 and 0.033), so agreement was 1.0 and the worst relative error was 0.033.
With a human review recorded, this passes the validation dimension.

## Example 3: uncertainty budget and gate

```bash
python vvuq/examples-vvuq/03_uncertainty_budget.py
```

```text
n_runs: 3 max_cv: 0.0068
accepted: True
reasons: []
scores: {'verification_fraction': 1.0, 'validation_agreement': 1.0, 'max_relative_error': 0.0, 'max_cv': 0.0068, 'n_runs': 3}
```

Three near-identical runs gave a maximum coefficient of variation of 0.0068, far
below the 0.10 threshold, and the gate accepted the deliverable.

## The full gate decision surface

The three examples above only show the accept path. To document the thesis (VVUQ
is stricter than codegen) the gate was exercised against six cases: one accept
and five distinct block reasons, including the escalate path. The verbatim
results follow.

| Case | Scenario | Accepted | Escalate | Blocking reason(s) |
|------|----------|----------|----------|--------------------|
| 1 | clean, human reviewed, low CV | yes | no | (none) |
| 2 | no human review recorded | no | no | human review not recorded |
| 3 | divergent runs, high CV | no | yes | max cv 0.365 above 0.1 |
| 4 | observed disagrees with reference | no | no | agreement 0.00 below 0.95; max rel error 0.600 above 0.05 |
| 5 | only 2 runs, need 3 | no | no | only 2 runs, need 3 |
| 6 | artifact exceeds 200K cap | no | no | verification fraction 0.83 below 1.0 |

Verbatim capture:

```text
##### CASE 1 ACCEPT (clean, human reviewed, low CV) #####
accepted: True | blocked: False | escalate: False
reasons: []
scores: {'verification_fraction': 1.0, 'validation_agreement': 1.0, 'max_relative_error': 0.0, 'max_cv': 0.0068, 'n_runs': 3}

##### CASE 2 BLOCK (no human review recorded) #####
accepted: False | blocked: True | escalate: False
reasons: ['human review not recorded']

##### CASE 3 BLOCK + ESCALATE (divergent runs, high CV) #####
accepted: False | blocked: True | escalate: True
reasons: ['max cv 0.365 above 0.1']
scores: {'verification_fraction': 1.0, 'validation_agreement': 1.0, 'max_relative_error': 0.0, 'max_cv': 0.3646, 'n_runs': 3}

##### CASE 4 BLOCK (observed disagrees with reference) #####
accepted: False | blocked: True | escalate: False
reasons: ['validation agreement 0.00 below 0.95', 'max relative error 0.600 above 0.05']

##### CASE 5 BLOCK (only 2 runs, need 3) #####
accepted: False | blocked: True | escalate: False
reasons: ['only 2 runs, need 3']

##### CASE 6 BLOCK (artifact exceeds 200K cap -> verification fails) #####
accepted: False | blocked: True | escalate: False
reasons: ['verification fraction 0.83 below 1.0']
```

In case 6 the oversize artifact failed exactly one of the six verification
checks (`within_file_cap`), dropping the verification fraction to 5 of 6, which
is 0.8333. Because the gate requires a fraction of 1.0, a single failed check is
enough to block. This is the strictness the thesis calls for: codegen would
happily emit a 250000 byte file, but VVUQ refuses to ship it.

## Uncertainty detail: low versus high dispersion

The uncertainty quantifier computes, per metric, the mean, the population
standard deviation, and the coefficient of variation (cv = stdev / mean). The
two run sets used above:

Low dispersion runs (accepted):

| Metric | Mean | Stdev | CV | Divergent at 0.10 |
|--------|------|-------|----|--------------------|
| acceleration_factor | 2.5033 | 0.0125 | 0.0050 | no |
| automated_days | 12.0000 | 0.0816 | 0.0068 | no |

High dispersion runs (blocked and escalated):

| Metric | Mean | Stdev | CV | Divergent at 0.10 |
|--------|------|-------|----|--------------------|
| acceleration_factor | 2.5667 | 0.6549 | 0.2552 | yes |
| automated_days | 12.3333 | 4.4969 | 0.3646 | yes |

The maximum cv jumps from 0.0068 to 0.3646 between the two sets. The gate not
only blocks the high-dispersion deliverable, it sets the escalate flag so a
human is notified, which is the configured policy for divergence.

## Why VVUQ is the more substantial process

The pipeline section produced a complete, syntactically valid, well-formed
deliverable in under a millisecond. That is the easy part. The VVUQ section
shows that turning a candidate into a shippable deliverable requires clearing
six verification checks, a 0.95 agreement bar with bounded relative error, a
recorded human review, and a dispersion bound across three independent runs.
Five of the six cases above were blocked. The decision logic, the thresholds,
and the escalation policy are where the assurance work lives, and they are
deliberately harder to satisfy than code generation is to perform.

## Outcome

| Item | Result |
|------|--------|
| Examples run | 3 of 3, all exit 0 |
| Verification checks demonstrated | 6 of 6 passing on a clean deliverable |
| Validation | agreement 1.0, worst relative error 0.033, human review recorded |
| Uncertainty (accept) | max cv 0.0068, well under 0.10 |
| Gate cases exercised | 6 (1 accept, 5 block, 1 of which escalates) |
| Thresholds source | configs/vvuq_thresholds.yaml (loaded, not defaulted) |

The VVUQ section is fully green and demonstrates both the accept path and every
block and escalate path the gate implements.
