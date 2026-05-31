# 02 - FDA Regulation of AI and ML Medical Devices

Scope: the U.S. Food and Drug Administration framework that governs artificial
intelligence and machine learning in medical devices and in drug and biologic
development. This file is the regulatory layer that implements the Title 21
statutes in file 01 and supplies the closest existing federal analogue to a
statutory verification, validation, and uncertainty quantification (VVUQ) regime
for robot-patient interaction code.

| Field | Value |
|:--|:--|
| File | 02 of 10 |
| Companion bibliography | federal-regulations-guidance.bib (FDA), standards-and-literature.bib (consensus standards) |
| Data current through | May 31, 2026 |
| Primary legal sources | federalregister.gov (Federal Register), ecfr.gov (eCFR), fda.gov (guidance) |
| Implements statutes from file 01 | §§ 360c, 360(k), 360e, 360e-4, 360j(o) |

## Role in the bill update (points a through d)

1. Point a (currency): captures the 2024 to 2026 FDA actions (PCCP final
   guidance, the January 2025 lifecycle and drug-AI drafts, the QMSR effective
   date) that postdate the prior bill's references.
2. Point b (grounding): the FDA computational-model credibility guidance and
   ASME V&V 40 give the bill a mass-recognized, risk-graded VVUQ vocabulary.
3. Point c (gap): no FDA authority yet imposes ex ante, automated VVUQ on
   autonomously generated robot-control code; that is the bill's contribution.
4. Point d (structure): supplies the device-classification and special-control
   language for the bill's statutory text and findings.

## A. The AI/ML device guidance stack (2021 to 2026)

| Key | Document | Type | FR or doc number | Date / status | Substance for the gate |
|:--|:--|:--|:--|:--|:--|
| fda-pccp-2024 | Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions | Final guidance | FR Doc. 2024-28361 | Final, Dec. 4, 2024 | Lets FDA pre-authorize device-software modifications if the plan states the change, the methodology to develop, validate, and implement it, and an impact assessment. FDA's closest analogue to validate-the-change-before-deploy; implements § 360e-4. |
| fda-aidsf-lifecycle-2025 | AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations | Draft guidance | FR Doc. 2024-31543 | Draft, FR availability Jan. 7, 2025; comments closed Apr. 7, 2025 | Total Product Life Cycle approach to design, validation, transparency, and bias, including evidence that the device performs across demographic groups. Supports validate-across-the-use-population and continuous monitoring. |
| fda-gmlp-2021 | Good Machine Learning Practice for Medical Device Development: Guiding Principles | Joint principles (FDA, Health Canada, MHRA) | 10 principles | Oct. 27, 2021 | Principles 2, 4, 7, 8, 10 cover software engineering, train/test independence, human-AI team performance, clinically relevant testing, and deployed-model monitoring. The V&V and human-team backbone of the gate. |
| fda-transparency-2024 | Transparency for Machine Learning-Enabled Medical Devices: Guiding Principles | Joint principles | 6 principles | June 2024 | Lifecycle transparency on who, what, where, when, why, and how, communicated to users. Supports disclosing uncertainty and credibility evidence to surgeons and patients before robot action. |

## B. Computational model credibility, the strongest VVUQ precedent

| Key | Document | Type | FR or standard | Date / status | Substance for the gate |
|:--|:--|:--|:--|:--|:--|
| fda-credibility-2023 | Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions | Final guidance | FR Doc. 2023-25470 | Final, Nov. 17, 2023 | FDA's risk-informed credibility framework: model risk equals model influence times decision consequence, with V&V activities proportionate to risk. The single most transplantable precedent for a statutory VVUQ mandate. |
| asmevv40 | ASME V&V 40-2018, Assessing Credibility of Computational Modeling through Verification and Validation: Application to Medical Devices | Consensus standard (FDA-recognized) | ASME V&V 40-2018 | Published 2018; recognized | The credibility methodology the FDA guidance incorporates; supplies the model-risk to required-rigor grading the bill operationalizes. Held in standards-and-literature.bib (see file 09). |
| fda-ai-drugs-2025 | Considerations for the Use of AI To Support Regulatory Decision-Making for Drug and Biological Products | Draft guidance | FR Doc. 2024-31542 | Draft, FR availability Jan. 7, 2025; comments closed Apr. 7, 2025 | A seven-step, risk-based credibility-assessment framework keyed to the model context of use, parallel to ASME V&V 40 logic. Supplies the trial-conduct vocabulary for oncology studies that also deploy robots. |

## C. The device boundary and clinical decision support

| Key | Document | Type | FR or citation | Date / status | Substance for the gate |
|:--|:--|:--|:--|:--|:--|
| fda-cds-2022 | Clinical Decision Support Software | Final guidance | FR Doc. 2022-20993 | Final, Sept. 28, 2022 | Interprets the § 520(o)(1)(E) non-device CDS criteria; real-time, non-independently-reviewable, treatment-driving outputs are devices. |
| fda-cds-2026 | Clinical Decision Support Software (updated final, current) | Final guidance | FDA media 191560 | Issued Jan. 6, 2026; re-issued Jan. 29, 2026; town hall Mar. 11, 2026 | Sharpens "medical information about a patient" without changing the statutory criteria. The current controlling CDS version. A surgical humanoid that drives and executes treatment cannot claim the CDS exclusion. |
| fda-samd-program | Software as a Medical Device (SaMD) and IMDRF risk categorization | Framework | IMDRF SaMD WG | Adopted; ongoing | Four-tier risk framework. A surgical-humanoid oncology system is Category IV (critical condition, treat or diagnose), the highest evidentiary tier. |

