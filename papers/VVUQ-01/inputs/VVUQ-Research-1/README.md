# README — VVUQ Research Chunk Set
## For: Claude Code Opus 4.7 (1M context) — New Physical AI Oncology Trial Paper

---

## Overview

This README describes a set of three chunked Markdown files derived word-for-word from the source document **"VVUQ in Clinical Trial Data Pipelines and Digital Twins"** (VVUQ-Research-1.docx). The original document is a structured research paper surveying Verification, Validation, and Uncertainty Quantification (VVUQ) methods as applied to AI-enabled clinical trial pipelines, digital twins, and oncology simulation frameworks. The three chunks divide the source content into: (1) main prose and figures, (2) tables, and (3) BibTeX references. No content has been summarized, abbreviated, or paraphrased — all text is reproduced verbatim from the source.

These chunks are intended to provide Claude Code Opus 4.7 with complete, granular access to the source paper's content as the basis for writing a new physical AI oncology trial paper.

---

## File Descriptions

### 1. `VVUQ_chunk1_text.md` — Main Paper Body Text

**Contents:** The full prose body of the source paper, including the introduction, all narrative paragraphs, the ASCII figure with caption, and the Key Recommendations section. Inline citation markers have been removed from the prose (they were hyperlink-based footnote numbers in the original), but all cited claims and factual statements remain intact and traceable to `VVUQ_chunk3_references.md`.

**Sections present in this file:**
- Opening synthesis paragraph on VVUQ consensus in AI-enabled clinical trials
- Carlisle et al. (2026) UODBLLM pipeline description — LLM-based clinical data extraction from prostate MRI reports
- Trooskens et al. (2026) Compiled AI pipeline — deterministic LLM code generation for healthcare workflows
- Sanofi and Phesi digital patient twin programs — QSP virtual cohorts and synthetic control arms
- National Academies (2024) VVUQ policy framework for digital twins
- Moradi et al. (2026) three-stage VVUQ oncology framework for image-based models
- Bridging paragraph connecting table rows to underlying case study evidence
- ASCII diagram: Example LLM-VVUQ Pipeline (Input → LLM → Verification → Validation → Output, with UQ Analysis branch)
- Figure caption for the pipeline diagram
- Key Recommendations section: constrained generation, routine validation, UQ methods (Monte Carlo/Bayesian), automated logging, continuous monitoring, ASME/FDA-style VVUQ

**Key entities and metrics in this file:**
- UODBLLM: 98.1% median field accuracy, IQR 96.3–99.2%, 1800 reports, 100% completion, ~9 s/report, $0.009/report
- Compiled AI: 96% task completion (384/400), 100% reliability post-validation, 96.7% prompt-injection detection, 87.5% static code safety, 9.6K one-time token cost, break-even ~17 uses
- Sanofi: QSP-based "Digital Patient Profile", blind-predicted Phase 1b asthma trial outcome
- Phesi: synthetic control arm from aggregated historical + RWD, >10× single-trial sample size
- NASEM 2024: VVUQ defined as verification = code correctness, validation = model vs. reality, UQ = quantifying output uncertainties
- Moradi 2026: three-stage framework — structural fidelity verification → internal/external data validation → uncertainty quantification

**Correlations to other chunks:**
- Every factual claim in this file is sourced from one or more references in `VVUQ_chunk3_references.md`. The mapping is: Carlisle2026 → UODBLLM; Trooskens2026 → Compiled AI; Klabunde2024 + Li2024 → Sanofi/Phesi; NASEM2024 → National Academies; Moradi2026 → image-based model framework; Zaid2025 → PBPK dosing; Studna2024 → DIA 2024 conference.
- The Key Recommendations section directly synthesizes all five pipeline rows from `VVUQ_chunk2_tables.md`.
- The ASCII figure visually represents the pipeline architecture described in detail across both the text body and the UODBLLM and Compiled AI rows in the table.

---

### 2. `VVUQ_chunk2_tables.md` — Tables

**Contents:** The single structured evidence table from the source paper, reproduced verbatim, titled "Sample VVUQ Methods and Outcomes in Clinical AI Pipelines." Inline citation hyperlinks have been removed while all content (methods, metrics, and outcomes) is preserved exactly.

**Table structure:**
- Column 1: **Application / Pipeline** — identifies the system and domain
- Column 2: **Method / VVUQ Approach** — describes verification, validation, and UQ techniques used
- Column 3: **Key Metrics & Outcomes** — quantitative and qualitative results

