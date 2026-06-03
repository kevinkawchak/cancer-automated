# VVUQ-05 draft-bill (LaTeX): H. R. 9510 Bill v3.0, the Visual Draft - v3.0.0

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Statute](https://img.shields.io/badge/Statute-Public%20Domain%20(U.S.%20Code)-lightgrey.svg)](https://uscode.house.gov)
[![Amends](https://img.shields.io/badge/Amends-Federal%20Food%2C%20Drug%2C%20and%20Cosmetic%20Act-darkblue.svg)](https://www.law.cornell.edu/uscode/text/21/chapter-9)
[![Current through](https://img.shields.io/badge/Current%20through-Pub.%20L.%20119--93-green.svg)](https://www.govinfo.gov/app/collection/plaw)
[![Stage](https://img.shields.io/badge/Stage-Visual%20draft%20scaffold%20(v3.0)-orange.svg)](.)
[![Bill](https://img.shields.io/badge/Bill-H.%20R.%209510%20(119th%20Cong.%2C%202d%20Sess.)-darkblue.svg)](.)
[![Prior Bill DOI](https://img.shields.io/badge/Prior%20Bill%20DOI%20(v2.0)-10.5281%2Fzenodo.20485580-blue.svg)](https://doi.org/10.5281/zenodo.20485580)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Files](https://img.shields.io/badge/Files-main.tex%20%7C%20.sty%20%7C%20.bib%20%7C%208%20sections%20%7C%20zip-orange.svg)](.)

A LaTeX **visual draft** of **H. R. 9510**, the *Verification Before Generation
in Physical AI Oncology Trials Act of 2026*, an amendment to the **Federal Food,
Drug, and Cosmetic Act** (21 U.S.C. § 301 et seq.), grounded on the Title 21
device provisions current through **Public Law 119-93**. This bundle is an
amendment **scaffold with bracketed drafting instructions and figure and table
slots**, not a finished bill. It keeps the full operative text of **Bill v2.0**
(the VVUQ-04 `final-bill`) so it stands on its own, and it adds a more visual
perspective: every operative part carries a figure or table slot, and a set-off
`DRAFTING INSTRUCTIONS` block tells a future **Claude Code Opus 4.8 (1M context)
Max** pass exactly which files in this repository to process to render that
figure or table on a white background as a text-based diagram, with no raster
image.

## What Bill v3.0 is for (the three primary objectives)

- **(a) A visualization of Bill v2.0.** Built on the VVUQ-01 through VVUQ-04
  developments, with the visuals drawn from the verbatim catalog in
  [`papers/VVUQ-05/update-bill/figures-bill`](../update-bill/figures-bill).
  Appendix A reorganizes the VVUQ-01 and VVUQ-02 engineering evidence into
  full-page text figures.
- **(b) Instructions for every submission deliverable.** Appendix B scaffolds the
  supplementary Markdown documents a U.S. House bill needs before submission, to
  be written in a later step under
  [`papers/VVUQ-05/deliverables`](../deliverables), based on the feedback in
  [`papers/VVUQ-05/update-bill/next-steps`](../update-bill/next-steps). Each
  deliverable is specified as a separate, complete, submission-quality document.
- **(c) A new explainability standard.** Appendix C establishes the VVUQ-01
  through VVUQ-04 developments as a reusable standard for explaining how a piece
  of United States legislation was created, mapped to the recorded prompts,
  outputs, VVUQ gates, and commit trail.

## The four bill-content goals (carried from Bill v2.0)

The instructions are written so the finished visual bill stays **(a) up to date**
with today's medical-AI law, **(b) grounded** in current, mass-adopted
medical-law references used meaningfully, **(c) relevant to emerging bills** as
research influences only (confined to Appendix D, a memo, or testimony, never the
operative text), and **(d) streamlined** to the structured amendment format.

## Table of Contents

- [Repository structure](#repository-structure)
- [The bill structure and where the instructions live](#the-bill-structure-and-where-the-instructions-live)
- [Figure and table inventory](#figure-and-table-inventory)
- [The submission deliverables package (Appendix B)](#the-submission-deliverables-package-appendix-b)
- [Lineage](#lineage)
- [How every file correlates to main.tex](#how-every-file-correlates-to-maintex)
- [Compile recipe (Overleaf, pdfLaTeX)](#compile-recipe-overleaf-pdflatex)
- [Formatting and fidelity conventions](#formatting-and-fidelity-conventions)
- [How the next AI pass should use this folder](#how-the-next-ai-pass-should-use-this-folder)
- [Responsible use](#responsible-use)
- [License](#license)

## Repository structure

```
papers/VVUQ-05/draft-bill/
  README.md                  (this file)
  main.tex                   (caption with the v3.0 process diagram, SECTION 1
                              short title and contents, the section inputs, the
                              back matter, and the references)
  usctitle.sty               (US Code reproduction + amendment apparatus +
                              draftbox + white-background visual primitives)
  references.bib             (94 provenance and research sources; ieeetr)
  draft-bill-LaTeX.zip       (Overleaf-ready bundle of all of the above)
  prompt-draft-bill.md       (the generating prompt, verbatim)
  output-draft-bill.md       (the narrative output of this step)
  sections/
    s2-findings.tex          (SEC. 2  Findings; Fig. 1 lineage, Tbl. 1 four works,
                              Fig. 2 timeline)
    s3-amendment.tex         (SEC. 3  New § 515D + conforming; Tbl. 2 gate
                              schedule, Fig. 3 gate funnel, Fig. 4 layering,
                              Tbl. 3 conforming crosswalk)
    s4-comparative.tex       (SEC. 4  Comparative print; Tbl. 4 change map,
                              Fig. 5 Title 21 threading)
    a5-evidence.tex          (Appendix A  Visual engineering evidence; Fig. 6-8,
                              Tbl. 5 standards map)
    a6-deliverables.tex      (Appendix B  Submission deliverables; Tbl. 6 matrix)
    a7-explainability.tex    (Appendix C  Explainability standard; Fig. 9-10,
                              Tbl. 7 standard)
    a8-research-matrix.tex   (Appendix D  Research influence matrix; Tbl. 8)
    a9-transparency.tex      (Appendix E  Transparency; Tbl. 9-10, Fig. 11)
```

## The bill structure and where the instructions live

`main.tex` is the single assembler. It carries the caption (condensed to a single
long title dated June 3, 2026, closing with an ASCII overview of the v3.0
process), SECTION 1, and the back matter; each numbered section and lettered
appendix is one `sections/*.tex` file with its own heading, operative or framing
text, figure and table slots, and a closing `draftbox`.

| Bill part | File | Role |
|:--|:--|:--|
| SECTION 1 | `main.tex` | Short title; table of contents |
| SEC. 2 | `sections/s2-findings.tex` | Findings; the evidence to law record |
| SEC. 3 | `sections/s3-amendment.tex` | New § 515D and the ten conforming amendments |
| SEC. 4 | `sections/s4-comparative.tex` | Comparative print; changes in existing law |
| Appendix A | `sections/a5-evidence.tex` | Visual engineering evidence (non-operative) |
| Appendix B | `sections/a6-deliverables.tex` | Required submission deliverables (non-operative) |
| Appendix C | `sections/a7-explainability.tex` | The VVUQ explainability standard (non-operative) |
| Appendix D | `sections/a8-research-matrix.tex` | Research influence matrix (non-operative) |
| Appendix E | `sections/a9-transparency.tex` | Development transparency and commit schedule |

## Figure and table inventory

Each slot marks where the future pass renders a white-background, text-based
figure or full-width table; the build instruction names the exact source files.

| Slot | Title | Lead source files |
|:--|:--|:--|
| Cover Fig. | Bill v3.0 visual draft process | `main.tex` (authored) |
| Figure 1 | Four-work evidence-to-law lineage | `figures-bill/01RootREADME.md` Visual 3; `papers/README.md` |
| Table 1 | The four works at a glance | `figures-bill/01RootREADME.md` Visual 2 |
| Figure 2 | Accelerated timeline | `figures-bill/01RootREADME.md` Visual 5 |
| Table 2 | Ten-gate threshold schedule | `VVUQ-04/final-bill/main.tex` § 515D(c)(4); `figures-bill/03VVUQ02.md` |
| Figure 3 | VVUQ gate decision surface and funnel | `figures-bill/02VVUQ01.md`, `03VVUQ02.md` |
| Figure 4 | Statutory layering through Title 21 | `figures-bill/05VVUQ04.md`; `VVUQ-04/final-bill/README.md` |
| Table 3 | Ten conforming amendments crosswalk | `VVUQ-04/final-bill/README.md` |
| Table 4 | Per-section comparative-print change map | `VVUQ-04/final-bill/README.md` |
| Figure 5 | How the eleven sections thread Title 21 | `figures-bill/05VVUQ04.md` |
| Figure 6 | The gate, from one dimension to ten | `figures-bill/02VVUQ01.md`, `03VVUQ02.md` |
| Figure 7 | The procedure timelines | `figures-bill/02VVUQ01.md`, `03VVUQ02.md` |
| Figure 8 | The humanoid safety figure | `figures-bill/03VVUQ02.md` |
| Table 5 | External standards map | `figures-bill/03VVUQ02.md`; `VVUQ-04/final-bill/main.tex` |
| Table 6 | The submission deliverables matrix | `VVUQ-05/update-bill/next-steps` |
| Figure 9 | Prompt evolution across the works | every `prompt-*.md` (VVUQ-02 to VVUQ-05) |
| Figure 10 | Internal bill evolution | `figures-bill/05VVUQ04.md`; `VVUQ-04/final-bill/README.md` |
| Table 7 | The VVUQ explainability standard | `figures-bill/README.md` (Sections 4-5) |
| Table 8 | Research influence matrix | `VVUQ-04/final-bill/main.tex` Appendix A; `instruct-bill/07`, `08` |
| Table 9 | Bill version lineage | `papers/README.md`; `VVUQ-04/final-bill/README.md` |
| Table 10 | Single-pull-request commit schedule | this pull request |
| Figure 11 | The build-and-handoff process | `main.tex` cover figure (authored) |

## The submission deliverables package (Appendix B)

Appendix B instructs a future pass to write each of these as a separate,
complete, submission-quality Markdown document under
[`papers/VVUQ-05/deliverables`](../deliverables).

| Output file | Purpose |
|:--|:--|
| `01-one-page-summary.md` | One-page plain-English summary |
| `02-section-by-section-analysis.md` | Section-by-section analysis |
| `03-plain-english-policy-memo.md` | Problem and solution policy memo |
| `04-legislative-findings.md` | Standalone findings of fact |
| `05-ramseyer-comparative-print.md` | Changes-to-existing-law comparative print |
| `06-constitutional-authority-statement.md` | Constitutional Authority Statement (Rule XII) |
| `07-paygo-and-cost-estimate.md` | PAYGO and cost note; earmark declaration |
| `08-sponsor-and-cosponsor-packet.md` | Sponsor and original cosponsor packet |
| `09-stakeholder-engagement-plan.md` | Stakeholder and standards-body outreach |
| `10-legislative-counsel-routing-memo.md` | HOLC legislative-form routing memo |
| `11-currency-and-cross-reference-matrix.md` | Currency and cross-reference verification |
| `12-testimony-and-research-influence-brief.md` | Hearing testimony; research influences |
| `README.md` | Package index (badges, tree, table of contents) |

## Lineage

```
  VVUQ-01 + VVUQ-02            VVUQ-03 bill (v1.0)        VVUQ-04 amendment (v2.0)
  (method + hard proof)        H. R. 9510 standalone      H. R. 9510 FD&C amendment
        |                              |                          |
        |   figures-bill (every ASCII diagram + table)            |
        |   next-steps   (the submission deliverables)            |
        +--------------------+---------+--------------------------+
                             v
        +-----------------------------------------------------------+
        |  VVUQ-05/draft-bill   <== THIS (Bill v3.0, the visual draft)|
        |  full operative text of v2.0 + figure and table slots +    |
        |  bracketed DRAFTING INSTRUCTIONS that name exact files     |
        +----------------------------+------------------------------+
                                     v
        Next pass: render the figures and write the deliverables to
        produce the final visual bill and the deliverables package.
```

## How every file correlates to main.tex

```
                         +------------------+
                         |   main.tex       |
                         | (assembles all)  |
                         +---+----------+---+
        \usepackage{usctitle}|          | \bibliography{references}
                             v          v
                   +-----------------+  +-----------------+
                   | usctitle.sty    |  | references.bib  |
                   | reproduction +  |  | 94 provenance + |
                   | amendment +     |  | research        |
                   | draftbox +      |  | sources         |
                   | visual macros   |  |                 |
                   +-----------------+  +-----------------+
                             |
        \input{sections/...}  (8 files: 3 bill-body + 5 appendices)
                             v
  s2-findings  s3-amendment  s4-comparative  a5-evidence  a6-deliverables
  a7-explainability  a8-research-matrix  a9-transparency
```

Every section file opens with its own `\billsec` or appendix heading, carries the
operative or framing text and the `\figslot` figure and table placeholders, and
ends with a `draftbox` of bracketed `\dstep` directives. All commands resolve
from `usctitle.sty`.

## Compile recipe (Overleaf, pdfLaTeX)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Set the Overleaf compiler to **pdfLaTeX**. The body font is Times-like via
`newtxtext` and `newtxmath` (standard on Overleaf); on a minimal installation,
substitute `\usepackage{mathptmx}` in `usctitle.sty`. ASCII figures use
`fancyvrb`. There are no images and no external assets beyond the four file
types. The `draft-bill-LaTeX.zip` is the Overleaf-ready bundle.

## Formatting and fidelity conventions

1. **White background throughout** - the page, the ASCII figure frames, and the
   figure and table slots are all set on white with black rules only.
2. **Even interword spacing, no overflow** - the body is set `RaggedRight`
   (ragged2e) so spacing is even, there are no rivers or large gaps, and no line
   runs off the right margin; `\RaggedRightRightskip` carries a small stretch so
   words stay evenly spaced.
3. **No stranded lines** - widow, orphan, and broken-line penalties are maximal;
   text is worded to avoid one- or two-word last lines and a single line carried
   alone to the next page, and to avoid large empty white bands.
4. **Single hyphens only** - no en dashes, em dashes, double, or triple dashes.
5. **The section symbol §** for every codified reference; never "SS".
6. **Left-aligned, ragged-right tables** - every column uses
   `>{\raggedright\arraybackslash}p{...}` (the `L` and `ragcol` helpers) or the
   flexible `Y` column, and every table is set to `\textwidth`.
7. **ASCII figures preserved** - text diagrams are set verbatim in monospace so
   they render as they would in a fenced GitHub Markdown block.
8. **No images, mermaid, or color figures** anywhere; links are black.

## How the next AI pass should use this folder

1. Read this README and `main.tex` to see the visual amendment structure and the
   figure and table inventory.
2. For each section, open its `draftbox` and process the **exact** files it names
   under `papers/VVUQ-05/update-bill/figures-bill`, `papers/VVUQ-05/update-bill/next-steps`,
   `papers/VVUQ-04`, and `papers/VVUQ-03`, resolving every cited authority to a
   key in `references.bib`.
3. Render each `\figslot` as a white-background, text-based figure or full-width
   table, preserving ASCII spacing, and keep the operative text of Bill v2.0
   intact so the bill still stands on its own.
4. Write each Appendix B deliverable as a separate, submission-quality Markdown
   document under `papers/VVUQ-05/deliverables`.
5. Delete each `draftbox` as its part is finished, run the compile recipe, and
   apply the formatting conventions above as a senior author would.

## Responsible use

The reproduced statutory text is a work of the United States Government and is in
the public domain; the authoritative version is the United States Code as
published by the Office of the Law Revision Counsel. This visual draft is an
independent research aid, **not legal advice and not an enacted law**, and is not
endorsed by the FDA, HHS, the OLRC, CFR, ICH, or any member of Congress. The
emerging 119th Congress bills and executive actions appear only in Appendix D as
research influences and are never cited as the basis of an operative clause.

## License

The reproduced statutory text is in the public domain. The generated amendment
framing, instructions, figures, tables, and this README are released under the
Creative Commons Attribution 4.0 International License (CC BY 4.0).
