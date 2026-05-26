# Image Instruction 04: Gate to Standard Binding Matrix

Chart family: heatmap / matrix plot (categorical binding matrix with margins).
Basis: both code generation (v0.7.0 `codegen/config/standards_map.yaml`,
`inputs/standards/manifest.yaml`) and code execution (v0.8.0 the `External
standards anchored here` tables in execution §02, §03, and §05). Required data R2:
the external-standards anchoring used throughout the directories must all be
represented in one image. Output: a single portrait, full page, 300 dpi PNG that
places the 10 VVUQ gates (rows) against the 15 governing standards (columns) and
marks every binding, with row and column margins.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The credibility of the assurance argument comes from binding each gate to
published consensus standards already used in real life, resolved at runtime from
the wired corpus. The matrix shows that every gate is anchored, that every one of
the 15 standards is used by at least one gate or the cross-cutting set, and that
the three catastrophe gates and the workhorse standard IEC 80601-2-77 carry the
densest anchoring.

## Grounding (cite in the footer)

Sources, used for every cell below:

- `papers/VVUQ-02/codegen/config/standards_map.yaml` (the machine-readable gate to
  standard binding and the cross-cutting set).
- `papers/VVUQ-02/inputs/standards/manifest.yaml` (the 14 consensus standards with
  designation and issuing body) and `papers/VVUQ-02/inputs/clinical/` (the Fistula
  Risk Score clinical anchor).
- `papers/VVUQ-02/execution/03-vvuq/artifacts/vvuq_decisions.json` and the
  `External standards anchored here` tables in execution §02, §03, and §05 for the
  resolved per-gate standards.

## The binding data (exact)

Columns, the 15 standards (left to right), grouped by domain:

| Col | Designation | Domain |
|-----|-------------|--------|
| C1 | ASME V&V 40-2018 | model credibility |
| C2 | NASA-STD-7009A | model credibility |
| C3 | IEC 80601-2-77:2019 | robotic surgery |
| C4 | IEC 60601-1 | robotic surgery |
| C5 | ISO/TS 15066:2016 | service-robot safety |
| C6 | ISO 13482:2014 | service-robot safety |
| C7 | ISO 10218-1:2011 | service-robot safety |
| C8 | ISO 9283:1998 | service-robot safety |
| C9 | IEC 62304 | software and risk |
| C10 | ISO 14971:2019 | software and risk |
| C11 | ISO 13849-1:2023 | software and risk |
| C12 | UL 4600 (2023) | autonomy |
| C13 | IEEE Std 7009-2024 | autonomy |
| C14 | FDA CM&S Credibility 2023 | regulatory |
| C15 | Fistula Risk Score | clinical |

Rows, the 10 gates plus a cross-cutting row at the bottom. A filled cell means the
gate binds to that standard.

| Row | Bound columns |
|-----|---------------|
| 01 bimanual-handeye-servo | C1, C3, C8 |
| 02 dexterous-finger-force | C3, C5 |
| 03 whole-body-balance | C4, C6 |
| 04 autonomous-plan-correctness | C9, C12, C13 |
| 05 instrument-grasp-handover | C3, C8 |
| 06 vascular-no-fly-hand (catastrophe) | C3, C10 |
| 07 bimanual-suturing-anastomosis | C3, C15 |
| 08 perception-scene-understanding | C1, C9 |
| 09 shared-or-human-collision (catastrophe) | C5, C6, C7 |
| 10 fault-estop-graceful-degradation (catastrophe) | C4, C11, C13 |
| cross-cutting (all gates) | C1, C2, C3, C9, C10, C14 |

