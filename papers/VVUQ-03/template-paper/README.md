# README — Chunked Source for *End-to-End Physical AI Oncology Clinical Trial Unification (Adaption of 21 CFR Part 312)*

## Purpose of this README

This README is a navigation and processing guide for **Claude Code Opus 4.8 (1M context) Max**. It accompanies ten Markdown (`.md`) chunks that together constitute the **complete, word-for-word** text of the source LaTeX document `Physical_AI_21_CFR_Part_312.tex`. The chunks are intended as authoritative reference material when drafting a **new Physical AI oncology trial paper**.

The source is an adaptation of the U.S. federal regulation **21 CFR Part 312 — Investigational New Drug Application (IND)**, extended throughout to govern the integration of Physical AI systems (autonomous robots, digital twins, simulation frameworks, and AI/ML agents) into oncology clinical trials. Author: Kevin Kawchak, ChemicalQDevice. Draft released 17 March 2026. DOI: 10.5281/zenodo.19057628.

## Provenance and fidelity guarantee

- The ten chunks were produced by splitting the original `.tex` file **only at top-level section and subpart boundaries** (`\section{...}` / `\section*{...}`). No text was rewritten, abbreviated, summarized, reordered, or supplemented. No section headings were added or removed.
- The chunks retain the **original LaTeX markup verbatim** — `\subsection`, `\subsubsection`, `\begin{description}`, `\begin{longtable}`, `\textit`, `\textbf`, `\S~`, `---`, citation brackets such as `[52 FR 8831, Mar. 19, 1987]`, and the trailing `\end{document}`.
- **Verification:** concatenating the ten chunks in numeric order (`chunk_01` … `chunk_10`) reproduces the original file with an **identical MD5 checksum** (`8f771f70eac81538d778428d7f9675c1`) and a zero-byte `diff`. Total line count across chunks = 2275, matching the source exactly.
- Because boundaries fall only at `\section`-level breaks, every individual regulatory section (`\subsection{\S~312.x}`) and its paired *Physical AI Adaptation* subsubsection are kept intact within a single chunk and are never split across files.

## How to read the chunks (LaTeX → meaning map)

When processing, interpret the markup as follows: `\section{SUBPART X ...}` = a top-level subpart; `\subsection{\S~312.NN ...}` = an individual regulation section (the inherited/baseline 21 CFR text); `\subsubsection{Physical AI Adaptation of \S~312.NN}` or `\subsubsection{Physical AI Definitions}` = the *new* Physical AI material grafted onto that section. Bracketed citations at the end of a section (e.g. `[52 FR 8831, Mar. 19, 1987. Physical AI adaptation added 17 March 2026.]`) mark the regulatory authority/history line. `\begin{description}[...]` blocks encode the lettered/numbered/roman sub-paragraph hierarchy `(a) (1) (i)` etc. The single large `\begin{longtable}` lives in chunk 01.

## The ten chunks at a glance

| # | File | Lines | Source span | Coverage |
|---|------|-------|-------------|----------|
| 01 | `chunk_01_front_matter.md` | 146 | 1–146 | Preamble, title page, TOC, Prefatory Note, Document History, Public Domain Notice, Change Summary Table |
| 02 | `chunk_02_subpart_a_general_provisions.md` | 282 | 147–428 | Subpart A — General Provisions (§§312.1–312.10) |
| 03 | `chunk_03_subpart_b_ind_application.md` | 434 | 429–862 | Subpart B — IND Application (§§312.20–312.38) |
| 04 | `chunk_04_subpart_c_administrative_actions.md` | 254 | 863–1116 | Subpart C — Administrative Actions (§§312.40–312.48) |
| 05 | `chunk_05_subpart_d_sponsor_responsibilities.md` | 214 | 1117–1330 | Subpart D, part 1 — Sponsor responsibilities (§§312.50–312.59) |
| 06 | `chunk_06_subpart_d_investigator_responsibilities.md` | 164 | 1331–1494 | Subpart D, part 2 — Investigator responsibilities (§§312.60–312.70) |
| 07 | `chunk_07_subpart_e_life_threatening_illnesses.md` | 134 | 1495–1628 | Subpart E — Life-threatening / severely-debilitating illnesses (§§312.80–312.88) |
| 08 | `chunk_08_subparts_f_g_miscellaneous_lab_research.md` | 167 | 1629–1795 | Subpart F — Miscellaneous (§§312.110–312.145) + Subpart G — Lab research / in vitro (§312.160) |
| 09 | `chunk_09_subparts_h_i_expanded_access.md` | 162 | 1796–1957 | Subpart H [Reserved] + Subpart I — Expanded Access (§§312.300–312.320) |
| 10 | `chunk_10_subpart_j_physical_ai_references.md` | 318 | 1958–2275 | Subpart J (NEW) — Physical AI Systems (§§312.400–312.405) + References & Bibliography |

