# Visual Representations Catalog — `papers/` VVUQ Corpus
### Master index and correlation guide for AI processing (built for Claude Code Opus 4.8, 1M context, Max)

This README is the **synthesis layer** over five companion Markdown files. Each
companion file is a *verbatim* catalog of every visual representation — ASCII
diagrams, ASCII timelines, repository-structure trees, and Markdown tables —
found in one directory of the `kevinkawchak/cancer-automated` repository's
`papers/` tree. This README explains what each file contains, how the visuals
relate **within** each directory, and how all five files relate **to each
other**, so a downstream AI can navigate the corpus without re-reading the
source repository.

> **One-line orientation.** `papers/` holds four sequential works — VVUQ-01 →
> VVUQ-02 → VVUQ-03 → VVUQ-04 — that carry one thesis (*verification before
> generation*) from a **method**, to a **hard engineering proof**, to a
> **proposed bill**, to a **precise FD&C Act amendment**. The five catalogs
> below are the extracted "visual skeleton" of that evidence-to-law pipeline.

---

## 0. The six files in this folder

| File | Role | Covers |
|:--|:--|:--|
| **`README.md`** (this file) | Synthesis / index / correlation guide | All five catalogs |
| `01-papers-root-README.md` | Catalog | `papers/README.md` (root only) — the master map |
| `02-VVUQ-01.md` | Catalog | `papers/VVUQ-01/` (README + all subdirectories) |
| `03-VVUQ-02.md` | Catalog | `papers/VVUQ-02/` (README + all subdirectories) |
| `04-VVUQ-03.md` | Catalog | `papers/VVUQ-03/` (README + all subdirectories) |
| `05-VVUQ-04.md` | Catalog | `papers/VVUQ-04/` (README + all subdirectories) |

Each catalog is **self-contained and self-describing**: it opens with a title
identifying its directory, a scope note, and an Index; every visual is then
reproduced verbatim under a labeled block that names its **source file**, the
**heading it sat under**, and its **type**; and it closes with a "files scanned
with no visuals" list and a Summary count. This README does not repeat the
visuals — it tells you which file and which heading to open.

---

## 1. The five catalogs at a glance

Approximate counts (the authoritative per-file totals live in each catalog's own
`## Summary counts` section). "Blocks" counts labeled visual entries; byte-identical
duplicates across `draft-paper` / `full-paper` / `final-paper` READMEs are
reproduced once and **referenced** thereafter, so distinct-visual counts are a
little lower than block counts.

| Catalog | Source directory | `.md`/`.txt` scanned | With visuals | Tables | ASCII diagrams | Timelines | Repo trees | ≈ Blocks |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
| `01-papers-root-README.md` | `papers/` (root README) | 1 | 1 | 2 | 2 | 1 | 1 | **6** |
| `02-VVUQ-01.md` | `papers/VVUQ-01/` | 64 | 45 | ~81 | ~20 | 3 | 6 | **~110** |
| `03-VVUQ-02.md` | `papers/VVUQ-02/` | 95 | 63 | 100 | 30 | 2 | 15 | **147** |
| `04-VVUQ-03.md` | `papers/VVUQ-03/` | 24 | 5 | 8 | 9 | 0 | 5 | **22** |
| `05-VVUQ-04.md` | `papers/VVUQ-04/` | 30 | 18 | ~72 | ~29 | 1 | 6 | **~108** |
| **Total** | `papers/` (4 works + root) | **214** | **132** | **~263** | **~90** | **7** | **33** | **~393** |

**Reading the spread:** VVUQ-02 (the autonomous humanoid codebase) and VVUQ-01
(the method + pipeline) are the visual-dense engineering halves; VVUQ-03 (the
bill) and VVUQ-04 (the amendment) are the legal halves — VVUQ-04 is table-heavy
because it carries large statutory *crosswalk* tables, while VVUQ-03 is
diagram-heavy relative to its size because its source LaTeX chunks (which hold
its big tables) are out of scope.

