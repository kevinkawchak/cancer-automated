# One-Page Summary: H. R. 9510, the Verification Before Generation in Physical AI Oncology Trials Act of 2026

*Independent research draft. Not an enacted law, not pending legislation, and not legal advice; not endorsed by the FDA, HHS, or any Member of Congress.*

**Bill:** H. R. 9510 (illustrative number; the Clerk assigns the real number at introduction), 119th Congress, 2d Session. **Refer to:** House Committee on Energy and Commerce (Subcommittee on Health).

## The problem: a sequencing gap that embodiment makes dangerous

Physical AI oncology trials place autonomous and semi-autonomous robots in direct physical contact with patients, and the robot's behavior at the moment of contact is set by software that is increasingly machine-generated. No Federal law governs the order of operations. A sponsor may generate robot-patient interaction code, run it, and document the checks afterward, because nothing requires the verification to come first. Embodiment raises the stakes. In a disembodied data pipeline an error yields a wrong number a human can catch downstream; in an embodied surgical system the same error class yields a wrong motion no human can catch in time.

## The solution: verify before generate, in a new section 515D

The bill adds a new section 515D to the Federal Food, Drug, and Cosmetic Act (codified at 21 U.S.C. § 360e-5), inserted right after the predetermined change control plan authority (§ 515C, § 360e-4). The core rule: no robot-patient interaction code may be generated or executed in a Physical AI oncology clinical investigation unless an automated verification, validation, and uncertainty quantification (VVUQ) process, bound to named external standards, has first cleared, with the record documented and attested. A record created after generation or execution does not satisfy the section. Each gate must emit ACCEPT, BLOCK, or ESCALATE; the verification fraction must equal 1.0; each gate carries a validation-agreement floor and a coefficient-of-variation bound; and three gates (vascular no-fly, human collision, and fault or emergency stop) carry a hard catastrophe predicate at agreement 1.00. The section also sets readiness gates, documentation and attestation duties, cybersecurity and human-oversight requirements, nondiscrimination duties, and a rule of construction that preserves existing exemptions and reclassifies nothing.

## What it changes: ten conforming amendments

Ten targeted edits thread the new rule through Title 21 so it is enforceable and consistent: § 201(h)/321(h) (device definition), § 301/331 (prohibited acts), § 501/351 (adulteration), § 505F/355g (real world evidence), § 510(k)/360(k) (premarket notice), § 513/360c (special controls), § 515/360e (premarket approval), § 515C/360e-4 (change control plans), § 520(o)/360j(o) (clinical-decision-support exclusion), and § 521/360k (State law savings clause).

## The assurance evidence

The requirement is feasible today, demonstrated on the record. VVUQ-01 held the verification fraction at 1.0 across 51 of 51 tests, accepting 1 candidate and blocking 5, with 1 escalation. VVUQ-02 cleared all 10 gates over a surgical-humanoid control codebase: 172 of 172 tests, 32 of 32 sweep iterations, composite mean 93.56, reproducible from deterministic seed 20260525.

## In-force analogues

The approach builds on tools Congress and the agencies already use: the § 515C predetermined change control plan authority and the FDA's final PCCP guidance for AI-enabled device software (the closest analogues, but voluntary and after-the-fact); the Quality Management System Regulation (21 CFR part 820, effective February 2, 2026) and 21 CFR part 11 record-integrity rules; and, for mandatory human-over-AI oversight, the CMS Medicare Advantage guardrail at 42 CFR 422.101(c).

## Cost

Rulemaking only. The bill directs final regulations within 365 days under § 515D(h) and creates no new spending program, so it is expected to be PAYGO neutral.

## The ask

A House sponsor to introduce H. R. 9510 and refer it to Energy and Commerce. Effective date: the first day of the first calendar quarter beginning at least 1 year after enactment, with a 180-day transition for investigations already enrolling.

*Author: CEO Kevin Kawchak, ChemicalQDevice (ORCID 0009-0007-5457-8667). AI-assisted (Claude Code Opus 4.8). DOI 10.5281/zenodo.xxxxxxxx.*
