# VVUQ-04 template-bill (LaTeX) - v2.1.0

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Statute](https://img.shields.io/badge/Statute-Public%20Domain%20(U.S.%20Code)-lightgrey.svg)](https://uscode.house.gov)
[![Source](https://img.shields.io/badge/Source-Title%2021%20Food%20and%20Drugs-darkblue.svg)](https://uscode.house.gov)
[![Current through](https://img.shields.io/badge/Current%20through-Pub.%20L.%20119--93-green.svg)](https://www.govinfo.gov/app/collection/plaw)
[![Prior Bill DOI](https://img.shields.io/badge/Prior%20Bill%20DOI-10.5281%2Fzenodo.20454870-blue.svg)](https://doi.org/10.5281/zenodo.20454870)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Files](https://img.shields.io/badge/Files-main.tex%20%7C%20.sty%20%7C%20.bib%20%7C%2011%20sections%20%7C%20zip-orange.svg)](.)

A LaTeX **template bill** that reproduces the look and feel of the official
**United States Code, Title 21 - Food and Drugs** (current through **Public Law
119-93**), reduced to only the sections that are relevant to the Physical AI
oncology clinical-trial context. The irrelevant chapters and sections of Title 21
have been removed; the retained sections are the device-regulation backbone of
the **Federal Food, Drug, and Cosmetic Act** on which the *VVUQ Physical AI
Oncology Trial Bill* (H.R. 9510, Draft 1.0; prior bill DOI
10.5281/zenodo.20454870) builds.

The source is the OLRC USLM XML in
`papers/VVUQ-04/template-bill/xml_usc21@119-93.zip` (the full 12.4 MB Title 21).
This bundle converts the retained sections to LaTeX that compiles in Overleaf to
a PDF with the same visual appearance as the United States Code: black serif
body, bold section catchlines, hanging-indent statutory hierarchy, centered
cross-headings for the editorial and statutory notes, small-caps note headings,
and parenthetical source credits. **No bracketed instructions or file names are
inserted into the statutory text;** the law is reproduced faithfully so a future
AI pass can read the laws currently in place and draft the required amendment.

## Purpose and place in the lineage

```
  VVUQ-03/final-paper            VVUQ-04/instruct-bill
  (prior bill H.R. 9510;         (legal crosswalk + bill-style;
   statutory crosswalk names      operative vs research-influence law;
   the Title 21 device sections)  current through May 31, 2026)
            \                              /
             \                            /
              v                          v
        +------------------------------------------+
        |  VVUQ-04/template-bill/LaTeX  <== THIS    |
        |  Title 21 device-provisions excerpt,      |
        |  faithful U.S. Code look and feel,        |
        |  current through Public Law 119-93        |
        +---------------------+--------------------+
                              |
                              v
        Next pass: read this excerpt + instruct-bill + final paper,
        then draft the amendment to Public Law 119-93, Title 21.
```

This excerpt is the **current-law substrate**: the instruct-bill says *which*
authorities are operative and how they map to bill sections, the final paper is
the *prior draft* to be updated, and this template bill is the *actual statutory
text* those two reason about, reduced to the relevant sections and rendered in
the United States Code style so the next pass can amend it precisely.

## Source and selection identity

| Field | Value |
|:--|:--|
| Source document | United States Code, Title 21 - Food and Drugs (USLM XML) |
| Source archive | `papers/VVUQ-04/template-bill/xml_usc21@119-93.zip` (12.4 MB; 757 sections, 29 chapters) |
| Publication point | Current through Public Law 119-93 |
| Publisher of record | Office of the Law Revision Counsel (OLRC), U.S. House of Representatives |
| Retained chapter | Chapter 9 - Federal Food, Drug, and Cosmetic Act |
| Retained sections | 11 (the device-regulation backbone) |
| Selection authority | `papers/VVUQ-04/instruct-bill` (files 01, 02, 10) and `papers/VVUQ-03/final-paper` (prior_law.tex crosswalk) |
| Visual model | The printed and PDF United States Code, not the navy Palatino VVUQ bill family |
| Statute status | Public domain (work of the U.S. Government); generated framing under CC BY 4.0 |

## Repository structure

```
papers/VVUQ-04/template-bill/
  xml_usc21@119-93.zip                (input: full Title 21 USLM XML, 12.4 MB)
  LaTeX/
    README.md                         (this file)
    main.tex                          (Title 21 head, TOC, chapter/subchapter
                                       structure, 11 \input lines, references)
    usctitle.sty                      (U.S. Code look and feel: Times serif,
                                       hanging-indent hierarchy, note styling)
    references.bib                    (provenance + VVUQ lineage; 11 entries)
    template-bill-LaTeX.zip           (Overleaf-ready bundle of all of the above)
    prompt-template-bill/LaTeX.md     (the generating prompt, verbatim)
    output-template-bill/LaTeX.md     (the narrative output of this step)
    sections/
      s301.tex      (§ 301   Short title)
      s321.tex      (§ 321   Definitions; generally)
      s331.tex      (§ 331   Prohibited acts)
      s351.tex      (§ 351   Adulterated drugs and devices)
      s355g.tex     (§ 355g  Utilizing real world evidence)
      s360.tex      (§ 360   Registration of producers of drugs or devices)
      s360c.tex     (§ 360c  Classification of devices intended for human use)
      s360e.tex     (§ 360e  Premarket approval)
      s360e-4.tex   (§ 360e-4 Predetermined change control plans for devices)
      s360j.tex     (§ 360j  General provisions respecting control of devices)
      s360k.tex     (§ 360k  State and local requirements respecting devices)
```

## Contents of each retained section

Each row is one `sections/*.tex` file. "FD&C §" is the Federal Food, Drug, and
Cosmetic Act section number; "Provisions" counts rendered statutory clauses;
"Lead instruct-bill file" is the VVUQ-04 summary that flags the section.

| File | 21 U.S.C. | FD&C § | Subchapter / Part | Heading | Provisions | Why it is retained | Lead instruct-bill file |
|:--|:--|:--|:--|:--|--:|:--|:--|
| s301 | § 301 | § 1 | I - Short Title | Short title | 1 + history | The "§ 301 et seq." anchor; carries the full short-title amendment history of the Act | 01 |
| s321 | § 321 | § 201 | II - Definitions | Definitions; generally | 149 | Subsection (h) is the threshold "device" definition for robot-patient software | 01 |
| s331 | § 331 | § 301 | III - Prohibited Acts | Prohibited acts | 108 | The enforcement hook to which device duties and penalties attach | 01 |
| s351 | § 351 | § 501 | V-A - Drugs and Devices | Adulterated drugs and devices | 32 | Ties device quality and QMSR to adulteration, the basis for VVUQ evidence | 02 |
| s355g | § 355g | § 505F | V-A - Drugs and Devices | Utilizing real world evidence | 31 | Cures Act real-world-evidence program for trial evidence generation | 01, 02 |
| s360 | § 360 | § 510 | V-A - Drugs and Devices | Registration of producers | 131 | Subsection (k) is the 510(k) premarket-notification pathway | 01, 02 |
| s360c | § 360c | § 513 | V-A - Drugs and Devices | Classification of devices | 190 | Class I/II/III scheme sets the premarket pathway and VVUQ rigor | 01, 02 |
| s360e | § 360e | § 515 | V-A - Drugs and Devices | Premarket approval | 158 | The Class III PMA pathway for a high-risk autonomous surgical humanoid | 01, 02 |
| s360e-4 | § 360e-4 | § 515C | V-A - Drugs and Devices | Predetermined change control plans | 11 | The single best statutory anchor for an automated verification-before-change rule | 01, 02 |
| s360j | § 360j | § 520 | V-A - Drugs and Devices | General provisions respecting devices | 267 | Subsection (o) is the software / CDS exclusion the bill must not fall through | 01, 02 |
| s360k | § 360k | § 521 | V-A - Drugs and Devices | State and local requirements | 8 | Device preemption, cited to keep § 360(k) and § 360k distinct | 01 |

## How the sections interact (statutory layering)

The retained sections are not independent; they form the device-regulation
pathway the bill threads through. The same layering the instruct-bill draws for
the bill is realized here in the actual statute.

```
  Robot-patient interaction code in a Physical AI oncology trial
        |
        v
  Is it a "device"?  ......................  § 321(h)        (s321)
        |  the § 360j(o) software/CDS exclusion may carve out
        |  clinician-informing software ...  § 360j(o)       (s360j)
        v  (an autonomous surgical humanoid is not excluded)
  Classify the device  ...................   § 360c          (s360c)
        |                                       |
  Class II -> 510(k) premarket notice ....   § 360(k)        (s360)
  Class III -> premarket approval (PMA) ..    § 360e          (s360e)
        |                                       |
        +----------> Predetermined change ->   § 360e-4       (s360e-4)
                     control plans (PCCP): the change-control
                     home for an automated VVUQ-on-change rule
        |
  Cross-cutting duties that attach regardless of pathway:
   - Adulteration / quality (QMSR) ........   § 351           (s351)
   - Prohibited acts / enforcement ........   § 331           (s331)
   - Real-world evidence for trials .......   § 355g          (s355g)
   - State preemption boundary ............   § 360k          (s360k)
   - Short title of the whole Act .........   § 301           (s301)
```

Narrative correlations:

1. **§ 321 -> § 360j(o):** the device definition and its software exclusion
   together decide whether robot-patient code is regulated at all. The bill must
   confirm the humanoid is a device and does not fall through the CDS exclusion.
2. **§ 360c -> § 360 / § 360e:** classification routes a device to 510(k)
   notification (§ 360(k)) or premarket approval (§ 360e); the class sets how
   much VVUQ the bill can demand.
3. **§ 360e -> § 360e-4:** the PCCP authority sits on top of PMA and 510(k) and
   is the closest existing analogue to "validate the change before deploy"; the
   bill makes that discipline mandatory, ex ante, and automated.
4. **§ 351, § 331:** adulteration and prohibited-acts provide the quality and
   enforcement backbone; **§ 355g** supplies the real-world-evidence program;
   **§ 360k** marks the federal/state boundary; **§ 301** anchors the Act.

## How every file correlates to the single file (main.tex)

`main.tex` is the one file that assembles the excerpt. It loads the style, sets
the Title 21 head and the section analysis, emits the chapter, subchapter, and
part headings, `\input`s the 11 section files in United States Code order, and
prints the provenance references.

```
                         +------------------+
                         |   main.tex       |
                         | (assembles all)  |
                         +---+----------+---+
        \usepackage{usctitle}|          | \bibliography{references}
                             v          v
                   +-----------------+  +-----------------+
                   | usctitle.sty    |  | references.bib  |
                   | look and feel:  |  | provenance +    |
                   | \uscsection     |  | VVUQ lineage    |
                   | \uscprov        |  | (11 entries)    |
                   | \usccrosshead   |  +-----------------+
                   | \uscsource ...  |
                   +-----------------+
                             |
            \input{sections/sXXX}  (11 files, U.S. Code order)
                             v
  s301  s321  s331 | s351  s355g  s360  s360c  s360e  s360e-4  s360j  s360k
  ----  ----  ---- | ----  -----  ----  -----  -----  -------  -----  -----
  Sub I Sub II SubIII        Subchapter V, Part A - Drugs and Devices
```

| File | Role | Provides / consumes | Resolves against main.tex by |
|:--|:--|:--|:--|
| `main.tex` | Assembler | Title head, TOC/section analysis, structural headings, references | is the single file; `\input`s every section |
| `usctitle.sty` | Style | `\uscsection`, `\uscprov`, `\uscquote`, `\usccrosshead`, `\uscnotehead`, `\uscnotepar`, `\uscsource`, structural heads | `\usepackage{usctitle}` |
| `references.bib` | Provenance | 11 entries: source, public law, statutory anchors, VVUQ lineage | `\bibliography{references}` + `\nocite{*}` |
| `sections/s301.tex` ... `s360k.tex` | Statutory text | One U.S. Code section each, with notes and source credit | one `\input{sections/sXXX}` per file |

Every section file begins with `\uscsection{§ ...}{heading}` and uses only the
commands defined in `usctitle.sty`, so each compiles in the context `main.tex`
sets up. The build is verified structurally: all 11 `\input` targets resolve,
braces and environments balance in every file, every `\usc...` command used is
defined, and the only non-ASCII character carried through is the intended `§`.

## What was excluded and why

Title 21 has 29 chapters and 757 sections. This excerpt keeps **one chapter**
(Chapter 9, the Federal Food, Drug, and Cosmetic Act) and **11 sections** within
it. Excluded as not relevant to the Physical AI oncology trial context:

| Excluded material | Examples | Reason |
|:--|:--|:--|
| Non-FD&C chapters | Ch. 1-8, 10-29 (teas, filled milk, meat and poultry inspection, narcotics and controlled substances, drug-abuse programs, pesticide monitoring, food safety, opioid sanctions) | Outside device regulation; no bearing on robot-patient VVUQ |
| FD&C food, cosmetics, tobacco, color | Subchapters IV, VI, IX; parts of VII | Not device or trial law |
| FD&C drug-only and supply-chain detail | Most of § 355 (new drugs), §§ 360aaa+ (advertising, supply chain), animal-drug and medical-gas parts | Drug-specific; the device backbone is what the bill amends |
| Device sections not load-bearing for the gate | e.g., § 360i (records/reports), § 360l (postmarket surveillance), § 360m (accreditation) | Useful context but not cited as operative anchors by the instruct-bill or the prior-bill crosswalk |

The retained set is the minimum faithful substrate that lets the next pass amend
the device pathway (define -> classify -> clear/approve -> change-control) with
the quality, enforcement, evidence, and preemption provisions that surround it.

## Compile recipe (Overleaf, pdfLaTeX)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Set the Overleaf compiler to **pdfLaTeX**. The body font is Times-like via
`newtxtext` and `newtxmath` (standard on Overleaf); on a minimal TeX
installation, substitute `\usepackage{mathptmx}` in `usctitle.sty`. The
bibliography is rendered with `ieeetr`; `\nocite{*}` prints every provenance
entry. There are no images and no external assets beyond the four file types.

## Style and fidelity conventions

1. **Black body text, Times-like serif, justified** - the printed United States
   Code look, not the navy Palatino VVUQ bill family.
2. **Bold section catchlines** (`§ 360e-4. Predetermined change control plans
   for devices`); **hanging-indent** (a)(1)(A)(i)(I) hierarchy; **centered
   cross-headings** (Editorial Notes; Statutory Notes and Related Subsidiaries);
   **small-caps note headings** (Amendments; Effective Date); **parenthetical
   source credits**.
3. The section symbol `§` is used for every codified reference.
4. The em dash and en dash of the source are reproduced as the printed Code
   prints them (`Title 21---FOOD AND DRUGS`; `§ 360e--4`), because the task is a
   faithful statutory reproduction and headings keep their exact source form.
5. Editorial "So in original" footnotes are kept as superscript markers with the
   note text set small and inline, so they never break headings or the table of
   contents.
6. **No bracketed instructions, no file names, no images** appear inside the
   statutory text. The only added matter is the front-matter scope note and
   disclaimer, clearly set off from the law.

## How the next AI pass should use this folder

1. Read this README and `main.tex` to see the retained pathway
   (define -> classify -> clear/approve -> change-control) and the cross-cutting
   provisions, then open the section files for the exact operative text.
2. Pair each section with its instruct-bill summary (files 01, 02, 10) and with
   the prior-bill crosswalk in `papers/VVUQ-03/final-paper/sections/prior_law.tex`.
3. Draft the amendment to Public Law 119-93, Title 21: amend or add within
   Chapter 9, Subchapter V, Part A (most naturally a new section after § 360e-4,
   or a special control under § 360j), citing the retained sections by their
   `21 U.S.C. §` numbers so the change maps cleanly back to the Code.
4. Keep the United States Code style of this excerpt for the amended text so the
   result reads as a current statute and converts cleanly to XML in a later step.

## Responsible use

The reproduced statutory text is a work of the United States Government and is in
the public domain; the authoritative version is the United States Code as
published by the Office of the Law Revision Counsel. This curated excerpt is an
independent research aid, not legal advice and not an enacted law, and is not
endorsed by the FDA, HHS, the OLRC, or any member of Congress. The section
selection reflects the Physical AI oncology trial context and is intended to
advance patient safety, efficacy, and clinical-trial speed; it is not a
statement that the omitted provisions are unimportant generally.

## License

The statutory text is in the public domain. The generated framing, tables, and
this README are released under the Creative Commons Attribution 4.0 International
License (CC BY 4.0).