---

## 2. Shared scope and extraction conventions (identical across all five catalogs)

So the corpus is interpreted consistently:

**In scope (extracted verbatim):**
- Markdown **pipe tables** (`| … |` with a `|---|` delimiter row) — kept as raw
  Markdown so they still render.
- **ASCII / text diagrams** in fenced code blocks (flow charts, funnels, decision
  surfaces, kinematic chains, heatmaps, state machines, mind maps, lineage and
  layering diagrams, value matrices, etc.) — fenced in ```text with original
  spacing and indentation preserved.
- **ASCII timelines** (phase timelines, schedule/Gantt-style bars) — fenced.
- **Repository / directory structure trees** — fenced.

**Out of scope (deliberately excluded; noted in each catalog):**
- Source/data/binary file types: `.tex`, `.sty`, `.bib`, `.py`, `.rs`, `.json`,
  `.jsonl`, `.csv`, `.yaml`/`.yml`, `.toml`, `.proto`, `.avsc`, `.ipynb`, `.zip`.
  LaTeX `tabular`/`longtable` and matplotlib scripts are *source for* visuals,
  not rendered visuals, so they are not extracted. (This is why VVUQ-03's ten
  `template-paper/chunk_*.md` files — verbatim 21 CFR Part 312 LaTeX — contribute
  no visuals.)
- **Captured-console `.txt` logs** that are line-oriented output rather than drawn
  diagrams (e.g. VVUQ-01 `execution_log.txt`; VVUQ-02 `pipeline_execution_log.txt`,
  `gate_decision_surface.txt`, `deployment_safety_log.txt`, `sensor_stream_analysis.txt`)
  — treated as out of scope. The drawn `.txt` artifacts (timelines, funnels,
  kinematic chains, heatmaps, support-polygon plots) **are** extracted.
- **Command recipes** (`pdflatex …`, `cat … > file.tex`, shell/Overleaf blocks)
  — generally not classed as visuals (one `cat` reassembly listing in VVUQ-03 was
  classed as a repository-structure tree as a judgment call).
- **Whitespace/tab-aligned pseudo-tables** with no `|` pipes (a few appear in
  VVUQ-03 `instruct-paper/output-*` and VVUQ-04 `update-bill/output-1`) — not
  Markdown pipe tables, so left out and flagged. *If you need these too, they can
  be added on request.*

**Per-visual block format** (used in every catalog):

```
**Source file:** `papers/VVUQ-0X/relative/path`
**Located under heading:** "<verbatim nearest Markdown heading above the visual>"
**Type:** Table | ASCII diagram | Timeline | Repository structure

<the visual, verbatim>
```

**Minor cosmetic note:** `03-VVUQ-02.md` titles its per-file sections with
backticked relative paths (e.g. `` ## `codegen/README.md` ``) while the other
catalogs use full paths (e.g. `## papers/VVUQ-01/execution/README.md`). Every
individual visual block still carries a full repo-relative **Source file:** line,
so resolution is unambiguous in all five files.

---

## 3. What each catalog contains (per-file detail)

### `01-papers-root-README.md` — the master map (6 visuals)

The root `papers/README.md` is the **index for the entire tree**, so its six
visuals are the highest-level objects in the corpus and the anchor for every
correlation below:

- **Table — "Final Papers and Bills on Zenodo (the four end goals)":** the four
  final artifacts and their Zenodo DOIs.
- **Table — "The four works at a glance":** each work's nature, release range,
  **headline assurance result** (51/51 tests; 172/172 + composite 93.56; 15
  sections/21 tables; new § 360e-5 + 10 conforming), and DOI. This single table
  is the numeric spine that the other four catalogs flesh out.
