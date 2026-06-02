# papers/ (root README) — Visual Representations Catalog

**Source directory:** `papers/` — root `README.md` only (per scope item 1: "papers (only README)").
**Source file:** `papers/README.md` — *Papers: VVUQ Verification Developments for Physical AI Oncology Trials*.
**Scope:** ASCII diagrams, timelines, repository-structure trees, and Markdown tables reproduced verbatim. Shields.io badge images, the Table-of-Contents link list, and prose are not catalogued as "visual representations."
**Extraction date:** 2026-06-02.

This root README is the **map of the whole `papers/` tree**. Its visuals define the four-work lineage (VVUQ-01 → 02 → 03 → 04), the shared five-method + VVUQ-gate pipeline, the accelerated timeline, and the full repository layout. It is the natural index for the four per-directory catalogs (`02`–`05`).

## Index

| # | Located under heading | Type |
|---|---|---|
| 1 | Final Papers and Bills on Zenodo (the four end goals) | Table |
| 2 | The four works at a glance | Table |
| 3 | Building process from one work to the next | ASCII diagram (four-work lineage) |
| 4 | Building process from one work to the next | ASCII diagram (five-method + VVUQ-gate flow) |
| 5 | Accelerated timeline versus conventional methods | Timeline (conventional vs. this directory) |
| 6 | Repository structure | Repository structure tree |

**Per-type totals:** Tables 2 · ASCII diagrams 2 · Timeline 1 · Repository structure 1 (6 visuals total).

---

## Visual 1 — Table

**Source file:** `papers/README.md`
**Located under heading:** "## Final Papers and Bills on Zenodo (the four end goals)"
**Type:** Table

| Work | Final artifact | Author final edits (PDF + LaTeX) |
|:--|:--|:--|
| [VVUQ-01](VVUQ-01) | *Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over Existing Generated Code* | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20372501) |
| [VVUQ-02](VVUQ-02) | *Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ* | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20421754) |
| [VVUQ-03](VVUQ-03) | *VVUQ Physical AI Oncology Trial Bill* (H. R. 9510) | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20454870) |
| [VVUQ-04](VVUQ-04) | *Verification Before Generation in Physical AI Oncology Trials Act of 2026* (H. R. 9510; FD&C Act amendment) | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20485580) |

---

## Visual 2 — Table

**Source file:** `papers/README.md`
**Located under heading:** "## The four works at a glance"
**Type:** Table

