# Policy Memo: Verify Robot Code Before It Touches a Patient (H. R. 9510)

*Independent research draft. Not an enacted law, not pending legislation, and not legal advice; not endorsed by the FDA, HHS, or any Member of Congress.*

**TO:** Health policy staff, Member of the House Committee on Energy and Commerce (Subcommittee on Health)
**FROM:** ChemicalQDevice
**DATE:** June 3, 2026
**RE:** H. R. 9510, the Verification Before Generation in Physical AI Oncology Trials Act of 2026 (illustrative)

This memo lays out one specific safety gap in how artificial intelligence is now used in cancer trials, explains why current law does not close it, and describes a narrow, low-cost bill that would. It is written so a non-engineer can read it in a few minutes and brief the Member.

## The problem

Cancer trials are starting to put robots in direct physical contact with patients: surgical humanoids that cut and suture, positioning systems that hold a patient during treatment, platforms that place biopsy or delivery needles, and supportive systems that monitor and assist. What a robot does at the instant it touches a patient is decided by software, and that software is increasingly written by AI in real time rather than typed line by line by a human engineer.

Here is the gap. No Federal law governs the order of operations. A trial sponsor may generate the robot-patient interaction code, run it on a patient, and document the safety checks afterward, in whatever order it likes, because the order is not regulated. We call this the sequencing gap.

Sequence matters because of embodiment. In an ordinary data pipeline, a software error produces a wrong number a human can catch downstream before anyone is harmed. In an embodied surgical system, the same class of error produces a wrong physical motion a human cannot catch in time, because one moving body concentrates every failure mode into a single instrument acting in real time. Checking the code after it has already moved is, in this setting, checking too late.

## Why current law is not enough

The existing framework is substantial, and this bill builds on it rather than replacing it. But every piece of it stops just short of requiring verification before the code is generated.

- The closest analogue is the predetermined change control plan (PCCP) authority Congress added in 2022 at section 515C of the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 360e-4), together with the FDA's final PCCP guidance for AI-enabled device software functions (December 4, 2024). That authority lets the FDA pre-authorize a planned change before it ships, which is the right idea. But it is voluntary, it is submission-based, it runs on the FDA's review clock, and it is not required in advance of generating new code.
- The Quality Management System Regulation (21 CFR part 820, effective February 2, 2026) and the electronic-records rule (21 CFR part 11) supply quality and record-integrity scaffolding. They make a verification record trustworthy; they do not require the verification to come first.
- For mandatory human-over-AI oversight, the strongest Federal precedent is the CMS Medicare Advantage guardrail (42 CFR § 422.101(c)): AI may assist a coverage decision, but a human must make the call on the patient's individual facts. That rule governs how a payer decides a claim, not how a robot's code is cleared before it acts.
- Federal nondiscrimination law (45 CFR § 92.210, Title VI at 42 U.S.C. § 2000d, and the Americans with Disabilities Act at 42 U.S.C. § 12101 et seq.) requires that a patient-facing algorithm minimize the risk of bias and respect accessibility. It does not require that the algorithm be verified before it is generated.
- Several States have acted, but at the claims and utilization-review layer, not the robot-code layer: California's Physicians Make Decisions Act (SB 1120), Illinois HB 1806, the Texas Responsible Artificial Intelligence Governance Act (HB 149), and Maryland HB 820. These are sound human-in-the-loop measures, but no two are identical, and none reaches trial-conduct code; a sponsor operating across States cannot build one robot-patient code base against four divergent claims-layer regimes.

The pattern is consistent. The substantive content a verification gate would enforce already exists, scattered across these authorities. The one rule that makes verification a precondition of generation does not exist anywhere. That single missing rule is what H. R. 9510 supplies.

Why now: clinical investigation is moving toward real-time, decentralized, machine-generated control code. A real-time trial cannot wait weeks for a manual, document-by-document code review between procedures, and manual review already cannot keep pace with the volume of code a multi-site trial produces. The gap widens with every robot added to a site. An automated gate that clears before generation is not a brake on modernization; it is the only assurance that can run at the speed modernization now demands.

## The proposal

H. R. 9510 amends the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.), current through Public Law 119-93. It adds one new section, 515D, codified at 21 U.S.C. § 360e-5, placed immediately after the section 515C change-control authority (§ 360e-4) it most resembles.

