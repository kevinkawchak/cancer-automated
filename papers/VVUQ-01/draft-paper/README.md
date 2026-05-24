# VVUQ-01 Draft Paper: Two Stage VVUQ Oncology Clinical Trial Verification Automation

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Repo DOI](https://img.shields.io/badge/Repo%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Release](https://img.shields.io/badge/Release-v0.5.0-brightgreen.svg)](../../../releases.md)
[![Engine](https://img.shields.io/badge/pdfLaTeX-Overleaf-success.svg)](https://www.overleaf.com/)
[![Style](https://img.shields.io/badge/Style-ieeetr%20%2B%20black%20links-lightgrey.svg)](references.bib)
[![Authored](https://img.shields.io/badge/Authored-Claude%20Code%20Opus%204.7%201M%20Max-purple.svg)](https://www.anthropic.com/news/claude-opus-4-7)

This directory holds the **draft paper scaffold** for the manuscript *Two Stage
VVUQ Oncology Clinical Trial Verification Automation Priority over Existing
Generated Code*. It is a complete, compilable LaTeX project whose section files
carry **bracketed processing instructions**, not finished prose. Each bracketed
block names the exact `kevinkawchak/cancer-automated` directories and files to
process and how to process them, so a future Claude Code Opus 4.7 (1M context)
Max pass can write the 70+ page final paper without rediscovering the sources.

> The bracketed instructions are the deliverable of this scaffold. The future
> pass replaces each `[ ... ]` block with grounded, publication quality content
> and keeps the title page, style, bibliography, and back matter intact.

## Thesis

The LLM VVUQ process needs to be more substantial than automated code generation
itself, as well as subsequent code execution, chart generation, and paper
generation operations. This LLM process helps to ensure faster, less expensive,
and more rigorous physical AI oncology clinical trials than conventional
verification methods.

## What compiles, what is instruction

```
  Now (this scaffold)                         Future pass (full paper)
  +-----------------------------------+       +-----------------------------------+
  | FINAL, do not rewrite             |       | REPLACE bracketed blocks only     |
  |   main.tex   (title, structure)   |       |   sections/abstract.tex           |
  |   new_paper.sty (layout, color)   |  -->  |   sections/introduction.tex       |
  |   references.bib (28 entries)     |       |   sections/methods.tex            |
  |   sections/back_matter.tex        |       |   sections/results.tex            |
  |   README.md (this file)           |       |   sections/discussion.tex         |
  |                                   |       |   sections/limitations_future.tex |
  | INSTRUCTION (bracketed)           |       |   sections/conclusions.tex        |
  |   the seven body section files    |       |   sections/references.tex (cites) |
  +-----------------------------------+       +-----------------------------------+
                |                                            |
                +--------------------> 70+ page paper <------+
```

## File layout

```
draft-paper/
  README.md            (this file: badges, structure, processing model)
  main.tex             (preamble, title page, disclaimer, keywords, TOC, \input lines)
  new_paper.sty        (single column serif style; black links, green ORCID)
  references.bib       (28 final entries, ieeetr, DOI + clickable URL each)
  sections/
    abstract.tex            (instruction: <300 word overview + key metrics)
    introduction.tex        (instruction: VVUQ principles, thesis, prior work)
    methods.tex             (instruction: five methods, gate, Stage 1 and 2 source)
    results.tex             (instruction: execution evidence, commit tables, figures)
    discussion.tex          (instruction: meaning of accept/block, server compare)
    limitations_future.tex  (instruction: honest gaps, all-trial future work)
    conclusions.tex         (instruction: restate thesis and forward path)
    references.tex          (instruction: citation map + the bibliography block)
    back_matter.tex         (FINAL: acknowledgments, ethics, rights, cite, data)
```

## Section to source map

The future pass draws each section from the directories below. Long file names
are abbreviated in the per-section tables; full paths live in the section
instructions. Do not process the `image-instruct/` directory, and use the
imagegen Python scripts for data, never the PNG files.

| Section | Primary source directories (abbreviated) |
|:--------|:------------------------------------------|
| Abstract | `execution/README.md` key metrics; `pipeline/`, `vvuq/`, `physical-ai/` READMEs |
| Introduction | `vvuq/` modules; `inputs/` paper and research READMEs; `execution/README.md` thesis |
| Methods | `pipeline/`, `vvuq/`, `physical-ai/`, `configs/`, `tests/`; `execution/01-foundation/` |
| Results | `execution/02..05`; imagegen `02,04,06,08` `.py` data; commit tables in this task |
| Discussion | `execution/README.md` server comparison; `08` cost bridge `.py`; prior 07-humanoid paper |
| Limitations and Future Work | `execution/README.md` limitations section |
| Conclusions | `execution/README.md` summary; the thesis |
| References | `references.bib` (final); `inputs/` BibTeX chunks; 07-humanoid `references.bib` |

## Compile recipe (Overleaf, pdfLaTeX plus BibTeX)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

A `draft-paper.zip` bundle of this project is provided in this directory for a
one step Overleaf upload. The scaffold compiles as is; the bracketed blocks
render as visible placeholders until the future pass replaces them.

## Formatting contract for the future pass

- Ragged right body, even inter-word spacing, no white rivers, no line running
  off the right margin (knobs in `new_paper.sty`).
- No orphan or widow lines; never strand a one or two word line on its own page.
  Do not overcrowd a page; some white space is acceptable.
- Single dashes only. No em dashes, no double dashes, no triple dashes. Replace
  any stray `SS` with the section sign `§`.
- Every table uses `>{\raggedright\arraybackslash}p{...}` columns (the `L`, `C`,
  `R` types in `main.tex`). Reference tables and figures in prose rather than
  restating their contents. Keep the correct amount of context per section.
- Body text and links render black; the ORCID mark renders ORCID green, matching
  the prior template.

## Bibliography rules

`references.bib` is final. It carries 28 entries rendered with `ieeetr`. Every
entry that has a DOI prints the human readable DOI string and a clickable
resolver URL inside its `note` field; repository entries print both a GitHub and
a Zenodo URL, each once, with no duplicate link and no `howpublished` field. Both
the repository DOI and the paper DOI are clickable. The future pass may extend
the file but must keep this convention and lose no detail.

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
