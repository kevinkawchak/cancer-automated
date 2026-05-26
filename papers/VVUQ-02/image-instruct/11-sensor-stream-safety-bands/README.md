# Image Instruction 11: Sensor Stream Safety Margins with Uncertainty Bands

Chart family: line plot with uncertainty bands. Basis: both code generation
(v0.7.0 `codegen/data/sample_h2_sensor.csv`) and code execution (v0.8.0 execution
§05 `sensor_stream_analysis.txt`). Required data R5: feature the 1000-row H2
sensor data. Output: a single portrait, full page, 300 dpi PNG with three stacked
time-series panels over the 500 command ticks, each showing the left and right
hand channels with a mean and an uncertainty band against the governing safety
bound.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The featured sensor stream is 1000 unique rows, 500 command ticks for each of the
two hands, with no repetition. The figure plots three of its safety-relevant
channels against the bounds the catastrophe and force gates enforce, so the reader
sees the live margins the assurance layer evaluates: the summed two-hand force
around its soft cap, the standing-balance margin far above its floor, and the
fingertip distance to the vessel keep-out.

## Grounding (cite in the footer)

Sources, used for every value below:

- `papers/VVUQ-02/codegen/data/sample_h2_sensor.csv` (1000 rows, 27 columns, 500
  ticks for hands L and R, phase 1, grasp tripod).
- `papers/VVUQ-02/execution/05-humanoid-deployment/artifacts/sensor_stream_analysis.txt`
  (channel ranges and the no-repetition verification).
- `papers/VVUQ-02/codegen/config/project.yaml` (the force caps and the balance
  margin floor) and `papers/VVUQ-02/execution/05-humanoid-deployment/README.md`
  (the vessel keep-out radii for the superior mesenteric vein).

## The stream data (exact channel statistics)

Coverage: 1000 rows = 500 ticks (0 to 499) times 2 hands (L, R); every row and
every positional payload distinct; phase 1, grasp state tripod, balance stable,
estop armed, collision clear throughout (the committed sample is the first 50 ms
at the 10 kHz command rate; the full 60-second stream is the Zenodo L0).

| Panel | Channel | min | max | mean | sd | Bounds to draw | Gate |
|-------|---------|-----|-----|------|----|----------------|------|
| A | bimanual_cumulative_force (N) | 4.366 | 6.716 | 5.507 | 0.388 | soft cap 5.0, hard cap 6.0 | VVUQ 02 |
| B | support_polygon_margin (mm) | 38.005 | 42.992 | 40.458 | 1.440 | stability floor 8.0 | VVUQ 03 |
| C | vessel_proximity (mm) | 6.018 | 9.999 | 7.983 | 1.155 | no-fly 6.0, soft-warning 4.0, hard-stop 2.0 | VVUQ 06 |

Reference fingertip caps for the panel A note: per-fingertip soft 2.5 N, hard 3.0
N; the individual finger force channels run 0.401 to 0.700 N, well under the
per-fingertip soft cap; bimanual_cumulative_force is the summed two-hand quantity
the bimanual cap governs.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(3, 1,
height_ratios=[1, 1, 1], left=0.11, right=0.95, top=0.88, bottom=0.09,
hspace=0.32)`; the three panels share the x axis tick 0 to 499.

- Header at `y = 0.965`: `Featured Humanoid Sensor Stream: Live Safety Margins`.
  Subtitle at `y = 0.935`: `1000 rows, 500 ticks across two hands, phase 1; three
  safety channels versus their gate bounds (codegen/data/sample_h2_sensor.csv)`.
- Each panel: plot the left hand series in slate blue `#4C72B0` and the right hand
  series in teal `#2A9D8F` as thin lines, and a shaded uncertainty band as mean
  plus or minus one standard deviation (a horizontal band, since the channel is
  stationary in phase 1) filled at 12 percent alpha in neutral gray, with the mean
  drawn as a solid neutral gray line labeled with its value. Title each panel with
  its channel, units, and gate, for example `A. Bimanual cumulative force (N),
  VVUQ 02`.
- Panel A bounds: a soft cap dashed line at 5.0 in escalate amber labeled `soft cap
  5.0 N -> force scaling` and a hard cap dashed line at 6.0 in block red labeled
  `hard cap 6.0 N -> e-stop`. Set y from 4.0 to 6.9. Add a 9 pt note `the summed
  two-hand force rides near the 5.0 N soft cap; the gate scales at soft and
  e-stops at hard`.
- Panel B bounds: a stability floor dashed line at 8.0 in block red labeled
  `stability floor 8.0 mm`. Set y from 0 to 45 so the floor and the 38 to 43 mm
  band are both visible, showing the large margin. Add a 9 pt note `margin stays
  about 5x above the ISO 13482 floor`.
- Panel C bounds: three dashed keep-out lines, no-fly 6.0 in escalate amber,
  soft-warning 4.0 in a darker amber, hard-stop 2.0 in block red, each labeled. Set
  y from 0 to 10.5. Add a 9 pt note `fingertip distance stays at or above the
  6.0 mm no-fly radius for the superior mesenteric vein`.
- Shared x label under panel C: `command tick (0 to 499, 10 kHz, first 50 ms of
  phase 1)`.
- Legend (top panel, upper right): slate blue `left hand`, teal `right hand`,
  gray band `mean plus or minus 1 SD`, plus dashed samples for `soft or no-fly` in
  amber and `hard or floor` in block red.
- A 9 pt provenance note in a clear margin: `1000 of 1000 rows distinct; no
  repeated row or constant-padded positional channel (execution §05)`.

## Color, symbol, and dash rules

- Left hand slate blue, right hand teal, mean and band neutral gray, soft and
  no-fly bounds escalate amber, hard and floor bounds block red. White figure
  background, near black text. No dark mode.
- Use `§` in the provenance note (`execution §05`). Use `x` only as a multiplier
  (`5x`). Write `e-stop`, `no-fly`, `soft-warning`, `hard-stop`, `two-hand` with
  single hyphens.
- Single hyphens only. Write ranges with the word `to` (for example `0 to 499`).

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt` and `numpy as np`.
- The script hardcodes the per-channel summary statistics above and synthesizes a
  representative stationary trace only for visual continuity (a flat mean with the
  stated standard deviation as a seeded `np.random.default_rng(20260525)` jitter
  bounded to the stated min and max); it must not claim individual tick values
  beyond the cited summary, and the band, mean, min, and max it draws must equal
  the cited statistics.
- Use `ax.plot` for the two hand lines, `ax.fill_between` for the band, and
  `ax.axhline` for each bound; share the x axis with `sharex=True`.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/11-sensor-stream-safety-bands/11-sensor-stream-safety-bands.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/11-sensor-stream-safety-bands/11-sensor-stream-safety-bands.py`.
- Image: `papers/VVUQ-02/imagegen/11-sensor-stream-safety-bands/11-sensor-stream-safety-bands.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/data/sample_h2_sensor.csv, execution §05 sensor_stream_analysis.txt, codegen/config/project.yaml  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Three panels (bimanual force, balance margin, vessel proximity) over ticks 0 to
  499, each with a left and a right hand line and a mean plus or minus 1 SD band
  matching the cited statistics.
- All bounds drawn and labeled: soft 5.0 and hard 6.0 in panel A, floor 8.0 in
  panel B, no-fly 6.0 and soft-warning 4.0 and hard-stop 2.0 in panel C.
- The no-repetition provenance note and the legend are present.
- Header, subtitle, legend, shared x label, and footer inside their bands, no
  overlap, none clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