- **ASCII diagram ×2 — "Building process from one work to the next":** (a) the
  four-work **lineage** boxes (VVUQ-01 → 02 → 03 → 04, with DOIs and the
  "evidence flows forward" note), and (b) the shared **five-method + VVUQ-gate
  flow** (instructions → code → execution → figures → paper/bill, gate =
  ACCEPT/BLOCK/ESCALATE).
- **Timeline — "Accelerated timeline versus conventional methods":** conventional
  months-to-years vs. this directory's ~11 days, broken out per work.
- **Repository structure — "Repository structure":** the full `papers/` tree with
  one-line gloss per subdirectory — effectively a table of contents for catalogs
  `02`–`05`.

### `02-VVUQ-01.md` — method + working pipeline (~110 visuals, 45/64 files)

Establishes the thesis that the LLM **VVUQ process must be held to a higher
standard than the code generation it checks**. Visual highlights by heading:
- **Execution chain (`execution/…`):** "The five established methods, as
  executed" (02-pipeline); **"The three dimensions, as executed"** verify →
  validate → quantify → gate, plus the **full gate decision surface** table (1
  ACCEPT / 5 BLOCK / 1 ESCALATE) and threshold table (03-vvuq); "ASCII view of
  the foundation gate" (01-foundation); "Daily deliverable pipeline", "Two-stage
  roadmap", and "VVUQ gate decision flow" (execution README).
- **Stage-2 physical AI:** a **safety-gating state machine** (DARK / RUNNING /
  ESTOP / FAULT) and a **168-day PDAC pilot timeline** (05-physical-ai-stage2,
  plus the raw `pdac_hybrid_pilot_timeline.txt`).
- **Ten figure specifications (`image-instruct/01–10`):** each spec carries dense
  **figure-data tables** — the gate funnel (6→1), acceleration waterfall, five-
  methods flowchart, assurance wheel, PDAC pilot timeline, test-coverage treemap,
  lights-off state machine, FDA cost-efficiency bridge, value-proposition matrix,
  file-generation sankey.
- **Input corpus (`inputs/…`):** "Cross-File Correlation Map" lineage trees, the
  LLM-VVUQ pipeline diagrams, a 38-cycle progress-bar console figure, and the
  clinical parameter tables (Table T1, dt-convergence, V&V test-suite,
  patient-adaptation).

### `03-VVUQ-02.md` — the hardest subject: one autonomous humanoid (147 visuals, 63/95 files)

Applies the thesis to a single autonomous **Unitree H2-Surgical 1.0** performing
a 60-second 8-phase Whipple, where one body concentrates all error potential and
a behavior must clear **10 standards-bound gates**. The richest catalog. Highlights:
- **Drawn `.txt` artifacts:** the **60-Second 8-Phase Whipple Timeline**; the
  **71-DOF kinematic chain**; the **Balance ZMP & support-polygon** plot; the
  **Ten VVUQ Gate Funnel** (candidates → ACCEPT, with per-gate V/CV thresholds
  and the three immediate-catastrophe gates); the **vessel no-fly proximity
  heatmap**.
