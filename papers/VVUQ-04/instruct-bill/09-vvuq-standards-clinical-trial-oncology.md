# 09 - VVUQ Standards and Clinical Trial and Oncology Law

Scope: the consensus standards, reporting guidelines, clinical-trial regulations,
and oncology programs that give the bill its technical credibility. These are the
external anchors the gate binds each threshold to, the same family the prior bill
used, refreshed and corrected through May 31, 2026.

| Field | Value |
|:--|:--|
| File | 09 of 10 |
| Companion bibliography | standards-and-literature.bib |
| Data current through | May 31, 2026 |
| Primary legal sources | ASME, IEC, ISO, IEEE, UL, NIST, eCFR, FDA, ICH, peer-reviewed literature |
| Correction carried | There is no ASME V&V 90 for machine learning; the ML standard is ASME VVUQ 70 (in development) |

## Role in the bill update (points a through d)

1. Point a (currency): adds the 2024 to 2026 items (IEEE 7009-2024, ISO 10218
   2025 revision, ICH E6(R3) adoption, the FDA-EMA joint AI principles, and the
   2024 to 2025 autonomous-surgery literature).
2. Point b (grounding): the credibility and robotics-safety standards are
   mass-adopted and FDA-recognized, anchoring each gate threshold.
3. Point c (influences): the reporting guidelines and digital-twin literature
   inform the research matrix and the methodology, not the operative text.
4. Point d (structure): supplies the definitions and the standards-binding table
   for the bill's statutory text.

## A. Computational model credibility and VVUQ

| Key | Standard | Year | What it grounds for the gate |
|:--|:--|:--|:--|
| asmevv40 | ASME V&V 40-2018, credibility of computational modeling for medical devices | 2018 | The keystone: model risk equals influence times decision consequence, with V&V rigor scaled to risk. The central credibility-commensurate-with-risk logic of the gate. |
| asmevv10 | ASME V&V 10-2019, V&V in computational solid mechanics | 2019 | Structural and kinematic verification of arm, end-effector, and tissue-contact force models. |
| asmevv20 | ASME V&V 20-2009 (R2021), V&V in computational fluid dynamics and heat transfer | 2009 (reaffirmed 2021) | Thermal and fluid aspects such as electrosurgical heating and ablation margins. |
| asmevvuq70 | ASME VVUQ 70, verification and validation of machine learning (in development) | In development | The ML-specific V&V standard, the most direct future anchor for AI robot-control code. Confirm publication status before citing as published. |
| nasastd7009 | NASA-STD-7009A, standard for models and simulations | 2016 | Treats uncertainty quantification as a first-class credibility factor (epistemic and aleatory), the basis for the gate dispersion bounds and a credibility-scoring rubric. |

## B. Autonomous-system fail-safe and safety case

| Key | Standard | Year | What it grounds |
|:--|:--|:--|:--|
| ieee7009 | IEEE Std 7009-2024, fail-safe design of autonomous and semi-autonomous systems | 2024 | Fail-safe behavior demonstrated before execution; the hand-back-to-human escalation rule. DOI 10.1109/IEEESTD.2024.10582898. |
| ul4600 | ANSI/UL 4600 (Edition 3, 2023), safety for the evaluation of autonomous products | 2023 | A claim-based safety case (claims, argument, evidence); the structured artifact the gate produces and checks. |

## C. Robotic surgery, medical electrical, and functional safety

| Key | Standard | Year | What it grounds |
|:--|:--|:--|:--|
| iec8060127 | IEC 80601-2-77:2019 (with Amd 1:2023), robotically assisted surgical equipment | 2019 | The dedicated surgical-robot safety standard; defines the essential performance the VVUQ protects. |
| iec60601 | IEC 60601-1, medical electrical equipment, basic safety and essential performance | current edition | The single-fault safe-state requirement underlying the fault and e-stop paths. |
| iec62304 | IEC 62304, medical device software life cycle processes | 2006 (Amd 1:2015) | Software safety classification (A, B, C) and life-cycle verification; its sole normative reference is ISO 14971. |
| iso14971 | ISO 14971:2019, application of risk management to medical devices | 2019 | The master risk-management process; the gate is a risk-control measure under ISO 14971. |
| iso13849 | ISO 13849-1, safety-related parts of control systems | 2023 | Performance levels for the protective-stop and force-limiting control path. |
| iso10218 | ISO 10218-1 and -2, safety requirements for industrial robots | 2011; 2025 revision | Speed and separation monitoring and safety-rated stops; the 2025 revision integrates ISO/TS 15066. |
| isots15066 | ISO/TS 15066:2016, collaborative robots | 2016 | Power-and-force limiting and biomechanical pain and injury thresholds for robot-patient contact. |
| iso13482 | ISO 13482:2014, personal care robots | 2014 | Stability, collision avoidance, and fail-safe behavior for a close-contact humanoid. |
| iso9283 | ISO 9283:1998, manipulating industrial robots, performance criteria | 1998 | Pose accuracy, repeatability, and path accuracy; the measurable metrics the gate verifies. |

