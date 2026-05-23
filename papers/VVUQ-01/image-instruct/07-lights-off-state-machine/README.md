# Image Instruction 07: Lights-Off Factory Safety State Machine

Chart family: state diagram with an interlock panel and a case table. Basis: both
code generation (v0.1.0 `physical-ai/lights_off_factory.py`) and code execution
(v0.2.0 execution §05). Output: a single portrait, full page, 300 dpi PNG that
draws the safety gating state machine, the four default interlocks, and the four
exercised cases.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

A lights off line leaves no time for a human in the loop, so the assurance has to
be enforced automatically. The figure shows that the controller only runs when
every interlock is satisfied, returns to dark when a batch completes within its
fault budget, and emergency stops the moment faults exceed the budget. One of the
four interlocks is `vvuq_gate_online`, which wires the Stage 1 assurance machinery
directly into the Stage 2 deployment safety chain.

## Grounding (cite in the footer)

- `physical-ai/lights_off_factory.py` and `physical-ai/README.md` for the state
  machine and interlocks (code generation v0.1.0).
- `papers/VVUQ-01/execution/05-physical-ai-stage2/README.md` for the four default
  interlocks and the four exercised cases (code execution v0.2.0).

## The states and transitions (exact)

States: `DARK` (idle), `RUNNING`, `ESTOP` (emergency stop), `FAULT` (blocked
before running).

| From | To | Condition |
|------|----|-----------|
| DARK | RUNNING | all interlocks satisfied |
| RUNNING | DARK | batch completes within fault budget |
| RUNNING | ESTOP | cumulative faults exceed budget |
| (pre run gate) | FAULT | any interlock unsatisfied, run blocked |

Default interlocks, all satisfied at start: `estop_armed`, `perimeter_clear`,
`vvuq_gate_online`, `human_oversight_remote`.

## The four exercised cases (exact, from execution §05)

| Case | Setup | End state | Blocked | Faults |
|------|-------|-----------|---------|--------|
| A clean run | 6 tasks, all succeed, budget 1 | DARK | no | 0 |
| B over budget | 9 tasks, every 3rd faults, budget 1 | ESTOP | no | 2 |
| C interlock off | `perimeter_clear` unsatisfied | FAULT | yes | not applicable |
| D within budget | 9 tasks, every 4th faults, budget 3 | DARK | no | 3 |

Case A per cell tally: cell-a 3 completed 0 faulted, cell-b 3 completed 0
faulted. Case B per cell tally: cell-a 1 completed 1 faulted, cell-b 1 completed
1 faulted, the line halted mid batch after the second fault because the budget
was 1.

## Layout specification (portrait, full page)

Use the shared page frame with three stacked regions: the interlock panel, the
state machine, and the case table. `GridSpec(3, 1, height_ratios=[0.7, 2.2,
1.1], left=0.06, right=0.94, top=0.90, bottom=0.07, hspace=0.22)`.

- Header at `y = 0.965`: `Lights-Off Factory Safety State Machine`. Subtitle at
  `y = 0.935`: `Runs only when every interlock is satisfied, emergency stops past
  the fault budget`.
- Interlock panel (top axis): four tokens in a row on panel fill `#F4F6F8`, each a
  rounded pill with an accept green `#2E7D32` check and the interlock name, 11 pt:
  `estop_armed`, `perimeter_clear`, `vvuq_gate_online`, `human_oversight_remote`.
  Give the `vvuq_gate_online` pill a primary navy `#1F3A5F` border at 2.5 pt and a
  small 9 pt caption `Stage 1 VVUQ wired into Stage 2 safety` so it stands out.
- State machine (middle axis), all geometry in axis coordinates, `axis("off")`:
  - Four state nodes drawn as rounded rectangles with `FancyBboxPatch`: `DARK`
    upper left in neutral gray `#6B7280`, `RUNNING` center in teal `#2A9D8F`,
    `ESTOP` lower right in block red `#C0392B`, `FAULT` lower left in escalate
    amber `#E1A93B`. State names in white 14 pt bold inside the nodes.
  - Directed edges with `FancyArrowPatch`, neutral gray, each labeled 9.5 pt:
    DARK to RUNNING `interlocks satisfied`; RUNNING back to DARK `batch within
    budget`; RUNNING to ESTOP `faults exceed budget`; a small pre run gate glyph
    (a diamond) between DARK and RUNNING with a branch to FAULT labeled `interlock
    unsatisfied, blocked`.
  - Small case tags placed next to the transition each case takes: tag `A` and
    `D` on the RUNNING to DARK edge, tag `B` on the RUNNING to ESTOP edge, tag `C`
    on the gate to FAULT branch. Tags are small filled circles with the case
    letter in white.
- Case table (bottom axis): a clean 5 column table (Case, Setup, End state,
  Blocked, Faults) rendered with `ax.table` or manual cells on alternating panel
  fill and white rows, 10 pt. Color the End state cell text by state color and
  bold it.

## Color, symbol, and dash rules

- DARK gray, RUNNING teal, ESTOP block red, FAULT escalate amber, interlock
  checks accept green, the highlighted interlock navy border, connectors neutral
  gray, panel fill for panels and alternating rows, near black text. White
  background, no dark mode.
- No section symbol required. Underscores in interlock names like
  `vvuq_gate_online` are code identifiers and are kept verbatim. Use single
  hyphens elsewhere; `Lights-Off` uses a single hyphen.
- Single hyphens only in visible text.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`; from `matplotlib.patches`
  import `FancyBboxPatch`, `FancyArrowPatch`, `Polygon`, `Circle`.
- Fix node centers as constants in axis coordinates so edges and tags compute
  from them and never overlap; route the RUNNING to DARK return edge with a
  curved `connectionstyle="arc3,rad=0.3"` so it does not collide with the
  outbound edge.
- Save to `papers/VVUQ-01/imagegen/07-lights-off-state-machine/07-lights-off-state-machine.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/07-lights-off-state-machine/07-lights-off-state-machine.py`.
- Image: `papers/VVUQ-01/imagegen/07-lights-off-state-machine/07-lights-off-state-machine.png`.

## Footer text

`cancer-automated v0.3.0  |  source: physical-ai/lights_off_factory.py, execution §05  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Four states with the four labeled transitions, the pre run gate branch to
  FAULT, and case tags A, B, C, D on the correct transitions.
- Interlock panel shows all four interlocks satisfied with `vvuq_gate_online`
  highlighted.
- Case table reproduces the four cases with correct end states and faults.
- Header, subtitle, and footer inside their bands, nothing clipped or
  overlapping.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
