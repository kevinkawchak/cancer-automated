# Image Instruction 15: VVUQ-02 Platform Mind Map

Chart family: mind map (radial hub with curved branches and leaf nodes). Basis:
both code generation (v0.7.0 the `codegen/` tree) and code execution (v0.8.0 the
`execution/` record). Output: a single portrait, full page, 300 dpi PNG that gives
a one-page overview of the whole VVUQ-02 platform, the hypothetical humanoid, the
codegen modules, the 10 gates, the external standards, the execution sections, and
the lineage, radiating from a central assurance hub.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

A reader new to VVUQ-02 should grasp the whole platform at a glance. The mind map
organizes the project into six branches around the assurance hub, so the
relationships, platform to code to gates to standards to execution to lineage, are
visible without reading the tree. It complements the sequential pipeline (figure
01) with a hierarchical overview.

## Grounding (cite in the footer)

Sources, used for every node below:

- `papers/VVUQ-02/codegen/config/project.yaml` (the platform: 71 DOF, 2 arms, 2
  hands, 8 phases, hypothetical 2030).
- `papers/VVUQ-02/execution/README.md`, the `Source executed` table (the codegen
  packages) and the five execution sections.
- `papers/VVUQ-02/execution/03-vvuq/README.md` (the 10 gates, the 3 catastrophe
  gates).
- `papers/VVUQ-02/codegen/config/standards_map.yaml` (the standards bodies) and the
  lineage in `codegen/config/project.yaml` (instructions to codegen to execution).

## The mind map data (exact, six branches)

Central hub: `VVUQ-02 H2-Surgical assurance`.

| Branch | Color | Leaf nodes |
|--------|-------|-----------|
| Platform | navy `#1F3A5F` | H2-Surgical 1.0 (hypothetical 2030); 71 total DOF; 2 x 7-DOF arms; 2 x 20-DOF hands; 60 s 8-phase Whipple |
| Codegen modules (v0.7.0) | slate blue `#4C72B0` | autonomy (intent, compile); kinematics; perception; hands; balance; suturing; safety; vvuq; simulation; metrics; llm; zenodo; sensors |
| 10 VVUQ gates | teal `#2A9D8F` | 01 handeye; 02 finger-force; 03 balance; 04 plan; 05 grasp-handover; 06 vascular no-fly (catastrophe); 07 suturing; 08 perception; 09 shared-OR collision (catastrophe); 10 fault e-stop (catastrophe) |
| External standards | autonomy purple `#6A4C93` | ASME V&V 40; NASA-STD-7009A; IEC 80601-2-77; IEC 60601-1; ISO 13482; ISO/TS 15066; ISO 10218-1; ISO 9283; IEC 62304; ISO 14971; ISO 13849-1; UL 4600; IEEE 7009; FDA CM&S; Fistula Risk Score |
| Execution record (v0.8.0) | escalate amber `#E1A93B` | 01 foundation (172 tests); 02 pipeline (concordance 1.000); 03 vvuq (5-case surface); 04 automation (32-iter sweep, tournament); 05 deployment (60 s, 1000-row stream) |
| Lineage | clinical rose `#B5566E` | instructions; codegen v0.7.0; execution v0.8.0; image-instruct v0.9.0 |

Mark the three catastrophe gate leaves (06, 09, 10) with a block red dot.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single full width axis in the
content band (`GridSpec` 1 by 1, `left=0.05, right=0.95, top=0.90, bottom=0.07`),
equal aspect, axis off, centered on the origin.

- Header at `y = 0.965`: `VVUQ-02 Platform Mind Map`. Subtitle at `y = 0.935`:
  `One-page overview: platform, code, 10 gates, standards, execution, lineage`.
- Central hub: a rounded rectangle at the center in primary navy with the hub label
  in white 13 pt bold, wrapped to about 14 characters.
- Six branches: distribute the six branch root nodes evenly around the hub (at
  about 60 degree spacing), each a colored rounded rectangle with the branch name
  in 11 pt bold. Connect each branch root to the hub with a smooth curved line
  (`FancyArrowPatch` with `connectionstyle="arc3,rad=0.2"`) in the branch color.
- Leaf nodes: from each branch root, fan out the leaf nodes as small pill labels
  (panel fill with a thin branch-color border, 8.5 pt text) connected to the
  branch root by short curved branch-color lines. Place leaves on the outer side
  of each branch so they do not cross the hub; for the long branches (codegen 13
  leaves, standards 15 leaves) stack the leaves in two short sub-columns to fit the
  portrait width without overlap.
- Catastrophe marks: a small block red dot on the 06, 09, 10 gate leaves, keyed in
  the legend.
- Legend (lower area): six swatches keyed to the six branch colors, plus a block
  red dot `immediate-catastrophe gate`.
- Balance the layout so the top branches (platform, gates) and the bottom branches
  (lineage, execution) use the vertical portrait space, and the wide branches
  (codegen, standards) use the horizontal space, all within the content band.

## Color, symbol, and dash rules

- Each branch and its leaves in the branch color, hub navy, catastrophe dots block
  red. White figure background, near black text, white text on the navy hub. No
  dark mode.
- Use `§` only if a clause is cited; otherwise plain names. Render `V&V`, `/TS`,
  `x` (as in `2 x 7-DOF`) as written.
- Single hyphens only. Write `no-fly`, `e-stop`, `finger-force`, `shared-OR`,
  `one-page`, and ranges with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `FancyBboxPatch` and `FancyArrowPatch`.
- Compute the six branch root positions on a circle around the origin with
  `np.linspace(0, 2*np.pi, 6, endpoint=False)`; compute leaf positions by fanning
  an angular spread around each branch direction, so all positions are derived and
  need no manual nudging.
- Draw curved connectors with `FancyArrowPatch(..., arrowstyle="-",
  connectionstyle="arc3,rad=0.2")`; draw nodes with `FancyBboxPatch`.
- Set `ax.set_xlim(-1.05, 1.05)`, `ax.set_ylim(-1.05, 1.05)`,
  `ax.set_aspect("equal")`, `ax.axis("off")`; pick a radius schedule (hub 0, branch
  roots about 0.42, leaves about 0.62 to 0.95) that keeps every node inside the
  axis.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/15-platform-mindmap/15-platform-mindmap.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/15-platform-mindmap/15-platform-mindmap.py`.
- Image: `papers/VVUQ-02/imagegen/15-platform-mindmap/15-platform-mindmap.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/config/project.yaml, execution README source-executed table, execution §03, codegen/config/standards_map.yaml  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Central hub plus six branches (platform, codegen modules, 10 gates, standards,
  execution, lineage), each with its leaf nodes, no node overlapping another.
- The three catastrophe gate leaves carry a block red dot; the standards branch
  lists all 15 entries; the execution branch lists the five sections.
- Legend present with the six branch colors and the catastrophe dot.
- Header, subtitle, legend, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§` where used; only single hyphens in visible
  text; no dark mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
