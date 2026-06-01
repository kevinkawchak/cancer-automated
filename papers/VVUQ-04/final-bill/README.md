# VVUQ-04 final-bill (LaTeX) - v2.3.0

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Statute](https://img.shields.io/badge/Statute-Public%20Domain%20(U.S.%20Code)-lightgrey.svg)](https://uscode.house.gov)
[![Amends](https://img.shields.io/badge/Amends-Federal%20Food%2C%20Drug%2C%20and%20Cosmetic%20Act-darkblue.svg)](https://www.law.cornell.edu/uscode/text/21/chapter-9)
[![Current through](https://img.shields.io/badge/Current%20through-Pub.%20L.%20119--93-green.svg)](https://www.govinfo.gov/app/collection/plaw)
[![Stage](https://img.shields.io/badge/Stage-Finished%20amendment%20(full%20bill)-brightgreen.svg)](.)
[![Bill](https://img.shields.io/badge/Bill-H.%20R.%209510%20(119th%20Cong.%2C%202d%20Sess.)-darkblue.svg)](.)
[![Prior Bill DOI](https://img.shields.io/badge/Prior%20Bill%20DOI-10.5281%2Fzenodo.20454870-blue.svg)](https://doi.org/10.5281/zenodo.20454870)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Files](https://img.shields.io/badge/Files-main.tex%20%7C%20.sty%20%7C%20.bib%20%7C%2011%20sections%20%7C%20zip-orange.svg)](.)

[PDF](https://doi.org/10.5281/zenodo.20485580) The finished LaTeX **amendment** to the **Federal Food, Drug, and Cosmetic Act**
(21 U.S.C. § 301 et seq.), grounded on the Title 21 device provisions current
through **Public Law 119-93**. This is **H. R. 9510**, the *Verification Before
Generation in Physical AI Oncology Trials Act of 2026*. It was produced from the
v2.2.0 `draft-bill` scaffold by executing every bracketed drafting instruction
against the named `instruct-bill` and `VVUQ-03/final-paper` sources; the
drafting-instruction blocks are gone and the operative text is fully drafted.

The operative mechanism is a **new section 515D of the Act (21 U.S.C. §
360e-5)**, "Verification before generation of robot-patient interaction code in
Physical AI oncology investigations," inserted immediately after the
predetermined change control plan authority (§ 515C; § 360e-4), with conforming
amendments to ten surrounding device provisions and a focused comparative print
of the changes in existing law.

## What changed from the draft scaffold

| Draft (v2.2.0) | Full bill (v2.3.0) |
|:--|:--|
| Bracketed `DRAFTING INSTRUCTIONS` under each part | Every instruction executed and removed |
| Caption with a blank bill number rule | Designated **H. R. 9510**, with a cover-page note on the AI-assisted provenance |
| Findings to be drafted | 14 grounded findings, each tied to an in-force authority or recorded study |
| New section 515D described | New section 515D fully drafted: subsections (a) through (j) plus the ten-gate threshold schedule |
| Conforming amendments listed | Ten conforming amendments drafted, with a focused comparative print marking each insertion and deletion |
| Whole Title 21 sections reproduced | Comparative print reduced to the affected provisions only, with an asterisk convention for omitted matter |
| Running header overlapped two fields | Header abbreviated (page, short title, bill number); no fields overlap |
| Reference URLs could overflow | URLs break on any character so no link runs off the page |

## The bill at a glance

| Field | Value |
|:--|:--|
| Bill | H. R. 9510, 119th Congress, 2d Session |
| Short title | Verification Before Generation in Physical AI Oncology Trials Act of 2026 |
| Underlying Act amended | Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.) |
| New operative section | § 515D of the Act (21 U.S.C. § 360e-5), inserted after § 515C (§ 360e-4) |
| Existing-law base | Eleven Title 21 device sections, current through Public Law 119-93 |
| Committee of referral | House Committee on Energy and Commerce |
| Stage | Finished amendment (independent research draft, not enacted, not legal advice) |

## Repository structure

```
papers/VVUQ-04/full-bill/
  README.md                  (this file)
  main.tex                   (caption, SECTION 1 short title and contents, SEC. 2
                              findings, SEC. 3 the amendment and new section 515D,
                              SEC. 4 comparative print, Appendix A research-influence
                              matrix, Appendix B transparency statement, references)
  usctitle.sty               (US Code reproduction commands + congressional
                              amendment apparatus + formatting hardening)
  references.bib             (79 provenance and research sources; ieeetr)
  full-bill-LaTeX.zip        (Overleaf-ready bundle of all of the above)
  prompt-full-bill.md        (the generating prompt, verbatim)
  output-full-bill.md        (the narrative output of this step)
  sections/
    s301.tex      (§ 301    Short title; 2026 amendment note)
    s321.tex      (§ 321    Device definition (h))
    s331.tex      (§ 331    Prohibited acts)
    s351.tex      (§ 351    Adulterated drugs and devices)
    s355g.tex     (§ 355g   Utilizing real world evidence)
    s360.tex      (§ 360    Registration; the 510(k) pathway)
    s360c.tex     (§ 360c   Classification of devices)
    s360e.tex     (§ 360e   Premarket approval)
    s360e-4.tex   (§ 360e-4 Predetermined change control plans - keystone)
    s360j.tex     (§ 360j   General provisions; the CDS exclusion (o))
    s360k.tex     (§ 360k   State and local requirements - preemption)
```

## The new operative section (FD&C Act § 515D; 21 U.S.C. § 360e-5)

| Subsection | Heading | Substance |
|:--|:--|:--|
| (a) | Requirement | Verify before generate: no robot-patient interaction code runs until an automated VVUQ process bound to named standards has cleared |
| (b) | Order of operations | A record created after generation or execution does not satisfy the section |
| (c) | Gate thresholds and decision rule | Verification fraction = 1.0; per-gate agreement; coefficient-of-variation bound; hard catastrophe predicate; ACCEPT, BLOCK, ESCALATE; ten-gate schedule |
| (d) | Readiness gates | Site Physical AI Standard Level pass; robot Unification Standard Level minimum by functional type; two-framework simulation validation |
| (e) | Documentation and attestation | Algorithm documentation, a signed compliance attestation, and a hash-chained audit trail satisfying 21 CFR part 11 |
| (f) | Cybersecurity, oversight, lifecycle | Access control, encryption, override and emergency stop, drift monitoring, decommissioning |
| (g) | Nondiscrimination | Bias minimization and accessibility |
| (h) | Regulations | Final regulations not later than 365 days after enactment; interim guidance permitted |
| (i) | Definitions | Fifteen operative terms |
| (j) | Rule of construction | Preserves the IDE, human-subject, IND, and change-control authorities; reclassifies nothing |

## Per-section comparative print (changes in existing law)

| File | 21 U.S.C. | FD&C § | Change made by H. R. 9510 |
|:--|:--|:--|:--|
| s301 | § 301 | § 1 | New "Short Title of 2026 Amendment" note |
| s321 | § 321(h) | § 201(h) | Device definition reaches software that generates or executes robot-patient interaction code |
| s331 | § 331 | § 301 | New prohibited act (jjj) for violating § 515D |
| s351 | § 351 | § 501 | New subsection (k): adulterated if used without a cleared § 515D record |
| s355g | § 355g | § 505F | Real world evidence includes § 515D records; new subsection (g) |
| s360 | § 360(k) | § 510(k) | A verification-governed change needs no new premarket notification |
| s360c | § 360c | § 513 | New subsection (l): special controls graduated by autonomy |
| s360e | § 360e | § 515 | New subparagraph (c)(1)(I): verification record in a PMA |
| s360e-4 | § 360e-4 | § 515C | Scope insertions and new subsection (d): the keystone |
| s360j | § 360j(o) | § 520(o) | Robot-control software is not within the CDS exclusion |
| s360k | § 360k | § 521 | New subsection (c): savings clause for State human-in-the-loop law |

## How the conforming amendments thread through Title 21

```
  Robot-patient interaction code in a Physical AI oncology trial
        |
        v
  Is it a "device"?  ......................  § 321(h)        (s321)
        |  the § 360j(o) CDS exclusion does NOT carve out
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
                   | reproduction +  |  | 79 provenance + |
                   | amendment +     |  | research        |
                   | formatting      |  | sources         |
                   +-----------------+  +-----------------+
                             |
        SEC. 4 \input{sections/sXXX}  (11 files, 21 U.S.C. order)
                             v
  s301  s321  s331  s351  s355g  s360  s360c  s360e  s360e-4  s360j  s360k
```

## Lineage

```
  VVUQ-03/final-paper        VVUQ-04/instruct-bill   VVUQ-04/template-bill
  (prior bill H.R. 9510;     (v2.0.0 legal           (v2.1.0 faithful Title 21
   operative text, defined    crosswalk + bill-style)  device excerpt)
   terms, gate thresholds)            |                       |
            \                         |                       /
             v                        v                      v
        VVUQ-04/draft-bill (v2.2.0: scaffold + bracketed instructions)
                             |
                             v
        VVUQ-04/full-bill  (v2.3.0: THIS finished amendment)
```

## Issues addressed in this finished version

1. **Running-header overlap.** The header now carries only short, fixed fields,
   the page number, the abbreviated title "Verification Before Generation Act of
   2026," and "H. R. 9510," so no two fields collide.
2. **The long title on the caption page.** In authentic introduced-House-bill
   form the long title appears twice, once in the caption block and once under
   the "A BILL" head; both are for the House (this is an H.R. measure). The
   wording is identical and correct, and the enacting clause carries the standard
   "Senate and House of Representatives" recital.
3. **Reference URLs.** URLs break on any character so no link runs off the right
   margin.

## Compile recipe (Overleaf, pdfLaTeX)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Set the Overleaf compiler to **pdfLaTeX**. The body font is Times-like via
`newtxtext` and `newtxmath` (standard on Overleaf); on a minimal installation,
substitute `\usepackage{mathptmx}` in `usctitle.sty`. There are no images and no
external assets beyond the four file types. The `full-bill-LaTeX.zip` is the
Overleaf-ready bundle.

## Formatting and fidelity conventions

1. **Even interword spacing, no overflow** - the body is set `RaggedRight`
   (ragged2e) so spacing is even, there are no rivers or large gaps, and no line
   runs off the right margin.
2. **No stranded lines** - widow, orphan, and broken-line penalties are maximal;
   text is worded to avoid one- or two-word last lines and a single line carried
   alone to the next page.
3. **Single hyphens only** - no en dashes, em dashes, double, or triple dashes.
4. **The section symbol §** for every codified reference in the reproduced Code;
   never "SS".
5. **Left-aligned, ragged-right tables** - every column uses
   `>{\raggedright\arraybackslash}p{...}` (the `L` and `ragcol` helpers) or the
   flexible `Y` column, and every table is set to `\textwidth` so it matches the
   body measure exactly.
6. **No images, mermaid, or color figures** anywhere in the document; links are
   black to match the printed Code.

## Responsible use

The reproduced statutory text is a work of the United States Government and is in
the public domain; the authoritative version is the United States Code as
published by the Office of the Law Revision Counsel. This amendment is an
independent research aid, **not legal advice and not an enacted law**, and is not
endorsed by the FDA, HHS, the OLRC, CFR, ICH, or any member of Congress. The
emerging 119th Congress bills and executive actions appear only in Appendix A as
research influences and are never cited as the basis of an operative clause.

## License

The reproduced statutory text is in the public domain. The generated amendment
framing, instructions, tables, and this README are released under the Creative
Commons Attribution 4.0 International License (CC BY 4.0).