**Five rows (pipeline entries):**

| Row | Pipeline | Domain |
|-----|----------|--------|
| 1 | UODBLLM (Carlisle et al. 2026) | LLM data extraction from clinical EHR |
| 2 | Compiled AI (Trooskens et al. 2026) | LLM code generation for healthcare workflows |
| 3 | Sanofi & Phesi | Digital twin trials and synthetic control arms |
| 4 | Theranostic Digital Twins (Zaid et al. 2025) | In silico PBPK dosing for radiopharmaceutical therapy |
| 5 | Cancer Therapy Simulations (Moradi et al. 2026) | Image-based models for personalized cancer therapy |

**Correlations to other chunks:**
- Each row in this table corresponds to a narrative description in `VVUQ_chunk1_text.md`. Rows 1–3 are described in depth in the prose body; rows 4–5 (PBPK dosing, image-based models) are referenced briefly in the prose and then elaborated in the table.
- Every row maps to one or more BibTeX entries in `VVUQ_chunk3_references.md`: Row 1 → Carlisle2026; Row 2 → Trooskens2026; Row 3 → Klabunde2024 + Li2024; Row 4 → Zaid2025; Row 5 → Moradi2026.
- The table provides the most concentrated, structured summary of VVUQ methodology per pipeline — it is the primary reference for comparative analysis when writing a new trial paper.
- The Key Recommendations section in `VVUQ_chunk1_text.md` synthesizes lessons from all five rows in this table.

---

### 3. `VVUQ_chunk3_references.md` — BibTeX References

**Contents:** All nine BibTeX reference entries from the source paper, reproduced verbatim, followed by a Source URL Index mapping each citation key to its canonical URL.

**BibTeX entries (9 total):**

| Citation Key | Author(s) | Year | Journal / Venue |
|---|---|---|---|
| Carlisle2026 | Carlisle MN et al. | 2026 | JMIR Bioinformatics and Biotechnology |
| Studna2024 | Studna A | 2024 | Applied Clinical Trials (DIA 2024 conference report) |
| Klabunde2024 | Klabunde T | 2024 | Sanofi Magazine |
| NASEM2024 | National Academies of Sciences, Engineering, and Medicine | 2024 | National Academies Press (techreport) |
| Zaid2025 | Zaid NRR, Hardiansyah D, Yusufaly T, Rahmim A | 2025 | medRxiv / PET Clinics (arXiv:2509.21697) |
| Moradi2026 | Moradi Kashkooli F et al. | 2026 | Frontiers in Radiology |
| Trooskens2026 | Trooskens G et al. | 2026 | arXiv preprint (arXiv:2604.05150) |
| Li2024 | Li G | 2024 | Applied Clinical Trials (Phesi blog / ACT) |
| Sel2025 | Sel K et al. | 2025 | npj Digital Medicine (DOI: 10.1038/s41746-025-01447-y) |

**Correlations to other chunks:**
- Sel2025 is cited in the opening paragraph of `VVUQ_chunk1_text.md` for the foundational VVUQ-in-digital-twins mandate.
- Moradi2026 is the source for the three-stage VVUQ framework (verify → validate → quantify uncertainty) referenced in both the prose and Row 5 of the table.
- Carlisle2026 underpins all UODBLLM metrics in both `VVUQ_chunk1_text.md` paragraphs and Row 1 of `VVUQ_chunk2_tables.md`.
- Trooskens2026 underpins all Compiled AI metrics in both `VVUQ_chunk1_text.md` paragraphs and Row 2 of `VVUQ_chunk2_tables.md`.
- Klabunde2024 and Li2024 together underpin Sanofi/Phesi claims in both `VVUQ_chunk1_text.md` and Row 3 of `VVUQ_chunk2_tables.md`.
- NASEM2024 underpins the regulatory and definitions section in `VVUQ_chunk1_text.md` and the continuous re-verification recommendation.
- Zaid2025 is the primary source for PBPK/theranostic twin content in Row 4 of `VVUQ_chunk2_tables.md` and is referenced briefly in `VVUQ_chunk1_text.md` Key Recommendations.
- Studna2024 is the source for the DIA 2024 conference quote about model requirements in `VVUQ_chunk1_text.md`.

---

## Cross-File Correlation Map

