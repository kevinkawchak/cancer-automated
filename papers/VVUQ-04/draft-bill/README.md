# VVUQ-04 draft-bill (LaTeX) - v2.2.0

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Statute](https://img.shields.io/badge/Statute-Public%20Domain%20(U.S.%20Code)-lightgrey.svg)](https://uscode.house.gov)
[![Amends](https://img.shields.io/badge/Amends-Federal%20Food%2C%20Drug%2C%20and%20Cosmetic%20Act-darkblue.svg)](https://www.law.cornell.edu/uscode/text/21/chapter-9)
[![Current through](https://img.shields.io/badge/Current%20through-Pub.%20L.%20119--93-green.svg)](https://www.govinfo.gov/app/collection/plaw)
[![Stage](https://img.shields.io/badge/Stage-Draft%20amendment%20scaffold-orange.svg)](.)
[![Prior Bill DOI](https://img.shields.io/badge/Prior%20Bill%20DOI-10.5281%2Fzenodo.20454870-blue.svg)](https://doi.org/10.5281/zenodo.20454870)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Files](https://img.shields.io/badge/Files-main.tex%20%7C%20.sty%20%7C%20.bib%20%7C%2011%20sections%20%7C%20zip-orange.svg)](.)

A LaTeX **draft amendment** to the **Federal Food, Drug, and Cosmetic Act**
(21 U.S.C. § 301 et seq.), grounded on the Title 21 device provisions current
through **Public Law 119-93**. This bundle is an amendment **scaffold with
bracketed drafting instructions**, not a finished bill. It lays out the exact
congressional amendment structure and, under every part, carries a set-off
`DRAFTING INSTRUCTIONS` block that tells a future **Claude Code Opus 4.8 (1M
context) Max** pass exactly which files in this repository to process, how to
process them, and how to combine them to produce publication-quality statutory
text.

It descends from the VVUQ-04 **template-bill** (the faithful Title 21
device-provisions excerpt): the eleven reproduced section files are carried in
unchanged as the comparative-print base, and bracketed instructions plus exact
directory and file names are added directly under each section so the next pass
has a precise, efficient starting point.

## Why an amendment, and to what

Per the amendment-drafting instructions, the correct target is **not** "Public
Law 119-93, Title 21." Public Law 119-93 is the public law *through which* Title
21 is current; it is not itself the law being changed. The substantive device
authorities live in the **Federal Food, Drug, and Cosmetic Act**, codified in
Title 21. This draft therefore amends the Federal Food, Drug, and Cosmetic Act
and cites each affected provision by its `21 U.S.C. §` number, naming Public Law
119-93 only as the currency point of the reproduced existing law.

The operative mechanism is a **new section 515D of the Act (21 U.S.C. §
360e-5)**, "Verification before generation of robot-patient interaction code in
Physical AI oncology investigations," inserted immediately after the
predetermined change control plan authority (§ 515C; § 360e-4), with conforming
amendments to ten surrounding device provisions.

## What the next pass must achieve (the four goals)

The bracketed instructions are written so the finished amendment will be:

- **(a) Up to date** with today's medical-AI laws and implement their medical
  and technology complexity, drawing on `papers/VVUQ-04/instruct-bill` files
  `01`-`05` and `09` (FDA PCCP final guidance, QMSR effective Feb. 2, 2026,
  45 CFR § 92.210, CMS Medicare Advantage AI guardrail, CPT autonomy taxonomy).
- **(b) Grounded** in current, mass-adopted medical-law references, used
  meaningfully: each operative duty is anchored to an in-force statute, rule, or
  recognized standard via a BibTeX key in `references.bib`.
- **(c) Relevant to emerging bills** as research influences only: the 119th
  Congress bills (`08-emerging-federal-bills.md`) and executive actions
  (`07-executive-actions-national-ai-strategy.md`) inform the findings, the
  policy memo, testimony, and **Appendix A. Research Influence Matrix**, but
  never the operative bill text.
- **(d) Streamlined** to the structured amendment format (SECTION 1 short title
  and table of contents; SEC. 2 findings; SEC. 3 the amendment; SEC. 4
  comparative print of changes in existing law).

## Purpose and place in the lineage

```
  VVUQ-03/final-paper          VVUQ-04/instruct-bill        VVUQ-04/template-bill
  (prior bill H.R. 9510;       (legal crosswalk +           (faithful Title 21
   operative text, defined      bill-style; operative vs.    device excerpt;
   terms, gate thresholds)      research-influence law)      11 section files)
            \                          |                          /
             \                         |                         /
              v                        v                        v
        +-----------------------------------------------------------+
        |  VVUQ-04/draft-bill/LaTeX   <== THIS                       |
        |  Draft amendment to the Federal Food, Drug, and Cosmetic   |
        |  Act: structure + bracketed DRAFTING INSTRUCTIONS that     |
        |  name exact files for a future Claude Code pass to process |
        +----------------------------+------------------------------+
                                     |
                                     v
        Next pass: execute the bracketed instructions against the named
        files to produce the finished, publication-quality amendment.
```

## Source and selection identity

| Field | Value |
|:--|:--|
| Underlying Act amended | Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.) |
| New operative section | § 515D of the Act (21 U.S.C. § 360e-5), inserted after § 515C (§ 360e-4) |
| Existing-law base | Eleven Title 21 device sections, current through Public Law 119-93 |
| Source archive | `papers/VVUQ-04/template-bill/xml_usc21@119-93.zip` (the OLRC USLM XML) |
| Prior bill | H.R. 9510, Draft 1.0 (`papers/VVUQ-03/final-paper`; DOI 10.5281/zenodo.20454870) |
| Law crosswalk | `papers/VVUQ-04/instruct-bill` (ten markdown files, five .bib files; through May 31, 2026) |
| Visual model | Reproduced law in United States Code style; amendment apparatus in congressional bill style |
| Stage | Draft amendment scaffold with bracketed drafting instructions (not enacted, not final) |

## Repository structure

```
papers/VVUQ-04/draft-bill/
  README.md                  (this file)
  main.tex                   (bill caption, A BILL, enacting clause, SECTION 1
                              short title + table of contents, SEC. 2 findings,
                              SEC. 3 the amendment, SEC. 4 comparative print,
                              Appendix A research-influence matrix, references)
  usctitle.sty               (US Code reproduction commands + congressional
                              amendment apparatus + formatting hardening)
  references.bib             (provenance + research sources; ieeetr)
  draft-bill-LaTeX.zip       (Overleaf-ready bundle of all of the above)
  prompt-draft-bill.md       (the generating prompt, verbatim)
  output-draft-bill.md       (the narrative output of this step)
  sections/
    s301.tex      (§ 301    Short title)
    s321.tex      (§ 321    Definitions; generally - the device definition)
    s331.tex      (§ 331    Prohibited acts)
    s351.tex      (§ 351    Adulterated drugs and devices)
    s355g.tex     (§ 355g   Utilizing real world evidence)
    s360.tex      (§ 360    Registration of producers; the 510(k) pathway)
    s360c.tex     (§ 360c   Classification of devices intended for human use)
    s360e.tex     (§ 360e   Premarket approval)
    s360e-4.tex   (§ 360e-4 Predetermined change control plans - keystone)
    s360j.tex     (§ 360j   General provisions; the software / CDS exclusion)
    s360k.tex     (§ 360k   State and local requirements - preemption)
```

## The amendment structure (and where the instructions live)

`main.tex` is the single assembler. It carries the bill caption and front
matter and four bill sections; the heavy, file-specific instructions for the
existing-law changes live in the eleven `sections/*.tex` files.

| Bill part | Role | Instruction source |
|:--|:--|:--|
| SECTION 1 | Short title; table of contents | `main.tex` draftbox |
| SEC. 2 | Findings (and the one place research influences may appear, as findings of fact) | `main.tex` draftbox |
| SEC. 3(a) | The new operative section § 360e-5 (§ 515D) | `main.tex` draftbox |
| SEC. 3(b) | Conforming amendments | `main.tex` draftbox + each `sections/*.tex` |
| SEC. 3(c)-(e) | Clerical amendment, rule of construction, effective date | `main.tex` draftboxes |
| SEC. 4 | Comparative print; changes in existing law | each `sections/*.tex` draftbox |
| Appendix A | Research Influence Matrix (non-operative) | `main.tex` draftbox |

## Contents of each reproduced section

Each row is one `sections/*.tex` file: the original Title 21 text is reproduced
in full, and a draftbox is added directly under it with the amendatory action
and the exact files to synthesize from. "FD&C §" is the Act section number.

| File | 21 U.S.C. | FD&C § | Role in the amendment | Lead source files |
|:--|:--|:--|:--|:--|
| s301 | § 301 | § 1 | Clerical anchor; add a Short Title of 2026 Amendment note | instruct-bill 10; final-paper statutory_text |
| s321 | § 321 | § 201 | Conform the device definition (h); confirm Physical AI software is a device | instruct-bill 01, 02; final-paper definitions |
| s331 | § 331 | § 301 | Add the prohibited act (generate/execute without a cleared record) | instruct-bill 01; final-paper statutory_text |
| s351 | § 351 | § 501 | Deem adulterated if used without a cleared § 360e-5 record (QMSR tie) | instruct-bill 02; final-paper attestations |
| s355g | § 355g | § 505F | Extend real-world evidence to device and Physical AI oncology trials | instruct-bill 01, 02; final-paper findings |
| s360 | § 360 | § 510 | 510(k) interaction with the verification protocol and a PCCP | instruct-bill 01, 02; final-paper statutory_text |
| s360c | § 360c | § 513 | Add special controls / classification by autonomy taxonomy | instruct-bill 02, 04; final-paper definitions |
| s360e | § 360e | § 515 | Require the verification record in a PMA application | instruct-bill 02; final-paper statutory_text |
| s360e-4 | § 360e-4 | § 515C | Keystone: require automated verification-before-change in a PCCP | instruct-bill 02; final-paper statutory_text |
| s360j | § 360j | § 520 | Confirm robot-control software is not in the CDS exclusion (o) | instruct-bill 01, 02, 03; final-paper definitions |
| s360k | § 360k | § 521 | Savings clause preserving non-conflicting state human-in-the-loop law | instruct-bill 06, 10; final-paper prior_law |

## How the sections interact (statutory layering)

The eleven sections form the device-regulation pathway the amendment threads
through; the new § 360e-5 attaches to the change-control node and the
cross-cutting duties around it.

```
  Robot-patient interaction code in a Physical AI oncology trial
        |
        v
  Is it a "device"?  ......................  § 321(h)        (s321)
        |  the § 360j(o) CDS exclusion must NOT carve out
        |  autonomous robot-control software  § 360j(o)      (s360j)
        v
  Classify the device  ...................   § 360c          (s360c)
        |                                       |
  Class II -> 510(k) premarket notice ....   § 360(k)        (s360)
  Class III -> premarket approval (PMA) ..    § 360e          (s360e)
        |                                       |
        +----------> Predetermined change ->   § 360e-4       (s360e-4)
                     control plans (PCCP)  ===> NEW § 360e-5  (verify before
                     the keystone the new            generation; the mandatory,
                     section makes mandatory         ex ante, automated VVUQ rule)
        |
  Cross-cutting duties the new section leans on:
   - Adulteration / quality (QMSR) ........   § 351           (s351)
   - Prohibited acts / enforcement ........   § 331           (s331)
   - Real-world evidence for trials .......   § 355g          (s355g)
   - State preemption boundary ............   § 360k          (s360k)
   - Short title of the whole Act .........   § 301           (s301)
```

## How every file correlates to the single file (main.tex)

```
                         +------------------+
                         |   main.tex       |
                         | (assembles all)  |
                         +---+----------+---+
        \usepackage{usctitle}|          | \bibliography{references}
                             v          v
                   +-----------------+  +-----------------+
                   | usctitle.sty    |  | references.bib  |
                   | reproduction +  |  | provenance +    |
                   | amendment +     |  | research        |
                   | draftbox macros |  | sources         |
                   +-----------------+  +-----------------+
                             |
        SEC. 4 \input{sections/sXXX}  (11 files, 21 U.S.C. order)
                             v
  s301  s321  s331  s351  s355g  s360  s360c  s360e  s360e-4  s360j  s360k
```

Every section file begins with `\uscsection{§ ...}{heading}`, reproduces the
existing law with the `\uscprov` hierarchy, and ends with a `draftbox` of
bracketed `\dstep` directives. All commands resolve from `usctitle.sty`.

## Compile recipe (Overleaf, pdfLaTeX)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Set the Overleaf compiler to **pdfLaTeX**. The body font is Times-like via
`newtxtext` and `newtxmath` (standard on Overleaf); on a minimal TeX
installation, substitute `\usepackage{mathptmx}` in `usctitle.sty`. There are no
images and no external assets beyond the four file types. The `draft-bill-LaTeX.zip`
is the Overleaf-ready bundle.

## Formatting and fidelity conventions

1. **Even interword spacing, no overflow** - the body is set `RaggedRight`
   (ragged2e) so spacing is even, there are no rivers or large gaps, and no line
   runs off the right margin.
2. **No stranded lines** - widow, orphan, and broken-line penalties are maximal;
   reword to avoid one- or two-word last lines and a single line carried alone
   to the next page.
3. **Single hyphens only** - no en dashes, em dashes, double, or triple dashes.
4. **The section symbol §** for every codified reference; never "SS".
5. **Left-aligned, ragged-right tables** - every column uses
   `>{\raggedright\arraybackslash}p{...}` via the `\ragcol` helper so no cell
   develops large interword gaps and nothing overflows.
6. **No images, mermaid, or color figures** anywhere in the document.

## How the next AI pass should use this folder

1. Read this README and `main.tex` to see the amendment structure and the new
   § 360e-5 design.
2. For each part, open its `draftbox` and process the **exact** files it names
   under `papers/VVUQ-04/instruct-bill/` and `papers/VVUQ-03/final-paper/`,
   resolving every cited authority to a key in `references.bib`.
3. Draft the operative text in SEC. 3 and mark the matching changes in the
   comparative print in SEC. 4, keeping operative authority and research
   influence strictly separated per goal (c).
4. Delete each `draftbox` as its part is finished, run the compile recipe, and
   apply the formatting conventions above as a senior author would.

## Responsible use

The reproduced statutory text is a work of the United States Government and is
in the public domain; the authoritative version is the United States Code as
published by the Office of the Law Revision Counsel. This draft amendment is an
independent research aid, **not legal advice and not an enacted law**, and is
not endorsed by the FDA, HHS, the OLRC, CFR, ICH, or any member of Congress.

## License

The reproduced statutory text is in the public domain. The generated amendment
framing, instructions, tables, and this README are released under the Creative
Commons Attribution 4.0 International License (CC BY 4.0).
