## output-instruct-bill

This is the narrative output of the instruct-bill step. It explains what was
produced, the legal reasoning behind the structure, the key findings through
May 31, 2026, the corrections applied, and how the set positions the next pass to
draft a more current and relevant version of the *VVUQ Physical AI Oncology Trial
Bill* (H.R. 9510, Draft 1.0; prior bill DOI 10.5281/zenodo.20454870). The 10
markdown files, the 5 BibTeX bibliographies, and the README are the deliverables;
this file is the connective summary, not a copy of them.

### 1. What was built and why it is organized this way

The prompt asked for U.S. medical AI law summaries that make the prior bill (a)
current, (b) grounded in mass-adopted law, (c) aware of emerging bills as research
influences only, and (d) streamlined to a structured, XML-ready law format. I
split the legal landscape into ten domains, one markdown file each, so that the
next pass can pull exactly the authority a given bill section needs without
rereading the whole corpus:

1. File 01 holds the standing statutes (the Acts of Congress). It is the floor:
   everything else implements or amends it.
2. Files 02 to 05 hold the federal agency layers that implement those statutes
   for AI specifically: FDA device regulation (02), ONC/ASTP algorithm
   transparency (03), CMS coverage and payment (04), and OCR and FTC privacy,
   security, and nondiscrimination rules (05).
3. File 06 holds the state laws, which are the human-over-AI and disclosure
   analogues a federal bill cites as mass-adopted practice.
4. Files 07 and 08 hold the executive actions and the emerging 119th Congress
   bills, kept deliberately separate because they are research influences, not
   operative authority.
5. File 09 holds the consensus standards, the clinical-trial regulations, and the
   oncology and autonomy literature that give the gate its technical credibility.
6. File 10 is the capstone: a research matrix that sorts every authority into
   operative text or memo-only matter, a bill-section map, and the structured law
   format and XML-readiness rules.

The five bibliographies follow the same domains so that each cited source lives in
exactly one file with no duplicate links: federal-statutes.bib, federal-
regulations-guidance.bib, state-laws.bib, executive-actions-and-emerging-bills.bib,
and standards-and-literature.bib.

### 2. The central legal finding that shapes the bill

The most important finding is a genuine gap. None of the roughly 1,200 AI devices
the FDA has authorized is an autonomous physical or surgical actuator; they are
overwhelmingly diagnostic software. No federal statute imposes a general
human-in-the-loop or automated-VVUQ requirement on AI that generates and executes
robot-patient interaction code. The closest existing mechanisms are:

1. The FDA Predetermined Change Control Plan authority (21 U.S.C. § 360e-4) and
   its December 2024 final guidance, which let the FDA pre-authorize AI device
   changes, but only voluntarily, by submission, and after authorization.
2. The FDA computational-model credibility guidance (November 2023), which
   operationalizes ASME V&V 40-2018 with a risk-graded verification and validation
   framework, but which expressly excludes standalone machine learning.
3. OMB M-25-21's high-impact AI minimums (pre-deployment testing, impact
   assessment, ongoing monitoring), which apply to federal agency use, not to
   private trials.

The bill's contribution is to make this discipline mandatory, ex ante, automated,
and specific to robot-patient interaction code, adding an explicit uncertainty
quantification prong and a pre-generation gate that none of the existing
instruments require. That is the throughline that file 10 carries into the
operative text and the findings.

### 3. Currency: what changed since the prior bill (goal a)

The prior bill cited four state laws and a core set of federal authorities. This
set adds the 2024 to 2026 developments that postdate it:

1. FDA: the PCCP final guidance (Dec. 2024), the January 2025 lifecycle and
   drug-AI draft guidances, the updated Clinical Decision Support guidance (Jan.
   2026), the Quality Management System Regulation effective February 2, 2026, and
   the FDA and EMA joint Good AI Practice principles (Jan. 14, 2026).
2. ONC/ASTP: the HTI-1 algorithm-transparency rule and, critically, the December
   2025 HTI-5 deregulatory proposal that would scale the transparency back, which
   is why the bill must be a freestanding statute.
3. CMS: the Medicare Advantage AI guardrail, the prior-authorization rule, the
   WISeR model that began January 1, 2026, and the March 2026 CPT autonomy-
   taxonomy revision.
4. Privacy and civil rights: the Section 1557 patient-care decision-support rule
   (§ 92.210, compliance May 1, 2025) and the January 2025 HIPAA Security Rule
   proposal.
5. State law: California AB 3030, SB 1120, and AB 489; Colorado SB 24-205 (now
   effective June 30, 2026); the Utah, Texas, and Illinois frameworks; and the
   2025 Maryland, Nebraska, and Nevada enactments.
