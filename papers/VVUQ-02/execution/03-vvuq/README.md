# Section 03: VVUQ Decision Surface (the 10-gate centerpiece)

This is the decision-bearing section and the operational proof of the thesis.
The pipeline in Section 02 produced candidate humanoid behaviors fast and
deterministically. This section runs the assurance layer that decides whether any
candidate may ship: 10 humanoid-specific gates, each a Verify then Validate then
Quantify gate bound to its own independent reference and to published external
standards. The assurance layer carries 64 of the 172 unit tests and is held to a
higher bar than the control code, exactly as the thesis claims.

## Contents

| File | What it records |
|------|-----------------|
| artifacts/gate_decision_surface.txt | Verbatim ACCEPT / BLOCK / ESCALATE captures across five cases |
| artifacts/vvuq_report.md | The nominal report: all 10 gates ACCEPT over their references |
| artifacts/vvuq_decisions.json | Per-gate decision, scores, and resolved external standards |

## The 10 gates and their thresholds (as loaded from config)

Each gate requires verification fraction equal to 1.0 (a single failed check
blocks). The validation agreement bound, the maximum relative error, and the
coefficient-of-variation bound tighten for the higher-risk gates. The three
immediate-catastrophe gates carry a 1.00 agreement bar, the tightest dispersion
bounds, and an extra hard predicate that must also hold.

| # | Gate | Agreement | Max rel err | CV bound | Catastrophe |
|---|------|-----------|-------------|----------|-------------|
| 01 | bimanual-handeye-servo | 0.97 | 0.050 | 0.08 | - |
| 02 | dexterous-finger-force | 0.95 | 0.050 | 0.10 | - |
| 03 | whole-body-balance | 0.98 | 0.030 | 0.06 | - |
| 04 | autonomous-plan-correctness | 0.95 | 0.050 | 0.10 | - |
| 05 | instrument-grasp-handover | 0.96 | 0.050 | 0.10 | - |
| 06 | vascular-no-fly-hand | 1.00 | 0.010 | 0.05 | YES |
| 07 | bimanual-suturing-anastomosis | 0.96 | 0.050 | 0.08 | - |
| 08 | perception-scene-understanding | 0.95 | 0.050 | 0.10 | - |
| 09 | shared-or-human-collision | 1.00 | 0.020 | 0.06 | YES |
| 10 | fault-estop-graceful-degradation | 1.00 | 0.020 | 0.05 | YES |

## Gate decision flow (as executed)

```
  candidate humanoid behavior
        |
        v
   verify() -----------> validate() -----------> quantify() -----------> evaluate()
   checks all True       agreement vs the         CV across 3+ seeded     hard predicate
   fraction == 1.0       independent reference     runs <= gate bound      (catastrophe gates)
        |                    |                          |                       |
        +--------------------+--------------------------+-----------------------+
                                       |
                 any dimension fails -> BLOCK
                 CV above bound      -> ESCALATE (default hand-back-to-human)
                 all pass + hard ok  -> ACCEPT
```

## A. Nominal: all 10 gates over their independent references

Run with observed equal to each gate's independent reference artifact, all checks
passing, a recorded human review, and three tight seeded runs:

```
  01 bimanual-handeye-servo             -> ACCEPT
  02 dexterous-finger-force             -> ACCEPT
  03 whole-body-balance                 -> ACCEPT
  04 autonomous-plan-correctness        -> ACCEPT
  05 instrument-grasp-handover          -> ACCEPT
  06 vascular-no-fly-hand               -> ACCEPT
  07 bimanual-suturing-anastomosis      -> ACCEPT
  08 perception-scene-understanding     -> ACCEPT
  09 shared-or-human-collision          -> ACCEPT
  10 fault-estop-graceful-degradation   -> ACCEPT
  all ACCEPT: True
```

This is the only path on which the composite score is reported. The full report
is `artifacts/vvuq_report.md` and the per-gate scores and resolved standards are
in `artifacts/vvuq_decisions.json`.

## B to E: the BLOCK and ESCALATE paths

The decision surface is only credible if the failing paths actually fail. Four
adversarial cases were run; the verbatim output is in
`artifacts/gate_decision_surface.txt`.

### B. BLOCK: a catastrophe-gate hard predicate fails

```
  vascular-no-fly-hand -> BLOCK; reasons: ['hard check failed: hard_stop_violations_zero']
```

The vascular no-fly gate (VVUQ 06) carries the extra predicate that the count of
hard-stop volume breaches must be zero. With every verification, validation, and
uncertainty dimension passing, a single hard-predicate failure still blocks. This
is the IEC 80601-2-77 hazardous-situation response and the ISO 14971 risk
control.

