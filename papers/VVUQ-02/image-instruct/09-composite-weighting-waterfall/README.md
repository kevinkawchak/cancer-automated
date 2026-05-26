# Image Instruction 09: Composite Weighting Waterfall

Chart family: waterfall (cumulative floating bars with a connector line and a
gating-overlay terminal). Basis: both code generation (v0.7.0
`codegen/config/project.yaml` composite weights) and code execution (v0.8.0
execution §04 gated composite). Output: a single portrait, full page, 300 dpi PNG
that cascades the six frozen composite-score weights to a full weight of 1.00, then
shows the gating overlay that decides whether the realized composite is reported
or withheld.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The composite score is a frozen 6-component weighted sum reused from the PDAC
baseline, and the assurance layer is decisive over it: the score is reported only
when all 10 gates ACCEPT, and the gating overlay sets it to null otherwise. The
waterfall builds the weighting to 1.00 component by component, then shows the
overlay as the final, conditional step, which is the thesis made mechanical: the
gate verdict, not the number, is the decision.

## Grounding (cite in the footer)

Sources, used for every value below:

- `papers/VVUQ-02/codegen/config/project.yaml`, block `composite_score_weights`
  (quality 0.30, time 0.20, cost 0.15, safety 0.15, patient_experience 0.05,
  anastomosis_quality 0.15).
- `papers/VVUQ-02/execution/04-automation/README.md` (the gating overlay sets the
  composite to null unless all 10 gates ACCEPT; the sweep composite mean is 93.56,
  range 93.417 to 93.715 over 32 iterations).

## The waterfall data (exact, six weights to 1.00)

Plot the six components in this order; each floating bar starts at the running
cumulative and rises by its weight. The weights sum to 1.00.

| Step | Component | Weight | Cumulative top | Grounding note |
|------|-----------|--------|----------------|----------------|
| 1 | Quality | 0.30 | 0.30 | largest weight |
| 2 | Time | 0.20 | 0.50 | carries the structural time-dimension caveat |
| 3 | Cost | 0.15 | 0.65 | the cost half of the thesis |
| 4 | Safety | 0.15 | 0.80 | the 3 catastrophe gates feed here |
| 5 | Anastomosis quality | 0.15 | 0.95 | graded against the Fistula Risk Score (VVUQ 07) |
| 6 | Patient experience | 0.05 | 1.00 | smallest weight |
| T | Full composite weight | 1.00 total | 1.00 | the complete 6-component weighting |

Terminal gating overlay (two outcomes, drawn as the final element, not a seventh
weight): `all 10 gates ACCEPT -> composite reported (sweep mean 93.56, range
93.417 to 93.715)` and `any BLOCK or ESCALATE -> composite = null (withheld)`.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(2, 1,
height_ratios=[3, 1], left=0.12, right=0.95, top=0.88, bottom=0.10, hspace=0.26)`:
the large top axis is the waterfall, the short bottom axis is the gating-overlay
terminal.

- Header at `y = 0.965`: `Composite Score Weighting and the Gating Overlay`.
  Subtitle at `y = 0.935`: `Six frozen weights sum to 1.00; the score is reported
  only when all 10 gates ACCEPT (project.yaml, execution §04)`.
- Waterfall axis: x is the seven categories (the six components plus the Full
  composite weight total), y is the cumulative weight from 0.0 to 1.05. Draw each
  component as a floating bar from its starting cumulative to its top cumulative,
  width about 0.6 of the category step. Color the six component bars: Quality navy
  `#1F3A5F`, Time slate blue `#4C72B0`, Cost teal `#2A9D8F`, Safety block red
  `#C0392B` tint, Anastomosis quality clinical rose `#B5566E`, Patient experience
  neutral gray `#6B7280`. Draw the Full composite weight bar as a solid full
  height bar from 0 to 1.00 in primary navy with white edge.
- Connector line: thin dashed neutral gray segments linking the top of each bar to
  the base of the next, so the cumulative build reads clearly.
- Bar labels: inside or above each bar, the weight in 11 pt bold (for example
  `0.30`) and the component name in 10 pt; the cumulative value (for example
  `0.50`) in 9 pt at each connector.
- Grounding notes: a 8.5 pt note under each component name from the table above,
  wrapped, so the reader sees what each weight ties to.
- Gating-overlay terminal axis: two stacked rounded cards. Top card (accept green
  accent): `x ACCEPT on all 10 gates -> composite reported; this sweep 32 of 32,
  mean 93.56, range 93.417 to 93.715`. Bottom card (split block red and escalate
  amber accent): `any BLOCK or ESCALATE -> composite = null, withheld by the
  gating overlay`. A short brace links the waterfall total to these two outcomes
  to show the overlay is a switch on the gate verdict.
- Legend (waterfall axis, upper left): six swatches keyed to the six component
  colors with their weights.

## Color, symbol, and dash rules

- Component bars in the six role colors above, total bar primary navy, connectors
  dashed neutral gray, terminal cards accept green and block red and escalate
  amber accents on panel fill. White figure background, near black text, white
  text on the navy total bar. No dark mode.
- Use `§` in the subtitle (`execution §04`). Use `=` in `composite = null`.
- Single hyphens only. Write weights as decimals; write ranges with the word `to`
  (for example `93.417 to 93.715`).

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Rectangle` and `FancyBboxPatch`.
- Compute the cumulative tops from the weight list with `np.cumsum`; assert the
  sum equals 1.00 as a self check; derive every bar base and height from the
  cumulative array so nothing is hand placed.
- Draw component bars with `ax.bar(bottom=...)` style by passing explicit
  `bottom` values, or with `Rectangle` patches; draw connectors with `ax.plot`.
- Build the two terminal cards with `FancyBboxPatch` on the second axis (axis
  off), text wrapped with `textwrap.fill` at about 48 characters.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/09-composite-weighting-waterfall/09-composite-weighting-waterfall.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/09-composite-weighting-waterfall/09-composite-weighting-waterfall.py`.
- Image: `papers/VVUQ-02/imagegen/09-composite-weighting-waterfall/09-composite-weighting-waterfall.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/config/project.yaml composite_score_weights, execution §04  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Six component floating bars with weights 0.30, 0.20, 0.15, 0.15, 0.15, 0.05
  cascading to a 1.00 total bar; connectors and cumulative labels present.
- The gating-overlay terminal shows both outcomes (reported with the sweep mean
  93.56 and range, or null on non-ACCEPT).
- Bars labeled with weights, grounding notes present, legend present.
- Header, subtitle, legend, terminal cards, and footer inside their bands, no
  overlap, none clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