Boundary rule for the bill: under 21 U.S.C. § 360j(o) (file 01), some clinician-informing
software is non-device, but a humanoid that autonomously generates and executes
motion on a patient is unambiguously a device, so a VVUQ mandate applies squarely.

## D. Premarket pathways and the quality system (device CFR)

| Key | Citation | Title | Status | Substance for the gate |
|:--|:--|:--|:--|:--|
| cfr-part860 | 21 CFR Part 860 | Classification procedures, including De Novo (Subpart D) | Current | Pathway for a novel low-to-moderate-risk component with no predicate; the natural place to write a VVUQ special control. |
| cfr-part814 | 21 CFR Part 814 | Premarket Approval (PMA) | Current | The Class III pathway most apt for a high-risk autonomous surgical humanoid; where a pre-execution VVUQ requirement would attach. |
| fr-qmsr-2024 | FR Doc. 2024-01709; 21 CFR Part 820 | Quality Management System Regulation (QMSR), incorporating ISO 13485:2016 | Final Feb. 2, 2024; effective Feb. 2, 2026 | Now mandates design verification, design validation, software validation, and lifecycle risk management. The live quality scaffold a 2026 trial sponsor already meets; the bill can be a special control bolted onto QMSR. |

## E. Inventory, oncology, and governance venues

| Key | Item | Date / status | Substance for the gate |
|:--|:--|:--|:--|
| fda-ai-device-list | AI-Enabled Medical Device List (CDRH) | Live; about 1,200 authorizations by mid-2025 | Authorizations are overwhelmingly diagnostic SaMD; none are autonomous physical or surgical actuators. This gap is the central justification for the bill. |
| fda-dhac | Digital Health Advisory Committee | First meeting Nov. 20 to 21, 2024 (generative AI device TPLC); second Nov. 6, 2025 | The body likely to review a Physical AI VVUQ framework; reinforces the models-change-after-authorization rationale. |
| fda-oce | Oncology Center of Excellence and Real-Time Oncology Review | Standing | Cross-center coordinator and the natural FDA home for oversight of AI and robotics in oncology trials. |
| fda-project-optimus | Project Optimus dose-optimization guidance | FR Doc. 2024-17771, Aug. 9, 2024 | Drug-dosing analogue, not device authority: rigorous pre-specified evidence before locking a treatment parameter. Cite for framing only. |
| fda-crosscenter-2024 | How CBER, CDER, CDRH, and OCP Are Working Together on AI | Mar. 15, 2024 | The cross-center governance architecture the bill plugs into. |
| fda-elsa-2025 | Elsa internal generative AI tool and CDER AI Council | Launched mid-2025; agentic expansion 2025 to 2026 | Precedent that FDA itself governs agentic AI with built-in human oversight, a principle the bill imposes on sponsors. |

## Where existing FDA law stops and the bill begins (ASCII)

```
  FDA today                              The bill adds
  -----------------------------------    --------------------------------------
  PCCP: validate a change, voluntary,    Automated VVUQ, mandatory and ex ante,
  submission-based, post-authorization   on every newly generated code path
        |                                        |
  CM&S credibility (ASME V&V 40):        Explicit Uncertainty Quantification
  risk-graded V and V for models    -->  prong + a pre-generation/pre-execution
        |                                gate for robot-patient interaction code
  GMLP + transparency principles:        Surgical-humanoid scope (Category IV),
  human-AI team, monitoring, bias        continuous re-run before execution,
        |                                hash-chained audit trail
  QMSR (Part 820): design V and V        A device-specific special control that
  and software validation baseline  -->  names the gate as a condition of use
```

## Crosswalk to prior-bill provisions

| Prior-bill element | FDA anchor | Use in the new draft |
|:--|:--|:--|
| Verification before generation | fda-pccp-2024; fda-credibility-2023; asmevv40 | Frame the gate as a risk-graded credibility discipline applied before code generation. |
| Ten gate thresholds bound to standards | fda-credibility-2023; fda-gmlp-2021 | Tie each threshold to a recognized credibility factor and GMLP principle. |
| Documentation and attestation | fr-qmsr-2024; fda-aidsf-lifecycle-2025 | Map filings to QMSR design controls and the lifecycle submission content. |
| Cybersecurity and human oversight | fda-gmlp-2021; fda-transparency-2024 | Ground human-AI team performance and transparency duties. |
| Device classification of the platform | cfr-part814; cfr-part860; fda-samd-program | State that the humanoid is Category IV, PMA or De Novo, not CDS-excluded. |

## Correlations to other VVUQ-04 files

1. File 01 supplies the statutes (§§ 360c, 360e, 360e-4, 360j(o)) these guidances implement.
2. File 03 (ONC transparency) and file 04 (CMS payment) cover the non-FDA federal layers.
3. File 09 (VVUQ standards) holds ASME V&V 40, IEC 62304, ISO 14971, and the robotics-safety standards the gate binds to.
4. File 10 (crosswalk) consolidates the device-classification language into the bill's statutory text.

## Bibliography pointer

FDA guidance, the QMSR rule, and the device CFR parts are carried in
federal-regulations-guidance.bib under the keys in the first column (for example
fda-pccp-2024, fda-credibility-2023, fr-qmsr-2024, cfr-part814). The consensus
standard asmevv40 is carried once in standards-and-literature.bib (file 09) and
referenced here, so no URL is duplicated across the bibliography set.
