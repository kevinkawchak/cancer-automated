# Image Instruction 04: VVUQ Assurance Wheel

Chart family: radar wheel (polar). Basis: both code generation (v0.1.0 `vvuq/`
thresholds) and code execution (v0.2.0 execution §03 scores). Output: a single
portrait, full page, 300 dpi PNG that plots the gate threshold ring, the
accepted deliverable that clears every spoke, and a failing marker per spoke
showing how each dimension can collapse below the ring.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

VVUQ is multi dimensional, and the gate accepts only when every dimension clears
its threshold. The wheel shows six normalized assurance spokes. The dashed ring
is the threshold the gate requires. The accepted deliverable (Case 1) sits on or
outside the ring on all six spokes. A single failing marker on each spoke shows
the worst blocked case for that dimension, so the reader sees that any one spoke
falling inside the ring is enough to block, which is the strictness the thesis
calls for.

## Grounding (cite in the footer)

- `configs/vvuq_thresholds.yaml` and `vvuq/README.md` for the thresholds, and
  `vvuq/verification.py`, `vvuq/validation.py`, `vvuq/uncertainty.py`,
  `vvuq/vvuq_gate.py` for the dimensions (code generation v0.1.0).
- `papers/VVUQ-01/execution/03-vvuq/README.md` for the accepted scores and the
  blocked case values (code execution v0.2.0).

## The six spokes (normalized so 1.0 is best)

Each spoke maps a gate dimension to a 0 to 1 score. Plot three series: the
threshold ring, the accepted deliverable, and the worst failing marker.

| Spoke label | Normalization | Threshold ring | Accepted (Case 1) | Worst failing marker |
|-------------|---------------|----------------|-------------------|----------------------|
| Verification fraction | fraction of checks passed | 1.00 | 1.00 | 0.83 (Case 6) |
| Validation agreement | agreement with reference | 0.95 | 1.00 | 0.00 (Case 4) |
| Validation precision | 1 minus max relative error | 0.95 | 1.00 | 0.40 (Case 4) |
| Uncertainty consensus | 1 minus max coefficient of variation | 0.90 | 0.9932 | 0.6354 (Case 3) |
| Consensus runs | runs divided by 3, capped at 1 | 1.00 | 1.00 | 0.667 (Case 5) |
| Human review | 1 if recorded else 0 | 1.00 | 1.00 | 0.00 (Case 2) |

Notes on provenance: accepted scores are verification fraction 1.0, agreement
1.0, max relative error 0.0 so precision 1.0, max cv 0.0068 so consensus 0.9932,
n runs 3 so runs 1.0, human review recorded so 1.0. Failing markers: Case 6
verification fraction 0.83; Case 4 agreement 0.00 and max relative error 0.600 so
precision 0.40; Case 3 max cv 0.3646 so consensus 0.6354, which is the escalated
case; Case 5 only 2 runs so 0.667; Case 2 no human review so 0.0.

## Layout specification (portrait, full page)

Use the shared page frame with two stacked regions: a large polar wheel on top
and a notes and legend panel below. `GridSpec(2, 1, height_ratios=[2.6, 1.0],
left=0.08, right=0.92, top=0.90, bottom=0.07, hspace=0.20)`; make the top axis
`projection="polar"`.

- Header at `y = 0.965`: `VVUQ Assurance Wheel`. Subtitle at `y = 0.935`: `The
  gate accepts only when every spoke clears the threshold ring`.
- Polar wheel:
  - Six spokes evenly spaced at `theta = 2*pi*k/6`. Radial limit 0 to 1.06.
    Place spoke labels just outside the rim at 11 pt, two lines each where needed
    so they do not crowd.
  - Threshold ring: plot the threshold values as a closed polygon, neutral gray
    `#6B7280`, dashed, line width 2, no fill, labeled `Gate threshold`.
  - Accepted deliverable: closed polygon of the accepted scores, accept green
    `#2E7D32` line width 2.5 with a light green fill at alpha 0.18, labeled
    `Accepted deliverable (Case 1)`.
  - Failing markers: one point per spoke at its worst failing value, drawn as
    filled circles, block red `#C0392B` for Cases 2, 4, 5, 6 and escalate amber
    `#E1A93B` for the uncertainty spoke (Case 3). Annotate each marker with a
    short 9 pt label `Case N value` placed radially inward so the labels sit
    inside the ring and do not overlap the rim labels.
  - Light radial gridlines in gridline gray `#D9DEE3` at 0.2, 0.4, 0.6, 0.8, 1.0
    with small radial tick labels.
- Lower notes panel on panel fill `#F4F6F8` with a thin border, two columns:
  - left, 10 pt: a compact legend restating the three series and the rule `block
    on any failure, escalate on divergence`.
  - right, 10 pt: the one line reading `Accepted clears all six spokes; every
    blocked case fails exactly the spoke shown, and one failing spoke is enough
    to block`.

## Color, symbol, and dash rules

- Threshold ring neutral gray dashed, accepted polygon accept green with light
  fill, failing markers block red except the escalated uncertainty marker in
  escalate amber, gridlines gridline gray, panel fill behind the notes, near
  black text. White background, no dark mode.
- No section symbol required. Write `1 minus max relative error` in words on the
  spoke label, not with a minus glyph that could read as a dash.
- Single hyphens only in any visible text.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`, `numpy as np`.
- Build `angles = np.linspace(0, 2*np.pi, 6, endpoint=False)` and close each
  series by appending its first value and the first angle before plotting, so the
  polygons close cleanly.
- Use `ax.set_theta_offset(np.pi/2)` and `ax.set_theta_direction(-1)` so spoke 1
  is at the top and the wheel reads clockwise.
- Place failing marker labels with `ax.annotate` at a slightly smaller radius
  than the marker so they sit inside the ring; keep rim labels outside via
  `ax.set_xticks(angles)` and `ax.set_xticklabels(...)`.
- Save to `papers/VVUQ-01/imagegen/04-vvuq-assurance-wheel/04-vvuq-assurance-wheel.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/04-vvuq-assurance-wheel/04-vvuq-assurance-wheel.py`.
- Image: `papers/VVUQ-01/imagegen/04-vvuq-assurance-wheel/04-vvuq-assurance-wheel.png`.

## Footer text

`cancer-automated v0.3.0  |  source: configs/vvuq_thresholds.yaml, vvuq/ modules, execution §03  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Six labeled spokes with the threshold ring, the accepted polygon clearing all
  spokes, and one failing marker per spoke at the correct value and case.
- The uncertainty failing marker is escalate amber; the other four are block red.
- Notes panel restates the block on any failure rule.
- Header, subtitle, legend, and footer inside their bands, nothing clipped.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
