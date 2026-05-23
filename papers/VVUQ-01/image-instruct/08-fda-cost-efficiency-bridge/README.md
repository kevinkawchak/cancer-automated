# Image Instruction 08: FDA Cost-Efficiency Bridge and Credibility Assessment

Chart family: financial bridge (top) plus bullet assessment (bottom), a combined
financial and value proposition figure. Basis: both code generation (v0.1.0
platform levers) and code execution (v0.2.0 execution comparison and credibility
context), with qualitative grounding from the input corpus. Output: a single
portrait, full page, 300 dpi PNG.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

The thesis has a cost half: the automated VVUQ process is accomplished faster and
less expensively than current verification methods. The top panel is a financial
bridge that attributes the cost reduction to each automation lever, indexed
against a conventional baseline. The bottom panel is a credibility assessment
using the measured compliance scores, framed against the FDA credibility section
and the ASME V&V 40 standard. Together they make the value proposition explicit.

## Honesty and labeling (mandatory)

The cost bridge is an illustrative planning index, not measured dollars. The
baseline is set to 100 and the lever reductions are a planning model grounded in
the real platform capabilities and the execution comparison, pending measured
cost data. The figure must label the top panel axis `Relative effort index
(baseline 100, illustrative planning model)` and carry a 9 pt note `Illustrative
planning index, not measured dollars; pending a cost study`. The credibility
scores in the bottom panel are the measured values cited below and are labeled as
measured.

## Grounding (cite in the footer)

- `papers/VVUQ-01/execution/README.md`, section comparing this execution with
  conventional high-end server processing, for the levers: near zero setup, one
  integrated loop, systematic assurance beyond the shipped tests, self verifying
  documentation (code execution v0.2.0).
- `pipeline/` stages and `vvuq/vvuq_gate.py` for the automation levers (code
  generation v0.1.0).
- Input corpus under `papers/VVUQ-01/inputs/` for the FDA MIDD cost efficiency
  framing, the FDA credibility section reference, the ASME V&V 40 standard, and
  the measured compliance scores Verification 81.9 of 100 and Validation 85.75
  percent.

## Top panel data, the cost bridge (illustrative index)

A horizontal cascading bridge from the baseline down to the automated index. The
reductions are the planning model.

| Step | Type | Index after step | Change | Lever, grounded in |
|------|------|------------------|--------|--------------------|
| Conventional verification | baseline | 100 | start | current manual MIDD verification |
| AI text protocol generation | reduction | 82 | minus 18 | instruction stage |
| AI Python model generation | reduction | 66 | minus 16 | codegen stage |
| Automated execution and log capture | reduction | 54 | minus 12 | execution stage |
| Automated VVUQ gate vs manual review | reduction | 40 | minus 14 | vvuq gate |
| Autonomous cloud loop, no provisioning | reduction | 30 | minus 10 | one integrated agent loop |
| Automated VVUQ cost | endpoint | 30 | land at 30 | net automated index |

Headline annotation: about 70 percent lower than the conventional baseline, an
illustrative 3.3x cost efficiency, pending measured data.

## Bottom panel data, credibility bullets (measured)

Two horizontal bullet rows on a 0 to 100 scale with qualitative bands.

| Metric | Measured value | Target marker | Reference |
|--------|----------------|---------------|-----------|
| Verification overall score | 81.9 of 100 | 80 | FDA §VI.B credibility |
| Validation tests final score | 85.75 of 100 | 80 | ASME V&V 40, FDA §VI.B |

Qualitative bands for both rows: 0 to 60 weak, 60 to 80 fair, 80 to 90 good, 90
to 100 strong. Add a 9 pt note: `Uncertainty margin, max cv 0.0068 against the
0.10 bound, ample headroom`.

## Layout specification (portrait, full page)

Use the shared page frame with two stacked panels. `GridSpec(2, 1,
height_ratios=[1.7, 1.2], left=0.08, right=0.94, top=0.90, bottom=0.08,
hspace=0.30)`.

- Header at `y = 0.965`: `FDA Cost-Efficiency Bridge and Credibility Assessment`.
  Subtitle at `y = 0.935`: `An illustrative cost index with measured VVUQ
  credibility scores`.
- Top panel, the bridge:
  - Vertical category axis listing the seven steps top to bottom; horizontal value
    axis is the index 0 to 100.
  - Baseline and endpoint as full bars from 0: baseline primary navy `#1F3A5F`,
    endpoint accept green `#2E7D32`.
  - The five reductions as floating teal `#2A9D8F` bars, each spanning from the
    previous index to the new index, connected by neutral gray `#6B7280` dashed
    leaders so the cascade reads as one bridge.
  - Label each reduction with its change (`-18`, `-16`, `-12`, `-14`, `-10`) and
    each total bar with its index value. Place the 3.3x headline in a small accept
    green pill near the endpoint.
  - The illustrative planning note sits under the panel axis title.
- Bottom panel, the bullets:
  - Two rows. For each, draw the four qualitative bands as graded light gray to
    panel fill rectangles behind a thinner measured value bar in primary navy,
    and a block red `#C0392B` vertical target marker at 80.
  - Label each row with the metric name and the measured value (`81.9 of 100`,
    `85.75 of 100`) and the reference using the section symbol `FDA §VI.B`.
  - Add the uncertainty margin note beneath the two rows.

## Color, symbol, and dash rules

- Bridge baseline navy, reductions teal, endpoint accept green, connectors neutral
  gray dashed; bullets banded grays with a navy measured bar and a block red
  target marker; panel fill backgrounds; near black text. White background, no
  dark mode.
- Use the section symbol `§` in `FDA §VI.B`. Do not write `SS` or `Section VI.B`.
- Single hyphens only in visible text. Write changes as `-18` with a single
  hyphen and factors as `3.3x`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`, `numpy as np`.
- Compute the bridge from `steps = [100, 82, 66, 54, 40, 30]` so the reduction
  bars and connectors derive from successive values; draw floating bars with
  `ax.barh` using a computed `left`.
- Build the bullet bands with stacked `ax.barh` segments and the target marker
  with `ax.plot` of a short vertical segment; keep both rows on a fixed 0 to 100
  axis.
- Save to `papers/VVUQ-01/imagegen/08-fda-cost-efficiency-bridge/08-fda-cost-efficiency-bridge.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/08-fda-cost-efficiency-bridge/08-fda-cost-efficiency-bridge.py`.
- Image: `papers/VVUQ-01/imagegen/08-fda-cost-efficiency-bridge/08-fda-cost-efficiency-bridge.png`.

## Footer text

`cancer-automated v0.3.0  |  source: execution README comparison, pipeline and vvuq levers, inputs corpus (FDA §VI.B, ASME V&V 40)  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Bridge cascades 100, 82, 66, 54, 40, 30 with correct reduction labels and a
  navy baseline and accept green endpoint, plus the 3.3x headline.
- The illustrative planning index note is present and clearly visible.
- Two bullet rows show 81.9 and 85.75 with a target marker at 80 and the FDA
  §VI.B reference using the section symbol.
- Header, subtitle, and footer inside their bands, nothing clipped.
- Only single hyphens in visible text; `§` used for the FDA section; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