### C. BLOCK: a verification check fails (fraction below 1.0)

```
  perception-scene-understanding -> BLOCK; reasons: ["verification fraction 0.80 below 1.0: ['all_structures_segmented: ']"]
```

Four of five structural checks pass, but the gate requires a fraction of exactly
1.0, so 0.80 blocks. Verification is pass or fail, not a weighted average.

### D. BLOCK: validation agreement below the bound

```
  whole-body-balance -> BLOCK; reasons: ['validation agreement 0.00 below 0.98', 'max relative error 0.500 above 0.03']
```

Driving the observed ZMP margin 50 percent off its independent reference collapses
agreement and breaches the 0.03 relative-error bound, so the balance gate (VVUQ
03) blocks on validation, the ISO 13482 stability property.

### E. ESCALATE: dispersion above the CV bound (divergence)

```
  dexterous-finger-force -> ESCALATE; escalate=True; reasons: ['max cv 0.163 above 0.1']
  scores: {'verification_fraction': 1.0, 'validation_agreement': 1.0, 'max_relative_error': 0.0, 'max_cv': 0.1633, 'n_runs': 3}
```

Verification and validation both pass, but three runs spread from 80 to 120
percent of the reference give a coefficient of variation of 0.163, above the 0.10
bound. The gate does not BLOCK outright; it ESCALATEs, which defaults the autonomy
and fault paths to hand-back-to-human under UL 4600 and IEEE 7009. This is the
quantification dimension (NASA-STD-7009A treats uncertainty as a first-class
credibility factor) doing its job.

## Decision surface summary

| Case | Gate | Dimension exercised | Decision |
|------|------|---------------------|----------|
| A | all 10 | nominal, observed equals reference | 10x ACCEPT |
| B | 06 vascular-no-fly | hard catastrophe predicate | BLOCK |
| C | 08 perception | verification fraction 0.80 | BLOCK |
| D | 03 balance | validation agreement and rel err | BLOCK |
| E | 02 finger-force | uncertainty CV 0.163 | ESCALATE |

Five cases, three distinct BLOCK mechanisms, one ESCALATE, one full-ACCEPT
sweep. The harness blocks or escalates on the first failing dimension and only
accepts when verification, validation, quantification, and any hard predicate all
hold.

## Why this is the substantial part (the thesis, operationalized)

The control behaviors in Section 02 were generated in microseconds. Turning any
one of them into a shippable result requires clearing a 1.0 verification
fraction, an agreement bar as high as 1.00, a relative-error bound as tight as
0.01, a CV bound as tight as 0.05, a recorded human review, and, on the three
catastrophe gates, an extra hard predicate. The assurance harness is larger
(64 of 172 tests), stricter, and more thoroughly exercised than the code it
judges. Because one humanoid concentrates all error potential into two hands with
no second cart and no human bedside assistant, that asymmetry is the whole point:
the assurance, not the generation, is the decision-bearing work, and an
autonomous agent performed all of it cheaply and reproducibly.

## External standards anchored here

| Gate | Resolved governing standards (from the wired corpus) |
|------|------------------------------------------------------|
| 01 bimanual-handeye-servo | IEC 80601-2-77:2019, ISO 9283:1998, ASME V&V 40-2018 |
| 02 dexterous-finger-force | IEC 80601-2-77:2019, ISO/TS 15066:2016 |
| 03 whole-body-balance | ISO 13482:2014, IEC 60601-1 |
| 04 autonomous-plan-correctness | UL 4600 (2023), IEEE Std 7009-2024, IEC 62304 |
| 05 instrument-grasp-handover | IEC 80601-2-77:2019, ISO 9283:1998 |
| 06 vascular-no-fly-hand | IEC 80601-2-77:2019, ISO 14971:2019 |
| 07 bimanual-suturing-anastomosis | IEC 80601-2-77:2019, Fistula Risk Score |
| 08 perception-scene-understanding | ASME V&V 40-2018, IEC 62304 |
| 09 shared-or-human-collision | ISO/TS 15066:2016, ISO 10218-1:2011, ISO 13482:2014 |
| 10 fault-estop-graceful-degradation | IEC 60601-1, ISO 13849-1:2023, IEEE Std 7009-2024 |

The standards are resolved at runtime from `inputs/standards/manifest.yaml`, so
every gate decision in `artifacts/vvuq_decisions.json` carries its governing
designations. The assurance argument is therefore traceable to published
consensus standards already used in real life, which is what makes it defensible
to a regulator and credible as the basis for a future physical AI oncology trial.
