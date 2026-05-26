# Image Instruction 07: Validation Parity Scatter

Chart family: scatter / parity plot (observed versus independent reference, with
error bars). Basis: both code generation (v0.7.0
`codegen/data/reference/` truth files) and code execution (v0.8.0 execution §03
`vvuq_decisions.json` and the four adversarial cases). Output: a single portrait,
full page, 300 dpi PNG that plots each gate decision against the y equals x parity
line, where on-diagonal points pass validation and off-diagonal points are blocked
or escalated.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

Validation asks whether the model matches an independent reference. A parity plot
makes that literal: the 10 nominal gates sit on the y equals x line because the
observed metric equals its independent reference (agreement 1.0). The adversarial
cases fall off the line in different ways, and the figure shows how each
deviation maps to a BLOCK or an ESCALATE, including the two cases that sit on the
line yet still do not ship because a hard predicate fails or the dispersion is too
high.

## Grounding (cite in the footer)

Sources, used for every point below:

- `papers/VVUQ-02/execution/03-vvuq/artifacts/vvuq_decisions.json` for the 10
  nominal gates (verification_fraction 1.0, validation_agreement 1.0,
  max_relative_error 0.0, max_cv 0.0, n_runs 3).
- `papers/VVUQ-02/execution/03-vvuq/README.md` for the four adversarial cases B to
  E and their verbatim metrics.
- `papers/VVUQ-02/codegen/config/vvuq_thresholds.yaml` for the bound annotations.

## The parity data (exact)

Axes: x is the independent reference value normalized to 1.0; y is the observed
value normalized to the same reference. The y equals x diagonal is perfect
validation.

| Point | What it is | x (reference) | y (observed) | Extra | Decision | Color |
|-------|-----------|---------------|--------------|-------|----------|-------|
| Nominal cluster | the 10 gates, observed equals reference | 1.0 | 1.0 | agreement 1.0, cv 0.0 | ACCEPT | accept green |
| Case D 03 balance | ZMP margin driven 50 percent off reference | 1.0 | 0.50 | agreement 0.00, rel err 0.500 above 0.03 | BLOCK | block red |
| Case C 08 perception | 4 of 5 structural checks pass | 1.0 | 0.80 | verification fraction 0.80 below 1.0 | BLOCK | block red |
| Case E 02 finger-force | 3 runs spread 80 to 120 percent of reference | 1.0 | 1.0 | error bar 0.80 to 1.20, max cv 0.163 above 0.10 | ESCALATE | escalate amber |
| Case B 06 vascular | continuous metrics match reference | 1.0 | 1.0 | hard check failed: hard_stop_violations | BLOCK | block red |

Cases B and E both sit at (1.0, 1.0): plot them with a small horizontal offset
from the nominal cluster so all three are visible, Case E carrying a vertical
error bar from 0.80 to 1.20 (the run spread that produces cv 0.163), Case B
carrying a block red `X` overlay marking the hard-predicate failure.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(2, 1,
height_ratios=[3, 1], left=0.12, right=0.95, top=0.88, bottom=0.10, hspace=0.22)`:
the large top axis is the parity plot, the short bottom axis holds two annotation
cards.

- Header at `y = 0.965`: `Validation Parity: Observed versus Independent
  Reference`. Subtitle at `y = 0.935`: `On the y = x line passes validation; off
  the line blocks; dispersion escalates (execution §03)`.
- Parity axis: x from 0.4 to 1.1, y from 0.4 to 1.1, equal aspect. Draw the y
  equals x line as a dashed neutral gray reference labeled `perfect validation (y =
  x)`. Shade a thin accept-green band along the diagonal at plus or minus the gate
  agreement tolerance to show the pass corridor near (1.0, 1.0).
- Points: plot the nominal cluster as a single accept green marker at (1.0, 1.0)
  with a count badge `10 gates: observed = reference`. Plot Case D at (1.0, 0.50)
  and Case C at (1.0, 0.80) as block red diamonds, each with a short leader to a
  9 pt label giving the verbatim reason. Plot Case E near (1.02, 1.0) as an
  escalate amber circle with the 0.80 to 1.20 vertical error bar. Plot Case B near
  (0.98, 1.0) as an accept-corner marker overlaid with a block red `X`.
- Drop lines: from Case D and Case C, draw thin vertical drop lines to the x axis
  to emphasize the size of the deviation from the reference.
- Legend (upper left of the parity axis): accept green `ACCEPT (on diagonal)`,
  block red `BLOCK (off diagonal or hard predicate)`, escalate amber `ESCALATE
  (dispersion)`, plus the dashed `y = x` sample.
- Bottom annotation axis: two rounded cards side by side. Left card (escalate amber
  accent): `Case E sits on the line but its three runs spread 80 to 120 percent of
  the reference; max cv 0.163 exceeds the 0.10 bound, so the gate ESCALATEs to
  hand-back-to-human`. Right card (block red accent): `Case B matches the reference
  on every continuous metric, but the hard predicate hard_stop_violations is
  non-zero, so the catastrophe gate BLOCKs anyway`.

## Color, symbol, and dash rules

- Nominal accept green, blocks block red, escalate amber, diagonal dashed neutral
  gray, pass corridor faint accept-green tint, cards on panel fill. White figure
  background, near black text. No dark mode.
- Use `§` in the subtitle (`execution §03`). Use `=` in `y = x`.
- Single hyphens only. Write `80 to 120 percent`, `4 of 5`, `hand-back-to-human`,
  and `non-zero` with single hyphens; use the word `to` for ranges.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt` and `numpy as np`.
- Plot the diagonal with `ax.plot([0.4, 1.1], [0.4, 1.1], ...)`; use
  `ax.errorbar` for Case E; use `ax.scatter` and `ax.annotate` for the rest; set
  `ax.set_aspect("equal")`.
- Drive the points from one list of dicts (label, x, y, yerr, decision, color,
  reason) so markers, leaders, and colors are derived.
- Build the two bottom cards with `FancyBboxPatch` on the second axis (axis off),
  text wrapped with `textwrap.fill` at about 46 characters.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/07-validation-parity-scatter/07-validation-parity-scatter.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/07-validation-parity-scatter/07-validation-parity-scatter.py`.
- Image: `papers/VVUQ-02/imagegen/07-validation-parity-scatter/07-validation-parity-scatter.png`.

## Footer text

`cancer-automated v0.9.0  |  source: execution §03 vvuq_decisions.json, codegen/config/vvuq_thresholds.yaml  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- The y equals x line and the accept corridor are drawn; the nominal cluster sits
  at (1.0, 1.0) with the 10-gate badge.
- Cases C (0.80) and D (0.50) are off-diagonal block red; Case E carries the 0.80
  to 1.20 error bar in amber; Case B carries the block red hard-predicate X.
- Both bottom annotation cards present with verbatim reasons; legend present.
- Header, subtitle, legend, cards, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