6. Standards and evidence: IEEE 7009-2024, the ISO 10218 2025 revision, ICH
   E6(R3) adopted January 2025, and the 2024 to 2025 autonomous-surgery literature
   showing language-conditioned autonomous soft-tissue surgery is now demonstrated.

### 4. Grounding and the operative versus influence line (goals b and c)

File 10 draws a hard line. Operative text may cite only enacted statutes, in-force
rules, and recognized standards: the FD&C Act and PCCP authority, HIPAA and
Section 1557, the Medicare Advantage rule and the WISeR architecture, the ASME,
IEC, ISO, and IEEE standards, the clinical-trial regulations, and the state
human-over-AI laws as findings. Emerging bills (H.R. 238 on AI prescribing, S.
1399 on Medicare payment for algorithm-based services, H.Res. 694 on halting the
WISeR pilot) and executive actions (EO 14179, the AI Action Plan, the federal
preemption order) appear only in the policy memo, findings narrative, appendix,
testimony, or research matrix. This keeps the operative bill grounded while still
capturing the legislative momentum.

### 5. Structure and style for the XML conversion (goal d)

File 10, section D, specifies the structured law format: a designation and short
title, an enacting clause, then numbered sections with the standard
(a)(1)(A)(i)(I) hierarchy, findings, definitions, operative requirements, and an
effective-date section. The XML-readiness rules ask the next pass to keep one idea
per clause, nest the hierarchy strictly, avoid inline footnotes in operative text,
and keep citations in a consistent form so they map to elements. The visual rules
carry the prior bill family forward: the section symbol § for every reference,
single hyphens only, left-aligned body-width tables, black text, and no images.

### 6. Corrections applied

1. Antidiscrimination citations are placed in Title 42 or Title 29, never Title
   26: Title VI at 42 U.S.C. § 2000d, the ADA at 42 U.S.C. § 12101, Section 504 at
   29 U.S.C. § 794, and ACA Section 1557 at 42 U.S.C. § 18116.
2. The 510(k) pathway is cited as 21 U.S.C. § 360(k), distinct from § 360k (state
   preemption).
3. The machine-learning credibility standard is identified as ASME VVUQ 70 (in
   development); there is no ASME V&V 90 for machine learning.
4. The diagnostics VALID Act is flagged as not present in the 119th Congress (the
   VALID Act of 2025 bill numbers are an unrelated VA-loan bill), so the
   laboratory-developed-test status is cited via litigation and rulemaking.
5. Law and bill names are given in full and correct form: the Physicians Make
   Decisions Act (California SB 1120), the Texas Responsible Artificial
   Intelligence Governance Act (HB 149), the Wellness and Oversight for
   Psychological Resources Act (Illinois HB 1806), and the Colorado Artificial
   Intelligence Act (SB 24-205).

### 7. Bibliography design

The five .bib files use the proven house conventions: a bare doi field, a resolver
or canonical url, and a note that carries one sentence of relevance plus the
clickable link; no howpublished field; and each link used once across the set so a
later merge with the prior final paper yields no duplicate references. DOIs are
included for every standard, guideline, and article that has one (for example IEEE
7009-2024 at 10.1109/IEEESTD.2024.10582898, NIST AI RMF at 10.6028/NIST.AI.100-1,
and the npj Digital Medicine digital-twin VVUQ survey at
10.1038/s41746-025-01447-y). Statutes, rules, and standards without a DOI carry
their Cornell LII, govinfo, Federal Register, eCFR, or publisher URL.

### 8. How the next pass should proceed

Read file 10 first, then pull operative authority from files 01 to 06 and 09 and
framing from files 07 and 08, resolving every key against the five bibliographies.
Open the prior bill at papers/VVUQ-03/final-paper for the section structure to
update, apply the structured law format and the XML-readiness conventions, and
keep the emerging bills out of operative text. The result should be a bill that is
markedly more current, better grounded, and cleanly styled for the XML step, with
the VVUQ-before-generation gate framed as the mandatory, automated extension of
the FDA credibility and change-control discipline that existing law only partially
provides.

### 9. Process and compliance

The deliverables were committed one file at a time and pushed to the branch in
real time within a single pull request: ten markdown files, five bibliographies,
this output file, the prompt file, and the README, followed by an error-fix
consolidation commit and a final repository-updates commit (the main README,
releases.md, CHANGELOG.md v2.0.0, and CITATION.cff). All additions are Markdown
and BibTeX, outside the ruff, yamllint, and pytest surface, so the lint-and-format
CI job stays green across Python 3.10, 3.11, and 3.12. Only kevinkawchak/cancer-
automated is edited; no other repository is touched.
