# README — VVUQ Research Chunk Set for Claude Code Opus 4 (1M Context)

## Purpose

This README, together with the three chunked `.md` files listed below, is provided to Claude Code Opus 4 (1M context, Max tier) to serve as a complete working knowledge base for authoring a **new physical AI oncology trial paper**. The source material is the research document `VVUQ-Research-2.docx`, which has been split into three standalone chunks — body text, tables, and BibTeX references — to enable efficient retrieval, cross-referencing, and synthesis during paper generation.

You (Claude Code Opus 4) should load all three chunk files alongside this README into your context window at the start of any session. Do not summarize or abbreviate content from the chunks; treat every word as source-of-truth input.

---

## File Manifest

| File | Role | Description |
|---|---|---|
| `chunk1_paper_text.md` | Primary narrative | Full body text of the source paper, word-for-word, including all section prose and the ASCII pipeline diagram |
| `chunk2_tables.md` | Structured data | The complete comparison table from the source paper contrasting Traditional vs. LLM-Enhanced trial data operations |
| `chunk3_references.md` | Citation library | All 10 BibTeX entries from the source paper plus a URL index mapping each entry to its online source |
| `README.md` (this file) | Navigation + context | Describes each chunk, the cross-chunk correlations, and guidance for new paper authoring |

---

## Chunk 1 — `chunk1_paper_text.md`

### What it contains
The complete narrative body of the source paper, divided into five thematic sections:

1. **Digital twins and VVUQ frameworks** — Defines digital twins, explains VVUQ (verification, validation, uncertainty quantification) requirements, and covers the challenges of integrating multi-omics and clinical data in oncology models. Key claim: formal model verification is rarely documented in publications; dynamic twins require ongoing iterative re-validation and Bayesian uncertainty tracking.

2. **LLMs for trial data operations** — Covers four LLM use cases: (a) eligibility criteria conversion to OMOP-CDM SQL via GPT-4 (Lee et al. 2025); (b) multimodal EHR-to-trial matching achieving 87–93% accuracy (Callies et al. 2025); (c) data extraction and summarization; (d) adverse event detection matching human annotators at F1 ≈94–99% (Leas et al. 2024). Includes quantitative benchmarks and hallucination rates (21–50%).

3. **Validation metrics and UQ practices** — Details how pipelines were evaluated: 760-prompt hallucination analysis (32.7% overall rate), sensitivity/specificity logging, 8-LLM comparison, and the SPUQ prompt-perturbation technique for uncertainty quantification (50% calibration error reduction).

4. **Regulatory context** — Summarizes FDA Draft Guidance (Jan 2025) and joint FDA/EMA Guiding Principles (Jan 2026), both requiring risk-based, context-of-use AI credibility frameworks. Stresses that LLM pipelines in trials must produce VVUQ evidence: error rate documentation, bias analysis, ongoing monitoring.

5. **Summary** — Synthesizes the core argument: AI pipelines accelerate trial operations but require rigorous VVUQ to be clinically and regulatorily acceptable. Identifies the gap: non-trivial error/hallucination rates (>20%) remain the primary obstacle.

Also includes an **ASCII pipeline diagram** depicting the flow: Trial Data → LLM Module → Automated Outputs → VVUQ & Expert Review.

### Key quantitative values (for new paper reference)
- GPT-4 mapping accuracy: 48.5% vs. 32% rule-based baseline
- GPT-4 SQL effective generation: 45% vs. 75% for smaller LLM variant
- Hallucination rates: 21–50% range; overall 32.7% across 760 prompts
- Callies et al. patient-matching accuracy: 93% (n2c2 benchmark), 87% (36-site oncology dataset)
- Chart-review time reduction: ~80%, to <9 minutes per patient
- ChatGPT AE detection F1: ≈94% any-AE, 99% serious-AE
- SPUQ calibration error reduction: ~50%

---

## Chunk 2 — `chunk2_tables.md`

### What it contains
A single four-row comparison table mapping four trial workflow components across two paradigms:

