# VVUQ-02: Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.20421754-blue.svg)](https://doi.org/10.5281/zenodo.20421754)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![Releases](https://img.shields.io/badge/Releases-v0.7.0%20to%20v1.2.0-brightgreen.svg)](../../releases.md)
[![Gates](https://img.shields.io/badge/VVUQ%20gates-10%20humanoid--specific-red.svg)](codegen/docs/vvuq_gate_spec.md)
[![Tests](https://img.shields.io/badge/pytest-172%20passed%2C%200%20skipped-brightgreen.svg)](execution/01-foundation/)
[![Sweep](https://img.shields.io/badge/Sweep-32%2F32%20clear%2C%20composite%2093.56-brightgreen.svg)](execution/04-automation/)
[![Standards](https://img.shields.io/badge/Standards-14%20%2B%202%20clinical-9cf.svg)](inputs/standards/)
[![Authored](https://img.shields.io/badge/Authored-Claude%20Code%20Opus%204.7%20(1M)%20Max-purple.svg)](https://www.anthropic.com/claude)

### Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20421754)

VVUQ-02 is the second work in the [papers](../) series. It applies the VVUQ-01
thesis to the hardest subject available: a single autonomous humanoid surgeon, a
clearly labeled hypothetical 2030 Unitree H2-Surgical 1.0, that performs the
60-second 8-phase Whipple on patient PAT-PDAC-0001 with its own two dexterous
hands and no teleoperation. Because one humanoid concentrates all error potential
into one body, the assurance layer must be more substantial, stricter, and more
thoroughly exercised than the control code it checks. This README focuses only on
the VVUQ-02 directory.

> **Thesis.** The robotic code assurance process, not code generation, is the
> substantial and decision-bearing part of the AI workflow, holding VVUQ to a
> higher standard than code itself. These safety measures help ensure upcoming
> Physical AI oncology trial developments are faster, less expensive, and more
> beneficial to patients than conventional verifications.

## Table of Contents

- [Verification developments and progress](#verification-developments-and-progress)
- [Building process within the work](#building-process-within-the-work)
- [The ten humanoid-specific gates](#the-ten-humanoid-specific-gates)
- [Results and what they mean for the industry](#results-and-what-they-mean-for-the-industry)
- [The processing feat accomplished by AI](#the-processing-feat-accomplished-by-ai)
- [Accelerated timeline versus conventional methods](#accelerated-timeline-versus-conventional-methods)
- [Repository structure](#repository-structure)
- [Related VVUQ works and final DOIs](#related-vvuq-works-and-final-dois)
- [Responsible use](#responsible-use)
- [License](#license)

## Verification developments and progress

VVUQ-02 advanced over six releases. The verification work moves from a generated
assurance codebase, to an autonomous execution record, to a figure program, and
finally to a manuscript built only from the recorded evidence.

| Release | Stage | VVUQ verification development |
|:--|:--|:--|
| v0.7.0 | Codegen | A standalone codebase implements 10 humanoid-specific gates bound to external standards; 172 tests including a 64-item 10-gate decision surface |
| v0.8.0 | Execution | The whole tree runs (exit 0), 172 of 172 tests pass, the 10-gate surface is recorded (10 ACCEPT, 3 BLOCK paths, 1 ESCALATE), and a 32-iteration sweep clears every gate |
| v0.9.0 | Image instructions | 15 figures are fully specified before any pixel, the assurance spec ahead of the render |
| v1.0.0 | Imagegen | 15 figures are rendered from the specification with the arithmetic reconciled to the source records |
| v1.1.0 | Draft paper | A LaTeX scaffold names the exact codegen, execution, inputs, and imagegen files each section must synthesize; 41 final references |
| v1.2.0 | Full paper | The scaffold is processed into a finished manuscript with 13 body-width tables and five figures |

## Building process within the work

VVUQ-02 is built in a straight line from the instruction specification to the
finished manuscript, with the generated codebase and its execution record at the
center.

```
  instructions/        inputs/                 codegen/  (v0.7.0)
  (spec, zero code)     (standards + clinical)  (generated 10-gate codebase)
  +----------------+    +------------------+     +-------------------------+
  | prompt-instruct|    | standards/ (14)  |     | config/ schemas/ src/   |
  | output-instruct| -> | clinical/ (2)    | ->  | data/ docs/ tests/(172) |
  | templates/T_04 |    | (ASME, IEC, ISO, |     | kinematics..vvuq..llm   |
  +----------------+    |  ISO/TS, UL, ...)|     +-------------------------+
                       +------------------+                 |
                                                            v
  execution/  (v0.8.0)                          image-instruct/   imagegen/
  +-------------------------+                    (v0.9.0, 15 specs) (v1.0.0, 15 figs)
  | 01 foundation           |                    +------------+     +------------+
  | 02 pipeline             |   ------------>     | NN/README  | --> | NN.py +    |
  | 03 vvuq (10-gate)       |   recorded          | full spec  |     | NN.png     |
  | 04 automation (sweep)   |   evidence          +------------+     +------------+
  | 05 humanoid-deployment  |                                 |
  +-------------------------+                                 v
            |                                       draft-paper/  (v1.1.0)
            |                                       +----------------------+
            +-------------------------------------> | scaffold + bracketed |
                          source files named        | build instructions   |
                          per section               | + final 41 refs      |
                                                     +----------------------+
                                                                |
                                                                v
                                                     full-paper/  (v1.2.0)
                                                     finished prose + 13 tables
                                                                |
                                                                v
                                                     final-paper/  (Zenodo)
                                                DOI 10.5281/zenodo.20421754
```

The execution record is staged in five numbered sections:

```
  01 foundation       determinism (sensor CSV byte-identical), 172 tests, lint green
        |
  02 pipeline         intent -> compile -> act -> score, concordance 1.000
        |
  03 vvuq             10-gate surface: 10 ACCEPT, 3 BLOCK paths, 1 ESCALATE
        |
  04 automation       32-iteration sweep (32/32 clear all gates), 1790-line tournament
        |
  05 deployment       60 s Whipple, 1000-row positional stream, 3 catastrophe gates
```

## The ten humanoid-specific gates

A candidate humanoid behavior must clear 10 distinct gates before it ships. Each
gate verifies (fraction == 1.0), validates against an independent reference, and
quantifies uncertainty across seeded runs; the three catastrophe gates add the
tightest bounds plus a hard predicate.

```
  candidate humanoid behaviors per iteration
        |
   +----v-------------------------------------------------------+
   | 01 bimanual-handeye-servo        06 vascular-no-fly-hand *  |
   | 02 dexterous-finger-force        07 bimanual-suturing       |
   | 03 whole-body-balance            08 perception-scene        |
   | 04 autonomous-plan-correctness   09 shared-or-collision *   |
   | 05 instrument-grasp-handover     10 fault-estop-degrade *   |
   +----v-------------------------------------------------------+
        |  each gate: Verify (== 1.0) -> Validate (independent
        |  reference) -> Quantify (coefficient of variation)
        v
   ACCEPT (all 10 pass)  /  BLOCK (any fail)  /  ESCALATE (divergence)
   composite reported only when all 10 gates ACCEPT
   * immediate-catastrophe gates: V == 1.0, tightest CV, plus a hard predicate
```

Standards anchor set: ASME V&V 40-2018 and NASA-STD-7009A for model credibility
(with the FDA 2023 computational modeling guidance), IEC 80601-2-77 and IEC
60601-1 for robotic surgery, ISO 13482, ISO/TS 15066, ISO 10218-1, and ISO 9283
for service and collaborative robot safety, IEC 62304, ISO 14971, and ISO
13849-1 for software and risk, and UL 4600 and IEEE 7009 for autonomy and
fail-safe design.

## Results and what they mean for the industry

The deterministic 32-iteration Latin hypercube sweep (seed 20260525) clears all
10 gates on every iteration; the composite mean is 93.56 (min 93.417, max
93.715), reported only because all gates ACCEPT. The two largest generated
artifacts are featured and processed: the 1790-line four-entrant
`comparison.json` (128 round verdicts, 100 percent caveat coverage) and the
1000-row, 27-column positional sensor stream (every row distinct, no repetition),
both reproduced byte for byte from the seed.

In the four-entrant tournament the single mobile humanoid lands second to the
eight-arm PancreSpeed cart by under half a composite point, because parallel arms
shorten the throughput-weighted score; the humanoid is nonetheless the
higher-risk, higher-assurance platform the paper is built around.

For the new Physical AI oncology trial industry the lesson is that the credibility
argument can be made defensible rather than ad hoc: every gate, behavior, and
safety surface is traced to a published external standard already used in
practice, so an inexpensive autonomous run can stand as evidence for a future
trial. VVUQ-02 is the practical proof that the VVUQ-01 thesis holds for the
hardest case (one autonomous body), and its records become the evidentiary core
that the VVUQ-03 and VVUQ-04 bills cite.

## The processing feat accomplished by AI

Claude Code Opus 4.7 (1M) Max generated and ran VVUQ-02 autonomously in a
managed, ephemeral cloud container, pushing each file in real time: the codebase
across 11 commits in one pull request, and the execution record across 8 commits
in another.

- **Generated a standalone assurance codebase:** eleven module families
  (kinematics, sensors, perception, autonomy, hands, balance, safety, suturing,
  vvuq, simulation, and more), with 172 tests including a 64-item 10-gate
  decision surface, runnable on the Python standard library with guarded optional
  backends.
- **Executed the whole tree and recorded it honestly:** every entry point to exit
  0, 172 of 172 tests passed with zero skipped, byte-identical determinism from
  seed 20260525, and the 10-gate ACCEPT, BLOCK, and ESCALATE surface captured.
- **Specified then rendered 15 figures:** each fully specified before any pixel,
  then rendered as self-contained matplotlib scripts whose arithmetic reconciles
  to the source files (treemap tiles sum to 172 tests, weights sum to 1.00,
  swimmer durations sum to 60 s).
- **Wrote the manuscript from a scaffold:** the bracketed sections were processed
  into finished prose with 13 body-width tables and five figures, without
  modifying the draft.
- **Kept the CI green:** all additions are LaTeX, Markdown, BibTeX, Python that is
  ruff clean, or a zip, so lint-and-format and tests passed across Python 3.10,
  3.11, and 3.12.

## Accelerated timeline versus conventional methods

VVUQ-02's end goal is the final paper. It was reached over roughly two days
(v0.7.0 on 2026-05-26 to v1.2.0 on 2026-05-27), versus the many months a
conventional verified surgical-robotics codebase with standards traceability,
its execution evidence, a figure program, and a manuscript would take.

```
  Conventional path (6-18 months)            VVUQ-02 (about 2 days)
  +-----------------------------------+      +-----------------------------------+
  | build the 10-gate codebase        |      | v0.7.0 codegen (172 tests)        |
  | run + document standards parity   |  vs  | v0.8.0 execution (32/32 sweep)    |
  | produce the figure program        |      | v0.9.0 + v1.0.0 figures (15)      |
  | draft + revise the manuscript     |      | v1.1.0 + v1.2.0 paper (13 tables) |
  +-----------------------------------+      +-----------------------------------+
        serial, multi-month effort             autonomous, real-time commits
```

## Repository structure

```
papers/VVUQ-02/
  README.md          (this file)
  instructions/      prompt-instruct.md, output-instruct.md (lineage)
  inputs/            wired standards corpus + clinical baselines
    standards/       ASME V&V 40, IEC 80601-2-77, ISO/TS 15066, ... (14)
    clinical/        Dutch cohort baseline, Fistula Risk Score (2)
  templates/         Template_04 regulatory and FDA submission scaffold
  codegen/           v0.7.0 standalone 10-gate humanoid codebase
    config/ schemas/ src/ data/reference/ docs/ tests/ (172 passing)
  execution/         v0.8.0 full run record of the codegen tree
    01-foundation/ 02-pipeline/ 03-vvuq/ 04-automation/ 05-humanoid-deployment/
  image-instruct/    v0.9.0 fifteen figure specifications + master README
  imagegen/          v1.0.0 fifteen rendered figures (scripts + 300 dpi PNGs)
  draft-paper/       v1.1.0 LaTeX scaffold (bracketed sections + 41 refs)
  full-paper/        v1.2.0 finished manuscript (13 tables, five figures)
  final-paper/       author-finalized manuscript (PDF + LaTeX on Zenodo)
```

## Related VVUQ works and final DOIs

VVUQ-02 builds on VVUQ-01 and is in turn cited by the two bills. The final paper
and bill DOI for each work in the series:

| Work | Final artifact | Author final edits (PDF + LaTeX) |
|:--|:--|:--|
| [VVUQ-01](../VVUQ-01) | Method paper | [10.5281/zenodo.20372501](https://doi.org/10.5281/zenodo.20372501) |
| VVUQ-02 (this work) | Humanoid VVUQ paper | [10.5281/zenodo.20421754](https://doi.org/10.5281/zenodo.20421754) |
| [VVUQ-03](../VVUQ-03) | H. R. 9510 bill | [10.5281/zenodo.20454870](https://doi.org/10.5281/zenodo.20454870) |
| [VVUQ-04](../VVUQ-04) | FD&C Act amendment | [10.5281/zenodo.20485580](https://doi.org/10.5281/zenodo.20485580) |

## Responsible use

The Unitree H2-Surgical 1.0 is a clearly labeled hypothetical 2030 platform and
every number in the supporting records is a simulation result; the four-entrant
comparison is simulation against simulation. The 10 VVUQ gates plus a recorded
human reviewer must clear any candidate before any non-simulated use, and a real
deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD clearance,
IRB approval, and regulatory authorization. Mentions of the FDA and other bodies
are respectful and non-presumptuous.

## License

Generated text and diagrams are distributed under the Creative Commons
Attribution 4.0 International License (CC BY 4.0).
