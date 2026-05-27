# VVUQ-02 draft-paper

LaTeX draft manuscript scaffold for **10 Mobile Pancreatic Cancer Unitree H2
Surgical Humanoids: VVUQ Processing Priority over Code Generation**, built from the
Template_04 regulatory and FDA submission scaffold at
`papers/VVUQ-02/templates/Template_04/`.

This bundle is a **head start, not a finished paper**. Every section body is a
`[bracketed instruction]` that names the exact repository files a future Claude
Code Opus 4.7 (1M context) Max pass must read and synthesise into
publication-quality prose. The references are already final. The five figure
floats, their one-line captions, their labels, and their `\autoref` targets are
already placed; the author drops the rendered PNGs into `Images/` later.

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![Template](https://img.shields.io/badge/Template-04%20regulatory%20fda-blue.svg)](../templates/Template_04/)
[![Standard](https://img.shields.io/badge/Standard-ASME%20V%26V%2040--2018-orange.svg)](https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices)
[![Gates](https://img.shields.io/badge/VVUQ%20Gates-10-red.svg)](../codegen/docs/vvuq_gate_spec.md)

## Thesis

The robotic code assurance process, not code generation, is the substantial and
decision-bearing part of the AI workflow, holding VVUQ to a higher standard than
code itself. These safety measures will ensure upcoming physical AI oncology trial
developments are faster, less expensive, and more beneficial towards patients than
conventional verifications.

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
  imagegen/                         (15 figure scripts + PNGs)
            |
            v
  draft-paper/   <=== THIS BUNDLE   (scaffold + bracketed build instructions)
            |
            v
  full-paper/ and final-paper/      (future 70+ page manuscript)
```

## File layout

```
draft-paper/
  README.md            (this file)
  main.tex             (preamble, title page, TOC, \input lines, format directives)
  new_paper.sty        (Palatino + navy style, unchanged from the template family)
  references.bib       (FINAL polished bibliography; DOIs + URLs; ieeetr)
  sections/
    abstract.tex
    introduction.tex
    methods.tex
    results.tex
    discussion.tex
    limitations_future.tex
    conclusions.tex
    back_matter.tex    (Acknowledgments, Ethics, Rights, Cite, Data Availability)
  Images/              (author drops the five rendered PNGs here later)
  prompt-draft-paper.md
  output-draft-paper.md
```

## Compile recipe (Overleaf)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Until the five PNGs are present in `Images/`, each figure float renders a labelled
placeholder box (via `\IfFileExists`), so the draft compiles cleanly now and again
once the images are added.

## Section to source-file map (what the future pass must read)

Long paths are given once here; the prose should keep them in tables, not inline.

| Section | Primary source files (under `papers/VVUQ-02/`) |
|:--|:--|
| Abstract | `execution/README.md` (key-results table); `execution/03-vvuq/README.md` |
| Introduction | `codegen/README.md`; `codegen/docs/vvuq_methodology.md`; `../VVUQ-01/final-paper/` |
| Methods | `execution/01-foundation/environment-and-verification.md`; `codegen/config/`; `inputs/standards/manifest.yaml`; `execution/02-pipeline/README.md` |
| Results | `execution/03-vvuq/`; `execution/04-automation/`; `codegen/results/comparison.json`; `codegen/data/sample_h2_sensor.csv`; `execution/05-humanoid-deployment/` |
| Discussion | `codegen/tests/`; `execution/01-foundation/test-suite.md`; `codegen/config/standards_map.yaml`; `execution/README.md` (cost section) |
| Limitations | `execution/README.md` (limitations section) |
| Conclusions | `execution/README.md` (headline finding) |
| References | `references.bib` (already final) |

## Figures (five placeholders, author adds PNGs)

Each label is referenced from the body with `\autoref`. Copy the PNG from the
`imagegen` script's directory into `Images/` under the same leaf name.

| Label | Section | Image file (place in `Images/`) | Render script directory |
|:--|:--|:--|:--|
| `fig:wheel` | Methods | `05-clinical-regulatory-standards-wheel.png` | `imagegen/05-clinical-regulatory-standards-wheel/` |
| `fig:forest` | Results | `03-ten-gate-threshold-forest.png` | `imagegen/03-ten-gate-threshold-forest/` |
| `fig:bands` | Results | `11-sensor-stream-safety-bands.png` | `imagegen/11-sensor-stream-safety-bands/` |
| `fig:matrix` | Discussion | `04-gate-standard-binding-matrix.png` | `imagegen/04-gate-standard-binding-matrix/` |
| `fig:cost` | Discussion | `13-assurance-cost-assessment.png` | `imagegen/13-assurance-cost-assessment/` |

## Production and formatting rules (senior-author finishing pass)

- Target a finished 70+ page manuscript; give each section comprehensive context,
  not filler.
- Prose reads as a top human author wrote it: connect ideas across sections, do not
  restate what a table or figure already shows, and reference tables and figures
  with `\autoref`.
- Tables carry the dense facts. Abbreviate long file names in cells and put the
  common parent path once near the top of the table.
- Every table column uses a left-aligned fixed width:
  `{>{\raggedright\arraybackslash}p{2cm}}`. Prepend `\raggedright\arraybackslash`
  to every `p{}` width so cells have even word spacing.
- Avoid large empty white bands. Where justification opens large inter-word gaps,
  tune spacing (`\sloppy`, `\emergencystretch`, `microtype`, or a local
  `\RaggedRight`) so words are evenly spaced and no line runs off the right margin.
- No orphan single lines at the top or bottom of a page, and no lines of one or two
  words. Keep the widow and club penalties at 10000.
- Use the section symbol `§` for clause references; never write `SS`.
- Single hyphens only; no em dashes, en dashes, double, or triple dashes.
- Keep the navy accent and Palatino body; do not restyle the headings or title.

## References policy

`references.bib` is final and must not lose detail. DOI numbers and their resolver
URLs both appear in the rendered bibliography (the `note` field carries them, and
`ieeetr` prints `note`). Repository entries carry the GitHub and the Zenodo link,
each once, with no duplicate link inside an entry, and no `howpublished` field
anywhere. Both the paper DOI and the repository DOI resolve as clickable links.
`\nocite{*}` in `main.tex` guarantees all 20+ entries render in the draft; the
future pass should additionally place inline `\cite` calls in the body.

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
