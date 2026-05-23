# Image Instruction 03: Five Established Methods Pipeline Flowchart

Chart family: process flowchart with an orchestrator swimlane and a gate
decision node. Basis: both code generation (v0.1.0 `pipeline/`) and code
execution (v0.2.0 execution §02). Output: a single portrait, full page, 300 dpi
PNG that shows one daily deliverable flowing through the four producing stages,
threaded by the orchestrator, and handed to the optional VVUQ gate.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

The pipeline packages five established methods into one repeatable engine. The
figure shows the four producing stages in strict order, the single `Deliverable`
object threaded through them by the orchestrator, the artifact each stage emits
with its measured size and stage duration, and the optional fifth method, the
VVUQ gate, that decides whether the candidate ships. It is the methods backbone
for a future paper.

## Grounding (cite in the footer)

- `pipeline/README.md`, `pipeline/orchestrator.py`, and the four stage modules
  `instruction_stage.py`, `codegen_stage.py`, `execution_stage.py`,
  `paper_stage.py`, plus `pipeline/deliverable.py` (code generation v0.1.0).
- `papers/VVUQ-01/execution/02-pipeline/README.md` for the per stage artifacts,
  byte counts, and stage durations from the DAILY-0001 orchestrator run, and the
  five deliverable runs across the three examples (code execution v0.2.0).

## The stage data (exact, from execution §02 DAILY-0001)

| Order | Method | Module | Artifact emitted | Bytes | Stage duration (s) |
|-------|--------|--------|------------------|-------|--------------------|
| 1 | Instruction generation | `instruction_stage.py` | `instructions.md` | 963 | 0.000010 |
| 2 | Code generation | `codegen_stage.py` | `generated_deliverable.py` | 735 | 0.000008 |
| 3 | Code execution | `execution_stage.py` | `execution_log.txt` | 95 | 0.000197 |
| 4 | Paper assembly | `paper_stage.py` | `paper.md` | 1000 | 0.000010 |

Threaded by `orchestrator.py` through a single `Deliverable`. The optional fifth
method, the VVUQ gate (`vvuq/vvuq_gate.py`), runs after the paper stage and is
exercised in execution §03. Total of the four stage durations is 0.000225 s, so
the entire deliverable is produced in well under a millisecond, and every
artifact is far under the 200000 byte per file cap. Across the three pipeline
examples, 5 deliverable runs completed, all 4 stages each, over IDs DAILY-0001
to DAILY-0003.

## Layout specification (portrait, full page)

Use the shared page frame, single content axis (`GridSpec` 1 by 1, `left=0.06,
right=0.94, top=0.91, bottom=0.07`), all geometry in axis coordinates with
`set_xlim(0, 1)`, `set_ylim(0, 1)`, `axis("off")`.

- Header at `y = 0.965`: `Five Established Methods, One Daily Deliverable`.
  Subtitle at `y = 0.935`: `Instruction to code to execution to paper, threaded
  by the orchestrator, gated by VVUQ`.
- Orchestrator swimlane: a tall rounded rectangle on the left (`x` about 0.06 to
  0.20, spanning the four stages vertically), panel fill `#F4F6F8` with a primary
  navy `#1F3A5F` border, label rotated 90 degrees, 12 pt bold, `orchestrator.py
  threads one Deliverable`. Inside, a thin navy vertical spine with four tick
  marks aligned to the four stage boxes, showing the orchestrator drives each.
- Four stage boxes stacked top to bottom in the main column (`x` about 0.24 to
  0.78), evenly spaced, drawn with `FancyBboxPatch` rounded corners. Color the
  left accent bar of each box by stage using the family progression: stage 1
  primary navy `#1F3A5F`, stage 2 slate blue `#4C72B0`, stage 3 teal `#2A9D8F`,
  stage 4 a deep teal toward green; box bodies on panel fill. Each box contains
  three rows of text:
  - line 1, 13 pt bold: `Method N  Title` (for example `Method 1  Instruction
    generation`).
  - line 2, 10.5 pt monospace: the module file name.
  - line 3, 10.5 pt: `emits artifact_name  (NNN bytes, 0.000NNN s)`.
- Down arrows between consecutive stage boxes, neutral gray `#6B7280`, each
  annotated 9 pt with what passes forward: `instructions` then `generated code`
  then `execution log and results`.
- VVUQ gate node: below stage 4, a diamond (rotated square `Polygon`) in escalate
  amber `#E1A93B` outline with white fill, 12 pt label `Optional method 5  VVUQ
  gate`, with two exits drawn as short labeled arrows: an accept green arrow to a
  small `ACCEPT and ship` pill and a block red arrow to a small `BLOCK` pill, and
  a note `evaluated in execution §03`.
- Right rail metrics card (`x` about 0.80 to 0.96): a panel fill card listing, 10
  pt, `Total stage time 0.000225 s`, `Largest artifact paper.md 1000 bytes`,
  `Per file cap 200000 bytes`, `Deliverable runs 5 of 5 complete`, `Stages per
  deliverable 4 of 4`.
- Legend along the bottom of the content band: four stage accent swatches with
  their method names, plus the amber gate diamond glyph labeled `VVUQ gate`.

## Color, symbol, and dash rules

- Stage accents navy, slate, teal, deep teal in order; orchestrator border navy;
  gate diamond amber; accept green and block red on the gate exits; panel fill
  for boxes and cards; neutral gray arrows; near black text. White background, no
  dark mode.
- Use `§` only in the gate note `evaluated in execution §03`.
- Single hyphens only in visible text. Durations are written with the leading
  zero, for example `0.000010 s`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`; from `matplotlib.patches`
  import `FancyBboxPatch`, `FancyArrowPatch`, `Polygon`.
- Drive the four stage box `y` centers from a single evenly spaced list so they
  align with the orchestrator ticks; place arrows from computed box edges so they
  never cross text.
- Keep all coordinates in axis space for a deterministic layout that needs no
  manual nudging.
- Save to `papers/VVUQ-01/imagegen/03-five-methods-flowchart/03-five-methods-flowchart.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/03-five-methods-flowchart/03-five-methods-flowchart.py`.
- Image: `papers/VVUQ-01/imagegen/03-five-methods-flowchart/03-five-methods-flowchart.png`.

## Footer text

`cancer-automated v0.3.0  |  source: pipeline/orchestrator.py and stage modules, execution §02  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Four stage boxes in order with correct module names, artifacts, byte counts,
  and stage durations.
- Orchestrator swimlane spans all four stages; VVUQ gate diamond shows accept and
  block exits and the `§03` note.
- Metrics card shows total time 0.000225 s and 5 of 5 deliverable runs.
- Header, subtitle, legend, and footer inside their bands, nothing clipped.
- Only single hyphens in visible text; `§` used only in the gate note; no dark
  mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