> Note: Subpart D is the largest body of regulation and was split across two chunks (05 and 06) at the §312.59 / §312.60 boundary, where the regulation itself pivots from **sponsor** duties to **investigator** duties. The split is a clean `\subsection` break; no section is divided.

---

## Detailed description of each chunk

### Chunk 01 — Front matter (`chunk_01_front_matter.md`)
Contains the LaTeX preamble (`\documentclass`, package/bib includes, title/author/date), the full `titlepage` (title, "Adaption: 21 CFR Part 312", IND subtitle, DOI, public-domain attribution under 17 U.S.C. §105), the `\tableofcontents`, and four `\section*` front-matter blocks: **Prefatory Note**, **Document History**, **Prior 21 CFR Part 312: Public Domain Notice**, and the **Change Summary Table**.
- The **Prefatory Note** introduces the three governing frameworks referenced everywhere downstream: the **USL** (Unification Standard Level) v1.4.0–v1.8.0 readiness scoring, the **national MCP-PAI standard** v1.2.0 (five-server topology, 23 tools, six actor roles, five conformance levels), and the companion repositories/DOIs (physical-ai-oncology-trials v2.5.0; ICH E6(R3) adaptation; 21 CFR Part 50 adaptation; federated-learning framework).
- The **Change Summary Table** (a `longtable`) is the master crosswalk: it lists *every* modified section §312.x and one-line summaries of the Physical AI additions, ending with the announcement of **New Subpart J**.
- **This is the index/orientation chunk.** Read it first; it defines vocabulary and points to every other chunk.

### Chunk 02 — Subpart A, General Provisions (`chunk_02_subpart_a_general_provisions.md`)
§§312.1 Scope, 312.2 Applicability, 312.3 Definitions and Interpretations, 312.6 Labeling, 312.7 Promotion, 312.8 Charging, 312.10 Waivers — each followed by its *Physical AI Adaptation* subsubsection.
- §312.1 establishes the **seven robot categories** and **five functional types**, the **four USL dimensions** and **minimum USL thresholds by procedure type** (surgical ≥7.0; therapeutic positioning / diagnostic needle ≥6.0; rehabilitative ≥4.0; companion monitoring ≥3.0), the **four simulation frameworks** (Isaac Lab v2.3.1, MuJoCo v3.4.0, Gazebo Sim v10.0.0, PyBullet v3.2.5) and the **cross-framework tolerances** (<2 mm trajectory, <0.5 N force).
- §312.3 contains the **22 Physical AI definitions** (`\subsubsection{Physical AI Definitions}`): Physical AI system, robot agent, USL, digital twin, simulation framework, robot capability profile, task order, emergency stop, human oversight, hash-chained audit trail, MCP, and more — the canonical glossary for the entire document.
- **This is the definitions/foundations chunk.** Any term used in chunks 03–10 is defined here or in chunk 01.

### Chunk 03 — Subpart B, IND Application (`chunk_03_subpart_b_ind_application.md`)
§§312.20 Requirement for an IND, 312.21 Phases of an Investigation, 312.22 General Principles, 312.23 IND Content and Format, 312.30 Protocol Amendments, 312.31 Information Amendments, 312.32 IND Safety Reporting, 312.33 Annual Reports, 312.38 Withdrawal — each with a Physical AI Adaptation.
- The **largest content chunk (434 lines).** §312.23 (IND Content and Format) carries the most detailed Physical AI documentation requirements: robot specifications, simulation-validation data, digital-twin models, AI/ML algorithm descriptions, and cybersecurity assessments.
- §312.21 introduces **simulation-based Phase 0 validation**; §312.32 introduces Physical-AI **safety-reporting** categories (robot malfunction, AI prediction error, digital-twin divergence, cybersecurity incident); §312.33 ties annual reporting to **USL score updates**.

### Chunk 04 — Subpart C, Administrative Actions (`chunk_04_subpart_c_administrative_actions.md`)
§§312.40 General Requirements for Use, 312.41 Comment and Advice, 312.42 Clinical Holds, 312.44 Termination, 312.45 Inactive Status, 312.47 Meetings, 312.48 Dispute Resolution — each with a Physical AI Adaptation.
- §312.42 defines Physical-AI **clinical-hold grounds** (robotic safety failures, AI model degradation, simulation-reality divergence); §312.40 ties IND effectiveness to **USL threshold verification**; §312.44 covers Physical-AI-driven **termination** (system failures, cybersecurity compromise).

