# Image Instruction 13: Assurance Cost Assessment (Autonomous Cloud versus Conventional)

Chart family: financial assessment (a cost-and-time bridge with a bullet
comparison and an honesty card). Basis: both code generation (v0.7.0 the
standard-library codegen tree) and code execution (v0.8.0 execution README, the
`This execution versus conventional high-end server processing` section). Output: a
single portrait, full page, 300 dpi PNG that frames the cost half of the thesis,
that the autonomous cloud assurance run is faster and less expensive than
conventional verification, while stating honestly what a conventional server still
does better.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The thesis claims the assurance work is accomplished faster and less expensively
than conventional verification. This figure makes the cost argument explicit and
honest. The bridge shows a conventional verification baseline reduced by four
documented advantages of the autonomous cloud run to a lower autonomous cost, the
bullet panel compares three cost drivers, and a card states the cases where a
conventional provisioned server still does more.

> Honesty note for the renderer. The repository does not record dollar figures, so
> the bridge uses an illustrative relative index (conventional baseline set to
> 100) to communicate direction and proportion only. The direction of each step,
> and the four advantages and three conventional strengths, are grounded verbatim
> in `execution/README.md`. Label the axis `relative cost index (illustrative,
> grounded in execution README this-run-versus-conventional)` so no reader mistakes
> it for a measured cost.

## Grounding (cite in the footer)

Sources, used for the structure and every label below:

- `papers/VVUQ-02/execution/README.md`, the `This execution versus conventional
  high-end server processing` section (the Better, Different, and Worse lists) and
  the thesis paragraph (faster, less expensive).
- `papers/VVUQ-02/execution/01-foundation/test-suite.md` (172 tests in about 1.38
  s) and `papers/VVUQ-02/codegen/README.md` (standard library plus a few small
  packages with guarded optional imports) for the grounded anchors.

## The assessment data (illustrative index, grounded direction)

Cost bridge, conventional baseline 100 reduced to the autonomous run. The step
sizes are illustrative; the reasons are grounded.

| Step | Direction | Grounded reason (execution README) |
|------|-----------|------------------------------------|
| Conventional verification baseline | 100 | human cycles terminal, editor, and git over days; installs the full optional matrix first |
| Near-zero setup | down | standard library plus four small packages with guarded imports; everything core ran immediately |
| One integrated agent loop | down | read, run, process, document, lint, commit, push in a single loop with no tool context switch |
| Assurance breadth in one pass | down | full ACCEPT, BLOCK, ESCALATE surface plus the safety surface plus structural processing of the 1790-line comparison and 1000-row stream |
| Self-verifying record | down | every command and verbatim output captured, reproducible rather than trusted |
| Autonomous cloud run | residual | the lower-cost result the bridge lands on |

Bullet comparison, three cost drivers (autonomous bar versus a conventional
reference tick), all illustrative index:

| Driver | Autonomous | Conventional reference |
|--------|------------|------------------------|
| Setup time | low | high (full optional matrix install) |
| Integration overhead | low (one loop) | high (manual tool cycling over days) |
| Assurance breadth per run | high | medium (unit tests alone) |

Conventional-strength card (the Worse list, stated plainly): live on-prem LLM
intent and judging, real Zenodo deposition, and mujoco or Isaac physics need a
provisioned server with GPUs and keys; no display, GPU, or persistent warm cache
in the ephemeral container.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(3, 1,
height_ratios=[3, 2, 1.4], left=0.12, right=0.95, top=0.88, bottom=0.09,
hspace=0.34)`: the cost bridge on top, the bullet comparison in the middle, the
honesty card at the bottom.

- Header at `y = 0.965`: `Assurance Cost Assessment`. Subtitle at `y = 0.935`:
  `Autonomous cloud VVUQ versus conventional verification; the cost half of the
  thesis (execution README)`.
- Cost bridge axis: a left-to-right waterfall. Draw the conventional baseline as a
  full bar from 0 to 100 in neutral gray, four downward floating reduction bars in
  teal `#2A9D8F` (each starting at the running total and dropping), and the
  autonomous residual as a solid bar in accept green `#2E7D32`. Connect bar tops
  with dashed neutral gray connectors. Label each step with its grounded reason
  wrapped to about 22 characters and the running index value. y axis `relative
  cost index (illustrative)` from 0 to 105.
- Bullet comparison axis: three horizontal bullet rows, one per driver. Each row
  has a light panel-fill track, an accept green bar for the autonomous value, and a
  block red vertical tick for the conventional reference, with the driver name at
  left and `lower is better` or `higher is better` noted per row in 8.5 pt.
- Honesty card (bottom axis, axis off): a single rounded rectangle, escalate amber
  left accent, titled `What a conventional server still does better` with the
  conventional-strength text in 9 pt, wrapped.
- Time annotation: a 10 pt italic note across the bridge, `faster too: the 172-test
  suite runs in about 1.38 s and generation is microsecond-scale; the assurance,
  not the generation, is where the cost sits`.
- Legend (bridge axis, upper right): neutral gray `conventional baseline`, teal
  `documented reduction`, accept green `autonomous cloud run`.

## Color, symbol, and dash rules

- Baseline neutral gray, reductions teal, autonomous accept green, conventional
  bullet ticks block red, honesty card escalate amber accent. White figure
  background, near black text. No dark mode.
- Use `§` only if a clause is cited; the execution README reference is by name.
  Use `x` only as a multiplier if needed.
- Single hyphens only. Write `near-zero`, `self-verifying`, `on-prem`,
  `microsecond-scale`, and ranges with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Rectangle` and `FancyBboxPatch`.
- Compute the bridge running totals with `np.cumsum` over the signed step list so
  the bars and connectors are derived; keep the step sizes in a single editable
  list clearly commented as illustrative.
- Build the bullet rows and the honesty card with `Rectangle` and `FancyBboxPatch`;
  wrap text with `textwrap.fill`.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/13-assurance-cost-assessment/13-assurance-cost-assessment.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/13-assurance-cost-assessment/13-assurance-cost-assessment.py`.
- Image: `papers/VVUQ-02/imagegen/13-assurance-cost-assessment/13-assurance-cost-assessment.png`.

## Footer text

`cancer-automated v0.9.0  |  source: execution README this-run-versus-conventional, execution §01 test-suite.md  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- The cost bridge runs from the conventional baseline through four labeled
  reductions to the autonomous residual; the index axis is labeled illustrative.
- The three-driver bullet comparison and the conventional-strength honesty card are
  present; the faster-too time note is present.
- The illustrative-index honesty note is reflected in the axis label so the figure
  does not overclaim measured cost.
- Header, subtitle, legend, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§` where used; only single hyphens in visible
  text; no dark mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
