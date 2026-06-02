# VVUQ-01: Two Stage VVUQ Oncology Clinical Trial Verification Automation

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20331505-blue.svg)](https://doi.org/10.5281/zenodo.20331505)
[![Releases](https://img.shields.io/badge/Releases-v0.1.0%20to%20v0.6.0-brightgreen.svg)](../../releases.md)
[![Tests](https://img.shields.io/badge/pytest-51%20passed%2C%200%20skipped-brightgreen.svg)](execution/)
[![Gate surface](https://img.shields.io/badge/VVUQ%20gate-1%20ACCEPT%20%7C%205%20BLOCK%20%7C%201%20ESCALATE-red.svg)](execution/03-vvuq/)
[![Figures](https://img.shields.io/badge/Figures-10%20rendered%20at%20300%20dpi-9cf.svg)](imagegen/)
[![Authored](https://img.shields.io/badge/Authored-Claude%20Code%20Opus%204.7%20(1M)%20Max-purple.svg)](https://www.anthropic.com/claude)

### Please see Zenodo for author final edits: PDF and LaTeX [Source Files](https://doi.org/10.5281/zenodo.20372501)

VVUQ-01 is the first work in the [papers](../) series and establishes the
governing thesis of the whole directory: the large language model VVUQ process
must be held to a higher standard than the code generation it checks. It pairs a
method paper, *Two Stage VVUQ Oncology Clinical Trial Verification Automation
Priority over Existing Generated Code*, with a working pipeline and a complete,
honest execution record. This README focuses only on the VVUQ-01 directory.

> **Thesis.** The LLM VVUQ process needs to be more substantial than the
> automated code generation itself, as well as subsequent code execution, chart
> generation, and paper generation. This workflow helps ensure faster, less
> expensive, and more rigorous Physical AI oncology clinical trials than
> conventional verification methods.

## Table of Contents

- [Verification developments and progress](#verification-developments-and-progress)
- [Building process within the work](#building-process-within-the-work)
- [The two-stage verification design](#the-two-stage-verification-design)
- [Results and what they mean for the industry](#results-and-what-they-mean-for-the-industry)
- [The processing feat accomplished by AI](#the-processing-feat-accomplished-by-ai)
- [Accelerated timeline versus conventional methods](#accelerated-timeline-versus-conventional-methods)
- [Repository structure](#repository-structure)
- [Related VVUQ works and final DOIs](#related-vvuq-works-and-final-dois)
- [Responsible use](#responsible-use)
- [License](#license)

## Verification developments and progress

VVUQ-01 advanced over six releases, each a discrete development that raised the
assurance the work could demonstrate. The verification idea matures from a gate
in code, to a recorded gate decision surface, to a figure-specification analog of
the gate, and finally to a manuscript that argues the thesis from the recorded
evidence.

| Release | Stage | VVUQ verification development |
|:--|:--|:--|
| v0.1.0 | Platform | The VVUQ gate is built stricter than code generation: verification, validation across a reference, and uncertainty across three runs, with thresholds in config and escalation to a human |
| v0.2.0 | Execution | The gate is exercised on real runs: 15 example scripts to exit 0, 51 of 51 tests passed, lint and format clean, and the gate decision surface recorded (1 ACCEPT, 5 BLOCK, 1 ESCALATE) |
| v0.3.0 | Image instructions | The full figure specification is written before any pixel, the image-generation analog of writing the assurance spec before the deliverable |
| v0.4.0 | Imagegen | Ten figures are rendered from the specification with no manual positioning, so the figures inherit the gate discipline |
| v0.5.0 | Draft paper | A compilable LaTeX scaffold separates final files from bracketed instruction files, the paper-generation analog of the gate |
| v0.6.0 | Full paper | The scaffold is processed into a finished, roughly 70-page manuscript that argues verification before generation from the recorded evidence |

## Building process within the work

VVUQ-01 is built in a straight line from ingested sources to the finished paper.
Each stage consumes the prior stage's output, and the VVUQ gate sits across the
whole flow.

```
  inputs/                  execution/                image-instruct/   imagegen/
  (ingested sources)       (run the v0.1.0 code)     (10 figure specs) (10 figures)
  +----------------+       +------------------+      +------------+    +------------+
  | Paper-VVUQ-1   |       | 01-foundation    |      | NN-name/   |    | NN-name/   |
  | Paper-VVUQ-2   |  ->   | 02-pipeline      |  ->  | README.md  | -> | NN.py +    |
  | VVUQ-Research-1|       | 03-vvuq          |      | full spec  |    | NN.png     |
  | VVUQ-Research-2|       | 04-stage1-autom. |      | (no pixels |    | 300 dpi,   |
  | templates/T_10 |       | 05-physical-ai-2 |      |  yet)      |    | no manual  |
  +----------------+       +------------------+      +------------+    +------------+
         |                          | 51 tests, gate surface, PDAC pilot      |
         |                          v                                         v
         |                 draft-paper/  (v0.5.0)             full-paper/  (v0.6.0)
         |                 +----------------------+           +----------------------+
         +---------------> | FINAL  main.tex,     |   ===>    | CARRIED OVER + seven |
         specification     |        new_paper.sty,|  process  |   body sections      |
         ahead of prose    |        references.bib|  +ground  |   WRITTEN IN FULL:   |
                           | INSTRUCT 7 sections  |           |   18 tables, figures |
                           +----------------------+           +----------------------+
                                                                          |
                                                                          v
                                                               final-paper/  (Zenodo)
                                                             DOI 10.5281/zenodo.20372501
```

The execution record itself is staged into five numbered sections, mirroring the
five established methods plus the two-stage roadmap:

```
  01 foundation     environment, determinism, 51 tests, lint and format clean
        |
  02 pipeline       the five methods: instruction -> code -> execution -> paper
        |
  03 vvuq           the gate decision surface: 1 ACCEPT, 5 BLOCK, 1 ESCALATE
        |
  04 stage1-autom.  triple simulation, ingestion, chunking, scheduler
        |
  05 physical-ai-2  the 2030 PDAC 60-second Whipple pilot and lights-off safety
```

## The two-stage verification design

The manuscript is "two stage" because verification is shown across the
near-to-mid-term automation stage and the mid-to-long-term physical deployment
stage, with the gate held higher than generation in both.

```
  Stage 1 (automation and assurance)         Stage 2 (physical AI deployment)
  +-----------------------------------+      +-----------------------------------+
  | VVUQ stricter than code gen       |      | code runs physical AI in          |
  | triple simulation with consensus  |  ->  |   lights-off factories            |
  | robust ingestion, autochunking    |      | hybrid surgery and medicine, the  |
  | non-stop commit scheduling        |      |   2030 PDAC 60-second Whipple     |
  +-----------------------------------+      +-----------------------------------+
  verify before you ship                     verify before you operate
```

## Results and what they mean for the industry

The execution record turns the thesis into a decision-bearing result: code is
generated and compiled cheaply, but clearing a candidate for ship requires the
full gate. The recorded surface is 1 ACCEPT, 5 BLOCK, and 1 ESCALATE, the
schedule acceleration is 2.5x (about 30 days down to 12), and the Stage 2 pilot
reference is the 168-day 2030 PDAC 60-second Whipple program.

For the new Physical AI oncology trial industry this matters because it shows the
assurance argument can be made the substantial, decision-bearing part of an
automated workflow rather than an afterthought. When the gate, not the generator,
decides what ships, an inexpensive automated run can stand as a credible building
block for a trial: the failures are caught and recorded, the acceleration is
real, and the path from a verified capability to a deployment pilot is explicit.
VVUQ-01 is the reference that the later works (VVUQ-02 codegen and execution,
VVUQ-03 and VVUQ-04 bills) cite as the proof that LLMs are appropriate for VVUQ
code verification.

## The processing feat accomplished by AI

Claude Code Opus 4.7 (1M) Max authored VVUQ-01 autonomously in a managed,
ephemeral cloud container, pushing each file in real time across commits in
single pull requests.

- **Executed an entire codebase and recorded it honestly:** 15 example scripts to
  exit 0, 51 of 51 tests passed with zero skipped, the lint-and-format surface
  clean, and an honest limitations section.
- **Specified then rendered 10 figures:** each figure fully specified before any
  pixel, then rendered as a self-contained matplotlib script at portrait, full
  size, 300 dpi on a white background with no manual positioning.
- **Wrote a roughly 70-page manuscript from a scaffold:** seven bracketed body
  sections were processed into grounded prose with 18 body-width tables, four
  placed figures, and 29 references, without modifying the final scaffold files.
- **Kept the CI green:** the additions are LaTeX, Markdown, and a zip, all outside
  the ruff, yamllint, and pytest surface, so lint-and-format passed across Python
  3.10, 3.11, and 3.12.

## Accelerated timeline versus conventional methods

VVUQ-01's end goal is the final paper. It was reached over roughly five days
(v0.1.0 on 2026-05-21 to v0.6.0 on 2026-05-25), versus the months a conventional
methodology paper with its own verified codebase, execution evidence, and figure
program would take.

```
  Conventional path (months)                 VVUQ-01 (about 5 days)
  +-----------------------------------+      +-----------------------------------+
  | build + verify the codebase       |      | v0.1.0 platform + gate            |
  | run + document the evidence       |  vs  | v0.2.0 execution (51 tests)       |
  | design + draw the figures         |      | v0.3.0 + v0.4.0 figures (10)      |
  | draft + revise the manuscript     |      | v0.5.0 + v0.6.0 paper (70 pages)  |
  +-----------------------------------+      +-----------------------------------+
  serial, multi-month effort                 autonomous, real-time commits
```

## Repository structure

```
papers/VVUQ-01/
  README.md          (this file)
  inputs/            ingested source paper and research chunks
    Paper-VVUQ-1/  Paper-VVUQ-2/  VVUQ-Research-1/  VVUQ-Research-2/
  paper-instruct/    instruction lineage
  templates/         Template_10 LaTeX manuscript template
  execution/         v0.2.0 execution record (index, badges, ASCII, limitations)
    01-foundation/   environment, tests (51 passed), lint and format
    02-pipeline/     the five established methods, generated artifacts
    03-vvuq/         gate decision surface (1 ACCEPT, 5 BLOCK, 1 ESCALATE)
    04-stage1-automation/   simulation, ingestion, chunking, scheduler
    05-physical-ai-stage2/  2030 PDAC pilot and lights-off safety surface
  image-instruct/    v0.3.0 ten figure specifications + master README
  imagegen/          v0.4.0 ten rendered figures (scripts + 300 dpi PNGs)
  draft-paper/       v0.5.0 LaTeX scaffold (final files + 7 bracketed sections)
  full-paper/        v0.6.0 finished manuscript (18 tables, figures, 29 refs)
  final-paper/       author-finalized manuscript (PDF + LaTeX on Zenodo)
```

## Related VVUQ works and final DOIs

VVUQ-01 is the first link in the chain; the later works build on its recorded
evidence. The final paper and bill DOI for each work in the series:

| Work | Final artifact | Author final edits (PDF + LaTeX) |
|:--|:--|:--|
| VVUQ-01 (this work) | Method paper | [10.5281/zenodo.20372501](https://doi.org/10.5281/zenodo.20372501) |
| [VVUQ-02](../VVUQ-02) | Humanoid VVUQ paper | [10.5281/zenodo.20421754](https://doi.org/10.5281/zenodo.20421754) |
| [VVUQ-03](../VVUQ-03) | H. R. 9510 bill | [10.5281/zenodo.20454870](https://doi.org/10.5281/zenodo.20454870) |
| [VVUQ-04](../VVUQ-04) | FD&C Act amendment | [10.5281/zenodo.20485580](https://doi.org/10.5281/zenodo.20485580) |

## Responsible use

Generated instructions, code, figures, and text are drafts. A VVUQ gate and a
human reviewer must clear any deliverable before clinical use. The Stage 2
references (the lights-off factory and the hybrid surgery and medicine pilot)
require VVUQ clearance, human oversight, IRB approval, and regulatory
authorization before any real use. Mentions of the FDA and other bodies are
respectful and forward looking; nothing here is endorsed by any regulator.

## License

Generated text and diagrams are distributed under the Creative Commons
Attribution 4.0 International License (CC BY 4.0).
