## output-template-bill/LaTeX

This is the narrative output of the template-bill/LaTeX step. It explains what
was produced, why the eleven Title 21 sections were retained and the rest
removed, how the United States Code look and feel was reproduced in LaTeX, and
how the bundle positions the next pass to draft the amendment to Public Law
119-93, Title 21. The deliverables are the LaTeX files (main.tex, usctitle.sty,
references.bib, eleven section files), the README, the Overleaf-ready zip, and
the prompt and output files; this file is the connective summary, not a copy of
the statutory text.

### 1. What was built

A LaTeX template bill that reproduces the look and feel of the official United
States Code, Title 21 - Food and Drugs (current through Public Law 119-93),
reduced to only the sections relevant to the Physical AI oncology clinical-trial
context. The source is the OLRC USLM XML in
papers/VVUQ-04/template-bill/xml_usc21@119-93.zip, a 12.4 MB file with 29
chapters and 757 sections. The bundle keeps one chapter (Chapter 9, the Federal
Food, Drug, and Cosmetic Act) and eleven sections within it, each in its own
sections/ file, wired into a single main.tex under the correct subchapter and
part headings. No bracketed instructions or file names are inserted into the
statutory text; the law is reproduced faithfully so a future AI pass can read the
laws currently in place.

### 2. The section selection and its authority

The selection is driven by two inputs. The instruct-bill (file 01, federal
statutory framework; file 02, FDA AI and ML device regulation; file 10, the legal
crosswalk) names the operative Title 21 device authorities, and the prior bill's
statutory crosswalk in papers/VVUQ-03/final-paper/sections/prior_law.tex confirms
the Federal Food, Drug, and Cosmetic Act, the device CFR framing, and the
investigational pathways as the law the bill builds on. The eleven retained
sections are the device-regulation backbone of the Act:

1. § 301 (Short title) - the "21 U.S.C. § 301 et seq." anchor and the full
   short-title amendment history of the Act.
2. § 321 (Definitions; generally) - subsection (h), the threshold "device"
   definition for robot-patient interaction software.
3. § 331 (Prohibited acts) - the enforcement hook for device duties and
   penalties.
4. § 351 (Adulterated drugs and devices) - device quality and good manufacturing
   practice (the QMSR) tied to adulteration.
5. § 355g (Utilizing real world evidence) - the Cures Act real-world-evidence
   program for trial evidence.
6. § 360 (Registration of producers) - subsection (k), the 510(k) premarket
   notification pathway.
7. § 360c (Classification of devices) - the Class I, II, III scheme that sets the
   premarket pathway and the rigor of VVUQ.
8. § 360e (Premarket approval) - the Class III PMA pathway for a high-risk
   autonomous surgical humanoid.
9. § 360e-4 (Predetermined change control plans for devices) - the single best
   statutory anchor for an automated verification-before-change rule on AI/ML
   device software; the keystone of the excerpt.
10. § 360j (General provisions respecting control of devices) - subsection (o),
    the software and clinical decision support exclusion the bill must not fall
    through.
11. § 360k (State and local requirements respecting devices) - device preemption,
    cited to keep § 360(k) and § 360k distinct.

Everything else in Title 21 was removed as not relevant to robot-patient VVUQ:
the non-FD&C chapters (teas, filled milk, meat and poultry inspection, controlled
substances, drug-abuse programs, pesticide monitoring, food safety, opioid
sanctions); the FD&C food, cosmetics, tobacco, and color subchapters; the
drug-only and supply-chain detail; and device sections that the crosswalk does
not treat as operative anchors (for example postmarket surveillance and
accreditation). The retained set is the minimum faithful substrate that lets the
next pass amend the device pathway, define to classify to clear or approve to
change-control, with the surrounding quality, enforcement, evidence, and
preemption provisions.

### 3. How the sections interact

The retained sections form one pathway rather than a list. Section 321(h) and
section 360j(o) together decide whether robot-patient code is a regulated device;
section 360c classifies it; section 360 (510(k)) and section 360e (PMA) are the
two clearance and approval routes; and section 360e-4 (PCCP) sits on top of both
as the change-control mechanism, the closest existing analogue to "validate the
change before deploy." Sections 351 and 331 supply the quality and enforcement
backbone, section 355g supplies the evidence program, section 360k marks the
federal and state boundary, and section 301 anchors the Act. The README carries
the full statutory-layering ASCII diagram and the section-to-section narrative.

### 4. How the look and feel was reproduced