| Work | What it is | Releases | Headline assurance result | End-goal DOI |
|:--|:--|:--|:--|:--|
| VVUQ-01 | Method paper plus the working pipeline and an execution record that hold VVUQ higher than code generation | v0.1.0 to v0.6.0 | 51 of 51 tests; 1 ACCEPT, 5 BLOCK, 1 ESCALATE gate surface; 2.5x acceleration | [20372501](https://doi.org/10.5281/zenodo.20372501) |
| VVUQ-02 | A generated 10-gate humanoid surgical codebase, its autonomous execution record, and the manuscript built from them | v0.7.0 to v1.2.0 | 172 of 172 tests; 10 gates; 32 of 32 sweep iterations clear; composite mean 93.56 | [20421754](https://doi.org/10.5281/zenodo.20421754) |
| VVUQ-03 | The *VVUQ Physical AI Oncology Trial Bill* (H. R. 9510), synthesized from the recorded evidence | v1.3.0 to v1.4.0 | 15 sections; 21 body-width tables; 60 references; verification before generation as statute | [20454870](https://doi.org/10.5281/zenodo.20454870) |
| VVUQ-04 | The bill recast as a precise amendment to the Federal Food, Drug, and Cosmetic Act, current through Public Law 119-93 | v2.0.0 to v2.3.0 | New § 360e-5 plus 10 conforming amendments; legal crosswalk current to May 31, 2026 | [20485580](https://doi.org/10.5281/zenodo.20485580) |

---

## Visual 3 — ASCII diagram (four-work lineage)

**Source file:** `papers/README.md`
**Located under heading:** "## Building process from one work to the next"
**Type:** ASCII diagram

```
  VVUQ-01                  VVUQ-02                  VVUQ-03                  VVUQ-04
  (method + pipeline)      (hard engineering)       (proposed law)           (precise amendment)
  +-------------------+    +-------------------+    +-------------------+    +-------------------+
  | inputs/ ingest    |    | instructions/     |    | template-paper/   |    | instruct-bill/    |
  | execution/ 51 tst | -> | codegen/ 10 gates | -> |  21 CFR Part 312  | -> |  10 md + 5 bib    |
  | image-instruct/   |    | execution/ 172tst |    | instruct-paper/   |    | template-bill/    |
  | imagegen/ 10 figs |    | image+imagegen/15 |    | draft-paper/      |    |  Title 21 sects   |
  | draft -> full ->  |    | draft -> full ->  |    | full-paper/       |    | draft -> full ->  |
  | final-paper       |    | final-paper       |    | final-paper (bill)|    | final-bill        |
  +-------------------+    +-------------------+    +-------------------+    +-------------------+
            | DOI                    | DOI                    | DOI                    | DOI
            v                        v                        v                        v
       zenodo.20372501          zenodo.20421754          zenodo.20454870          zenodo.20485580
            \________________________\________________________\_______________________/
                                                 |
              evidence flows forward: each work cites the records of the prior works
              (VVUQ-02 cites VVUQ-01; VVUQ-03 cites VVUQ-01, VVUQ-02, and the
              national-platform paper; VVUQ-04 cites VVUQ-03 and the Title 21 statute)
```

---

## Visual 4 — ASCII diagram (five-method + VVUQ-gate flow)

**Source file:** `papers/README.md`
**Located under heading:** "## Building process from one work to the next"
**Type:** ASCII diagram

```
  instructions  ->  code/text  ->  execution  ->  figures  ->  paper/bill
       |               |               |             |             |
       +---------------+------ VVUQ gate (stricter than generation) ----+
                               ACCEPT  /  BLOCK  /  ESCALATE to human
```

---

## Visual 5 — Timeline

**Source file:** `papers/README.md`
**Located under heading:** "## Accelerated timeline versus conventional methods"
**Type:** Timeline (conventional path vs. this directory, ~11 days)

```
  Conventional path (months to years)        This directory (about 11 days)
  +-----------------------------------+      +-------------------------------------+
  | Method paper drafting   ~months   |      | VVUQ-01  v0.1.0 -> v0.6.0  ~5 days  |
  | Verified robotics code  6-18 mo   |  vs  | VVUQ-02  v0.7.0 -> v1.2.0  ~2 days  |
  | Peer-style manuscript   ~months   |      | VVUQ-03  v1.3.0 -> v1.4.0  ~1 day   |
  | Federal bill + counsel  mo-years  |      | VVUQ-04  v2.0.0 -> v2.3.0  ~2 days  |
  +-----------------------------------+      +-------------------------------------+
  years of serial effort                     days of autonomous, real-time work
                                             reaching the final VVUQ-04 Bill
```

---

## Visual 6 — Repository structure tree

**Source file:** `papers/README.md`
**Located under heading:** "## Repository structure"
**Type:** Repository structure

```
papers/
  README.md          (this file: the four works, lineage, and final DOIs)
  VVUQ-01/           (method + pipeline; final paper DOI 10.5281/zenodo.20372501)
    inputs/          source paper and research chunks (ingestion inputs)
    paper-instruct/  instruction lineage
    templates/       LaTeX manuscript template (Template_10)
    execution/       v0.2.0 execution record (51 tests; gate surface; PDAC pilot)
    image-instruct/  v0.3.0 ten figure specifications
    imagegen/        v0.4.0 ten rendered figures (scripts + PNGs)
    draft-paper/     v0.5.0 LaTeX scaffold (bracketed instructions)
    full-paper/      v0.6.0 finished manuscript (18 tables, 4 figures, 29 refs)
    final-paper/     author-finalized manuscript (Zenodo)
  VVUQ-02/           (humanoid VVUQ; final paper DOI 10.5281/zenodo.20421754)
    instructions/    prompt and output lineage
    inputs/          standards corpus (14) + clinical baselines (2)
    templates/       Template_04 regulatory and FDA scaffold
    codegen/         v0.7.0 standalone 10-gate humanoid codebase (172 tests)
    execution/       v0.8.0 full run record (5 sections; 32-iteration sweep)
    image-instruct/  v0.9.0 fifteen figure specifications
    imagegen/        v1.0.0 fifteen rendered figures (scripts + PNGs)
    draft-paper/     v1.1.0 LaTeX scaffold (41 refs)
    full-paper/      v1.2.0 finished manuscript (13 tables, 5 figures)
    final-paper/     author-finalized manuscript (Zenodo)
  VVUQ-03/           (the bill; final paper DOI 10.5281/zenodo.20454870)
    template-paper/  21 CFR Part 312 adaptation (10 chunks + .sty + .bib)
    instruct-paper/  multi-model instruction generation (rated outputs)
    draft-paper/     v1.3.0 bill scaffold (15 bracketed sections; 60 refs)
    full-paper/      v1.4.0 finished H. R. 9510 bill (15 sections; 21 tables)
    final-paper/     author-finalized bill (Zenodo)
  VVUQ-04/           (FD&C Act amendment; final bill DOI 10.5281/zenodo.20485580)
    instruct-bill/   v2.0.0 legal crosswalk (10 md + 5 bib; 145 entries)
    template-bill/   v2.1.0 Title 21 device sections, US Code look and feel (LaTeX)
    draft-bill/      v2.2.0 amendment scaffold (bracketed drafting instructions)
    full-bill/       v2.3.0 finished amendment (new § 360e-5 + 10 conforming)
    final-bill/      author-finalized bill (Zenodo)
    update-bill/     supplementary multi-model prompts and outputs
```

---

## Files scanned with no visual representations

- None other than `papers/README.md` (scope item 1 limits this catalog to the root README). The non-visual portions of `papers/README.md` (title, badge row, narrative prose, Table-of-Contents link list, "Responsible use", "License") were reviewed and intentionally excluded.

## Summary counts

- **Tables:** 2
- **ASCII diagrams:** 2
- **Timelines:** 1
- **Repository structures:** 1
- **Total visuals:** 6
- **Files scanned:** 1 (`papers/README.md`)
