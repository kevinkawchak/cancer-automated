# VVUQ-04: Verification Before Generation in Physical AI Oncology Trials Act of 2026 (H. R. 9510)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Bill DOI](https://img.shields.io/badge/Bill%20DOI-10.5281%2Fzenodo.20485580-blue.svg)](https://doi.org/10.5281/zenodo.20485580)
[![Prior Bill DOI](https://img.shields.io/badge/Prior%20Bill%20DOI-10.5281%2Fzenodo.20454870-blue.svg)](https://doi.org/10.5281/zenodo.20454870)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![Releases](https://img.shields.io/badge/Releases-v2.0.0%20to%20v2.3.0-brightgreen.svg)](../../releases.md)
[![Amends](https://img.shields.io/badge/Amends-Federal%20Food%2C%20Drug%2C%20and%20Cosmetic%20Act-darkblue.svg)](https://www.law.cornell.edu/uscode/text/21/chapter-9)
[![New section](https://img.shields.io/badge/New%20section-%C2%A7%20515D%20(21%20U.S.C.%20%C2%A7%20360e--5)-red.svg)](full-bill/)
[![Current through](https://img.shields.io/badge/Current%20through-Pub.%20L.%20119--93-green.svg)](https://www.govinfo.gov/app/collection/plaw)
[![Authored](https://img.shields.io/badge/Authored-Claude%20Code%20Opus%204.8%20(1M)%20Max-purple.svg)](https://www.anthropic.com/claude)

### Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20485580)

VVUQ-04 is the fourth and culminating work in the [papers](../) series. It makes
the VVUQ-03 bill precise and current by recasting **H. R. 9510** as a properly
targeted amendment to the **Federal Food, Drug, and Cosmetic Act** (21 U.S.C. §
301 et seq.), current through **Public Law 119-93**. The short title is
*Verification Before Generation in Physical AI Oncology Trials Act of 2026*. This
README focuses only on the VVUQ-04 directory.

> **Operative mechanism.** A new section 515D of the Act (21 U.S.C. § 360e-5): no
> robot-patient interaction code may be generated or executed in a Physical AI
> oncology investigation until an automated verification, validation, and
> uncertainty quantification process bound to named external standards has
> cleared, with the cleared record documented and attested.

## Table of Contents

- [Verification developments and progress](#verification-developments-and-progress)
- [Building process within the work](#building-process-within-the-work)
- [How the amendment threads through Title 21](#how-the-amendment-threads-through-title-21)
- [The new operative section (FD&C Act 515D)](#the-new-operative-section-fdc-act-515d)
- [Results and what they mean for the industry](#results-and-what-they-mean-for-the-industry)
- [The processing feat accomplished by AI](#the-processing-feat-accomplished-by-ai)
- [Accelerated timeline versus conventional methods](#accelerated-timeline-versus-conventional-methods)
- [Repository structure](#repository-structure)
- [Related VVUQ works and final DOIs](#related-vvuq-works-and-final-dois)
- [Responsible use](#responsible-use)
- [License](#license)

## Verification developments and progress

VVUQ-04 advanced over four releases. The verification requirement is no longer a
standalone bill; it is drafted as a precise insertion into the existing device
law, anchored to in-force authorities and current to the day.

| Release | Stage | VVUQ verification development |
|:--|:--|:--|
| v2.0.0 | Instruct bill | A research head start: 10 markdown summaries plus 5 BibTeX files (145 entries) bring the prior bill current with medical AI law through May 31, 2026, with a legal crosswalk separating operative law from research influences |
| v2.1.0 | Template bill | A faithful LaTeX reproduction of the 11 relevant Title 21 device sections in the United States Code look and feel, reduced from 29 chapters and 757 sections |
| v2.2.0 | Draft bill | An amendment scaffold: each of the 11 reproduced sections keeps its text and adds a draftbox of bracketed drafting instructions naming the exact source files |
| v2.3.0 | Full bill | Every instruction executed: the new section 515D plus ten conforming amendments, 14 grounded findings, and a focused comparative print; drafting blocks removed |

## Building process within the work

VVUQ-04 starts from the prior bill and the actual statute, builds a current legal
crosswalk and a faithful Title 21 excerpt, scaffolds the amendment, and processes
it into the finished bill.

```
  instruct-bill/  (v2.0.0)        template-bill/  (v2.1.0)
  (legal crosswalk, current)       (Title 21 device sections, LaTeX)
  +----------------------+         +----------------------+
  | 01..10 md summaries  |         | xml_usc21@119-93.zip |
  | 5 .bib (145 entries) |         |   (12.4 MB USLM XML) |
  | operative vs memo    |         | -> 11 sections, US   |
  | (through 2026-05-31) |         |    Code look + feel  |
  +----------------------+         +----------------------+
            \                               /
             \                             /
              v                           v
            draft-bill/  (v2.2.0)  amendment scaffold
            +-------------------------------------------+
            | 11 reproduced sections + draftbox each:   |
            | bracketed DRAFTING INSTRUCTIONS naming    |
            | the exact instruct-bill and final-paper   |
            | files a processing pass must read         |
            +-------------------------------------------+
                              |
                              v
            full-bill/  (v2.3.0)  finished amendment
            +-------------------------------------------+
            | SECTION 1 short title + contents          |
            | SEC. 2 findings (14)                      |
            | SEC. 3 new section 515D + 10 conforming   |
            | SEC. 4 comparative print                  |
            | Appendix A research-influence matrix      |
            | Appendix B transparency; 79 references    |
            +-------------------------------------------+
                              |
                              v
            final-bill/  (Zenodo)   DOI 10.5281/zenodo.20485580
```

The supplementary `update-bill/` directory holds multi-model prompts and outputs
(ChatGPT 5.5 Thinking Extended and Gemini 3.1 Pro) on U.S. medical AI law and on
Public Law 119-93, used to keep the amendment current.

## How the amendment threads through Title 21

The new duty is inserted exactly where the device pathway already governs change,
right after the predetermined change control plan keystone, with conforming
amendments to the surrounding provisions.

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

## The new operative section (FD&C Act 515D)

The new section 515D (21 U.S.C. § 360e-5) carries the requirement in subsections
(a) through (j).

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

## Results and what they mean for the industry

The result is a finished, ready-to-introduce amendment: the new section 515D plus
ten conforming amendments to § 321(h), § 331, § 351, § 355g, § 360(k), § 360c,
§ 360e, § 360e-4, § 360j(o), and § 360k, with 14 grounded findings and a focused
comparative print of the changes in existing law. It is current through Public
Law 119-93 and grounded in a legal crosswalk current to May 31, 2026, with the
emerging 119th Congress bills and executive actions kept to a non-operative
research-influence appendix.

For the new Physical AI oncology trial industry, this is the difference between a
standalone proposal and a precise instrument lawmakers and counsel can act on.
Rather than create a parallel regime, the amendment inserts verification before
generation exactly where Title 21 already governs device change (after the PCCP
keystone), so it inherits the existing classification, premarket, quality, and
enforcement machinery. That makes a defensible standard of care actionable:
the industry gets a clear, ex ante, automated VVUQ requirement bound to named
external standards, anchored in the statute that already regulates the devices.

## The processing feat accomplished by AI

Claude Code Opus 4.8 (1M) Max authored VVUQ-04 autonomously in a managed,
ephemeral cloud container, pushing each file in real time across sequential
commits in single pull requests, then a second-to-last error-fix-and-bundle
commit and a final repository-updates commit per release.

- **Processed statute at scale:** a 12.4 MB Title 21 USLM XML corpus was reduced
  from 29 chapters and 757 sections to the 11 device sections that matter, then
  reproduced faithfully in the United States Code look and feel.
- **Built a current legal crosswalk:** 10 markdown summaries and 5 BibTeX files
  (145 entries) bring the prior bill current with FDA PCCP guidance, the QMSR, 45
  CFR § 92.210, the CMS Medicare Advantage AI guardrail, and the CPT autonomy
  taxonomy, separating operative law from research influences.
- **Drafted a precise amendment:** the new section 515D with subsections (a)
  through (j) and the ten-gate schedule, ten conforming amendments, 14 grounded
  findings, and a comparative print marking each insertion and deletion.
- **Fixed the flagged issues in the finished version:** the running header is
  abbreviated so no two fields overlap, long reference URLs break rather than run
  off the page, and every table is set to the body measure with left-aligned
  ragged-right columns.
- **Kept the CI green:** all additions are LaTeX, BibTeX, Markdown, and a zip, all
  outside the ruff, yamllint, and pytest surface, so lint-and-format passed across
  Python 3.10, 3.11, and 3.12.

## Accelerated timeline versus conventional methods

VVUQ-04's end goal is the finished FD&C Act amendment (the full bill). It was
reached in about two days (v2.0.0 on 2026-05-31 to v2.3.0 on 2026-06-01), versus
the months to years a conventional amendment, drafted with counsel against the
live United States Code and a current medical AI legal crosswalk, would take.

```
  Conventional path (months to years)        VVUQ-04 (about 2 days)
  +-----------------------------------+      +-----------------------------------+
  | research current medical AI law   |      | v2.0.0 instruct bill (145 refs)   |
  | reproduce the Title 21 provisions |  vs  | v2.1.0 template bill (11 sects)   |
  | draft the amendment + conforming  |      | v2.2.0 draft bill (scaffold)      |
  | comparative print + counsel review|      | v2.3.0 full bill (new 360e-5)     |
  +-----------------------------------+      +-----------------------------------+
        serial, multi-month effort             autonomous, real-time commits
```

## Repository structure

```
papers/VVUQ-04/
  README.md          (this file)
  instruct-bill/     v2.0.0 legal crosswalk (10 md + 5 bib; 145 entries)
    01..10 *.md  federal-statutes.bib  ...  standards-and-literature.bib
  template-bill/     v2.1.0 Title 21 device sections, US Code look and feel
    xml_usc21@119-93.zip   LaTeX/ (main.tex, usctitle.sty, references.bib, 11 sections)
  draft-bill/        v2.2.0 amendment scaffold (bracketed drafting instructions)
    main.tex  usctitle.sty  references.bib  draft-bill-LaTeX.zip  sections/ (11)
  full-bill/         v2.3.0 finished amendment (new section 515D + 10 conforming)
    main.tex  usctitle.sty  references.bib  full-bill-LaTeX.zip  sections/ (11)
  final-bill/        author-finalized bill (PDF + LaTeX on Zenodo)
  update-bill/       supplementary multi-model prompts and outputs (ChatGPT, Gemini)
```

## Related VVUQ works and final DOIs

VVUQ-04 recasts the VVUQ-03 bill as a precise FD&C Act amendment, grounded in the
recorded evidence of VVUQ-01 and VVUQ-02. The final paper and bill DOI for each
work in the series:

| Work | Final artifact | Author final edits (PDF + LaTeX) |
|:--|:--|:--|
| [VVUQ-01](../VVUQ-01) | Method paper | [10.5281/zenodo.20372501](https://doi.org/10.5281/zenodo.20372501) |
| [VVUQ-02](../VVUQ-02) | Humanoid VVUQ paper | [10.5281/zenodo.20421754](https://doi.org/10.5281/zenodo.20421754) |
| [VVUQ-03](../VVUQ-03) | H. R. 9510 bill | [10.5281/zenodo.20454870](https://doi.org/10.5281/zenodo.20454870) |
| VVUQ-04 (this work) | FD&C Act amendment | [10.5281/zenodo.20485580](https://doi.org/10.5281/zenodo.20485580) |

## Responsible use

This is an independent research draft of a bill, not an enacted law and not legal
advice; it is not endorsed by the FDA, HHS, the OLRC, CFR, ICH, or any member of
Congress. The reproduced statutory text is in the public domain; the generated
framing is released under CC BY 4.0. The emerging 119th Congress bills and
executive actions appear only as research influences in Appendix A and are never
cited as the basis of an operative clause. All supporting numbers are simulation
results, and the Unitree H2-Surgical 1.0 is a clearly labeled hypothetical 2030
platform.

## License

Generated text is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0). Reproduced United States Code statutory text is
in the public domain.