| Component | Traditional Process | LLM-Enhanced Process |
|---|---|---|
| Eligibility Criteria & Query Generation | Human SQL / rule-based | GPT-4 free-text-to-SQL (with reference cohort validation) |
| Patient Recruitment/Match | Manual chart review / keyword | Multimodal LLM on EHR notes + genomic data |
| Data Extraction & Cleaning | Manual/NLP pipelines (brittle) | LLM normalization with human oversight |
| Report Generation | Analyst-written narratives | LLM draft summaries, expert-verified |

### Correlations with chunk1_paper_text.md
Each row in this table directly expands a concept discussed in the **"LLMs for trial data operations"** section of Chunk 1:
- Row 1 (Eligibility/Query) ↔ Lee et al. 2025 system (GPT-4 → OMOP-CDM SQL)
- Row 2 (Patient Matching) ↔ Callies et al. 2025 multimodal pipeline
- Row 3 (Data Extraction) ↔ general LLM data parsing discussion in Chunk 1
- Row 4 (Report Generation) ↔ discharge summary / AE detection discussion, Leas et al. 2024

### Correlations with chunk3_references.md
The table caption references [20†] and [31†] (internal document numbering); these correspond to `Lee2025` and `Callies2025` in the BibTeX library. When expanding this table in a new paper, always pair new rows with their corresponding BibTeX keys.

### Use in new paper authoring
This table should anchor any Methods or Background section that contrasts traditional trial operations with emerging AI pipelines. It is designed to be extended: new rows can be added for imaging analysis, biomarker discovery, or synthetic control arm generation as the new paper scope expands.

---

## Chunk 3 — `chunk3_references.md`

### What it contains
Ten fully-formed BibTeX entries plus a URL index. Entries span four source types:

| BibTeX Key | Type | Topic |
|---|---|---|
| Sel2025 | @article | VVUQ survey for digital twins in precision medicine (NPJ Digital Medicine) |
| Olawade2026 | @article | Digital twins in oncology, predictive modelling to personalised treatment (Crit Rev Oncol/Hematol) |
| Callies2025 | @article | Multimodal LLM pipeline for clinical trial patient matching (Communications Medicine) |
| Lee2025 | @article | LLM automation of OMOP-CDM query generation from eligibility criteria (JMIR Med Informatics) |
| FDA2025 | @misc | FDA Draft Guidance on AI for regulatory decision-making (Jan 2025) |
| FDA2026 | @misc | FDA/EMA Guiding Principles of Good AI Practice in Drug Development (Jan 2026) |
| Vidovszky2024 | @article | Acceptance of AI-generated digital twins in clinical trial applications (Clin Transl Sci) |
| Azenkot2025 | @inproceedings | AI/ML innovations for oncology trial design and representativeness (ASCO Educ Book) |
| Gao2024 | @misc | SPUQ method for LLM uncertainty quantification (Intuit/EACL 2024) |
| Leas2024 | @article | ChatGPT for adverse event detection, content analysis case study (JMIR) |

### Correlations with chunk1_paper_text.md
Every quantitative claim in Chunk 1 maps to one or more of these BibTeX keys. The mapping is:
- VVUQ framework challenges → Sel2025, Olawade2026
- GPT-4 OMOP SQL pipeline metrics → Lee2025
- Patient-matching pipeline metrics → Callies2025
- AE detection F1 scores → Leas2024
- SPUQ uncertainty quantification → Gao2024
- FDA regulatory context → FDA2025, FDA2026
- Digital twin adoption/trust position paper → Vidovszky2024
- AI/ML in oncology trial design → Azenkot2025

### Correlations with chunk2_tables.md
Table rows in Chunk 2 cite [20†] = Lee2025 and [31†] = Callies2025. Any table expansion in the new paper should add corresponding BibTeX keys from this file or append new entries to chunk3.

### Use in new paper authoring
When Claude Code Opus 4 generates a new paper section that cites a finding from Chunk 1, the correct BibTeX key should be inserted immediately. If the new paper introduces new sources not in this file, append new BibTeX entries to chunk3_references.md before finalizing the bibliography.

---

## Cross-File Correlation Map

