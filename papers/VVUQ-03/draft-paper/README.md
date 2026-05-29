# VVUQ-03 draft-paper

LaTeX **draft-paper** scaffold for the *VVUQ Physical AI Oncology Trial Bill*
(Draft 1.0), a proposed United States bill that would require an automated
verification, validation, and uncertainty quantification (VVUQ) process to clear
robot-patient interaction code **before** that code is generated or executed in a
Physical AI oncology clinical trial.

This bundle is a **head start, not a finished bill**. Every section body is a
`[bracketed instruction]` that names the exact repository files a future Claude
Code Opus 4.8 (1M context) Max pass must read and synthesise into
publication-quality legislative prose. The references are already final. No
section is processed here; the brackets are the build order, not the text.

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![cancer-automated DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![physical-ai DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Template](https://img.shields.io/badge/Template-VVUQ--03%2021%20CFR%20Part%20312-blue.svg)](../template-paper/)
[![Standards](https://img.shields.io/badge/Standards-USL%20%7C%20PSL%20%7C%20ASME%20V%26V%2040-orange.svg)](https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices)

## Thesis

Physical AI oncology trials require rigorous AI VVUQ code automation methods for
new robot-patient interactions. State of the art repository based AI models are
also capable of synthesising VVUQ code generation and execution results into
public documents to improve and accelerate the legislative process. This bill
prioritises and solidifies a law that requires the code verification process
ahead of code generation to ensure patient safety and efficacy.

## Position in the lineage

```
  VVUQ-01/final-paper   LLMs are appropriate for VVUQ code verification
            |           (verification ahead of generation; 51/51 tests; gate decides)
            v
  VVUQ-02 (codegen + execution + final-paper)
            |           Practical VVUQ codegen and execution against External Standards
            v           (14 + 2 sources; 1790-line comparison.json; 1001-row sensor CSV)
  physical-ai-oncology-trials/national-platform/new_paper/final_paper
            |           USL + PSL standards; trial, sponsor, and mobile simulations
            v
  VVUQ-03/template-paper   Adaption of 21 CFR Part 312 (cover page + .sty + .bib model)
            |
            v
  VVUQ-03/draft-paper   <=== THIS BUNDLE (bill scaffold + bracketed build instructions)
            |
            v
  VVUQ-03/full-paper and final-paper   (future 70+ page bill)
```

## File layout

```
draft-paper/
  README.md                 (this file)
  main.tex                  (cover page, TOC, \input wiring, format directives)
  new_paper.sty             (Palatino body, navy accent; carried from the prior template family)
  references.bib            (FINAL bibliography; DOIs + URLs; ieeetr; no howpublished)
  sections/
    abstract.tex                  (Abstract and Bill Synopsis)
    policy_memo.tex               (Policy Memorandum and Concept Paper)
    problem_statement.tex         (Problem Statement and Current-Law Gap)
    definitions.tex               (Definitions and Technical Terminology)
    findings.tex                  (Legislative Findings and Evidentiary Record)
    algorithm_documentation.tex   (Algorithm Documentation Requirements)
    attestations_compliance.tex   (Attestations and Compliance Statements)
    prior_law.tex                 (Prior Law References and Statutory Crosswalk)
    supporting_documentation.tex  (Supporting Documentation Referenced, Not Attached)
    statutory_text.tex            (Draft Statutory Text)
    implementation_enforcement.tex(Implementation, Oversight, Enforcement, Fiscal)
    section_by_section.tex        (Section-by-Section Analysis)
    limitations_future.tex        (Limitations and Future Work)
    conclusions.tex               (Conclusions and Effective Date)
    back_matter.tex               (Acknowledgments, Rights, Cite, Data, Stakeholders)
  prompt-draft-paper.md     (the generating prompt, verbatim)
  output-draft-paper.md     (the narrative output of this draft-paper step)
  draft-paper.zip           (Overleaf-ready LaTeX bundle)
```

## Compile recipe (Overleaf)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

The draft compiles now: section bodies are bracketed instructions (plain text),
the bibliography is final, and `\nocite{*}` guarantees every entry renders. No
images are used anywhere in this bill; tables carry the dense facts.

## Section to source-file map (what the future pass must read)

Long paths are given once here; the future pass keeps file names in tables, not
in prose. Cancer-automated paths are repo-relative (`papers/...`). The national
platform paper lives in the sibling repository `physical-ai-oncology-trials`
(GitHub `kevinkawchak/physical-ai-oncology-trials`, DOI 10.5281/zenodo.19244918);
its files are shown under `national-platform/new_paper/final_paper/`.

| Section | Primary source files |
|:--|:--|
| Abstract | `papers/VVUQ-01/final-paper/sections/abstract.tex`; `papers/VVUQ-02/final-paper/sections/abstract.tex`; this README Thesis |
| Policy memo | `papers/VVUQ-03/template-paper/chunk_01_front_matter.md`; `papers/VVUQ-01/final-paper/sections/introduction.tex`; national-platform `sections/executive_summary.tex` |
| Problem statement | `papers/VVUQ-01/final-paper/sections/introduction.tex`; national-platform `sections/regulatory_landscape.tex`, `sections/gov_framework.tex` |
| Definitions | `papers/VVUQ-03/template-paper/chunk_02_subpart_a_general_provisions.md`; national-platform `sections/psl_usl_standards.tex`; `papers/VVUQ-02/codegen/docs/vvuq_methodology.md` |
| Findings | `papers/VVUQ-01/final-paper/`; `papers/VVUQ-02/final-paper/`, `papers/VVUQ-02/execution/README.md`; national-platform `sections/site_establishment.tex`, `sections/patient_journey.tex` |
| Algorithm documentation | `papers/VVUQ-02/codegen/` (docs, config, results); `papers/VVUQ-02/codegen/results/comparison.json`; `papers/VVUQ-02/codegen/data/sample_h2_sensor.csv` |
| Attestations and compliance | `papers/VVUQ-02/codegen/docs/ci_compliance_checklist.md`, `standards_map.md`; national-platform `sections/psl_usl_standards.tex` |
| Prior law | `references.bib` (federal and state law keys); `papers/VVUQ-03/template-paper/chunk_01_front_matter.md`; national-platform `sections/regulatory_landscape.tex` |
| Supporting documentation | `papers/VVUQ-02/execution/`, `papers/VVUQ-02/codegen/data/`, `results/`; national-platform `sections/source_documents.tex`, `sections/appendices.tex` |
| Statutory text | `papers/VVUQ-03/template-paper/chunk_10_subpart_j_physical_ai_references.md`; `papers/VVUQ-02/codegen/docs/vvuq_gate_spec.md` |
| Implementation and fiscal | national-platform `sections/implementation_strategy.tex`, `sections/financial_analysis.tex`; `papers/VVUQ-02/execution/README.md` (cost) |
| Section-by-section | all `sections/*.tex` above; `papers/VVUQ-03/template-paper/chunk_01_front_matter.md` (change-summary table model) |
| Limitations | `papers/VVUQ-01/final-paper/sections/limitations_future.tex`; `papers/VVUQ-02/final-paper/sections/limitations_future.tex`; `papers/VVUQ-02/execution/README.md` |
| Conclusions | `papers/VVUQ-01/final-paper/sections/conclusions.tex`; `papers/VVUQ-02/final-paper/sections/conclusions.tex` |
| Back matter | `papers/VVUQ-02/final-paper/sections/back_matter.tex` |

## Production and formatting rules (senior-author finishing pass)

- Target a finished 70+ page bill; give each section comprehensive context, not
  filler. The legislation must read as if a top human author wrote it, with ideas
  connected across sections.
- Tables carry the dense facts. Abbreviate long file names in cells and put the
  common parent path once near the top of the table or its caption. Do not state
  in prose what a table already shows; reference the table instead.
- Every table column uses a left-aligned fixed width of the form
  `{>{\raggedright\arraybackslash}p{2cm}}`. Prepend `\raggedright\arraybackslash`
  to **every** `p{}` width so there are no large inter-word gaps in cells, and put
  the longer parent path toward the top of the table where appropriate.
- Avoid large empty white bands. Where justification opens large inter-word gaps,
  tune `\raggedright` spacing, `\sloppy`, `\emergencystretch`, and `microtype` so
  words are evenly spaced and no line runs off the right margin.
- Avoid orphan and widow lines, single lines separated from a paragraph on the
  next page, and lines of only one or two words; the widow and club penalties in
  `new_paper.sty` are 10000.
- Use the section symbol `§` for any clause reference (for example
  `42 U.S.C. § 1395y` or `ASME V&V 40-2018 § 8`); never write `SS`.
- Use single hyphens only. No em dashes, en dashes, double, or triple dashes.
- No images anywhere. Keep the navy accent and Palatino body from `new_paper.sty`.
- Senior-author finishing: balance each page so it stands on its own, adding or
  trimming text to remove awkward white space without overcrowding (some white
  space is fine).

## References policy

`references.bib` is final and must not lose detail. It is rendered with
`\bibliographystyle{ieeetr}`, which prints the `note` field, so every entry shows
its human readable DOI string and its clickable resolver URL. Conventions:

- `doi` is the bare DOI string; `url` is the full `https://doi.org/` resolver (or
  the canonical landing page when no DOI exists); `note` opens with `DOI: <doi>.`
  when a DOI exists, gives one sentence of relevance, then ends with the clickable
  link(s) wrapped in `\url{...}`.
- Repository entries carry the GitHub and the Zenodo link, each once, so both
  render as clickable links and no link is duplicated within an entry.
- Do not use the `howpublished` field anywhere. Both the paper DOI and the
  repository DOIs resolve as clickable links.

The federal laws are cited as `usc-1395y` (42 U.S.C. § 1395y, Medicare),
`cfr-hipaa` (45 CFR Parts 160 and 164), `cfr-devices` (21 CFR Parts 860 to 892),
`usc-titlevi` (42 U.S.C. § 2000d), and `usc-ada` (42 U.S.C. § 12101). The state
laws are `ny-a9149`, `tx-sb1822`, `ca-sb1120`, and `fl-hb527`.

## Responsible use

This is an independent draft. It is not endorsed, sponsored, or approved by any
trial sponsor, CRO, site, IRB, regulator, or medical society, and is not endorsed
by CFR, ICH, or FDA. Mentions of the FDA and other governing bodies are
respectful and non-presumptuous: the bill is written to advance the new field of
Physical AI oncology trials and to keep the United States first in the world in
surgical humanoid VVUQ with external standards for patient safety, efficacy, and
clinical-trial speed. All supporting numbers are simulation results; the Unitree
H2-Surgical 1.0 is a clearly labelled hypothetical 2030 platform.

## License

Generated text under the Creative Commons Attribution 4.0 International License
(CC BY 4.0).
