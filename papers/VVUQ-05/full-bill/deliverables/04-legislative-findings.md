# Legislative Findings of Fact: H. R. 9510, the Verification Before Generation in Physical AI Oncology Trials Act of 2026

*Independent research draft. Not an enacted law, not pending legislation, and not legal advice; not endorsed by the FDA, HHS, or any Member of Congress.*

**Bill:** H. R. 9510 (illustrative number; the Clerk assigns the real number at introduction), 119th Congress, 2d Session. **Act:** the Verification Before Generation in Physical AI Oncology Trials Act of 2026. **Vehicle:** an amendment to the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.), current through Public Law 119-93.

This document reproduces the legislative findings of fact set out in section 2 of the bill. The findings are not operative commands; they supply the evidentiary and legal predicate a court or agency would consult when construing the Act, and they establish both the need for and the feasibility of the bill's central rule: that an automated verification, validation, and uncertainty quantification process must clear robot-patient interaction code before that code is generated or executed in a Physical AI oncology clinical investigation.

Congress finds the following:

(1) Physical AI oncology clinical investigations place autonomous and semi-autonomous robots in direct physical contact with patients, and the behavior of such a robot at the moment of contact is determined by software that is increasingly machine-generated.

(2) No Federal law requires the verification of robot-patient interaction code to clear before that code is generated or executed; a sponsor may generate the code, execute it, and document afterward, because the order of operations is not regulated.

(3) Embodiment raises the stakes from software quality to patient safety: in a disembodied pipeline an error yields a wrong number a human can catch downstream, while in an embodied surgical system the same error class yields a wrong motion a human cannot catch in time.

(4) The predetermined change control plan authority in section 515C of the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 360e-4) and the Food and Drug Administration final guidance on such plans for artificial intelligence-enabled device software functions are the closest existing analogues to validating a change before deployment, but each remains voluntary, submission-based, and neither automated nor required in advance of generation.

(5) The Quality Management System Regulation (part 820 of title 21, Code of Federal Regulations), effective February 2, 2026, and the electronic-records requirements of part 11 of such title supply quality and record-integrity scaffolding but do not impose a rule that verification precede generation.

(6) A recognized consensus standard, ASME V&V 40-2018, and the Food and Drug Administration guidance assessing the credibility of computational modeling establish a credibility framework, in which model risk is the product of model influence and decision consequence, that an automated gate can implement.

(7) Recognized consensus standards, including NASA-STD-7009A, IEEE Std 7009-2024, IEC 80601-2-77, ISO 14971, and ISO/TS 15066, supply the dispersion bounds, fail-safe requirements, and biomechanical contact limits to which such a gate may be bound.

(8) Automated verification of robot-patient interaction code is feasible today: a pipeline held the verification fraction at 1.0, accepting one candidate artifact and blocking five, and a ten-gate assurance suite over control software for a surgical humanoid cleared reproducibly from a fixed seed, each gate bound to a published external standard.

(9) Human-over-AI review is already widely adopted in State law, including the California Physicians Make Decisions Act (Senate Bill 1120), the Illinois Wellness and Oversight for Psychological Resources Act (House Bill 1806), the Texas Responsible Artificial Intelligence Governance Act (House Bill 149), and Maryland House Bill 820, each preserving a licensed human's authority over an artificial-intelligence-influenced decision.

(10) The strongest Federal precedent for mandatory human-over-AI oversight is the Medicare Advantage artificial-intelligence guardrail (section 422.101(c) of title 42, Code of Federal Regulations), under which an algorithm alone may not justify a coverage denial.

(11) Federal nondiscrimination law, including section 92.210 of title 45, Code of Federal Regulations, title VI of the Civil Rights Act of 1964 (42 U.S.C. § 2000d), and the Americans with Disabilities Act of 1990 (42 U.S.C. § 12101 et seq.), requires that a patient-facing algorithm minimize the risk of bias and respect accessibility.

(12) The artificial-intelligence taxonomy maintained by the American Medical Association, distinguishing assistive, augmentative, and autonomous functions, provides a graduated spine for matching verification rigor to the degree of autonomy of a device.

(13) A Physical AI system is at once a medical product and a research tool, and a requirement that verification precede generation is agnostic to that classification, because whatever the system is called, its patient-facing code must clear the gate before it runs.

(14) As clinical investigation moves toward real-time and decentralized designs governed by harmonized good clinical practice, manual, document-by-document review cannot keep pace with the volume of machine-generated control code, and an automated gate that clears before generation serves rather than impedes that modernization.

## Sources and authorities

The following table maps each finding to the principal authority on which it rests, for auditability. Statutes, in-force rules, and recognized consensus standards carry the operative weight; demonstrated engineering results establish feasibility.

| Finding | Authority |
| --- | --- |
| (1) Robots in direct physical contact; behavior set by machine-generated code | National Physical AI platform record (VVUQ-01 through VVUQ-04 developments) |
| (2) No Federal rule on the order of operations | Absence of a verify-before-generate mandate in Title 21; VVUQ-01 pipeline record |
| (3) Embodiment raises stakes from quality to safety | VVUQ-01 method and pipeline record |
| (4) Closest analogues are voluntary and after-the-fact | FDCA § 515C (21 U.S.C. § 360e-4); FDA final PCCP guidance for AI-enabled device software functions |
| (5) Quality and record-integrity scaffolding, not sequencing | Quality Management System Regulation (21 CFR part 820, eff. Feb. 2, 2026); 21 CFR part 11 |
| (6) Credibility framework an automated gate can implement | ASME V&V 40-2018; FDA computational-modeling credibility guidance |
| (7) Dispersion bounds, fail-safe, and contact limits to bind a gate | NASA-STD-7009A; IEEE Std 7009-2024; IEC 80601-2-77; ISO 14971; ISO/TS 15066 |
| (8) Automated verification is feasible today | VVUQ-01 (verification fraction 1.0; 1 accept, 5 block); VVUQ-02 (ten-gate surgical-humanoid suite, fixed seed) |
| (9) Human-over-AI review widely adopted in State law | CA SB 1120; IL HB 1806; TX HB 149 (TRAIGA); MD HB 820 |
| (10) Strongest Federal human-over-AI precedent | Medicare Advantage AI guardrail (42 CFR § 422.101(c)) |
| (11) Nondiscrimination and accessibility duties | 45 CFR § 92.210; Title VI (42 U.S.C. § 2000d); ADA (42 U.S.C. § 12101 et seq.) |
| (12) Graduated spine for matching rigor to autonomy | AMA AI taxonomy (assistive, augmentative, autonomous) |
| (13) Rule is agnostic to product-versus-tool classification | National Physical AI platform record |
| (14) Automated ex ante gate serves trial modernization | ICH E6(R3) harmonized good clinical practice |

*The authorities in this document are research influences and grounding sources for the findings; only enacted statutes, in-force rules, and recognized standards carry operative weight in the Act. All supporting numbers are simulation or illustrative results reproducible from the deterministic seed 20260525, and no patient-identifiable information is included.*
