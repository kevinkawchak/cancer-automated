# 03 - ONC/ASTP Health IT Certification and Algorithm Transparency

Scope: the health IT certification rules issued by the Assistant Secretary for
Technology Policy and Office of the National Coordinator for Health Information
Technology (ASTP/ONC) that govern transparency for predictive algorithms in
certified health IT. The HTI-1 rule is the closest existing federal analogue to a
documentation-and-transparency regime for medical AI, and the proposed HTI-5
rollback is the most important 2026 caution for a bill that builds on it.

| Field | Value |
|:--|:--|
| File | 03 of 10 |
| Companion bibliography | federal-regulations-guidance.bib |
| Data current through | May 31, 2026 |
| Primary legal sources | federalregister.gov, ecfr.gov, healthit.gov, hhs.gov |
| Statute implemented | 21st Century Cures Act, information-blocking provisions (file 01) |

## Role in the bill update (points a through d)

1. Point a (currency): adds the HTI-1 through HTI-5 sequence (2024 to 2026),
   including the December 2025 deregulatory proposal absent from the prior bill.
2. Point b (grounding): the HTI-1 Decision Support Intervention (DSI) criterion,
   its 31 predictive source attributes, and its Intervention Risk Management (IRM)
   factors are a mass-adopted, ready-made template for the bill's documentation
   and transparency duties.
3. Point c (caution): HTI-5 would delete that template; the bill must therefore
   stand as a freestanding statutory requirement, not lean on the DSI criterion.
4. Point d (structure): the source-attribute list and IRM factors map directly to
   the bill's Algorithm Documentation and Attestation sections.

## A. The HTI rulemaking sequence

| Key | Rule | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| fr-hti1 | HTI-1: Certification Program Updates, Algorithm Transparency, and Information Sharing | 89 FR 1192; doc. 2023-28857; 45 CFR Part 170 | Published Jan. 9, 2024; effective Mar. 11, 2024; DSI compliance Jan. 1, 2025 | Created the DSI criterion (§ 170.315(b)(11)) replacing the 2012 CDS criterion. Defines Predictive DSI and requires certified health IT to surface 31 source attributes for predictive DSIs and 13 for evidence-based DSIs, plus IRM practices. |
| fr-hti2-tefca | HTI-2: Trusted Exchange Framework and Common Agreement | 89 FR 101772; doc. 2024-29163 | Published Dec. 16, 2024 | Codified TEFCA and a Manner Exception; background plumbing for nationwide exchange of trial and robot-interaction data. |
| fr-hti3 | HTI-3: Protecting Care Access | 89 FR 102512; doc. 2024-29683; 45 CFR Part 171 | Published Dec. 17, 2024 | Added a good-faith information-blocking exception. A useful drafting pattern for a trial-data carve-out that protects unvalidated AI output. |
| onc-hti4 | HTI-4: Electronic Prescribing, Real-Time Prescription Benefit, and Electronic Prior Authorization | 90 FR (within the FY2026 IPPS vehicle); doc. 2025-14681 | Published Aug. 4, 2025; staggered 2026 to 2028 | Finalized certification criteria for electronic prior authorization, the certified-EHR counterpart to the CMS prior-authorization rule in file 04. |
| fr-hti5 | HTI-5: ASTP/ONC Deregulatory Actions To Unleash Prosperity | 90 FR 60970; doc. 2025-23896 | Proposed Dec. 29, 2025; comments closed Feb. 27, 2026; not finalized as of May 31, 2026 | Would retire the legacy CDS criterion and scale back the DSI criterion, removing the model-card transparency, the source attributes, and the IRM elements, asserting no public evidence of patient benefit. The single most consequential item for the bill. |
| fr-hti2-withdrawal | HTI-2: Patient Engagement, Information Sharing, Public Health Interoperability (withdrawal of non-finalized balance) | 90 FR; doc. 2025-23890 | Withdrawn Dec. 29, 2025 | Confirms the deregulatory pivot: proposed AI and interoperability expansions are being rolled back, not extended. |
| cfr-part171 | Information Blocking | 45 CFR Part 171; Cures Act § 4004 | In effect; disincentives rule doc. 2024-13793 (July 1, 2024) | Constrains whether trial data and AI outputs must be shared; a VVUQ regime that withholds unvalidated output must fit a Part 171 exception. |

