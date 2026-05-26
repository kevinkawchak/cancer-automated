# Image Instruction 01: Platform Generation to Assurance Pipeline

Chart family: workflow / pipeline / flow diagram. Basis: both code generation
(v0.7.0 `codegen/`) and code execution (v0.8.0 execution §02 and the execution
README flow). Output: a single portrait, full page, 300 dpi PNG that traces one
candidate humanoid behavior from the on-prem LLM intent through deterministic
compilation and the behavior models into the 10-gate assurance layer, showing
that generation is fast and deterministic while assurance is the substantial,
decision bearing stage.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The figure makes the thesis legible as a process: producing candidate behaviors
is microsecond cheap and deterministic, while deciding whether any one may ship is
the substantial work. The pipeline reads left to right and top to bottom in three
horizontal tiers, with a visible asymmetry between the thin, fast generation tier
and the thick, gated assurance tier.

## Grounding (cite in the footer)

Sources, used for every node and label below:

- `papers/VVUQ-02/execution/02-pipeline/README.md` for the data flow (propose
  intents to compile to act to the composite) and the per behavior-group results
  (autonomy concordance 1.000, kinematics tip frame, perception Dice, hands force,
  balance ZMP margin, suturing RMSE).
- `papers/VVUQ-02/execution/README.md` for the execution flow (the five sections)
  and the gate decision (ACCEPT, BLOCK, ESCALATE).
- `papers/VVUQ-02/codegen/config/project.yaml` for the platform (71 DOF, 2 hands,
  8 phases, 60 s) and the 6-component composite weights.

## The pipeline data (exact, three tiers)

Tier A, generation (thin, fast). Two nodes connected by an arrow:

| Node | Label lines | Source |
|------|-------------|--------|
| A1 on-prem LLM intent | `propose_intents()` / `phase 1, phase 5` / `source=reference (offline)` | execution §02.1 |
| A2 deterministic compile | `compile_intents()` / `20-DOF finger target + tip frame + grasp` / `concordance 1.000` | execution §02.1 |

Tier B, behavior models (the act stage). Six nodes in a row, each a behavior group
with its one-line executed result:

| Node | Behavior group | Executed result | Gate |
|------|----------------|-----------------|------|
| B1 | kinematics | `tip = (-0.2796, -0.2895, 1.8185) m` | 01 |
| B2 | perception | `mean Dice 1.0000 at 0 occlusion` | 08 |
| B3 | hands | `track 1.84 N; bimanual 5.0 N within hard` | 02, 05 |
| B4 | balance | `ZMP margin 130.00 mm; stable` | 03 |
| B5 | suturing | `PJ RMSE 0.00326 N; grade A` | 07 |
| B6 | safety | `vessel, collision, fault surfaces` | 06, 09, 10 |

Tier C, assurance (thick, gated). One wide band holding the 10 gates feeding a
single decision node:

- The 10 gates `01` to `10`, with `06`, `09`, `10` flagged as immediate
  catastrophe (block red accent).
- Each gate annotated `Verify (fraction == 1.0) -> Validate (vs independent
  reference) -> Quantify (CV bound)`.
- Decision node: `ACCEPT (all 10 pass) / BLOCK (any fail) / ESCALATE (divergence)`
  and below it `composite reported only when all 10 ACCEPT (mean 93.56)`.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single full width axis in the
content band (`GridSpec` 1 by 1, `left=0.06, right=0.94, top=0.91, bottom=0.07`),
all geometry in axis coordinates `0..1`.

- Header at `y = 0.965`: `Platform Pipeline: Generation is Fast, Assurance is the
  Decision`. Subtitle at `y = 0.935`: `One candidate behavior from on-prem intent
  to a gated ship decision (VVUQ-02 execution §02 to §03)`.
- Tier A occupies the top ~18 percent of the content axis. Draw A1 and A2 as two
  small rounded rectangles (`FancyBboxPatch`, autonomy purple `#6A4C93` edge,
  panel fill) with a teal arrow A1 to A2. Place a 9 pt italic stamp to the right:
  `generation: microseconds, deterministic`.
- Tier B occupies the middle ~30 percent. Draw B1 to B6 as six equal rounded
  rectangles in a row (slate blue `#4C72B0` edge, panel fill), each with its
  behavior name in 11 pt bold and its executed result in 9 pt. A single teal
  down-arrow from the A2 node fans into the six B nodes (use thin neutral gray
  connectors).
- Tier C occupies the lower ~44 percent and is visibly the thickest. Draw one wide
  primary navy `#1F3A5F` framed band titled `Assurance layer (the substantial,
  decision-bearing stage)` in 14 pt bold white on a navy header strip. Inside,
  arrange the 10 gate chips in two rows of five (chips `01` to `10`); fill the
  catastrophe chips `06`, `09`, `10` with block red `#C0392B` and the rest with
  teal `#2A9D8F`, white chip text. Below the chips, a single horizontal band reads
  the per-gate sequence `Verify -> Validate -> Quantify`.
- Decision node at the bottom of Tier C: a centered rounded rectangle split into
  three colored segments, accept green `ACCEPT`, block red `BLOCK`, escalate amber
  `ESCALATE`, with the caption `composite reported only when all 10 gates ACCEPT
  (sweep mean 93.56)` in 9 pt beneath.
- Asymmetry caption: a 10 pt italic note spanning the left gutter between Tier B
  and Tier C, rotated 90 degrees, `assurance carries 64 of 172 tests`.
- Connectors: vertical arrows B tier to C tier (six thin gray lines converging),
  and a single bold teal arrow from the gate band to the decision node.
- Legend at the lower right of the content band: four swatches, autonomy purple
  `on-prem intent`, slate blue `behavior model`, teal `gate (pass path)`, block
  red `immediate-catastrophe gate`.

## Color, symbol, and dash rules

- Generation tier purple and slate, behavior tier slate, assurance band navy with
  teal and block red gate chips, decision node accept green, block red, escalate
  amber. White figure background, near black text, white text on the navy and the
  colored chips.
- Use `§` for the section references in the subtitle and any node note (for
  example `execution §02`, `execution §03`).
- Single hyphens only. Write `microseconds`, `64 of 172 tests`, and ranges with
  the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `FancyBboxPatch`, `FancyArrowPatch`, and
  `Rectangle`.
- One axis spanning the content band; `ax.set_xlim(0, 1)`, `ax.set_ylim(0, 1)`,
  `ax.axis("off")`. Lay out all tiers and chips from a small list of (x, y, w, h)
  tuples computed from the tier fractions above, so positions are derived and need
  no manual nudging.
- Wrap node result text with `textwrap.fill` at about 22 characters so it stays
  inside each box.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/01-platform-pipeline-flow/01-platform-pipeline-flow.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/01-platform-pipeline-flow/01-platform-pipeline-flow.py`.
- Image: `papers/VVUQ-02/imagegen/01-platform-pipeline-flow/01-platform-pipeline-flow.png`.

## Footer text

`cancer-automated v0.9.0  |  source: execution §02 pipeline, execution README flow, codegen/config/project.yaml  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Three tiers present with the assurance tier visibly thickest; all six behavior
  nodes and all 10 gate chips present and labeled.
- Catastrophe gates `06`, `09`, `10` flagged in block red; decision node shows
  ACCEPT, BLOCK, ESCALATE.
- Header, subtitle, legend, asymmetry note, and footer inside their bands, no
  overlap, none clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