```
VVUQ_chunk1_text.md  <-->  VVUQ_chunk2_tables.md
  - Prose narratives for UODBLLM, Compiled AI, Sanofi/Phesi, NASEM, Moradi
    are the expanded descriptions of the 5 table rows.
  - Key Recommendations synthesize all 5 table rows into design principles.
  - The ASCII pipeline figure illustrates the architecture common to all rows.

VVUQ_chunk1_text.md  <-->  VVUQ_chunk3_references.md
  - Every factual claim in the prose traces to a BibTeX key.
  - Citation key order of appearance in text: Sel2025, Moradi2026,
    Carlisle2026, Trooskens2026, Studna2024, Klabunde2024, Li2024,
    NASEM2024, Zaid2025.

VVUQ_chunk2_tables.md  <-->  VVUQ_chunk3_references.md
  - Each of the 5 table rows maps directly to 1–2 BibTeX entries.
  - Row 1 → Carlisle2026
  - Row 2 → Trooskens2026
  - Row 3 → Klabunde2024, Li2024
  - Row 4 → Zaid2025
  - Row 5 → Moradi2026
```

---

## Guidance for New Physical AI Oncology Trial Paper

When using these three files to write a new physical AI oncology trial paper, the following workflow is recommended:

1. **Use `VVUQ_chunk2_tables.md` as the structural scaffold.** The five pipeline rows represent five distinct VVUQ implementation strategies. Each can map to a proposed method or validation stage in the new trial protocol (e.g., LLM data extraction → EHR preprocessing for oncology imaging; PBPK digital twins → dosimetry planning for radiopharmaceutical oncology trials).

2. **Use `VVUQ_chunk1_text.md` as the narrative evidence base.** Each prose paragraph provides the clinical context, rationale, and quantitative performance benchmarks that justify adapting a given VVUQ approach. The Key Recommendations section is directly translatable into a Methods/Design section of the new paper.

3. **Use `VVUQ_chunk3_references.md` for all citations.** All nine BibTeX entries are ready for direct inclusion in the new paper's bibliography. Sel2025 and NASEM2024 are appropriate for introduction/background sections on VVUQ foundations. Carlisle2026, Trooskens2026, Moradi2026, and Zaid2025 are appropriate for related-work and methods sections. Klabunde2024, Li2024, and Studna2024 are appropriate for discussion sections on industry adoption and regulatory context.

4. **Oncology-specific focus areas identified in the source paper:**
   - Theranostic digital twins for radiopharmaceutical therapy (Zaid2025 / Row 4) — directly applicable to physical oncology trial design with dosimetry endpoints
   - Image-based personalized cancer therapy simulations (Moradi2026 / Row 5) — directly applicable to imaging-guided oncology trials
   - Digital twin control arms (Li2024 / Row 3) — applicable to reducing or eliminating physical control groups in oncology trials
   - QSP-based virtual patient cohorts (Klabunde2024 / Row 3) — applicable to patient stratification and eligibility modeling in oncology

5. **Key VVUQ terminology to carry forward into the new paper:**
   - Verification: structural fidelity, code correctness, schema validation, syntax/security checks
   - Validation: blind prediction, concordance rates, internal/external data comparison, surrogate testing
   - Uncertainty Quantification: Monte Carlo simulation, Bayesian approaches, confidence intervals, sensitivity analysis
   - Continuous monitoring / re-verification as the physical trial system evolves
   - Clinically credible simulation (Moradi2026 terminology)
   - Zero run-time nondeterminism (Trooskens2026 terminology, adaptable to pipeline design)

---

## Source Document Metadata

- **Original filename:** VVUQ-Research-1.docx
- **Paper title:** VVUQ in Clinical Trial Data Pipelines and Digital Twins
- **Publication status:** Research synthesis / review document (not a primary trial report)
- **Primary subject:** Verification, Validation, and Uncertainty Quantification (VVUQ) in AI-enabled clinical trial pipelines and digital twins
- **Secondary subjects:** LLM pipelines for clinical data extraction, deterministic AI code generation, digital patient twins, PBPK pharmacokinetic modeling, image-based oncology simulation
- **Temporal scope of cited literature:** 2024–2026
- **Number of references:** 9 (BibTeX)
- **Number of tables:** 1 (five-row comparative evidence table)
- **Figure:** 1 ASCII pipeline diagram (LLM-VVUQ flow)
- **Chunked by:** Claude Sonnet 4.6 (claude.ai), May 2026