Agency note: ONC was retitled ASTP/ONC in July 2024 and gained department-wide
technology, data, and AI-policy roles (a Chief AI Officer among them); in March
2026 HHS narrowed the office back toward health-IT interoperability. The
transparency mandate is therefore contracting at the federal level, which is the
context the bill is drafted into.

## B. The HTI-1 IRM factors as a VVUQ template

The DSI Intervention Risk Management practice requires risk analysis and
mitigation across eight factors. These map almost one-to-one onto a VVUQ and
safety checklist for robot-patient interaction code.

| IRM factor (HTI-1) | VVUQ or safety analogue in the bill |
|:--|:--|
| Validity | Validation against external standards and clinical baselines |
| Reliability | Repeatability across the triple-simulation runs |
| Robustness | Behavior under perturbation and edge cases |
| Fairness | Nondiscrimination gate (file 05) |
| Intelligibility | Transparency of the gate decision to the surgeon |
| Safety | Catastrophe gates and fail-safe defaults (file 09) |
| Security | Hash-chained audit trail and cybersecurity (file 05) |
| Privacy | PHI handling under HIPAA (file 05) |

## C. The 31 source attributes as a documentation model

The predictive-DSI source attributes (the AI "nutrition label") group into
plain-language categories that the bill's Algorithm Documentation section can
adopt:

1. Identity and intended use of the intervention.
2. Development details: data source, variables, and training population.
3. Performance: validity, fairness, and validation process.
4. Maintenance: update cadence and ongoing monitoring.
5. Funding and developer conflicts.

```
  HTI-1 predictive-DSI nutrition label        Bill Algorithm Documentation
  -------------------------------------        -----------------------------
  identity + intended use            ------->  scope of the robot-patient code
  data source + training population  ------->  provenance of the training data
  validity + fairness + validation   ------->  VVUQ gate evidence (V, V, UQ)
  update cadence + monitoring        ------->  re-run before each new code path
  developer + funding disclosure     ------->  attestation and conflict block
```

## Crosswalk to prior-bill provisions

| Prior-bill element | ONC anchor | Use in the new draft |
|:--|:--|:--|
| Algorithm Documentation Requirements | fr-hti1 source attributes | Model the six-item filing duty on the predictive-DSI nutrition label. |
| Attestations and Compliance | fr-hti1 IRM practices | Map each attestation line to an IRM factor. |
| Transparency to the surgeon | fr-hti1 intelligibility attribute | Require the gate decision and uncertainty to be surfaced at the point of use. |
| Independence from a fragile baseline | fr-hti5 | Draft the duty as a freestanding statute so it survives the DSI rollback. |

## Correlations to other VVUQ-04 files

1. File 01 supplies the Cures Act information-blocking statute these rules implement.
2. File 04 (CMS) pairs HTI-4 electronic prior authorization with the CMS prior-authorization rule.
3. File 05 (privacy and nondiscrimination) holds the security, privacy, and fairness duties the IRM factors reference.
4. File 08 (emerging bills) and file 07 (executive actions) explain the deregulatory pressure behind HTI-5.
5. File 10 (crosswalk) folds the source attributes and IRM factors into the bill's documentation and attestation tables.

## Bibliography pointer

The HTI rules and the information-blocking part are carried in
federal-regulations-guidance.bib under fr-hti1, fr-hti2-tefca, fr-hti3,
onc-hti4, fr-hti5, fr-hti2-withdrawal, and cfr-part171. The Cures Act statute is
in federal-statutes.bib (pl-cures), referenced but not duplicated here.