```
chunk1_paper_text.md
│
├── Narrative claim (VVUQ challenges, digital twins)
│       └── cites → Sel2025, Olawade2026 [chunk3_references.md]
│
├── Narrative claim (GPT-4 OMOP SQL, hallucination rates)
│       ├── cites → Lee2025 [chunk3_references.md]
│       └── expands → Table Row 1, Eligibility Criteria [chunk2_tables.md]
│
├── Narrative claim (multimodal LLM patient matching, 87–93% accuracy)
│       ├── cites → Callies2025 [chunk3_references.md]
│       └── expands → Table Row 2, Patient Recruitment [chunk2_tables.md]
│
├── Narrative claim (AE detection, F1 ≈94–99%)
│       ├── cites → Leas2024 [chunk3_references.md]
│       └── expands → Table Row 4, Report Generation [chunk2_tables.md]
│
├── Narrative claim (SPUQ, 50% calibration error reduction)
│       └── cites → Gao2024 [chunk3_references.md]
│
├── Narrative claim (FDA AI credibility guidance Jan 2025)
│       └── cites → FDA2025 [chunk3_references.md]
│
├── Narrative claim (FDA/EMA guiding principles Jan 2026)
│       └── cites → FDA2026 [chunk3_references.md]
│
├── Narrative claim (digital twin trust / adoption position paper)
│       └── cites → Vidovszky2024 [chunk3_references.md]
│
└── Narrative claim (AI/ML oncology trial design/representativeness)
        └── cites → Azenkot2025 [chunk3_references.md]
```

---

## Instructions for Claude Code Opus 4 — New Paper Authoring

1. **Load all three chunk files in full** into your context at session start. Do not truncate or summarize them.

2. **Preserve word-for-word fidelity** when quoting or paraphrasing from the chunks. These chunks are the authoritative source; do not invent statistics, benchmark results, or citations not present in the chunks.

3. **For each new paper section**, identify which chunk(s) supply the relevant background, and annotate your draft with the BibTeX key from chunk3_references.md.

4. **Extend, do not replace, the table in chunk2_tables.md** when introducing new trial components (e.g. imaging biomarker extraction, synthetic control arm generation, adaptive dose optimization). New rows must be paired with new or existing BibTeX keys.

5. **Append new BibTeX entries** to chunk3_references.md as new sources are introduced. Maintain the existing key naming convention: AuthorYear (e.g. Smith2025).

6. **Regulatory claims must cite FDA2025 or FDA2026** (or both) whenever they concern AI model credibility, context of use, or VVUQ compliance in drug development.

7. **The ASCII diagram in chunk1_paper_text.md** is the canonical pipeline architecture. New paper figures should extend this diagram (e.g. adding a physical AI / robotic arm node between the LLM Module and the output stage) rather than replacing it.

8. **Hallucination rates and accuracy benchmarks** from the source paper (listed in the Chunk 1 key values above) are baseline comparators. Any new pipeline described in the new paper should be explicitly benchmarked against these figures.

9. **The new paper's scope** (physical AI oncology trial) expands the source paper by adding a physical/robotic AI component. The VVUQ framework from Sel2025 and the regulatory requirements from FDA2025/FDA2026 apply equally to physical AI systems and should be discussed in the new paper's Methods and Discussion sections.

10. **Do not web-search** for additional context. All background is contained in the three chunk files. If a claim cannot be sourced to a chunk, flag it as a new citation needed rather than fabricating a reference.

---

## Summary of Source Paper Argument (for quick orientation)

The source paper argues that:
- AI/LLM pipelines can automate core oncology trial operations (eligibility screening, patient matching, data extraction, reporting)
- Current LLM systems achieve high accuracy (87–93%) but carry non-trivial hallucination rates (21–50%)
- VVUQ — systematic verification, validation, and uncertainty quantification — is required to make these pipelines clinically and regulatorily acceptable
- FDA (2025) and FDA/EMA (2026) now mandate risk-based AI credibility frameworks for any AI used in drug development
- The path forward is hybrid pipelines: LLM automation + rule-based checks + expert review + documented uncertainty metrics

The new paper will extend this argument into the physical AI domain (robotic/physical AI systems in oncology trial settings), using this chunk set as the literature foundation.
