# Image Instruction 06: Test Suite Coverage Treemap

Chart family: treemap. Basis: code execution (v0.2.0 execution §01
`test-suite.md`). Output: a single portrait, full page, 300 dpi PNG that tiles
the 51 passing tests across the 8 test modules, with each tile area proportional
to its test count and a sequential color by count.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

The treemap shows the shape of the verification floor: 51 of 51 tests passed with
0 skipped, distributed across 8 modules that map one to one onto the source
packages. Area encodes how much test weight each package carries, so a reader
sees at a glance that the foundation and the VVUQ modules carry the most checks.

## Grounding (cite in the footer)

- `papers/VVUQ-01/execution/01-foundation/test-suite.md` for the per module
  counts and the 51 passed, 0 skipped result (code execution v0.2.0).
- The module to package mapping mirrors the source packages under `pipeline/`,
  `vvuq/`, `simulation/`, `ingestion/`, `chunking/`, `scheduler/`, `physical-ai/`
  and the repository and config files exercised by `test_foundation.py`.

## The treemap data (exact, sums to 51)

| Module | Tests | Target package | All passed |
|--------|-------|----------------|------------|
| `test_foundation.py` | 17 | repository files, configs, verify script | yes |
| `test_vvuq.py` | 8 | vvuq, verification, validation, uncertainty, gate | yes |
| `test_pipeline.py` | 5 | pipeline, five established methods | yes |
| `test_physical_ai.py` | 5 | physical-ai, lights off factory, hybrid pilot | yes |
| `test_simulation.py` | 4 | simulation, triple runner, consensus | yes |
| `test_ingestion.py` | 4 | ingestion, web search, pdf processor | yes |
| `test_chunking.py` | 4 | chunking, chunker, readme generator | yes |
| `test_scheduler.py` | 4 | scheduler, commit scheduler | yes |
| total | 51 | all packages | yes |

## Deterministic layout (so no positioning is needed)

Tile the treemap inside the content rectangle in three full width rows, sorted by
count. Areas are exactly proportional to counts because each tile area equals
`count / 51`. Use these normalized rectangles (origin lower left, the content
axis spans 0 to 1 in both directions):

| Tile | x start | x end | y start | y end | Area, equals count over 51 |
|------|---------|-------|---------|-------|----------------------------|
| `test_foundation.py` (17) | 0.000 | 1.000 | 0.667 | 1.000 | 0.333 |
| `test_vvuq.py` (8) | 0.000 | 0.444 | 0.314 | 0.667 | 0.157 |
| `test_pipeline.py` (5) | 0.444 | 0.722 | 0.314 | 0.667 | 0.098 |
| `test_physical_ai.py` (5) | 0.722 | 1.000 | 0.314 | 0.667 | 0.098 |
| `test_simulation.py` (4) | 0.000 | 0.250 | 0.000 | 0.314 | 0.0784 |
| `test_ingestion.py` (4) | 0.250 | 0.500 | 0.000 | 0.314 | 0.0784 |
| `test_chunking.py` (4) | 0.500 | 0.750 | 0.000 | 0.314 | 0.0784 |
| `test_scheduler.py` (4) | 0.750 | 1.000 | 0.000 | 0.314 | 0.0784 |

The future script should derive these rectangles programmatically from the
counts (row 1 is the largest module; row 2 is the next three summing to 18; row 3
is the four 4 test modules summing to 16) and then verify the drawn rectangles
match the table above. Row heights are the row test sums over 51 (0.333, 0.353,
0.314) and within row widths are each tile count over the row sum.

## Color, symbol, and dash rules

- Sequential fill by test count inside the teal to navy family: map count 4 to a
  light teal near `#7FC9BE`, count 17 to primary navy `#1F3A5F`, with counts 5
  and 8 interpolated between. Because all tests passed, overlay a small accept
  green `#2E7D32` check glyph and the word `PASSED` in the corner of each tile.
- Tile borders white at 2 pt so tiles separate cleanly on white background.
- Tile text: module name 12 pt bold, `N tests` 11 pt, target package 9 pt, all in
  white when the tile is dark navy or deep teal and in near black `#1A1A1A` when
  the tile is light teal, so every label stays legible.
- No section symbol required. Single hyphens only in visible text. The hyphen in
  `physical-ai` is a single hyphen and is correct.

## Layout specification (portrait, full page)

Use the shared page frame with two stacked regions: the treemap and a scale and
total strip. `GridSpec(2, 1, height_ratios=[3.2, 0.5], left=0.06, right=0.94,
top=0.90, bottom=0.07, hspace=0.14)`. The treemap axis uses `set_xlim(0, 1)`,
`set_ylim(0, 1)`, `axis("off")`.

- Header at `y = 0.965`: `Test Suite Coverage Treemap`. Subtitle at `y = 0.935`:
  `51 of 51 tests passed, 0 skipped, across 8 modules`.
- Treemap axis: draw the 8 rectangles from the table with `matplotlib.patches.
  Rectangle`, then place the per tile text centered.
- Bottom strip: a horizontal sequential color bar from light teal to navy labeled
  `tests per module, 4 to 17`, and a bold total readout `Total 51 of 51 passed,
  0 skipped, Python 3.11.15, pytest 9.0.3`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`, `numpy as np`; from
  `matplotlib.patches` import `Rectangle`; use `matplotlib.colors.LinearSegmentedColormap`
  or `matplotlib.cm` to build the teal to navy sequential scale.
- Compute rectangles from the counts as described, assert the row sums are 17,
  18, 16, and place labels at each rectangle center so they never leave the tile.
- Choose label text color by tile luminance so contrast stays high.
- Save to `papers/VVUQ-01/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.py`.
- Image: `papers/VVUQ-01/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.png`.

## Footer text

`cancer-automated v0.3.0  |  source: execution §01 test-suite.md  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Eight tiles with areas proportional to 17, 8, 5, 5, 4, 4, 4, 4 matching the
  layout table, sorted with the largest on top.
- Each tile labeled with module, test count, target package, and a PASSED check;
  all labels legible against their fill.
- Bottom strip shows the sequential scale and the total 51 of 51 passed.
- Header, subtitle, and footer inside their bands, nothing clipped.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
