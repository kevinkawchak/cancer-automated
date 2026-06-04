# VVUQ-05 final-bill (LaTeX): H. R. 9510 Bill v3.0, the Visual Amendment - v3.1.0

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Statute](https://img.shields.io/badge/Statute-Public%20Domain%20(U.S.%20Code)-lightgrey.svg)](https://uscode.house.gov)
[![Amends](https://img.shields.io/badge/Amends-Federal%20Food%2C%20Drug%2C%20and%20Cosmetic%20Act-darkblue.svg)](https://www.law.cornell.edu/uscode/text/21/chapter-9)
[![Current through](https://img.shields.io/badge/Current%20through-Pub.%20L.%20119--93-green.svg)](https://www.govinfo.gov/app/collection/plaw)
[![Stage](https://img.shields.io/badge/Stage-Finished%20visual%20amendment%20(v3.0)-brightgreen.svg)](.)
[![Bill](https://img.shields.io/badge/Bill-H.%20R.%209510%20(119th%20Cong.%2C%202d%20Sess.)-darkblue.svg)](.)
[![Bill DOI (v3.0)](https://img.shields.io/badge/Bill%20DOI%20(v3.0)-10.5281%2Fzenodo.20535429-blue.svg)](https://doi.org/10.5281/zenodo.20535429)
[![Prior Bill DOI (v2.0)](https://img.shields.io/badge/Prior%20Bill%20DOI%20(v2.0)-10.5281%2Fzenodo.20485580-blue.svg)](https://doi.org/10.5281/zenodo.20485580)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Release](https://img.shields.io/badge/Release-v3.1.0-orange.svg)](.)

[Bill PDF and Source Files](https://doi.org/10.5281/zenodo.20535429): A LaTeX **finished visual amendment** of **H. R. 9510**, the *Verification Before
Generation in Physical AI Oncology Trials Act of 2026*, an amendment to the
**Federal Food, Drug, and Cosmetic Act** (21 U.S.C. § 301 et seq.), grounded on
the Title 21 device provisions current through **Public Law 119-93**. It was
produced from the VVUQ-05 [`draft-bill`](../draft-bill) scaffold by executing
every bracketed drafting instruction against the named
[`figures-bill`](../update-bill/figures-bill),
[`next-steps`](../update-bill/next-steps), and
[`VVUQ-04/final-bill`](../../VVUQ-04/final-bill) sources. The drafting-instruction
blocks and figure slots are gone: **eleven text figures and ten full-width tables
are rendered**, on a white background, centered, and sized to their content, so
they read as they would in a fenced GitHub Markdown block, with no raster image.

It keeps the full operative text of **Bill v2.0** so it stands on its own, and it
adds a visual perspective and five non-operative appendices. The
**submission-deliverables package** is written under
[`deliverables`](deliverables) as twelve standalone, submission-quality Markdown
documents plus a package index.

## What Bill v3.0 delivers (the three objectives)

- **(a) A visualization of Bill v2.0.** Built on the VVUQ-01 through VVUQ-04
  developments, with the visuals drawn from the verbatim catalog in
  [`papers/VVUQ-05/update-bill/figures-bill`](../update-bill/figures-bill).
  Appendix A reorganizes the VVUQ-01 and VVUQ-02 engineering evidence into
  full-page text figures.
- **(b) Every submission deliverable, written.** Appendix B catalogs the
  supplementary Markdown documents a U.S. House bill needs before submission,
  written under [`deliverables`](deliverables), based on the feedback in
  [`papers/VVUQ-05/update-bill/next-steps`](../update-bill/next-steps).
- **(c) A new explainability standard.** Appendix C establishes the VVUQ-01
  through VVUQ-04 developments as a reusable standard for explaining how a piece
  of United States legislation was created, mapped to the recorded prompts,
  outputs, VVUQ gates, and commit trail.

## The four bill-content goals (carried from Bill v2.0)

The finished visual bill stays **(a) up to date** with today's medical-AI law,
**(b) grounded** in current, mass-adopted medical-law references used
meaningfully, **(c) relevant to emerging bills** as research influences only
(confined to Appendix D, a memo, or testimony, never the operative text), and
**(d) streamlined** to the structured amendment format.

## Table of Contents

- [Repository structure](#repository-structure)
- [The bill structure](#the-bill-structure)
- [Figure and table inventory](#figure-and-table-inventory)
- [The submission deliverables package](#the-submission-deliverables-package)
- [Lineage](#lineage)
- [How every file correlates to main.tex](#how-every-file-correlates-to-maintex)
- [Compile recipe (Overleaf, pdfLaTeX)](#compile-recipe-overleaf-pdflatex)
- [Formatting and fidelity conventions](#formatting-and-fidelity-conventions)
- [Responsible use](#responsible-use)
- [License](#license)

## Repository structure

```
papers/VVUQ-05/full-bill/
  README.md                  (this file)
  main.tex                   (caption with the centered cover figure, SECTION 1
                              short title and the clickable page-filling contents,
                              the eight section inputs, the back matter, references)
  usctitle.sty               (US Code reproduction + amendment apparatus + the
                              centered white-background ASCII figure + the
                              clickable table-of-contents macros)
  references.bib             (provenance and research sources; ieeetr)
  full-bill-LaTeX.zip        (Overleaf-ready bundle of all of the above)
  prompt-full-bill.md        (the generating prompt, verbatim)
  output-full-bill.md        (the narrative output of this step)
  sections/
    s2-findings.tex          (SEC. 2  Findings; Fig. 1 lineage, Tbl. 1 four works,
                              Fig. 2 timeline)
    s3-amendment.tex         (SEC. 3  New section 515D + conforming; Tbl. 2 gate
                              schedule, Fig. 3 decision rule and funnel, Fig. 4
                              layering, Tbl. 3 conforming crosswalk)
    s4-comparative.tex       (SEC. 4  Comparative print; Tbl. 4 change map, Fig. 5
                              section order, the eleven reproduced provisions)
    a5-evidence.tex          (Appendix A  Visual evidence; Fig. 6-8, Tbl. 5)
    a6-deliverables.tex      (Appendix B  Submission deliverables; Tbl. 6)
    a7-explainability.tex    (Appendix C  Explainability standard; Fig. 9-10, Tbl. 7)
    a8-research-matrix.tex   (Appendix D  Research influence matrix; Tbl. 8)
    a9-transparency.tex      (Appendix E  Transparency; Tbl. 9-10, Fig. 11)
  deliverables/
    README.md                (package index: badges, tree, contents)
    01-one-page-summary.md             07-paygo-and-cost-estimate.md
    02-section-by-section-analysis.md   08-sponsor-and-cosponsor-packet.md
    03-plain-english-policy-memo.md     09-stakeholder-engagement-plan.md
    04-legislative-findings.md          10-legislative-counsel-routing-memo.md
    05-ramseyer-comparative-print.md    11-currency-and-cross-reference-matrix.md
    06-constitutional-authority-statement.md  12-testimony-and-research-influence-brief.md
```

## The bill structure

`main.tex` is the single assembler. It carries the caption (condensed to a single
long title dated June 3, 2026, closing with a centered ASCII overview of the v3.0
process), SECTION 1 with a clickable, page-filling table of contents, and the back
matter; each numbered section and lettered appendix is one `sections/*.tex` file.

| Bill part | File | Role |
|:--|:--|:--|
| SECTION 1 | `main.tex` | Short title; clickable table of contents |
| SEC. 2 | `sections/s2-findings.tex` | Findings; the evidence to law record |
| SEC. 3 | `sections/s3-amendment.tex` | New section 515D and the ten conforming amendments |
| SEC. 4 | `sections/s4-comparative.tex` | Comparative print; eleven reproduced provisions |
| Appendix A | `sections/a5-evidence.tex` | Visual engineering evidence (non-operative) |
| Appendix B | `sections/a6-deliverables.tex` | Required submission deliverables (non-operative) |
| Appendix C | `sections/a7-explainability.tex` | The VVUQ explainability standard (non-operative) |
| Appendix D | `sections/a8-research-matrix.tex` | Research influence matrix (non-operative) |
| Appendix E | `sections/a9-transparency.tex` | Development transparency and commit schedule |

## Figure and table inventory

Eleven figures and ten tables, each rendered on a white background, centered, and
sized to its content.

| Slot | Title | Where |
|:--|:--|:--|
| Cover Fig. | Bill v3.0 visual process | `main.tex` |
| Figure 1 | Four-work evidence-to-law lineage | SEC. 2 |
| Table 1 | The four works at a glance | SEC. 2 |
| Figure 2 | Accelerated timeline | SEC. 2 |
| Table 2 | Ten-gate threshold schedule | SEC. 3 |
| Figure 3 | Gate decision rule and funnel | SEC. 3 |
| Figure 4 | Statutory layering through Title 21 | SEC. 3 |
| Table 3 | Ten conforming amendments crosswalk | SEC. 3 |
| Table 4 | Per-section comparative-print change map | SEC. 4 |
| Figure 5 | The eleven sections in comparative-print order | SEC. 4 |
| Figure 6 | The gate, from one dimension to ten | Appendix A |
| Figure 7 | The procedure timelines | Appendix A |
| Figure 8 | The humanoid safety figure | Appendix A |
| Table 5 | External standards map | Appendix A |
| Table 6 | The submission deliverables matrix | Appendix B |
| Figure 9 | Prompt evolution across the works | Appendix C |
| Figure 10 | Internal bill evolution | Appendix C |
| Table 7 | The VVUQ explainability standard | Appendix C |
| Table 8 | Research influence matrix | Appendix D |
| Table 9 | Bill version lineage | Appendix E |
| Table 10 | Single-pull-request commit schedule | Appendix E |
| Figure 11 | The build-and-handoff process | Appendix E |

## The submission deliverables package

Each is a separate, complete, submission-quality Markdown document under
[`deliverables`](deliverables).

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
VVUQ-01 + VVUQ-02              VVUQ-03 bill (v1.0)         VVUQ-04 amendment (v2.0)
(method + hard proof)          H. R. 9510 standalone       H. R. 9510 FD&C amendment
        |                              |                              |
        |   figures-bill (every ASCII diagram + table)                |
        |   next-steps   (the submission deliverables)                |
        +------------------------------+------------------------------+
                                       v
        +-------------------------------------------------------------+
        |  VVUQ-05/draft-bill   (Bill v3.0 scaffold: slots +          |
        |  bracketed DRAFTING INSTRUCTIONS naming exact files)        |
        +------------------------------+------------------------------+
                                       v
        +-------------------------------------------------------------+
        |  VVUQ-05/full-bill   <== THIS (Bill v3.0, visual amendment) |
        |  every figure and table rendered; deliverables written      |
        +-------------------------------------------------------------+
```

## How every file correlates to main.tex

```
                         +-------------------------+
                         |        main.tex         |
                         |      (assembles all)    |
                         +-------------------------+
   \usepackage{usctitle} |                         | \bibliography{references}
                         v                         v
                   +-----------------+  +-----------------+
                   | usctitle.sty    |  | references.bib  |
                   | reproduction +  |  | provenance +    |
                   | amendment +     |  | research        |
                   | centered ascii +|  | sources         |
                   | clickable toc   |  |                 |
                   +-----------------+  +-----------------+
                             |
        \input{sections/...} | (8 files: 3 bill-body + 5 appendices)
                             v
  s2-findings  s3-amendment  s4-comparative  a5-evidence  a6-deliverables
  a7-explainability  a8-research-matrix  a9-transparency
```

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
`fancyvrb` (the `BVerbatim` box, framed and centered). There are no images and no
external assets beyond the four file types. The `full-bill-LaTeX.zip` is the
Overleaf-ready bundle.

## Formatting and fidelity conventions

1. **White background throughout** - the page, the ASCII figure frames, and every
   table are set on white with black rules only.
2. **Centered, content-width figures** - each ASCII figure is captured into a
   content-width box, framed, and centered on the page, so it is neither
   off-center nor stretched, and a wide diagram is set a size smaller so no line
   runs off the right margin.
3. **Even interword spacing, no overflow** - the body is set `RaggedRight`
   (ragged2e) so spacing is even, with no rivers or large gaps and no line off the
   right margin.
4. **No stranded lines** - widow, orphan, and broken-line penalties are maximal;
   text is worded to avoid one- or two-word last lines.
5. **Single hyphens only** - no en dashes, em dashes, double, or triple dashes.
6. **The section symbol §** for every codified reference; never "SS".
7. **Left-aligned, ragged-right tables** - every column uses
   `>{\raggedright\arraybackslash}p{...}` (the `L` and `ragcol` helpers) or the
   flexible `Y` column, and every table is set to `\textwidth`.
8. **Clickable, page-filling contents** - each SECTION 1(b) entry links to its
   part and the entries are distributed to fill the page.
9. **No images, mermaid, or color figures** anywhere; links are black.

## Responsible use

The reproduced statutory text is a work of the United States Government and is in
the public domain; the authoritative version is the United States Code as
published by the Office of the Law Revision Counsel. This visual amendment is an
independent research aid, **not legal advice and not an enacted law**, and is not
endorsed by the FDA, HHS, the OLRC, CFR, ICH, or any member of Congress. The
emerging 119th Congress bills and executive actions appear only in Appendix D as
research influences and are never cited as the basis of an operative clause.

## License

The reproduced statutory text is in the public domain. The generated amendment
framing, figures, tables, deliverables, and this README are released under the
Creative Commons Attribution 4.0 International License (CC BY 4.0).