- **`codegen/docs/` specs:** V/V/UQ gate flow ("The three dimensions, as
  executed"), the **data-and-control-flow architecture** diagram, the file-size
  pyramid (L0–L4) layering table, hand-kinematics, robot-spec, perception-stack,
  sensor-spec, suturing/anastomosis, and **standards-map** tables.
- **Execution record:** gate-decision flow, **automation flow**, the
  **deployment safety surface** (3-catastrophe-gate box), the 32-iteration sweep
  and **four-entrant comparison leaderboard**, composite-score tables.
- **15 figure specifications (`image-instruct/01–15`)** and the repository-
  structure trees for `codegen/`, `execution/`, `image-instruct/`, `imagegen/`.

### `04-VVUQ-03.md` — recorded evidence becomes a proposed bill (22 visuals, 5/24 files)

Converts the recorded evidence of VVUQ-01 + VVUQ-02 (plus the national-platform
paper and USL/PSL standards) into **H. R. 9510**, modeled on 21 CFR Part 312.
Smaller and diagram-led:
- **"Building process within the work"** — template → instruct (multi-model,
  rated 9.5/8.5/8.0) → draft → full → final pipeline, and the 15-section ordering
  chain.
- **"How the bill is assembled"** — evidence + existing law → prior-law crosswalk
  → draft statutory text → section-by-section → implementation.
- **"Position in the lineage"** — VVUQ-01 → VVUQ-02 → national-platform →
  template → draft → full, with a `<=== THIS BUNDLE` marker (in draft/full/final).
- **"Accelerated timeline versus conventional methods"** — months vs. ~1 day.
- **Two cross-cutting tables** that are the corpus's most explicit cross-file
  links: the **"Section to source-file map"** (every bill section → the exact
  files it synthesises in VVUQ-01, VVUQ-02, and national-platform) and the
  **"ten chunks at a glance"** 21-CFR-Part-312 table.

### `05-VVUQ-04.md` — a precise, current FD&C Act amendment (~108 visuals, 18/30 files)

Recasts the bill as a targeted amendment to the Federal Food, Drug, and Cosmetic
Act (Title 21), current through Public Law 119-93, adding **new § 360e-5** plus
**10 conforming amendments**. Table-dense (legal crosswalks). Highlights:
- **Statutory-layering diagrams** ("How the sections interact", "How the
  amendment / conforming amendments thread through Title 21"): device → classify
  → 510(k)/PMA → **PCCP (§ 360e-4)** → new § 360e-5, in the top/draft/full/final/
  template READMEs.
- **`main.tex` assembly diagram** and the **Title 21 device-section repository
  tree** (template-bill).
- **Lineage diagrams** ("Purpose and place in the lineage") feeding draft-bill →
  full-bill, and the instruct-bill **"How the files correlate"** box-and-arrow map
  of files 01–10.
- **Legal-crosswalk tables** across `instruct-bill/01–10` (federal statutes, FDA
  AI-device regulation, ONC/ASTP transparency, CMS coverage, privacy/security,
  state laws, executive actions, emerging bills, VVUQ standards) and the
  **retained-section / excluded-material** tables (template-bill), including the
  "Lead instruct-bill file" column that points each statute back to its summary.

---

## 4. How the five catalogs correlate (the cross-file map)

The corpus is **one chain, not four silos.** Every catalog is downstream of the
root map (`01`) and, except for VVUQ-01, explicitly consumes the recorded
artifacts of the works before it. The correlations below are *visible in the
extracted visuals themselves* — they are not editorial inferences.

### 4.1 The master lineage (root `01` governs all four)

`01`'s two "Building process" diagrams and "four works at a glance" table define
the spine that `02`–`05` instantiate:

```
VVUQ-01 (method+pipeline) -> VVUQ-02 (hard proof) -> VVUQ-03 (proposed law) -> VVUQ-04 (precise amendment)
  evidence flows forward; each work cites the records of the prior works
```

Each downstream catalog re-draws its **own** position in this chain: VVUQ-03's
"Position in the lineage" and VVUQ-04's "Purpose and place in the lineage"
diagrams both start from VVUQ-01 and VVUQ-02 and end at their own bundle — so the
same lineage is told four times at increasing zoom.

### 4.2 Recurring visual motifs (the same diagram pattern across catalogs)

| Motif (heading family) | Appears in | What stays constant / what changes |
|:--|:--|:--|
| **"Building process within the work"** pipeline | `01` (root), `02`, `03`, (assembly form in `05`) | Same five-method shape (instruct → generate → execute → figures → paper/bill); the payload changes per work |
| **VVUQ gate** (funnel / decision surface / "three dimensions") | `02` (VVUQ-01 exec + image-instruct 01), `03` (VVUQ-02 codegen `ten_vvuq_gate_funnel.txt`, exec gate flow, image-instruct 02–03) | The gate scales from **1 gate / 3 dimensions** (VVUQ-01) to **10 standards-bound gates** (VVUQ-02); ACCEPT/BLOCK/ESCALATE semantics identical |
| **"Accelerated timeline versus conventional methods"** | `01` (~11 days), `02` (VVUQ-01 ~5 days), `04` (VVUQ-03 ~1 day), `05` (VVUQ-04) | Same conventional-vs-this side-by-side box; the per-work span shrinks |
| **"Position / place in the lineage"** | `04` (VVUQ-03 draft/full/final), `05` (VVUQ-04 draft/full/final/template) | Same upstream chain (VVUQ-01 → 02 → national-platform), different `<=== THIS BUNDLE` endpoint |
| **Statutory layering / "How the bill is assembled"** | `04` (bill form), `05` (actual Title 21 form) | VVUQ-03 draws the *intended* legal pathway; VVUQ-04 realizes it on the *real statute* (device → classify → 510(k)/PMA → PCCP → § 360e-5) |
| **Repository-structure tree** | all five (`01` root tree contains all four sub-trees) | The root tree (`01`) is the master index; per-work `draft/full/final` trees repeat the same section-file set |
| **"Cross-File Correlation Map"** (box-and-arrow file maps) | `02` (VVUQ-01 input corpora), `05` (VVUQ-04 instruct-bill) | The corpus documents its *own* internal file relationships the same way at multiple levels — self-similar |
| **`main.tex` assembly diagram** | `04` (paper family), `05` (template-bill) | Same `main.tex` → `.sty` + `.bib` + `\input{sections/*}` assembly pattern across every LaTeX bundle |

### 4.3 Shared evidentiary objects (the same artifact cited across works)

These concrete objects are *produced* in one catalog's directory and *cited as
evidence* in later catalogs — the literal mechanism of "evidence to law":

- **The 10-gate threshold schedule bound to external standards** (ASME V&V 40,
  IEC 80601-2-77, ISO 13482, ISO/TS 15066, NASA-STD-7009A): defined in **`03`**
  (VVUQ-02 `viz/ten_vvuq_gate_funnel.txt`, `docs/standards_map.md`,
  `docs/vvuq_gate_spec.md`), cited as the regulated schedule in **`04`** (VVUQ-03
  statutory text), and anchored to actual Title 21 sections in **`05`** (VVUQ-04).
- **`comparison.json` (1790-line, four-entrant) and the ~1000-row × 27-column
  sensor stream**: generated in **`03`** (VVUQ-02), cited as the evidentiary
  record in **`04`** (VVUQ-03 "Algorithm documentation" row of the section map).
- **The 60-second 8-phase Whipple timeline**: appears in **`03`** (VVUQ-02, two
  byte-identical copies in `codegen` and `execution`) and is **explicitly reused
  from the PDAC 8-arm baseline** that VVUQ-01 carries — tying VVUQ-02's humanoid
  back to **`02`**'s PDAC pilot timeline for direct comparability.
- **Headline assurance numbers**: 51/51 tests + 2.5× acceleration (**`02`**) →
  172/172 tests + 32/32 sweep + composite 93.56 + seed-`20260525` determinism
  (**`03`**) → recited as legislative findings (**`04`**) → operationalized as a
  statutory requirement (**`05`**, new § 360e-5). The root "four works at a
  glance" table (**`01`**) is where all four numbers sit side by side.

### 4.4 The most explicit cross-links: VVUQ-03's section-to-source-file maps

The single strongest correlation in the corpus is the **"Section to source-file
map"** table reproduced in `04-VVUQ-03.md` (from VVUQ-03 draft/full/final
READMEs). Each row names a bill section and the **exact files in VVUQ-01,
VVUQ-02, and the national platform** it synthesises (e.g. *Algorithm
documentation* → `VVUQ-02/codegen/{docs,config,results}` + `comparison.json` +
`sample_h2_sensor.csv`; *Findings* → `VVUQ-01/final-paper/` +
`VVUQ-02/execution/README.md`). VVUQ-04's template-bill tables do the same
upward, with a "Lead instruct-bill file" column mapping each Title 21 section to
its `instruct-bill/01–10` summary. **To trace any legal claim back to its
engineering evidence, start from these tables.**

### 4.5 Directory-reference matrix (which catalog points where)

| ↓ Catalog references → | VVUQ-01 (`02`) | VVUQ-02 (`03`) | VVUQ-03 (`04`) | VVUQ-04 (`05`) | National platform / Title 21 |
|:--|:--:|:--:|:--:|:--:|:--:|
| **`02` VVUQ-01** | self | — | — | — | PDAC clinical baseline |
| **`03` VVUQ-02** | cites (thesis, PDAC timeline) | self | — | — | external standards corpus |
| **`04` VVUQ-03** | **section map** | **section map** | self | — | national-platform + USL/PSL |
| **`05` VVUQ-04** | (via VVUQ-03) | (10-gate schedule) | **prior bill / crosswalk** | self | **Title 21 statute** |
| **`01` root** | indexes | indexes | indexes | indexes | DOIs for all |

Read top-to-bottom, the references accumulate: each work's catalog points back at
all the catalogs above it, and `01` indexes them all.

---

## 5. How a downstream AI should use this corpus

1. **Start here, then open `01`.** This README + `01-papers-root-README.md` give
   you the whole tree, the lineage, the shared pipeline, and the DOI/number spine
   before you touch any single work.
2. **Resolve any visual to its source.** Every block is tagged with a full
   `papers/VVUQ-0X/...` **Source file** path and the **heading** it sat under, so
   you can open the exact source for surrounding prose. Treat the catalogs as a
   spatial index over the repository's visual content.
3. **Use the motif table (§4.2) to compare across works** — e.g. to see how the
   VVUQ gate evolves, read the gate visuals in `02` (1 gate / 3 dimensions) then
   `03` (10 gates) in that order.
4. **Use the section-to-source maps (§4.4) to move between layers** — from a
   legal clause in `04`/`05` down to the engineering artifact in `02`/`03` that
   substantiates it, or upward from evidence to statute.
5. **Trust verbatim fidelity; mind the duplicates.** Visuals are byte-accurate
   (spot-checked with `diff`). Where a `full-paper`/`final-paper` (or `full-bill`/
   `final-bill`) visual is byte-identical to a sibling, the later one is a
   labeled **reference** ("identical to …") rather than a re-paste — follow the
   pointer.
6. **Remember the scope boundary (§2).** If a needed artifact is LaTeX `tabular`/
   `longtable`, a matplotlib figure script, a JSON/CSV data file, a captured
   console log, or a tab-aligned pseudo-table, it is intentionally **not** here —
   open the named source file directly, or request that class be added.

---

## 6. Provenance and integrity

- **Source:** the `papers/` tree of `kevinkawchak/cancer-automated`. Every
  deliverable in that tree was authored autonomously by Claude Code Opus 4.7 /
  4.8 (1M) Max; the works are independent research drafts (a hypothetical 2030
  Unitree H2-Surgical platform; simulation results; an un-enacted draft bill /
  amendment), not enacted law, clinical guidance, or legal advice.
- **Extraction:** `.md` and `.txt` files only, processed recursively per
  directory; visuals reproduced verbatim with source-file + heading + type tags;
  byte-identical duplicates referenced rather than re-pasted; completeness
  reconciled (every scanned file is either catalogued or listed under "no
  visuals"). Per-file authoritative counts are in each catalog's `## Summary counts`.
- **This bundle is local-only.** Per request, these six files are **not** committed
  to GitHub (the folder is excluded via the repository's local `.git/info/exclude`);
  the working tree is left clean.
- **Extraction date:** 2026-06-02.