### Chunk 05 — Subpart D part 1, Sponsor Responsibilities (`chunk_05_subpart_d_sponsor_responsibilities.md`)
Opens Subpart D (`\section{SUBPART D ...}`) and covers §§312.50 General Responsibilities of Sponsors, 312.52 Transfer to a CRO, 312.53 Selecting Investigators and Monitors, 312.54 Emergency Research, 312.55 Informing Investigators, 312.56 Review of Ongoing Investigations, 312.57 Recordkeeping, 312.58 Inspection of Sponsor's Records, 312.59 Disposition of Unused Supply — each with a Physical AI Adaptation.
- Focus: **sponsor-side** duties — system selection/validation/lifecycle (§312.50), CRO transfer of Physical AI obligations (§312.52), Physical AI logging/simulation/digital-twin recordkeeping (§312.57), audit-trail inspection access (§312.58).

### Chunk 06 — Subpart D part 2, Investigator Responsibilities (`chunk_06_subpart_d_investigator_responsibilities.md`)
Continues Subpart D (no new `\section`; begins directly at `\subsection{\S~312.60}`) with §§312.60 General Responsibilities of Investigators, 312.61 Control of the Drug, 312.62 Investigator Recordkeeping, 312.64 Investigator Reports, 312.66 Assurance of IRB Review, 312.68 Inspection of Investigator's Records, 312.69 Handling of Controlled Substances, 312.70 Disqualification — each with a Physical AI Adaptation.
- Focus: **investigator-side** duties — system oversight (§312.60), access control (§312.61), case-history/interaction logs (§312.62), and disqualification for **Physical AI system misuse** (§312.70).
- **Important continuity note:** chunk 06 has no `\section{SUBPART D}` header of its own because that header is in chunk 05. Treat chunks 05 + 06 as one continuous subpart.

### Chunk 07 — Subpart E, Life-Threatening Illnesses (`chunk_07_subpart_e_life_threatening_illnesses.md`)
§§312.80 Purpose, 312.81 Scope, 312.82 Early Consultation, 312.83 Treatment Protocols, 312.84 Risk-Benefit Analysis, 312.85 Phase 4 Studies, 312.86 Focused FDA Regulatory Research, 312.87 Active Monitoring, 312.88 Safeguards for Patient Safety.
- Most sections carry a Physical AI Adaptation; **§312.81 and §312.86 do not** (they retain original text only) — relevant if the new paper claims every section was modified. Themes: accelerated pathways for Physical-AI-assisted therapies, design review, post-market performance monitoring.

### Chunk 08 — Subparts F & G (`chunk_08_subparts_f_g_miscellaneous_lab_research.md`)
**Two subparts in one chunk.** Subpart F — Miscellaneous: §§312.110 Import/Export, 312.120 Foreign Clinical Studies, 312.130 Public Disclosure, 312.140 Address for Correspondence, 312.145 Guidance Documents (the **8 Physical-AI-specific guidance topics**). Subpart G — §312.160 Drugs for Investigational Use in Lab Research Animals or In Vitro Tests. Each section has a Physical AI Adaptation.
- §312.120 covers acceptance of **foreign Physical AI validation data**; §312.110 covers **import/export of Physical AI components and software**.

### Chunk 09 — Subparts H & I (`chunk_09_subparts_h_i_expanded_access.md`)
Subpart H is `[RESERVED]` (one line, preserved verbatim). Subpart I — Expanded Access: §§312.300 General, 312.305 Requirements for All Expanded Access Uses, 312.310 Individual Patient Access (incl. emergencies), 312.315 Intermediate-Size Patient Populations, 312.320 Treatment IND/Protocol — each with a Physical AI Adaptation.
- Themes: Physical-AI-assisted treatment under expanded access, emergency individual access, and multi-site deployment.

### Chunk 10 — Subpart J (NEW) + References (`chunk_10_subpart_j_physical_ai_references.md`)
**The novel core of the document plus its bibliography.** Subpart J — Physical AI Systems in Clinical Investigations (entirely new, no inherited 21 CFR text): §312.400 Purpose and Scope, §312.401 System Classification, §312.402 Validation Requirements, §312.403 Cybersecurity Requirements, §312.404 Human Oversight Requirements, §312.405 Lifecycle Management. Unlike all other subparts, these sections are **not** split into baseline + adaptation — they are wholly new requirements.
- Followed by `\section*{REFERENCES AND BIBLIOGRAPHY}` with eight thematic `\subsection*` groups: Primary Regulatory Sources, FDA Guidance Documents, Robotics and Physical AI Standards, Physical AI and Simulation Literature, Oncology Robotics and Drug Delivery, AI/ML in Clinical Trials, Cybersecurity in Medical Systems, Digital Twins and Treatment Planning.
- Ends with `\end{document}`.
- **This is the citation source-of-truth chunk.** Pull all references for the new paper from here.

