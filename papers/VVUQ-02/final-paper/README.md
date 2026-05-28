# VVUQ-02 full-paper

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.20421754-blue.svg)](https://doi.org/10.5281/zenodo.20421754)
[![Paper DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![Template](https://img.shields.io/badge/Template-04%20regulatory%20fda-blue.svg)](../templates/Template_04/)
[![Standard](https://img.shields.io/badge/Standard-ASME%20V%26V%2040--2018-orange.svg)](https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices)
[![Gates](https://img.shields.io/badge/VVUQ%20Gates-10-red.svg)](../codegen/docs/vvuq_gate_spec.md)
[![Tests](https://img.shields.io/badge/pytest-172%20passed-brightgreen.svg)](../execution/01-foundation/test-suite.md)
[![Standards corpus](https://img.shields.io/badge/Standards-14%20%2B%202%20clinical-9cf.svg)](../inputs/standards/manifest.yaml)

[Full PDF and LaTeX Source Files](https://doi.org/10.5281/zenodo.20421754) are available on Zenodo. Overleaf-compilable LaTeX manuscript for **Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ**,
processed from the bracketed scaffold in `papers/VVUQ-02/draft-paper/`.

Every section now carries finished publication prose and left-aligned,
body-width tables synthesised from the repository records under
`papers/VVUQ-02/` (the wired `inputs/` standards corpus, the `codegen/`
platform, and the five-section `execution/` record). The five figure floats keep
their labels and `\autoref` targets; the author drops the rendered PNGs from
`papers/VVUQ-02/imagegen/` into `Images/` later, and a labelled placeholder
renders until then so the bundle always compiles.

## Thesis

The robotic code assurance process, not code generation, is the substantial and
decision-bearing part of the AI workflow, holding VVUQ to a higher standard than
code itself. These safety measures will ensure upcoming physical AI oncology
trial developments are faster, less expensive, and more beneficial towards
patients than conventional verifications.

## Position in the lineage

```
  instructions/output-instruct.md   (specification, zero code)
            |
            v
  codegen/                          (generated codebase, v0.1.0)
            |
            v
  execution/                        (autonomous execution record, 5 sections)
            |
            v
  imagegen/                         (figure scripts + PNGs)
            |
            v
  draft-paper/                      (scaffold + bracketed build instructions)
            |
            v
  full-paper/   <=== THIS BUNDLE    (processed manuscript, finished prose)
            |
            v
  final-paper/                      (future submission-ready manuscript)
```

## File layout

```
full-paper/
  README.md             (this file)
  main.tex              (preamble, title page, abstract, TOC, \input lines)
  new_paper.sty         (Palatino + navy style, unchanged from the draft)
  references.bib        (FINAL ieeetr bibliography; DOIs + URLs in notes)
  full-paper.zip        (the complete LaTeX bundle for Overleaf upload)
  prompt-full-paper.md  (the generating prompt, verbatim)
  output-full-paper.md  (the narrative output of this run)
  sections/
    abstract.tex
    introduction.tex
    methods.tex
    results.tex
    discussion.tex
    limitations_future.tex
    conclusions.tex
    back_matter.tex     (Acknowledgments, Ethics, Rights, Cite, Data)
  Images/
    README.md           (author drops the five rendered PNGs here later)
```

## Compile recipe (Overleaf)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Upload `full-paper.zip` to Overleaf and set `main.tex` as the document root, or
clone the repository and compile in place. Until the five PNGs are present in
`Images/`, each figure float renders a labelled placeholder box (via
`\IfFileExists`), so the manuscript compiles cleanly with or without the images.

## Manuscript structure (assurance flow)

```
        candidate humanoid behaviors (generated, microsecond-scale)
                          |
   +----------------------v-----------------------------------------+
   | 01 bimanual-handeye-servo        06 vascular-no-fly-hand   *    |
   | 02 dexterous-finger-force        07 bimanual-suturing          |
   | 03 whole-body-balance            08 perception-scene           |
   | 04 autonomous-plan-correctness   09 shared-or-collision    *    |
   | 05 instrument-grasp-handover     10 fault-estop-degrade    *    |
   +----------------------v-----------------------------------------+
        each gate:  Verify (fraction == 1.0) -> Validate (>= agreement
                    vs an independent reference) -> Quantify (CV bound)
                    -> Evaluate (hard predicate on the catastrophe gates)
                          |
                          v
        ACCEPT (all 10 pass)  /  BLOCK (any fail)  /  ESCALATE (divergence)

   * immediate-catastrophe gates: 1.00 agreement, tightest CV bounds, plus an
     extra hard predicate; any ESCALATE defaults to hand-back-to-human.
```

## Section to source-file map

Long paths are given once here; the prose keeps them in tables, not inline.

| Section | Primary source records (under `papers/VVUQ-02/`) |
|:--|:--|
| Abstract | `execution/README.md`; `execution/03-vvuq/README.md` |
| Introduction | `codegen/README.md`; `codegen/docs/vvuq_methodology.md`; `../VVUQ-01/final-paper/` |
| Methods | `execution/01-foundation/`; `codegen/config/`; `inputs/standards/manifest.yaml`; `execution/02-pipeline/` |
| Results | `execution/03-vvuq/`; `execution/04-automation/`; `codegen/results/comparison.json`; `codegen/data/sample_h2_sensor.csv`; `execution/05-humanoid-deployment/` |
| Discussion | `codegen/tests/`; `execution/01-foundation/test-suite.md`; `codegen/config/standards_map.yaml`; `execution/README.md` |
| Limitations | `execution/README.md` (limitations and cost sections) |
| Conclusions | `execution/README.md` (headline finding) |

## Figures (five placeholders, author adds PNGs)

Each label is referenced from the body with `\autoref`. Copy the PNG from the
`imagegen` render directory into `Images/` under the same leaf name.

| Label | Section | Image leaf name | Render script directory |
|:--|:--|:--|:--|
| `fig:wheel` | Methods | `05-clinical-regulatory-standards-wheel.png` | `imagegen/05-clinical-regulatory-standards-wheel/` |
| `fig:forest` | Results | `03-ten-gate-threshold-forest.png` | `imagegen/03-ten-gate-threshold-forest/` |
| `fig:bands` | Results | `11-sensor-stream-safety-bands.png` | `imagegen/11-sensor-stream-safety-bands/` |
| `fig:matrix` | Discussion | `04-gate-standard-binding-matrix.png` | `imagegen/04-gate-standard-binding-matrix/` |
| `fig:cost` | Discussion | `13-assurance-cost-assessment.png` | `imagegen/13-assurance-cost-assessment/` |

## Headline results carried into the manuscript

| Quantity | Value |
|:--|:--|
| Automated tests passed | 172 of 172 (0 skipped) |
| Assurance share of the test budget | 64 of 172 (the 10-gate suite) |
| VVUQ decision cases exercised | 5 (10 ACCEPT, 3 BLOCK, 1 ESCALATE) |
| Tightest gate bounds (catastrophe) | agreement 1.00, rel err 0.01, CV 0.05 |
| Deterministic sweep | 32 of 32 iterations cleared all 10 gates |
| Composite across the sweep | min 93.417, max 93.715, mean 93.562 |
| Featured tournament | 4 entrants, 128 verdicts, 100% caveat coverage |
| Featured sensor stream | 1000 unique rows, 27 columns, 0 duplicates |
| Determinism | all three large artifacts reproduced from seed 20260525 |

## Four-entrant tournament leaderboard (frozen-weight composite)

The single mobile humanoid lands 2nd to the 8-arm cart on the throughput-weighted
composite, within about half a point, and is the higher-risk, higher-assurance
platform that the paper is about.

| Rank | Entrant | Composite mean | Win rate | Total wins |
|:--|:--|:--|:--|:--|
| 1 | PancreSpeed 1.0 (8-arm cart) | 93.782 | 0.875 | 56 |
| 2 | H2-Surgical 1.0 (humanoid) | 93.334 | 0.75 | 72 |
| 3 | da Vinci-successor 2030 (teleop) | 83.970 | 0.0 | 0 |
| 4 | Dutch human baseline (2025) | 67.885 | 0.0 | 0 |

Every robot-involving verdict carries the simulation-against-simulation caveat,
and every human-versus-robot round carries the structural time-dimension caveat.

## Production and formatting rules (senior-author finishing pass)

- A comprehensive manuscript: each section gives full context, not filler.
- Prose reads as a top human author wrote it: ideas connect across sections, and
  tables and figures are referenced with `\autoref` rather than narrated.
- Tables carry the dense facts; long paths appear once near the top of a table
  and body cells keep abbreviated leaf names.
- Every table is a `tabularx` set to `\textwidth`, so it matches the body
  measure exactly, and every column is left aligned and ragged right via the
  `L{}` and `Y` column types (each prepends `\raggedright\arraybackslash`).
- No large white bands or right-margin overflow; `\sloppy`, `\emergencystretch`,
  and `microtype` keep words evenly spaced.
- No orphan or widow line and no lines of one or two words; the widow and club
  penalties stay at 10000.
- The section symbol `§` is used for clause references; `SS` is never used.
- Single hyphens only; no em dashes, en dashes, double, or triple dashes.
- The navy accent and Palatino body are preserved from the draft.

## References policy

`references.bib` is final and loses no detail. DOI numbers and their resolver
URLs both appear in the rendered bibliography (the `note` field carries them, and
`ieeetr` prints `note`). Repository entries carry the GitHub and the Zenodo link
once each, with no duplicate link inside an entry, and no `howpublished` field
anywhere. Both the paper DOI and the repository DOI resolve as clickable links.
`\nocite{*}` guarantees all 41 entries render, and the body prose additionally
anchors each reference with an inline `\cite`.

## Responsible use

The Unitree H2-Surgical 1.0 is a clearly labelled hypothetical 2030 platform and
every number in the supporting records is a simulation result; the four-entrant
comparison is simulation against simulation. The ten VVUQ gates plus a recorded
human reviewer must clear any candidate before any non-simulated use, and a real
deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III
clearance, IRB approval, and regulatory authorization. Mentions of the FDA and
other bodies are respectful and non-presumptuous.

## License

Generated text and diagrams under the Creative Commons Attribution 4.0
International License (CC BY 4.0).