The priority was to match the printed and PDF United States Code, not the navy
Palatino VVUQ bill family. usctitle.sty sets a Times-like serif body (newtxtext),
black text, letter geometry, and a running header (page; Title 21 - Food and
Drugs; current section). It defines the statutory grammar: \uscsection for the
bold section catchline, \uscprov for the hanging-indent (a)(1)(A)(i)(I)
hierarchy, \usccrosshead for the centered cross-headings (Editorial Notes;
Statutory Notes and Related Subsidiaries), \uscnotehead for the small-caps note
headings (Amendments; Effective Date; Prior Provisions), \uscnotepar for note
text, \uscsource for the parenthetical source credits, and \uscquote for indented
quoted matter. The USLM XML was converted element by element, so subsections,
paragraphs, subparagraphs, clauses, source credits, and the editorial and
statutory notes all render as they appear in the Code.

Fidelity choices: the section symbol § is used for every codified reference; the
em dash and en dash of the source are reproduced as the printed Code prints them
(Title 21---FOOD AND DRUGS; § 360e--4) because the task is a faithful statutory
reproduction and headings keep their exact source form; editorial "So in
original" footnotes are kept as superscript markers with the note text set small
and inline so they never break a heading or the table of contents; and titles,
references, and headings keep their exact source formatting.

### 5. The single-file assembly

main.tex is the one file that assembles the excerpt: it loads usctitle.sty, sets
the Title 21 head and a section analysis of the retained provisions, emits the
Chapter 9, subchapter, and part headings, \input{}s the eleven section files in
United States Code order, and prints the provenance references from
references.bib. Every section file begins with \uscsection and uses only commands
defined in usctitle.sty, so each compiles in the context main.tex sets up. The
README gives the file-to-main.tex correlation diagram and table.

### 6. Build validation

pdflatex is not available in the build container and the bundle is compiled in
Overleaf, so the LaTeX was validated structurally and made compile-safe. All
checks pass: the eleven \input targets resolve and every section is wired in;
braces and \begin/\end environments balance in main.tex, usctitle.sty, and every
section file; every \usc command used is defined; no blank line falls inside any
macro argument (whitespace is collapsed so each provision is one paragraph); the
longest line is 4125 characters; there is no unescaped ampersand in body text
(the eleven in main.tex are longtable separators); math is balanced; and the only
non-ASCII character in compiled text is the intended section symbol, with em and
en dashes rendered as the --- and -- ligatures. The one literal en dash sits in a
comment (the exact USLM identifier /us/usc/t21/s360e-4) and is not typeset. The
references.bib has eleven entries, no duplicate keys, no howpublished field, and
no duplicate links.

### 7. How the next pass should proceed

Read the README and main.tex to see the retained pathway and the cross-cutting
provisions, then open the section files for the exact operative text. Pair each
section with its instruct-bill summary (files 01, 02, 10) and with the prior-bill
crosswalk in papers/VVUQ-03/final-paper/sections/prior_law.tex. Draft the
amendment to Public Law 119-93, Title 21, within Chapter 9, Subchapter V, Part A,
most naturally a new section after § 360e-4 or a special control under § 360j,
citing the retained sections by their 21 U.S.C. § numbers so the change maps
cleanly back to the Code, and keep the United States Code style of this excerpt
so the result reads as a current statute and converts cleanly to XML later.

### 8. Process and compliance

The deliverables were committed one file at a time and pushed to the branch in
real time within a single pull request: main.tex, then usctitle.sty, then
references.bib, then the README, then the eleven section files in United States
Code order, then a second-to-last error-fix commit that normalized whitespace
across the notes-heavy sections, and finally this repository-updates commit (the
prompt and output files, the Overleaf-ready zip, the main README, releases.md,
CHANGELOG.md v2.1.0, and CITATION.cff). All additions are LaTeX, BibTeX, Markdown,
and a zip, all outside the ruff, yamllint, and pytest surface, so the
lint-and-format CI job stays green across Python 3.10, 3.11, and 3.12. Only
kevinkawchak/cancer-automated is edited; nothing is committed to
kevinkawchak/physical-ai-oncology-trials or any other repository.

### 9. Responsible use

The reproduced statutory text is a work of the United States Government and is in
the public domain; the authoritative version is the United States Code as
published by the Office of the Law Revision Counsel. This curated excerpt is an
independent research aid, not legal advice and not an enacted law, and is not
endorsed by the FDA, HHS, the OLRC, or any member of Congress. The section
selection reflects the Physical AI oncology trial context and is intended to
advance patient safety, efficacy, and clinical-trial speed; it is not a statement
that the omitted provisions are unimportant generally.
