# VVUQ Methodology (Grounded in ASME V&V 40-2018)

This codegen tree implements a Verification, Validation, and Uncertainty
Quantification (VVUQ) assurance layer for an autonomous surgical humanoid. The
methodology is not invented here. It instantiates the risk-informed credibility
framework of real, in-use standards so that the assurance argument is defensible
to a regulator.

## Why a standard-based VVUQ layer

The thesis of VVUQ-02 is that the assurance process must be held to a higher
standard than the code it gates. "A higher standard" is made literal here by
binding the gate to published consensus standards rather than to ad hoc
thresholds.

## Primary anchor: ASME V&V 40-2018

ASME V&V 40-2018 ("Assessing Credibility of Computational Modeling through
Verification and Validation: Application to Medical Devices") is the standard the
United States FDA references in its 2023 guidance on assessing the credibility of
computational modeling and simulation in medical device submissions. Its core
construct is reused directly by this tree:

1. Question of interest: the specific decision the model informs.
2. Context of use (COU): the role and scope of the model in that decision.
3. Model risk = model influence x decision consequence.
4. Credibility goals set in proportion to model risk.
5. Verification and validation activities sized to meet those goals.

In this tree each of the 10 VVUQ gates declares its question of interest and COU
in `docs/vvuq_gate_spec.md`, and its model risk drives the strictness of its
thresholds in `config/vvuq_thresholds.yaml`. The three immediate-catastrophe
gates (06 vascular no-fly, 09 human collision, 10 fault and e-stop) carry the
highest model risk and therefore the tightest credibility goals (verification
pass fraction 1.0, the lowest coefficient-of-variation bounds, and an extra hard
predicate).

## The three dimensions, as executed

The gate composes three results, mirroring the VVUQ-01 framework at
`papers/VVUQ-01/execution/03-vvuq/README.md` and the top-level `vvuq/` package.

```
  candidate humanoid behavior (one of 10 capabilities)
        |
        v
  +-------------------------------+
  | Verification (V&V 40 sec 8)   |  did we build it right?
  | verify(case)                  |  structural and policy checks
  +-------------------------------+  pass fraction must equal 1.0
        |
        v
  +-------------------------------+
  | Validation (V&V 40 sec 9)     |  did we build the right thing?
  | validate(observed, reference) |  agreement vs an INDEPENDENT reference,
  +-------------------------------+  max relative error, human review recorded
        |
        v
  +-------------------------------+
  | Uncertainty quantification    |  how dispersed are the >= 3 runs?
  | quantify(runs)                |  coefficient of variation per metric
  +-------------------------------+  (NASA-STD-7009A credibility, UQ factor)
        |
        v
  +-------------------------------+
  | VVUQGate.evaluate(...)        |  block on any failure;
  |                               |  escalate to human on divergence
  +-------------------------------+
        |
        +--> ACCEPT   (all dimensions pass)
        +--> BLOCK    (any dimension fails)
        +--> ESCALATE (uncertainty divergence, hand back to human)
```

### Verification

Verification answers "did we build the deliverable right?" with structural and
policy predicates only. It does not look at numeric correctness, which is
validation's job. Each gate supplies its own predicate list (for example, ZMP
samples present for all ticks, no NaN in the centre-of-mass trace, output file
under the size cap, lint clean). The gate requires `fraction_passed == 1.0`,
consistent with ASME V&V 40 code and calculation verification expectations and
with IEC 62304 software verification.

### Validation against an INDEPENDENT reference

Validation compares observed metrics against a trusted reference that is produced
independently of the run under test. The reference artifacts in `data/reference/`
are derived from standard-defined nominal values and closed-form analytic models,
not from the same stochastic simulation that produces the observed values. This
independence is what makes the comparison a validation rather than a self-check,
per ASME V&V 40 section 9 (comparator and validation activities). Agreement is
the fraction of compared metrics within the per-gate maximum relative error, and
a human review must be recorded (ISO 14971 risk control verification).

### Uncertainty quantification

Across at least three seeded runs the tree computes, per metric, the mean, the
population standard deviation, and the coefficient of variation (cv = stdev /
mean). The maximum cv is compared against a per-gate bound. Divergence above the
bound sets ESCALATE, following the NASA-STD-7009A treatment of uncertainty as a
first-class credibility factor and the UL 4600 and IEEE 7009 requirement that an
autonomous system default to a safe state under uncertainty.

## Decision policy

`block_on_any_failure: true` and `escalate_on_divergence: true`. Any single
failing dimension blocks the candidate. The autonomy path (gate 04) and the fault
path (gate 10) must default to hand-back-to-human on any ESCALATE, which is the
fail-safe behaviour required by IEEE 7009-2024 and UL 4600.

## Mapping to the standards corpus

The binding from each gate to its governing standards is machine-readable in
`config/standards_map.yaml` and is wired into the runtime by
`src/vvuq/gate_registry.py`, which loads the corpus manifest from
`../inputs/standards/manifest.yaml`. See `docs/standards_map.md` for the human
readable table.