## D. AI-specific governance and trustworthiness

| Key | Standard or framework | Year | What it grounds |
|:--|:--|:--|:--|
| isoiec42001 | ISO/IEC 42001:2023, AI management system | 2023 | The organizational layer that operates the gate: policy, roles, internal audit, continual improvement. |
| isoiec23894 | ISO/IEC 23894:2023, AI risk management guidance | 2023 | The AI-specific risk process running inside the management system: bias, robustness, failure modes. |
| isoiec24028 | ISO/IEC TR 24028:2020, overview of trustworthiness in AI | 2020 | The property catalog (transparency, robustness, reliability, safety, security, privacy) the bill can enumerate as VVUQ-checkable. |
| nist-airmf | NIST AI Risk Management Framework 1.0 (AI 100-1) | 2023 | The Govern, Map, Measure, Manage functions; the Measure function is the VVUQ home. DOI 10.6028/NIST.AI.100-1. |
| nist-genai-profile | NIST AI 600-1, Generative AI Profile | 2024 | A generative-AI risk taxonomy for VVUQ test design where the robot uses generative planning or perception. |

## E. AI clinical-study reporting guidelines

| Key | Guideline | Year | What it grounds | DOI |
|:--|:--|:--|:--|:--|
| tripodai | TRIPOD+AI, reporting of clinical prediction models using ML | 2024 | Reporting completeness for any predictive model in the surgical AI. | 10.1136/bmj-2023-078378 |
| decideai | DECIDE-AI, early-stage clinical evaluation of AI decision-support | 2022 | First-in-human and early-trial reporting most relevant to a first surgical-humanoid oncology trial. | 10.1038/s41591-022-01772-9 |
| spiritai | SPIRIT-AI, trial protocols for AI interventions | 2020 | Protocol-level disclosure of AI version, inputs, outputs, and human-AI interaction. | 10.1038/s41591-020-1037-7 |
| consortai | CONSORT-AI, trial reports for AI interventions | 2020 | Results-level disclosure of AI interventions. | 10.1038/s41591-020-1034-x |
| claim | CLAIM, checklist for AI in medical imaging (2024 update) | 2020; 2024 | Perception and imaging-model reporting for surgical vision and guidance. | 10.1148/ryai.240300 |

## F. Clinical-trial regulatory framework

| Key | Item | Citation or status | What it grounds |
|:--|:--|:--|:--|
| cfr-part312 | Investigational New Drug Application | 21 CFR Part 312 | The legal vehicle under which an oncology trial and its VVUQ gate operate. |
| cfr-part50 | Protection of human subjects, informed consent | 21 CFR Part 50 | Patient-protection and disclosure of robot autonomy. |
| cfr-part56 | Institutional Review Boards | 21 CFR Part 56 | Independent ethics oversight of the trial. |
| cfr-part11 | Electronic records and electronic signatures | 21 CFR Part 11 | Record integrity for the gate's logs and generated-code records. |
| iche6r3 | ICH E6(R3) Good Clinical Practice | Adopted Jan. 6, 2025; FDA final guidance Sept. 2025 | The risk-based, quality-by-design GCP backbone a VVUQ gate mirrors. |
| iche8r1 | ICH E8(R1) general considerations for clinical studies | Step 4, Oct. 6, 2021 | Quality by design and critical-to-quality factors. |
| iche9r1 | ICH E9(R1) statistical principles, estimands addendum | FDA final May 2021 | Rigorous definition of the treatment effect and endpoints. |
| fda-dct-2024 | FDA guidance, conducting clinical trials with decentralized elements | Sept. 18, 2024 | Remote and automated trial-conduct safeguards; expects Part 11-compliant systems. |
| fda-ema-2026 | FDA and EMA joint Guiding Principles of Good AI Practice in Drug Development | Jan. 14, 2026 | Ten high-level principles across the medicines lifecycle; the most current federal framing for the findings section. |