---

## Cross-chunk correlations (how the files relate)

**Spine of inheritance.** Chunks 02–09 share one repeating structure: an inherited 21 CFR `\subsection{\S~312.NN}` immediately followed by a `\subsubsection{Physical AI Adaptation of \S~312.NN}`. To understand any single rule, read the pair together — the baseline establishes the legal obligation; the adaptation grafts Physical AI requirements onto it. Chunk 10's Subpart J breaks this pattern (new-only, no baseline).

**Definition dependency (everything → chunk 02, then chunk 01).** Terms such as *USL*, *digital twin*, *robot agent*, *MCP server*, *hash-chained audit trail*, *emergency stop*, *human oversight*, *simulation framework*, *robot capability profile*, and *task order* appear across nearly every chunk but are **defined once** in chunk 02 (§312.3 Physical AI Definitions) and previewed in chunk 01 (Prefatory Note). When resolving a term anywhere in 03–10, look it up in chunk 02 first, chunk 01 second.

**Crosswalk dependency (everything ↔ chunk 01).** The Change Summary Table in chunk 01 is a one-to-one index into the per-section adaptations in chunks 02–10. Use it to confirm whether a given §312.x was modified and to get a one-line summary before reading the full text. It also pre-announces Subpart J (chunk 10).

**Numeric-threshold chain (chunk 02 → 03, 04, 10).** The USL thresholds and simulation tolerances first stated in chunk 02 (§312.1) are operationalized as IND submission content in chunk 03 (§312.23), as clinical-hold/effectiveness criteria in chunk 04 (§§312.40, 312.42), and as formal validation/classification rules in chunk 10 (§§312.401, 312.402). A change to a threshold value must be reconciled across all four chunks.

**Sponsor ↔ investigator pairing (chunk 05 ↔ chunk 06).** These two chunks are a single regulatory subpart (D) split at the sponsor/investigator pivot. Sponsor duties in chunk 05 (selection, validation, lifecycle, recordkeeping, inspection) have mirror-image investigator duties in chunk 06 (oversight, control, case histories, reporting, disqualification). Read them as a complementary pair when describing trial-conduct roles.

**Safety/audit thread (chunks 02, 03, 04, 06, 10).** The safety constructs — *emergency stop*, *hash-chained audit trail* (21 CFR Part 11 alignment), *human oversight* — are defined in chunk 02, surface as safety reporting in chunk 03 (§312.32), as clinical-hold triggers in chunk 04 (§312.42), as investigator recordkeeping in chunk 06 (§312.62), and as dedicated requirement sections in chunk 10 (§§312.403 cybersecurity, §312.404 human oversight, §312.405 lifecycle).

**MCP infrastructure thread (chunks 01, 02 → 05, 06, 10).** The five-server MCP-PAI topology (trialmcp-authz, -fhir, -dicom, -ledger, -provenance), 23 tools, and six actor roles are introduced in chunk 01 and defined in chunk 02 (§312.3). They underpin data-access/audit obligations in Subpart D (chunks 05–06) and the lifecycle/cybersecurity rules in chunk 10.

**Citation closure (all chunks → chunk 10).** Any factual or regulatory claim made in chunks 01–09 traces to a reference enumerated in chunk 10's bibliography. When citing the source paper in the new paper, resolve references through chunk 10.

**Reading order recommendation for the new paper.** (1) chunk 01 for orientation and the crosswalk; (2) chunk 02 for definitions and quantitative thresholds; (3) chunk 10 for the novel Physical AI requirements and the bibliography; (4) chunks 03–09 as needed for specific regulatory obligations, always pairing each baseline section with its Physical AI adaptation.

## Reassembly / integrity check

To reconstitute the exact original LaTeX source:

```bash
cat chunk_01_front_matter.md \
    chunk_02_subpart_a_general_provisions.md \
    chunk_03_subpart_b_ind_application.md \
    chunk_04_subpart_c_administrative_actions.md \
    chunk_05_subpart_d_sponsor_responsibilities.md \
    chunk_06_subpart_d_investigator_responsibilities.md \
    chunk_07_subpart_e_life_threatening_illnesses.md \
    chunk_08_subparts_f_g_miscellaneous_lab_research.md \
    chunk_09_subparts_h_i_expanded_access.md \
    chunk_10_subpart_j_physical_ai_references.md \
    > Physical_AI_21_CFR_Part_312.tex   # MD5 == 8f771f70eac81538d778428d7f9675c1
```
