# VVUQ-03 full-paper

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![cancer-automated DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![physical-ai DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![VVUQ-01 DOI](https://img.shields.io/badge/VVUQ--01%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![VVUQ-02 DOI](https://img.shields.io/badge/VVUQ--02%20DOI-10.5281%2Fzenodo.20421754-blue.svg)](https://doi.org/10.5281/zenodo.20421754)
[![Bill](https://img.shields.io/badge/Bill-H.R.%209510%20(119th%2C%202d%20Sess.)-darkblue.svg)](https://www.congress.gov/browse/119th-congress)
[![Standards](https://img.shields.io/badge/Standards-USL%20%7C%20PSL%20%7C%2014%20External-orange.svg)](https://www.asme.org/codes-standards/find-codes-standards/assessing-credibility-of-computational-modeling-through-verification-and-validation-application-to-medical-devices)

LaTeX **full-paper** for the *VVUQ Physical AI Oncology Trial Bill*
(**H.R. 9510**, 119th Congress, 2d Session; Draft 1.0), a proposed United States
bill that would require an automated verification, validation, and uncertainty
quantification (VVUQ) process to clear robot-patient interaction code **before**
that code is generated or executed in a Physical AI oncology clinical trial.

This bundle is the **finished bill**, built from the `draft-paper` scaffold: every
`[bracketed instruction]` in the scaffold has been synthesised into
publication-quality legislative prose with left-aligned, fixed-width tables that
carry the dense facts. The references are final, no images are used anywhere, and
the bundle compiles to PDF in Overleaf with the recipe below.

## Thesis

Physical AI oncology trials require rigorous AI VVUQ code automation methods for
new robot-patient interactions. State of the art repository based AI models are
also capable of synthesising VVUQ code generation and execution results into
public documents to improve and accelerate the legislative process. This bill
prioritises and solidifies a law that requires the code verification process
ahead of code generation to ensure patient safety and efficacy.

## Bill identity

| Field | Value |
|:--|:--|
| Short title | Verification Before Generation in Physical AI Oncology Trials Act of 2026 |
| Designation | H.R. 9510 |
| Congress | 119th Congress, 2d Session (2026) |
| Sponsor of record | CEO Kevin Kawchak, ChemicalQDevice |
| Status | Independent draft (Draft 1.0); not enacted, not endorsed by CFR, ICH, or FDA |
| Core mandate | Verification before generation for robot-patient interaction code |

The designation **H.R. 9510** is a 2026-specific number chosen to sit ahead of
the bills already filed in the 119th Congress; the number is unused in the 119th
Congress (it last appeared in the 117th and 118th Congresses, now closed), so no
naming collision exists.

## Position in the lineage

```
  VVUQ-01/final-paper   LLMs are appropriate for VVUQ code verification
            |           (verification ahead of generation; 51/51 tests; gate decides)
            v
  VVUQ-02 (codegen + execution + final-paper)
            |           Practical VVUQ codegen and execution against External Standards
            v           (14 + 2 sources; 1790-line comparison.json; 1001-row sensor CSV)
  physical-ai-oncology-trials/national-platform/.../final_paper
            |           USL + PSL standards; trial, sponsor, and mobile simulations
            v
  VVUQ-03/template-paper   Adaption of 21 CFR Part 312 (cover page + .sty + .bib model)
            |
            v
  VVUQ-03/draft-paper   Bill scaffold + bracketed build instructions
            |
            v
  VVUQ-03/full-paper   <=== THIS BUNDLE (finished H.R. 9510 bill, 70+ pages)
```

## How the bill is assembled

```
   Recorded technical evidence              Existing law
   (VVUQ-01, VVUQ-02, national               (federal + 4 states)
    platform, USL/PSL, 5 sims)                      |
            |                                       |
            v                                       v
   Findings + Algorithm Doc +   --->   Prior-Law Crosswalk   --->   Draft Statutory Text
   Attestations + Supporting Doc                                    (H.R. 9510, Sections 1-9)
            |                                                              |
            +----------------------> Section-by-Section Analysis <---------+
                                              |
                                              v
                              Implementation, Enforcement, Fiscal
                                              |
                                              v
                                   Limitations -> Conclusions
```

## File layout

```
full-paper/
  README.md                 (this file)
  main.tex                  (cover page + H.R. 9510 header, TOC, \input wiring, formatting)
  new_paper.sty             (Palatino body, navy 143A5A accent; carried from the template family)
  references.bib            (FINAL bibliography; 60 entries; DOIs + URLs; ieeetr; no howpublished)
  sections/
    abstract.tex                  (Abstract and Bill Synopsis; no citations)
    policy_memo.tex               (Policy Memorandum and Concept Paper)
    problem_statement.tex         (Problem Statement and Current-Law Gap)
    definitions.tex               (Definitions and Technical Terminology; USL/PSL longtable)
    findings.tex                  (Legislative Findings and Evidentiary Record)
    algorithm_documentation.tex   (Algorithm Documentation Requirements; comparison.json + sensor CSV)
    attestations_compliance.tex   (Attestations and Compliance Statements)
    prior_law.tex                 (Prior Law References and Statutory Crosswalk)
    supporting_documentation.tex  (Supporting Documentation Referenced, Not Attached)
    statutory_text.tex            (Draft Statutory Text; Sections 1-9, (a)(1)(i) hierarchy)
    implementation_enforcement.tex(Implementation, Oversight, Enforcement, Fiscal)
    section_by_section.tex        (Section-by-Section Analysis longtable)
    limitations_future.tex        (Limitations and Future Work)
    conclusions.tex               (Conclusions and Effective Date)
    back_matter.tex               (Acknowledgments, Rights, Cite, Data, Stakeholders)
  prompt-full-paper.md      (the generating prompt, verbatim)
  output-full-paper.md      (the narrative output of this full-paper step)
  full-paper.zip            (Overleaf-ready LaTeX bundle)
```

## Compile recipe (Overleaf)

```
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

Set the Overleaf compiler to pdfLaTeX. The bibliography is rendered with
`ieeetr`; `\nocite{*}` guarantees every entry appears, and inline `\cite` calls
anchor each reference where it is used in the body.

## Section to source-file map (what each section synthesises)

Long paths are given once here; the body keeps file names in tables, not in
prose. Cancer-automated paths are repo-relative (`papers/...`). The national
platform paper lives in the sibling repository `physical-ai-oncology-trials`
(DOI 10.5281/zenodo.19244918); its files are shown under
`national-platform/.../final_paper/`.

| Section | Primary source files |
|:--|:--|
| Abstract | `papers/VVUQ-01/final-paper/`; `papers/VVUQ-02/final-paper/`; Thesis |
| Policy memo | `template-paper/chunk_01_front_matter.md`; VVUQ-01 `introduction.tex`; national `executive_summary.tex` |
| Problem statement | VVUQ-01 `introduction.tex`; national `regulatory_landscape.tex`, `gov_framework.tex` |
| Definitions | `template-paper/chunk_02_subpart_a_general_provisions.md`; national `psl_usl_standards.tex`; VVUQ-02 `vvuq_methodology.md` |
| Findings | VVUQ-01 and VVUQ-02 `final-paper/` + `execution/README.md`; national `site_establishment.tex`, `patient_journey.tex` |
| Algorithm documentation | `VVUQ-02/codegen/` (docs, config, results); `comparison.json`; `sample_h2_sensor.csv` |
| Attestations and compliance | `VVUQ-02/codegen/docs/ci_compliance_checklist.md`, `standards_map.md`; national `psl_usl_standards.tex` |
| Prior law | `references.bib` (federal and state keys); `chunk_01_front_matter.md`; national `regulatory_landscape.tex` |
| Supporting documentation | `VVUQ-02/execution/`, `codegen/data/`, `results/`; national `source_documents.tex`, `appendices.tex` |
| Statutory text | `template-paper/chunk_10_subpart_j_physical_ai_references.md`; `VVUQ-02/codegen/docs/vvuq_gate_spec.md` |
| Implementation and fiscal | national `implementation_strategy.tex`, `financial_analysis.tex`; `VVUQ-02/execution/README.md` |
| Section-by-section | all `sections/*.tex`; `chunk_01_front_matter.md` (change-summary model) |
| Limitations | VVUQ-01 and VVUQ-02 `limitations_future.tex`; `VVUQ-02/execution/README.md` |
| Conclusions | VVUQ-01 and VVUQ-02 `conclusions.tex` |
| Back matter | `VVUQ-02/final-paper/sections/back_matter.tex` |

## Production and formatting rules (senior-author finishing pass)

- The bill reads as a top human author of legislation would write it, with ideas
  connected across sections; tables are referenced, not narrated.
- Every table is set to the body measure (`\textwidth`) with left-aligned,
  ragged-right fixed-width columns of the form
  `{>{\raggedright\arraybackslash}p{2cm}}`; `\raggedright\arraybackslash` is
  prepended to **every** `p{}` width so cells never open large inter-word gaps,
  and the longer parent path is placed once near the top of each table.
- Body text avoids large empty white bands; `\sloppy`, `\emergencystretch`, and
  `microtype` keep words evenly spaced and stop any line running off the right
  margin. Long URLs break on any character.
- No orphan or widow line, no single line split from its paragraph onto the next
  page, and no one- or two-word lines; the widow and club penalties in
  `new_paper.sty` are 10000.
- The section symbol `§` is used for every clause reference (for example
  `42 U.S.C. § 1395y` or `ASME V&V 40-2018 § 8`); `SS` is never used.
- Single hyphens only. No em dashes, en dashes, double, or triple dashes.
- No images anywhere. The navy 143A5A accent and Palatino body are preserved.

## References policy

`references.bib` is final and loses no detail. It is rendered with
`\bibliographystyle{ieeetr}`, which prints the `note` field, so every entry shows
its human readable DOI string and its clickable resolver URL. The `doi` field is
the bare DOI string; `url` is the `https://doi.org/` resolver (or the canonical
landing page when no DOI exists); `note` opens with `DOI: <doi>.` when a DOI
exists and ends with the clickable link(s) in `\url{...}`. Repository entries
carry the GitHub and the Zenodo link once each; there is no `howpublished` field;
both the paper DOI and the repository DOIs resolve as clickable links; and no
link is duplicated within an entry.

The federal laws are cited as `usc-1395y` (42 U.S.C. § 1395y, Medicare),
`cfr-hipaa` (45 CFR Parts 160 and 164), `cfr-devices` (21 CFR Parts 860 to 892),
`usc-titlevi` (42 U.S.C. § 2000d), and `usc-ada` (42 U.S.C. § 12101). The state
laws are `ny-a9149`, `tx-sb1822`, `ca-sb1120`, and `fl-hb527`.

## Build validation (compile-safety)

The bundle was validated structurally before the final commit, because pdflatex
is not available in the build container and the bill is compiled in Overleaf. The
checks, all passing:

- Every `\input{sections/...}` in `main.tex` resolves to a present file, and
  every section file is wired into `main.tex` (15 of 15).
- Braces balance in all files; `\begin`/`\end` environments balance (titlepage,
  abstract, minipage, document, every table, tabularx, xltabular, longtable, and
  description list).
- No unescaped `&`, no em or en or double or triple dashes, and balanced dollar
  signs in active (non-comment) text; single hyphens only.
- The only non-ASCII character is the intended `§`, safe under `utf8` inputenc
  and `T1` fontenc; `SS` is never used for a section.
- `references.bib` has 60 entries, no duplicate keys, and no `howpublished`
  field; every `\url{...}` is free of raw ampersands.

## Responsible use

This is an independent draft. It is not endorsed, sponsored, or approved by any
trial sponsor, CRO, site, IRB, regulator, or medical society, and is not endorsed
by CFR, ICH, or FDA. Mentions of the FDA and other governing bodies are
respectful and non-presumptuous: the bill is written to advance the new field of
Physical AI oncology trials and to keep the United States first in the world in
surgical-humanoid VVUQ with external standards for patient safety, efficacy, and
clinical-trial speed. All supporting numbers are simulation results; the Unitree
H2-Surgical 1.0 is a clearly labelled hypothetical 2030 platform.

## License

Generated text under the Creative Commons Attribution 4.0 International License
(CC BY 4.0).