Derived margins (compute, do not hardcode beyond a cross check): the per-row count
(standards per gate) and the per-column count (gates per standard, counting the
cross-cutting row once). Every column has at least one filled cell, so all 15
standards are represented.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec` that reserves the
top of the content band for the matrix and a slim strip below for the column
margin, plus a slim right column for the row margin. A practical layout:
`GridSpec(2, 2, width_ratios=[20, 2], height_ratios=[20, 2], left=0.20,
right=0.95, top=0.86, bottom=0.16, wspace=0.04, hspace=0.04)`; the main matrix is
the top left cell, the row margin the top right, the column margin the bottom
left.

- Header at `y = 0.965`: `Gate to Standard Binding Matrix`. Subtitle at `y =
  0.935`: `Every VVUQ gate anchored to published consensus standards; all 15
  standards used (standards_map.yaml, execution §02 §03 §05)`.
- Main matrix: 11 rows (10 gates plus cross-cutting) by 15 columns. Draw each
  filled cell as a rounded square colored by the standard column domain (model
  credibility navy `#1F3A5F`, robotic surgery teal `#2A9D8F`, service-robot safety
  slate blue `#4C72B0`, software and risk escalate amber `#E1A93B`, autonomy
  autonomy purple `#6A4C93`, regulatory neutral gray `#6B7280`, clinical clinical
  rose `#B5566E`). Empty cells are panel fill `#F4F6F8` with a thin gridline gray
  border. Use a faint full grid so the lattice reads cleanly.
- Row labels at the far left, `NN slug` in 9 pt; catastrophe rows (06, 09, 10) in
  block red bold. The cross-cutting row label in italic.
- Column labels rotated 90 degrees above the matrix, the designation in 8 pt;
  color each column label by its domain to key the legend.
- Row margin (top right cell): a thin horizontal lollipop per row showing the
  standards-per-gate count, with the integer at the tip, primary navy.
- Column margin (bottom left cell): a thin vertical lollipop per column showing the
  gates-per-standard count, with the integer at the tip, teal.
- Domain legend at the bottom (`y` about 0.10): seven swatches keyed to the seven
  domain colors above, 9 pt.
- A 9 pt note under the legend: `IEC 80601-2-77 and the cross-cutting credibility
  set (ASME V&V 40, NASA-STD-7009A, FDA CM&S) anchor the most gates`.

## Color, symbol, and dash rules

- Cells colored by standard domain as listed, empty cells panel fill, catastrophe
  row labels block red. White figure background, near black text. No dark mode and
  no sequential dark fill; the matrix is categorical by domain.
- Use `§` in the subtitle (`execution §02`, `§03`, `§05`). Render `V&V` and `/`
  as written in designations.
- Single hyphens only. Write counts as integers and any range with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `FancyBboxPatch` (or use `ax.add_patch` with
  `Rectangle` and rounded corners via `FancyBboxPatch`).
- Encode the bindings as an 11 by 15 integer or boolean array built from the row
  to column lists above; derive both margin counts from the array with
  `array.sum(axis=...)` so the margins always reconcile with the matrix.
- Map each column to a domain color via a dict, and fill each true cell with its
  column domain color; keep empty cells panel fill.
- Use `ax.set_xticks`/`set_yticks` at integer centers and turn the spines off; draw
  the grid with thin `ax.hlines`/`ax.vlines`.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/04-gate-standard-binding-matrix/04-gate-standard-binding-matrix.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/04-gate-standard-binding-matrix/04-gate-standard-binding-matrix.py`.
- Image: `papers/VVUQ-02/imagegen/04-gate-standard-binding-matrix/04-gate-standard-binding-matrix.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/config/standards_map.yaml, inputs/standards/manifest.yaml, execution §02 §03 §05  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- 11 rows by 15 columns matrix with every listed binding filled; all 15 standard
  columns have at least one filled cell.
- Catastrophe rows 06, 09, 10 flagged block red; cross-cutting row present and
  italic; both margins reconcile with the matrix counts.
- Column labels rotated and readable, domain legend present, the dense-anchor note
  present.
- Header, subtitle, margins, legend, and footer inside their bands, no overlap,
  none clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
