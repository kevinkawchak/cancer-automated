# Image Instruction 10: File Generation Sankey

Chart family: Sankey flow diagram. Basis: both code execution (v0.2.0 file
generation outcomes in the execution README) and code generation (v0.1.0 pipeline
that produced the artifacts). Output: a single portrait, full page, 300 dpi PNG
that flows the 13 generated files from the run, through the five execution
sections, into the four future paper roles, with ribbon widths proportional to
bytes.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

The execution produced 13 documentation and artifact files that map onto a future
paper. The Sankey shows how byte weight flows from the single run, into the five
numbered sections, and onward into the paper roles Methods, Verification,
Results, and Core Results. It makes the Methods plus Results skeleton of a future
paper visible as a flow.

## Grounding (cite in the footer)

- `papers/VVUQ-01/execution/README.md`, the `File generation outcomes` table, for
  the 13 files, their byte counts, and their future paper roles (code execution
  v0.2.0).
- `pipeline/` produced the three saved pipeline artifacts; the section reports are
  the evidence around them (code generation v0.1.0 plus execution v0.2.0).

## The flow data (exact, bytes)

Source node: `VVUQ-01 Execution Run`, 13 files, 54127 bytes total.

Middle nodes, the five sections by total bytes:

| Section node | Bytes | Files |
|--------------|-------|-------|
| 01 Foundation | 17304 | README 1899, environment-and-verification 4994, test-suite 7166, lint-format-yaml 3245 |
| 02 Pipeline | 10659 | README 8601, instructions 963, execution_log 95, paper 1000 |
| 03 VVUQ | 8812 | README 8812 |
| 04 Stage 1 automation | 9152 | README 8646, chunk_reconstruction_README 506 |
| 05 Physical-AI Stage 2 | 8200 | README 7538, pdac_hybrid_pilot_timeline 662 |

Right nodes, the four paper roles, with the section to role flows:

| Paper role | Bytes | Fed by |
|------------|-------|--------|
| Methods | 6893 | 01 Foundation (1899 plus 4994) |
| Verification | 10411 | 01 Foundation (7166 plus 3245) |
| Core Results | 8812 | 03 VVUQ (8812) |
| Results | 28011 | 02 Pipeline 10659, 04 Stage 1 9152, 05 Stage 2 8200 |

Totals reconcile: 6893 plus 10411 plus 8812 plus 28011 equals 54127, the same as
the section total 17304 plus 10659 plus 8812 plus 9152 plus 8200. Only 01
Foundation splits, into Methods and Verification; every other section flows whole
into one role.

## Layout specification (portrait, full page)

Use the shared page frame. Orient the Sankey top to bottom in three node rows so
it fills the portrait page, single content axis with `set_xlim(0, 1)`,
`set_ylim(0, 1)`, `axis("off")`. `GridSpec` 1 by 1, `left=0.06, right=0.94,
top=0.90, bottom=0.07`.

- Header at `y = 0.965`: `File Generation Sankey`. Subtitle at `y = 0.935`: `13
  generated files, 54127 bytes, flowing into four future paper roles`.
- Three node rows:
  - top row near `y = 0.86`: the single source node, a wide rounded bar in
    primary navy `#1F3A5F` spanning most of the width, labeled `VVUQ-01 Execution
    Run, 13 files, 54127 bytes` in white 11 pt.
  - middle row near `y = 0.50`: five section nodes as rounded bars laid left to
    right, each width proportional to its bytes over 54127, separated by small
    gaps. Color them 01 navy, 02 slate blue `#4C72B0`, 03 teal `#2A9D8F`, 04
    accept green `#2E7D32`, 05 escalate amber `#E1A93B`. Label each with its
    section name and bytes, 9.5 pt, below the bar.
  - bottom row near `y = 0.14`: four role nodes as rounded neutral gray `#6B7280`
    bars, widths proportional to role bytes, labeled `Methods 6893`,
    `Verification 10411`, `Core Results 8812`, `Results 28011`.
- Ribbons: draw each flow as a filled cubic Bezier band from the bottom edge of
  the upper node to the top edge of the lower node, width equal to the flow bytes
  in the same proportional units, at alpha 0.55, colored by the section it leaves.
  The source to section ribbons carry the section colors; the section to role
  ribbons keep the section color so a reader can trace 01 Foundation splitting
  into Methods and Verification.
- A small inventory note at lower left, 9 pt: `Three saved pipeline artifacts
  (instructions, execution log, paper) plus the chunk reconstruction README and
  the PDAC timeline are the primary generated deliverables`.
- Legend at upper right: five section color swatches with their names.

## Color, symbol, and dash rules

- Section colors navy, slate, teal, accept green, escalate amber; source node
  navy; role nodes neutral gray; ribbons inherit the section color at alpha 0.55;
  near black text on light, white text on dark bars. White background, no dark
  mode.
- No section symbol required. Single hyphens only in visible text; file names
  like `lint-format-yaml` and `Physical-AI` use single hyphens and are kept
  verbatim.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`, `numpy as np`; from
  `matplotlib.patches` import `FancyBboxPatch` and `PathPatch`; from
  `matplotlib.path` import `Path`.
- Compute node widths from the byte values divided by 54127 and a fixed total
  drawing width, and lay out each row by cumulative offset so nodes never overlap
  and ribbons align to the correct sub spans of each node.
- Build each ribbon as a closed `Path` with `CURVE4` segments on both edges so the
  band has smooth parallel sides; track per node horizontal offsets so multiple
  ribbons leaving or entering a node stack without crossing.
- Save to `papers/VVUQ-01/imagegen/10-file-generation-sankey/10-file-generation-sankey.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/10-file-generation-sankey/10-file-generation-sankey.py`.
- Image: `papers/VVUQ-01/imagegen/10-file-generation-sankey/10-file-generation-sankey.png`.

## Footer text

`cancer-automated v0.3.0  |  source: execution README file generation outcomes, pipeline artifacts  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Source, five section, and four role nodes with widths proportional to the byte
  values, and ribbons whose widths match the flows.
- 01 Foundation visibly splits into Methods and Verification; the role totals
  6893, 10411, 8812, 28011 sum to 54127.
- Legend, inventory note, header, subtitle, and footer inside their bands, no
  overlap or clipping.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
