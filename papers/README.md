# Papers: VVUQ Verification Developments for Physical AI Oncology Trials

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![VVUQ-01 Paper DOI](https://img.shields.io/badge/VVUQ--01%20Paper%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![VVUQ-02 Paper DOI](https://img.shields.io/badge/VVUQ--02%20Paper%20DOI-10.5281%2Fzenodo.20421754-blue.svg)](https://doi.org/10.5281/zenodo.20421754)
[![VVUQ-03 Bill DOI](https://img.shields.io/badge/VVUQ--03%20Bill%20DOI-10.5281%2Fzenodo.20454870-blue.svg)](https://doi.org/10.5281/zenodo.20454870)
[![VVUQ-04 Bill DOI](https://img.shields.io/badge/VVUQ--04%20Bill%20DOI-10.5281%2Fzenodo.20485580-blue.svg)](https://doi.org/10.5281/zenodo.20485580)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Bill](https://img.shields.io/badge/Bill-H.%20R.%209510%20(119th%2C%202d%20Sess.)-darkblue.svg)](https://www.congress.gov/browse/119th-congress)
[![Authored](https://img.shields.io/badge/Authored-Claude%20Code%20Opus%204.7%20%2F%204.8%20(1M)%20Max-purple.svg)](https://www.anthropic.com/claude)

This directory holds the four sequential VVUQ works that carry a single thesis
from a method, to a hard engineering proof, to a manuscript, and finally to a
ready-to-introduce United States bill. Each work is built on the one before it.
Together they are a reproducible **evidence to law** pipeline for the new
Physical AI oncology trial industry, where the central principle is
**verification before generation**: an automated verification, validation, and
uncertainty quantification (VVUQ) process, held to a higher standard than code
generation, must clear robot-patient interaction code before that code is
generated or executed.

> **Thesis carried across all four works.** The large language model VVUQ
> process needs to be more substantial than automated code generation itself, as
> well as subsequent execution, chart generation, and paper generation. This
> workflow makes Physical AI oncology clinical trials faster, less expensive, and
> more rigorous than conventional verification methods.

Every deliverable in this directory was authored autonomously by Claude Code
Opus 4.7 and 4.8 (1M context) Max running in managed, ephemeral cloud
containers, across sequential commits in single pull requests, one file per
commit pushed to GitHub in real time. The generated instructions, code, figures,
papers, and bills are drafts: a VVUQ gate and a human reviewer must clear any
deliverable before clinical or legal use.

## Final Papers and Bills on Zenodo (the four end goals)

Each work culminates in an author-finalized PDF and LaTeX source bundle on
Zenodo. The end-goal DOI for each of the four works is below, organized so the
final artifact of every work resolves in one place.

| Work | Final artifact | Author final edits (PDF + LaTeX) |
|:--|:--|:--|
| [VVUQ-01](VVUQ-01) | *Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over Existing Generated Code* | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20372501) |
| [VVUQ-02](VVUQ-02) | *Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ* | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20421754) |
| [VVUQ-03](VVUQ-03) | *VVUQ Physical AI Oncology Trial Bill* (H. R. 9510) | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20454870) |
| [VVUQ-04](VVUQ-04) | *Verification Before Generation in Physical AI Oncology Trials Act of 2026* (H. R. 9510; FD&C Act amendment) | Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20485580) |

## Table of Contents

- [The four works at a glance](#the-four-works-at-a-glance)
- [Building process from one work to the next](#building-process-from-one-work-to-the-next)
- [VVUQ-01: establishing the verification thesis](#vvuq-01-establishing-the-verification-thesis)
- [VVUQ-02: proving VVUQ on the hardest subject](#vvuq-02-proving-vvuq-on-the-hardest-subject)
- [VVUQ-03: turning recorded evidence into proposed law](#vvuq-03-turning-recorded-evidence-into-proposed-law)
- [VVUQ-04: a precise, current FD&C Act amendment](#vvuq-04-a-precise-current-fdc-act-amendment)
- [What the results mean for the Physical AI oncology trial industry](#what-the-results-mean-for-the-physical-ai-oncology-trial-industry)
- [The processing feat accomplished by AI](#the-processing-feat-accomplished-by-ai)
- [Accelerated timeline versus conventional methods](#accelerated-timeline-versus-conventional-methods)
- [Repository structure](#repository-structure)
- [Responsible use](#responsible-use)
- [License](#license)

## The four works at a glance

| Work | What it is | Releases | Headline assurance result | End-goal DOI |
|:--|:--|:--|:--|:--|
| VVUQ-01 | Method paper plus the working pipeline and an execution record that hold VVUQ higher than code generation | v0.1.0 to v0.6.0 | 51 of 51 tests; 1 ACCEPT, 5 BLOCK, 1 ESCALATE gate surface; 2.5x acceleration | [20372501](https://doi.org/10.5281/zenodo.20372501) |
| VVUQ-02 | A generated 10-gate humanoid surgical codebase, its autonomous execution record, and the manuscript built from them | v0.7.0 to v1.2.0 | 172 of 172 tests; 10 gates; 32 of 32 sweep iterations clear; composite mean 93.56 | [20421754](https://doi.org/10.5281/zenodo.20421754) |
| VVUQ-03 | The *VVUQ Physical AI Oncology Trial Bill* (H. R. 9510), synthesized from the recorded evidence | v1.3.0 to v1.4.0 | 15 sections; 21 body-width tables; 60 references; verification before generation as statute | [20454870](https://doi.org/10.5281/zenodo.20454870) |
| VVUQ-04 | The bill recast as a precise amendment to the Federal Food, Drug, and Cosmetic Act, current through Public Law 119-93 | v2.0.0 to v2.3.0 | New § 360e-5 plus 10 conforming amendments; legal crosswalk current to May 31, 2026 | [20485580](https://doi.org/10.5281/zenodo.20485580) |

## Building process from one work to the next

The four works are a deliberate chain: each one consumes the recorded artifacts
of the prior work as grounding and raises the assurance bar. VVUQ-01 establishes
the principle; VVUQ-02 proves it on the hardest subject (one autonomous
humanoid); VVUQ-03 turns the recorded evidence into a proposed law; and VVUQ-04
makes that law precise and current as a targeted FD&C Act amendment.

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

The same five established methods run inside every work: instruction generation,
code generation, code execution, figure generation, and paper assembly, with the
VVUQ gate sitting across the whole flow so a deliverable ships only once it is
verified, validated, and within its uncertainty budget.

```
  instructions  ->  code/text  ->  execution  ->  figures  ->  paper/bill
       |               |               |             |             |
       +---------------+------ VVUQ gate (stricter than generation) ----+
                               ACCEPT  /  BLOCK  /  ESCALATE to human
```

## VVUQ-01: establishing the verification thesis

[VVUQ-01](VVUQ-01) establishes that the LLM VVUQ process must be held to a
higher standard than the code generation it checks. It pairs a method paper,
*Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over
Existing Generated Code*, with the working pipeline (instruction, code,
execution, paper) and a complete execution record. The execution leg runs all 15
example scripts to exit 0, passes 51 of 51 tests with zero skipped, keeps the
lint-and-format surface clean, and reports the full VVUQ gate decision surface (1
ACCEPT, 5 BLOCK, 1 ESCALATE) along with a 2.5x schedule acceleration and the
2030 PDAC 60-second Whipple pilot reference. Ten publication figures are
specified before any pixel is rendered (the image-generation analog of the gate)
and then rendered as self-contained matplotlib scripts, before the draft
scaffold is processed into a full, 70-page manuscript with 18 tables and 29
references.

- **Developments and progress:** v0.1.0 platform; v0.2.0 execution; v0.3.0 image
  instructions; v0.4.0 rendered figures; v0.5.0 draft scaffold; v0.6.0 full
  paper.
- **End goal (final paper):** Please see Zenodo for author final edits: PDF and
  LaTeX [Source Files](https://doi.org/10.5281/zenodo.20372501).

## VVUQ-02: proving VVUQ on the hardest subject

[VVUQ-02](VVUQ-02) applies the thesis to the hardest subject available: a single
autonomous humanoid surgeon (a clearly labeled hypothetical 2030 Unitree
H2-Surgical 1.0) that performs the 60-second 8-phase Whipple with its own two
hands and no teleoperation. Because one body concentrates all error potential,
the assurance layer must be more substantial than the control code, and a
candidate behavior must clear 10 humanoid-specific gates bound to external
standards (ASME V&V 40, IEC 80601-2-77, ISO 13482, ISO/TS 15066, and more)
before it ships. Claude generated the standalone codebase (v0.7.0), executed the
whole tree (v0.8.0, 172 of 172 tests, byte-identical determinism from seed
20260525, a 32 of 32 iteration sweep at composite mean 93.56), specified and
rendered 15 figures (v0.9.0 and v1.0.0), then processed the draft scaffold
(v1.1.0) into the full manuscript (v1.2.0).

- **Developments and progress:** v0.7.0 codegen; v0.8.0 execution; v0.9.0 image
  instructions; v1.0.0 imagegen; v1.1.0 draft paper; v1.2.0 full paper.
- **End goal (final paper):** Please see Zenodo for author final edits: PDF and
  LaTeX [Source Files](https://doi.org/10.5281/zenodo.20421754).

## VVUQ-03: turning recorded evidence into proposed law

[VVUQ-03](VVUQ-03) converts the recorded technical evidence of VVUQ-01 and
VVUQ-02 (plus the national-platform paper and the USL and PSL standards) into a
proposed United States bill: the *VVUQ Physical AI Oncology Trial Bill*,
designated **H. R. 9510** (119th Congress, 2d Session). It is built from a
template-paper that adapts the structure of 21 CFR Part 312, with instruction
generation drawing on multiple AI models, and a draft scaffold of bracketed
instructions processed into a finished bill of 15 sections and 21 body-width
tables grounded in the 1790-line `comparison.json` and 1001-row sensor stream.
The Draft Statutory Text codifies verification before generation, the ten-gate
threshold schedule bound to the external standards, and the PSL and USL readiness
gates.

- **Developments and progress:** v1.3.0 draft paper (bill scaffold); v1.4.0 full
  paper (finished H. R. 9510 bill).
- **End goal (final paper):** Please see Zenodo for author final edits: PDF and
  LaTeX [Source Files](https://doi.org/10.5281/zenodo.20454870).

## VVUQ-04: a precise, current FD&C Act amendment

[VVUQ-04](VVUQ-04) makes the bill precise and current. It recasts H. R. 9510 as
a properly targeted amendment to the Federal Food, Drug, and Cosmetic Act (21
U.S.C. § 301 et seq.), current through Public Law 119-93, with the short title
*Verification Before Generation in Physical AI Oncology Trials Act of 2026*. A
research head start (instruct-bill: 10 markdown summaries plus 5 BibTeX files,
145 entries, current through May 31, 2026) and a faithful LaTeX reproduction of
the 11 relevant Title 21 device sections (template-bill) feed a draft amendment
scaffold (draft-bill), which is processed into the finished amendment (full-bill).
The operative mechanism is a new section 515D of the Act (21 U.S.C. § 360e-5),
inserted after the predetermined change control plan keystone (§ 360e-4), with
ten conforming amendments threaded through the surrounding device provisions and a
focused comparative print of the changes in existing law.

- **Developments and progress:** v2.0.0 instruct bill; v2.1.0 template bill;
  v2.2.0 draft bill; v2.3.0 full bill.
- **End goal (final bill):** Please see Zenodo for author final edits: PDF and
  LaTeX [Source Files](https://doi.org/10.5281/zenodo.20485580).

## What the results mean for the Physical AI oncology trial industry

The four works, taken together, stand up the scaffolding for a new industry in
which autonomous and semi-autonomous robots participate in oncology clinical
trials under a defensible assurance regime.

- **A governing principle with a working reference.** Verification before
  generation is shown to be implementable end to end: a candidate behavior is
  generated and compiled in microseconds, but clearing one for ship requires a
  full verification fraction, an agreement bar, a coefficient-of-variation bound,
  a recorded human review, and a hard predicate on each catastrophe gate.
- **External-standards anchoring makes credibility defensible.** Every gate,
  behavior, and safety surface is traced to a published standard already used in
  practice, so an inexpensive autonomous run can stand as credible evidence for a
  future trial rather than as an ad hoc demonstration.
- **An evidence to law pipeline.** The same recorded artifacts that argue
  technical credibility (tests, sweeps, the featured comparison and sensor
  records) become the evidentiary basis for proposed statute, then for a precise
  amendment that lawmakers and counsel can act on. The chain shortens the
  distance between a verified capability and the law that would govern it.
- **A template others can reuse.** The directory is a repeatable pattern: ingest
  the law and the prior evidence, generate and execute the code, render the
  figures, write the manuscript, and draft the statute, all with the CI green and
  the provenance recorded.

## The processing feat accomplished by AI

The full directory was produced autonomously by Claude Code Opus 4.7 and 4.8 (1M
context) Max in managed, ephemeral cloud containers, with each file pushed in
real time across sequential commits in single pull requests.

- **A complete, standalone codebase, generated and executed.** Eleven module
  families implement 10 humanoid-specific VVUQ gates; 172 tests pass with zero
  skipped; the three large artifacts (the 1790-line four-entrant
  `comparison.json` and the 1000-row, 27-column sensor stream among them)
  reproduce byte for byte from seed 20260525.
- **Twenty-five publication figures, specified before rendering.** Ten figures in
  VVUQ-01 and 15 in VVUQ-02 are each fully specified ahead of any pixel, then
  rendered as self-contained matplotlib scripts on a white background with no
  manual positioning, with the arithmetic reconciled to the source records.
- **Four publication-grade LaTeX documents.** Two manuscripts and two
  legislative instruments, each built from a bracketed scaffold into finished
  prose with body-width tables, clickable DOIs, and no images.
- **Statute processed at scale.** A 12.4 MB Title 21 USLM XML corpus is reduced
  from 29 chapters and 757 sections to the 11 device sections that matter, then
  reproduced in the United States Code look and feel and amended with a new
  section and ten conforming amendments.
- **Multiple models in the loop.** Instruction generation drew on rated outputs
  from Claude Haiku 4.5, ChatGPT 5.5 Thinking Extended, and Gemini 3.1 Pro
  (see `VVUQ-03/instruct-paper` and `VVUQ-04/update-bill`), which is why the
  contributor set spans several model families.
- **CI stayed green throughout.** Every addition is LaTeX, Markdown, BibTeX, or a
  zip, all outside the ruff, yamllint, and pytest surface, so lint-and-format
  passed across Python 3.10, 3.11, and 3.12 on every pull request.

## Accelerated timeline versus conventional methods

The entire arc, from the initial automation platform to the finished FD&C Act
amendment, ran from 2026-05-21 to 2026-06-01, roughly eleven days.

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

Conventionally, each step is its own multi-month project: a methodology paper,
a regulated robotics codebase with traceability to external standards, a
peer-style manuscript, and a federal bill drafted as a section-by-section FD&C
Act amendment with legal counsel. Running them serially is measured in months to
years. Here the same chain was produced in days, with provenance recorded and the
CI green, and it reaches the final VVUQ-04 Bill (H. R. 9510, the new § 360e-5)
in about eleven days from the platform's first commit.

## Repository structure

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

## Responsible use

Everything here is an independent research draft. The papers and bills are not
enacted law and are not legal advice; they are not endorsed by the FDA, HHS, the
OLRC, CFR, ICH, or any member of Congress. The Unitree H2-Surgical 1.0 is a
clearly labeled hypothetical 2030 platform, and every supporting number is a
simulation result. Generated instructions, code, figures, and text are drafts: a
VVUQ gate and a human reviewer must clear any deliverable, and a real deployment
would require the cited external standards, IRB approval, and regulatory
authorization. Mentions of the FDA and other bodies are respectful and forward
looking.

## License

Generated text and diagrams are distributed under the Creative Commons
Attribution 4.0 International License (CC BY 4.0). Reproduced United States Code
statutory text is in the public domain.