The core rule is a single sequencing requirement: no robot-patient interaction code may be generated or executed in a Physical AI oncology clinical investigation unless an automated verification, validation, and uncertainty quantification (VVUQ) process, bound to named external standards, has first cleared for that interaction, with the record documented and attested. A record created after generation or execution does not satisfy the section; the timing of the record is itself the compliance fact.

The gate is concrete, not aspirational. Each check emits one of three results: ACCEPT, BLOCK, or ESCALATE (which returns the interaction to a qualified human). For each interaction the verification fraction must equal 1.0, meaning every verification check passes, with no partial credit, and each gate also carries a validation-agreement floor and a bound on run-to-run variation. Three gates carry a hard catastrophe predicate at perfect agreement: no breach of a vascular no-fly volume, a guaranteed minimum clearance from any human sharing the room, and a guaranteed safe state on fault or emergency stop. The thresholds are tied to recognized external standards, including ASME V&V 40-2018, NASA-STD-7009A, IEEE 7009-2024, IEC 80601-2-77, ISO 14971, and ISO/TS 15066, so the test is auditable rather than left to anyone's discretion.

The section also sets readiness gates for the site and each robot, documentation and attestation duties signed by a responsible officer, cybersecurity and human-oversight controls, and nondiscrimination duties, plus a rule of construction that preserves existing exemptions and reclassifies no device.

## Why it is feasible

This is not a hope; it has been run. In a first study (VVUQ-01), an automated pipeline held the verification fraction at 1.0 across 51 of 51 tests, accepting 1 candidate artifact, blocking 5, and escalating 1. In a second study (VVUQ-02), a ten-gate assurance suite over the control software for a surgical humanoid cleared 172 of 172 tests and 32 of 32 sweep iterations, composite mean 93.56, reproducibly from a fixed seed (20260525). The bill asks sponsors to do, as a precondition, what has already been demonstrated to work.

## Why it fits existing law

The bill is additive, not disruptive. It leaves the investigational-device exemption, human-subject protection (21 CFR part 50), and the IND framework (21 CFR part 312) in place. It frames the new gate as a pre-authorized change-control discipline of the kind section 515C already contemplates, and routes its records through the part 11 electronic-records rule and the part 820 quality system that 2026 sponsors already meet. It carries the CMS human-over-AI principle and Federal nondiscrimination norms into the gate as criteria, and adds a savings clause so the State human-in-the-loop laws above are preserved, giving those States a stable upstream rule to build on instead of a vacuum.

## Anticipated questions and answers

| Question | Answer |
|:--|:--|
| Does this create a new agency or program? | No. It adds one section to an existing statute the FDA already administers and directs rulemaking only. |
| What does it cost? | Rulemaking only, expected to be PAYGO neutral. The Secretary must issue final regulations within 365 days; the statute is self-executing in the meantime. |
| Will it slow down cancer research? | The opposite. Manual review already cannot keep pace with machine-generated code; an automated gate fits real-time, decentralized trials. |
| Is it technically possible to verify code before it runs? | Yes, demonstrated on the record (51 of 51 and 172 of 172 tests, verification fraction held at 1.0). |
| Does it preempt State law? | No. It adds a savings clause that preserves State human-in-the-loop and audit requirements. |
| Does it reclassify devices or disturb existing trial rules? | No. A rule of construction preserves the IDE exemption, part 50, part 312, and section 515C outside this context, and reclassifies nothing. |
| Why the FD&C Act and not a standalone law? | The substantive content already lives in device, privacy, and civil-rights authorities. Amending the FD&C Act adds the one missing sequencing rule with the least disruption. |

## Recommendation

We recommend that the Member consider introducing H. R. 9510 and refer it to the Committee on Energy and Commerce (Subcommittee on Health). It closes a narrow, well-defined, and growing safety gap with a proven, low-cost mechanism; it builds on tools the FDA and CMS already use; it preserves existing State protections; and it positions the United States to set the global standard for verifying surgical-robot software before that software ever touches a patient.

*Author: CEO Kevin Kawchak, ChemicalQDevice (ORCID 0009-0007-5457-8667). AI-assisted (Claude Code Opus 4.8). DOI 10.5281/zenodo.xxxxxxxx.*