The FDA computational-model credibility guidance and the FDA AI-for-drugs draft
are carried in federal-regulations-guidance.bib (file 02) under fda-credibility-2023
and fda-ai-drugs-2025, referenced here as the regulatory bridge to ASME V&V 40.

## G. Oncology programs and autonomous-surgery evidence

| Key | Item | Year | What it grounds | DOI |
|:--|:--|:--|:--|:--|
| fda-oce | FDA Oncology Center of Excellence | 2017 | The institutional home for an oncology-specific gate. | n/a |
| fda-project-optimus | Project Optimus, dose optimization | 2021 | Rigorous pre-specified evidence before locking a treatment parameter; an in-silico dose model needs VVUQ. | n/a |
| fda-project-orbis | Project Orbis, concurrent multinational review | 2019 | International review alignment for an oncology trial. | n/a |
| yang2017autonomy | Yang et al., levels of autonomy in medical robotics | 2017 | The 0 to 5 autonomy taxonomy scoping which systems trigger the gate and how strictly. | 10.1126/scirobotics.aam8638 |
| lee2024lasr | Lee et al., levels of autonomy in FDA-cleared surgical robots | 2024 | Empirical baseline: cleared robots are overwhelmingly Level 1, so a higher-autonomy humanoid trial is genuinely novel. | 10.1038/s41746-024-01102-y |
| kim2025srth | Kim et al., SRT-H hierarchical framework for autonomous surgery | 2025 | The 2025 state of the art: language-conditioned autonomous soft-tissue surgery is demonstrated, the capability the bill anticipates. | 10.1126/scirobotics.adt5254 |
| sel2025digitaltwin | Survey on VVUQ of digital twins for precision medicine | 2025 | The academic state of the art tying medical-AI VVUQ to ASME V&V 40 and NASA-STD-7009 thinking. | 10.1038/s41746-025-01447-y |

## Standards-to-gate binding (ASCII)

```
  Gate concern                         Anchoring standard(s)
  ----------------------------------   --------------------------------------
  Credibility scaled to risk       ->  ASME V&V 40; FDA credibility guidance
  Uncertainty quantification       ->  NASA-STD-7009A
  Fail-safe + safety case          ->  IEEE 7009-2024; UL 4600
  Surgical-robot essential perf.   ->  IEC 80601-2-77; IEC 60601-1
  Software life cycle + risk       ->  IEC 62304; ISO 14971; ISO 13849-1
  Human-contact force limits       ->  ISO/TS 15066; ISO 10218; ISO 13482
  Pose accuracy and repeatability  ->  ISO 9283
  AI governance + risk             ->  ISO/IEC 42001; 23894; NIST AI RMF
  Trial conduct + record integrity ->  21 CFR 312/50/56/11; ICH E6(R3)
  Autonomy-level scoping           ->  Yang 0-5; LASR review; SRT-H evidence
```

## Crosswalk to prior-bill provisions

| Prior-bill element | Standards anchor | Use in the new draft |
|:--|:--|:--|
| Ten gate thresholds bound to standards | asmevv40, iec8060127, isots15066, iso9283, ieee7009 | Refresh each binding and add the 2024 to 2026 editions. |
| Uncertainty budget | nasastd7009 | Cite UQ as a first-class credibility factor. |
| Definitions of autonomy and VVUQ | yang2017autonomy; isoiec24028 | Update the autonomy taxonomy and trustworthiness vocabulary. |
| Trial conduct and audit | cfr-part11; iche6r3; fda-dct-2024 | Ground the audit trail and GCP posture. |
| Findings on feasibility | kim2025srth; lee2024lasr | Cite demonstrated autonomous soft-tissue surgery and the low-autonomy baseline. |

## Correlations to other VVUQ-04 files

1. File 02 (FDA) holds the credibility guidance and the device CFR that recognize these standards.
2. File 05 (privacy) shares the security and privacy properties enumerated in ISO/IEC TR 24028.
3. File 07 (strategy) holds the NIST framework family these standards complement.
4. File 10 (crosswalk) binds each standard to a specific bill provision and to the prior bill's gate table.

## Bibliography pointer

All standards, reporting guidelines, clinical-trial regulations, ICH guidelines,
the FDA-EMA joint principles, the oncology programs, and the autonomy literature
are carried in standards-and-literature.bib under the keys in the tables (for
example asmevv40, ieee7009, iso14971, iche6r3, yang2017autonomy, kim2025srth).
DOIs are included where they exist; statutes and standards without a DOI carry the
canonical publisher or eCFR URL. No link is duplicated across the bibliography set.
