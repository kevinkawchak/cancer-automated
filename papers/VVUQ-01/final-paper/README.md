# VVUQ-01 Full Paper: Two Stage VVUQ Oncology Clinical Trial Verification Automation

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Repo DOI](https://img.shields.io/badge/Repo%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../releases.md)
[![Engine](https://img.shields.io/badge/pdfLaTeX-Overleaf-success.svg)](https://www.overleaf.com/)
[![Style](https://img.shields.io/badge/Style-ieeetr%20%2B%20black%20links-lightgrey.svg)](references.bib)
[![Bibliography](https://img.shields.io/badge/References-29%20entries%2C%20DOI%20%2B%20URL-informational.svg)](references.bib)
[![Authored](https://img.shields.io/badge/Authored-Claude%20Code%20Opus%204.7%201M%20Max-purple.svg)](https://www.anthropic.com/news/claude-opus-4-7)

This directory holds the **full paper** for the manuscript *Two Stage VVUQ
Oncology Clinical Trial Verification Automation Priority over Existing Generated
Code*. It is a complete, compilable single column LaTeX project. Every body
section that carried a bracketed processing instruction in the
[draft scaffold](../draft-paper) is now written out in full: grounded,
publication grade prose, tables, and figures, targeting roughly 70 typeset
pages. The title page, the style file, the bibliography, the references block,
and the back matter follow the draft conventions without change in intent.

> The full paper is built from the draft scaffold without modifying it. The
> draft under `../draft-paper` remains the processing specification; this
> directory is the realized manuscript.

## Thesis

The LLM VVUQ process needs to be more substantial than the automated code
generation itself, as well as subsequent code execution, chart generation, and
paper generation operations. This LLM workflow helps to ensure faster, less
expensive, and more rigorous physical AI oncology clinical trials than
conventional verification methods.

## How the manuscript is built

```
  Draft scaffold (../draft-paper)             Full paper (this directory)
  +-----------------------------------+       +-----------------------------------+
  | main.tex     (title, structure)   |       | main.tex     (carried over)       |
  | new_paper.sty (layout, color)     |       | new_paper.sty (carried over)      |
  | references.bib (29 entries)       |  -->  | references.bib (carried over)     |
  | back_matter.tex (final)           |       | back_matter.tex (carried over)    |
  | seven body sections = INSTRUCTION |       | nine sections = WRITTEN IN FULL   |
  +-----------------------------------+       +-----------------------------------+
                |                                            |
                +-----------> 70 page Overleaf PDF <---------+
```

## File layout

```
full-paper/
  README.md            (this file: badges, structure, compile recipe)
  main.tex             (preamble, title page, disclaimer, keywords, TOC, \input lines)
  new_paper.sty        (single column serif style; black links, green ORCID)
  references.bib       (29 entries, ieeetr, DOI + clickable URL each)
  full-paper.zip       (Overleaf ready bundle of this project)
  Images/              (the four author supplied figures; placeholders until added)
  sections/
    abstract.tex            (<300 word overview, no citations, headline metrics)
    introduction.tex        (need, the three VVUQ dimensions, thesis, contributions)
    methods.tex             (five methods, the gate, Stage 1 and 2, per commit codegen)
    results.tex             (execution evidence, gate surface, three figures, commits)
    discussion.tex          (meaning of accept and block, server compare, one figure)
    limitations_future.tex  (honest gaps and the all-trial roadmap)
    conclusions.tex         (restated thesis and the forward path)
    references.tex          (the bibliography block)
    back_matter.tex         (acknowledgments, ethics, rights, cite, data)
```

## Section to source map

Each section is grounded in the repository directories below. Long file names
are abbreviated in the per section source tables inside the paper; full paths
live in those tables, not in the running prose.

| Section | Primary source directories (abbreviated) |
|:--------|:------------------------------------------|
| Abstract | `execution/README.md` key metrics; `pipeline/`, `vvuq/`, `physical-ai/` READMEs |
| Introduction | `vvuq/` modules; `inputs/` paper and research READMEs; `execution/README.md` thesis |
| Methods | `pipeline/`, `vvuq/`, `physical-ai/`, `configs/`, `tests/`; `execution/01-foundation/` |
| Results | `execution/02..05`; imagegen `02,04,06` `.py` data; the commit tables |
| Discussion | `execution/README.md` server comparison; imagegen `08` `.py`; prior 07-humanoid paper |
| Limitations and Future Work | `execution/README.md` limitations section |
| Conclusions | `execution/README.md` summary; the thesis |
| References | `references.bib` (final); `inputs/` BibTeX chunks |

## Figures

The paper carries four figures. Each figure environment uses a placeholder slot
that compiles immediately and is replaced automatically once the author drops
the final image into `Images/` under the matching name. Three figures support
the Results and one supports the Discussion.

| Slot | Image name in `Images/` | Grounded in (imagegen script) | Section |
|:-----|:------------------------|:------------------------------|:--------|
| Schedule acceleration waterfall | `acceleration-waterfall.png` | `02-acceleration-waterfall` | Results |
| VVUQ assurance wheel | `vvuq-assurance-wheel.png` | `04-vvuq-assurance-wheel` | Results |
| Test coverage treemap | `test-coverage-treemap.png` | `06-test-coverage-treemap` | Results |
| FDA cost efficiency bridge | `fda-cost-bridge.png` | `08-fda-cost-efficiency-bridge` | Discussion |

## Compile recipe (Overleaf, pdfLaTeX plus BibTeX)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

A `full-paper.zip` bundle of this project is provided for a one step Overleaf
upload. The project compiles as is; figure slots render as labeled placeholders
until the author adds the four images, after which the real figures render with
no further edits.

## Formatting contract

- Ragged right body, even inter-word spacing, no white rivers, and no line
  running off the right margin (knobs in `new_paper.sty`).
- No orphan or widow lines; never strand a one or two word line on its own page.
  Some white space at a page foot is acceptable.
- Single dashes only. No em dashes, no double dashes, no triple dashes. The
  section sign `§` is used where a section is referenced.
- Every table uses `>{\raggedright\arraybackslash}p{...}` columns (the `L`, `C`,
  `R` types in `main.tex`) and is sized to the body text width. Tables and
  figures are referenced in prose rather than restated.
- Body text and links render black; the ORCID mark renders ORCID green.

## Bibliography rules

`references.bib` carries 29 entries rendered with `ieeetr`. Every entry with a
DOI prints the human readable DOI string and a clickable resolver URL inside its
`note`; repository entries print both a GitHub and a Zenodo URL, each once, with
no duplicate link and no `howpublished` field. Both the repository DOI and the
paper DOI are clickable.

## Responsible use

Generated instructions, code, figures, and papers are drafts. A VVUQ gate and a
human reviewer must clear any deliverable before clinical use. The Stage 2
references (the lights-off factory and the hybrid surgery and medicine pilot)
require VVUQ clearance, human oversight, IRB approval, and regulatory
authorization before any real use. Mentions of the FDA and other bodies are
respectful and forward looking; nothing here is endorsed by any regulator.

## License

Distributed under the Creative Commons Attribution 4.0 International License
(CC BY 4.0).
