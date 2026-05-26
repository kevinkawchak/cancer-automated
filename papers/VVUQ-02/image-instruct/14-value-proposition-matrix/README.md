# Image Instruction 14: Value Proposition Matrix

Chart family: value proposition matrix (a 2 by 2 positioning quadrant plus value
pillars and a stakeholder panel). Basis: both code generation (v0.7.0 the platform
features) and code execution (v0.8.0 execution README and the thesis). Output: a
single portrait, full page, 300 dpi PNG that positions the VVUQ-02 autonomous
assurance approach against the alternatives on credibility versus efficiency, then
states the three value pillars and the value to each stakeholder.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The thesis is a value claim: holding VVUQ to a higher standard than code, done
autonomously, makes upcoming physical AI oncology trial deliverables faster, less
expensive, and more beneficial to patients than conventional verification. The
matrix places the approaches so the reader sees VVUQ-02 occupying the
high-credibility and high-efficiency quadrant, then maps the three value pillars to
the platform features that deliver them and to each stakeholder.

## Grounding (cite in the footer)

Sources, used for every claim below:

- `papers/VVUQ-02/execution/README.md` (the thesis paragraph; the
  this-run-versus-conventional advantages; the 64 of 172 assurance share).
- `papers/VVUQ-02/execution/03-vvuq/README.md` (the 10-gate surface, the catastrophe
  hard predicates, the hand-back-to-human default).
- `papers/VVUQ-02/codegen/config/standards_map.yaml` and
  `papers/VVUQ-02/inputs/` (the wired external-standards credibility basis).

## The value data (exact, grounded)

Positioning quadrant, x is verification efficiency (cost and time, low to high), y
is assurance credibility (low to high). Place four approaches:

| Approach | x efficiency | y credibility | Quadrant | Note |
|----------|--------------|---------------|----------|------|
| VVUQ-02 autonomous assurance | high | high | top right (featured, star) | 10 gates bound to standards, run autonomously and reproducibly |
| Conventional manual V&V | low | high | top left | credible but slow and expensive, human cycling tools over days |
| Raw LLM code generation | high | low | bottom right | fast and cheap but ungated, not defensible |
| Ad hoc spot checks | low to medium | low to medium | bottom left | neither fast nor credible |

Three value pillars (from the thesis) and the grounding feature for each:

| Pillar | Delivered by |
|--------|--------------|
| Faster | one integrated autonomous loop; generation in microseconds; 172 tests in about 1.38 s; commit-per-section in real time |
| Less expensive | standard-library tree with guarded imports; no human tool cycling; assurance breadth in a single pass |
| More beneficial to patients | 10 gates bound to real standards, 3 catastrophe hard predicates, hand-back-to-human default, recorded human review before ship |

Stakeholder value rows:

| Stakeholder | Value delivered |
|-------------|-----------------|
| Trial sponsor | faster, cheaper, reproducible assurance evidence for a submission |
| Surgeon and care team | a single autonomous humanoid gated to defined safety bounds with human hand-back |
| Patient | safety measures proportional to the concentrated risk of one body, before any non-simulated use |
| Regulator | each decision traceable to a published consensus standard (ASME V&V 40, IEC, ISO, UL, IEEE, FDA) |

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(3, 1,
height_ratios=[3, 1.4, 1.6], left=0.12, right=0.95, top=0.88, bottom=0.08,
hspace=0.32)`: the positioning quadrant on top, the value pillars in the middle,
the stakeholder panel at the bottom.

- Header at `y = 0.965`: `Value Proposition Matrix`. Subtitle at `y = 0.935`:
  `Higher-standard VVUQ, run autonomously: faster, less expensive, more beneficial
  to patients (thesis, execution README)`.
- Quadrant axis: x from 0 to 1 (verification efficiency), y from 0 to 1 (assurance
  credibility). Draw the four quadrants with thin gridline-gray dividers at 0.5,
  shade the top-right quadrant a faint accept-green tint and label it `faster and
  defensible`. Place the four approaches as bubbles at sensible positions
  (VVUQ-02 near 0.82, 0.88 with a star marker and an accept-green ring; manual V&V
  near 0.22, 0.85; raw LLM near 0.85, 0.22; ad hoc near 0.30, 0.32). Axis labels
  `verification efficiency (cost and time) ->` on x and `assurance credibility ->`
  on y, with `low` and `high` at the ends.
- Value pillars axis (middle): three equal rounded cards side by side titled
  `Faster`, `Less expensive`, `More beneficial to patients`, colored teal, accept
  green, and clinical rose respectively, each with its grounding feature text in 9
  pt wrapped.
- Stakeholder panel (bottom): four rows, each a slim rounded bar with the
  stakeholder name at left (trial sponsor, surgeon and care team, patient,
  regulator) and the value delivered in 9 pt at right, alternating panel fill for
  readability.
- Legend (quadrant axis, lower area): a star `VVUQ-02 autonomous assurance
  (featured)` plus a bubble `alternative approach`.

## Color, symbol, and dash rules

- VVUQ-02 bubble accept green with a star, alternatives slate blue or neutral gray,
  top-right quadrant faint accept-green tint, pillar cards teal and accept green
  and clinical rose, stakeholder bars panel fill. White figure background, near
  black text. No dark mode.
- Use `§` only if a clause is cited. Use `->` for the axis direction arrows in
  labels.
- Single hyphens only. Write `hand-back-to-human`, `commit-per-section`,
  `standard-library`, `top-right`, and ranges with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `FancyBboxPatch` and `Rectangle`.
- Drive the quadrant bubbles from a list of (label, x, y, marker, color); use
  `ax.scatter` with a large star marker for VVUQ-02; draw the dividers with
  `ax.axvline`/`ax.axhline` at 0.5.
- Build the pillar cards and stakeholder bars with `FancyBboxPatch`; wrap text with
  `textwrap.fill` at about 30 and 54 characters respectively.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/14-value-proposition-matrix/14-value-proposition-matrix.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/14-value-proposition-matrix/14-value-proposition-matrix.py`.
- Image: `papers/VVUQ-02/imagegen/14-value-proposition-matrix/14-value-proposition-matrix.png`.

## Footer text

`cancer-automated v0.9.0  |  source: execution README thesis and this-run-versus-conventional, execution §03, codegen/config/standards_map.yaml  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- The quadrant places all four approaches with VVUQ-02 starred in the top-right
  accept-green quadrant; both axes labeled with direction and low or high.
- The three value pillars (Faster, Less expensive, More beneficial to patients)
  and the four stakeholder rows are present with grounded text.
- Legend present.
- Header, subtitle, legend, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§` where used; only single hyphens in visible
  text; no dark mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
