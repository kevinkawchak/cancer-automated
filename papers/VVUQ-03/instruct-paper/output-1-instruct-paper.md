## output-1-instruct-paper

### ChatGPT 5.5 Thinking Extended
Author Rating: 8.5, Verbose, basic details (web search Off)

Below, “code” can mean two different things. Computer source code is almost never attached to a U.S. bill or enacted medical-AI law as the thing the law legally depends on. Legal code—the U.S. Code, Code of Federal Regulations, state codes, and existing Acts—is constantly referenced and amended.

Bottom line

For U.S. medical-AI legislation, the binding artifact is almost always legislative text, not executable software. A bill can amend the Federal Food, Drug, and Cosmetic Act, the Social Security Act, the Public Health Service Act, or a state health/safety/insurance code; it can direct FDA, HHS, CMS, ONC, NIH, or state regulators to issue rules or guidance; and it can require documentation such as audit policies, disclosures, risk assessments, SBOMs, validation evidence, or FDA submissions. But the source code of an AI model is not normally filed with Congress or attached to the statute.

The closest “code-like” dependencies appear after legislation, at the regulatory or product-submission stage. For FDA-regulated AI medical-device software, FDA may expect documentation on datasets, validation, cybersecurity, architecture, SBOMs, and predetermined change control plans. FDA’s cybersecurity guidance says manufacturers should maintain custodial control of device source code, such as escrow or backups, but source code is not required in premarket submissions.  

1. What can legislation legally depend on?

A medical-AI bill or law may depend on several categories of text or external material:

Category	Is it usually attached to the bill?	Can it be legally operative?	Example in medical AI
Bill/statutory text	Yes	Yes	A bill amending the FD&C Act to define AI-enabled prescribing, utilization review, or device review
Existing legal code/statutes	Referenced, not attached	Yes	“Amend section 520 of the FD&C Act…” or “amend title XVIII of the Social Security Act…”
Definitions from other statutes	Referenced	Yes	“AI” by cross-reference to 15 U.S.C. 9401 or FD&C Act definitions
Technical standards	Usually not in bill text; may be incorporated later by regulation	Sometimes, if properly incorporated	IEC/ISO/NIST-type standards in FDA or HHS rules
Agency guidance	Not legally binding unless tied to statute/regulation	Usually nonbinding guidance	FDA AI-device guidance, FDA PCCP guidance
Computer source code	Almost never attached to a bill/law	Rarely, and not typical	Manufacturer-controlled source code, SBOM, model documentation in FDA review
AI model weights/datasets	Not legislative attachments	May be reviewed or documented in product regulation	Training, tuning, test data summaries; validation; bias analysis
Dockets/comments/hearing record	Not statutory text	Informative record, not the law itself	Public comments, technical assistance, testimony, CBO estimate

The House drafting guide makes the legal-text point clearly: bills and joint resolutions are the vehicles used for making law, and legislative drafting is built around forms of legislation, statutory organization, amendatory language, definitions, findings, effective dates, and similar legal-text conventions.  

2. “Code” as legal code: yes, constantly

Medical-AI bills usually work by amending existing law. The House Office of Legislative Counsel explains that if a U.S. Code title is positive law, drafters cite or amend the Code section; if it is not positive law, they cite or amend the underlying statute, often with a U.S. Code parenthetical for reader convenience.  

That matters because many health laws are built on older statutory frameworks. For example, medical AI bills may amend or reference the FD&C Act, Social Security Act, Public Health Service Act, HIPAA-related provisions, Medicare payment provisions, or state health-insurance/utilization-review statutes. The “dependency” is not a code repository; it is the existing statutory architecture.

3. “Code” as computer code: generally no, but product regulation may require technical artifacts

At the bill stage, Congress is not reviewing or attaching model source code. At the medical device stage, FDA may review software documentation, risk management, architecture, data practices, validation, cybersecurity, and SBOMs. FDA’s eSTAR is an interactive PDF used to structure medical-device submissions; 510(k) and De Novo submissions generally must use eSTAR unless exempted, while PMA, Pre-Submissions, IDE, and 513(g) requests are voluntary uses.  

FDA’s cybersecurity guidance distinguishes source-code custody from source-code submission. It recommends that manufacturers maintain source-code custody through methods such as escrow or backups, but says source code is not required in premarket submissions. Instead, submissions should include plans for updating or replacing third-party software components if support ends or issues arise.  

For cyber devices, the stronger dependency is usually an SBOM, not raw source code. FDA recommends SBOM documentation in premarket submissions and says SBOMs are required for cyber devices under FD&C Act section 524B(b)(3). FDA also recommends machine-readable SBOMs consistent with NTIA minimum elements, plus support status and end-of-support date for software components.  

4. External technical standards can become binding through incorporation by reference

If an agency wants a regulation to legally depend on an external standard, specification, or similar material, it can use incorporation by reference. Under 1 CFR Part 51, eligible material must be published data, criteria, standards, specifications, techniques, illustrations, or similar material; it must be reasonably available and usable by the affected class.  

Important limitation: incorporation by reference is tied to the specific approved edition. Future amendments or revisions are not automatically included. That makes “depend on a live GitHub repo” or “always use the latest model code” a poor fit for traditional incorporation-by-reference lawmaking.  

For final rules, the agency must request formal approval, discuss availability, summarize the material, use proper incorporation language, and ensure a copy is on file with the Office of the Federal Register. The incorporation language must say “incorporated by reference,” identify the title/date/edition/author/publisher/identifier, state that the publication is a requirement, and explain where it can be examined and obtained.  

5. What is needed throughout bill development?

A. Policy development before drafting
Usually needed:
•	Policy memo or concept paper.
•	Problem statement and current-law gap.
•	Current-law research: FD&C Act, Medicare, PHSA, HIPAA, state insurance/medical-practice law, civil-rights/nondiscrimination law.
•	Stakeholder materials: health systems, clinicians, patient groups, AI developers, payers, device makers, regulators.
•	Technical definitions: AI, generative AI, algorithm, high-risk AI, AI-enabled device software function, clinical decision support, utilization review tool.
•	Implementation choices: disclosure, auditability, human review, FDA review, CMS reimbursement, grant program, reporting duty, enforcement authority.
•	Budget/funding plan and any offsets.
•	Section-by-section explanation.
•	Draft statutory text
Not usually needed: executable code, model weights, training datasets, or Git repositories.

B. Formal drafting

Legislative counsel converts the concept into legal text. The Senate Office of Legislative Counsel says it drafts bills, resolutions, amendments, markups, and conference reports, and helps incorporate proposals into existing law while identifying legal or constitutional concerns.  

For a medical-AI bill, the drafter typically needs:
•	Existing statutory target: FD&C Act, Social Security Act, PHSA, state insurance code, etc.
•	Definitions and scope.
•	Who is regulated: provider, insurer, developer, deployer, manufacturer, federal agency.
•	What AI uses are covered: diagnosis, prescribing, triage, utilization review, patient communications, medical-device software, reimbursement, education, grants.
•	Duties: disclosure, validation, nondiscrimination, human review, appeal, audit access, reporting.
•	Enforcement: FDA, HHS OCR, CMS, FTC, state insurance department, attorney general, licensing board.
•	Effective date, transition period, rulemaking deadline.
•	Privacy/confidentiality carveouts.
•	Preemption and interaction with state law.
•	Reporting to Congress or public transparency requirements.

C. Introduction in Congress

For the House eHopper, the prepared documents include the bill or resolution, a constitutional authority statement for H.R. and H.J. Res., and an optional original-cosponsor form; documents need the Member’s signature or a staff authorization form.  

House eHopper format rules are very practical: PDF is preferred; if HOLC drafted the legislation, submit it as received without renaming or removing printed file names; edits are discouraged; and Word documents are required for legislation not drafted by HOLC.  

In the Senate, a bill ready for introduction can be delivered to the bill clerk’s desk when the Senate is in session; the sponsor signs the bill and may attach cosponsors on a separate form.  

D. Committee development

During committee work, the needed resources may include:
•	Hearing testimony and witness statements.
•	Technical assistance from FDA, HHS, CMS, ONC, NIH, FTC, NIST, or state agencies.
	•	Amendments and substitute text.
	•	Markup documents.
	•	Committee report.
	•	CBO cost estimate; CBO says it is required to produce a cost estimate for nearly every bill approved by a full House or Senate committee.  
	•	Letters of support/opposition.
	•	Section-by-section summary.
	•	Data, model-risk evidence, privacy analysis, civil-rights analysis, cybersecurity analysis.

Again, these materials may influence the bill, but they are not the law unless incorporated into the statutory text or later into regulations.

E. Publication and public formats

GovInfo says congressional bills are legislative proposals from the House and Senate, and that bill versions track the process from introduction through enrolled version. It provides published bill versions from the 103rd Congress forward and bulk bill text/summaries in XML.  

Actual bill pages often provide multiple public formats. For example, H.R. 238, the Healthy Technology Act of 2025, is available in PDF, text, XML, MODS, PREMIS, and ZIP formats, and its title says it would amend the FD&C Act to clarify that AI/ML technologies can qualify as a practitioner eligible to prescribe drugs if authorized by the state and FDA-approved/cleared/authorized.  

The House XML site also notes that legislation prepared in XML has been available starting in January 2004, and that U.S. Code XML, schema, user guides, and related files are available from the Office of Law Revision Counsel.  

6. Rulemaking and regulatory-submission format requirements

If the law requires FDA/HHS/CMS/another agency to issue regulations, the agency uses Federal Register drafting rules. The Office of the Federal Register’s Document Drafting Handbook explains transmission, format, and editorial requirements under the Federal Register Act and 1 CFR chapter I.  

The DDH includes technical restrictions for MS Word documents: remove active or embedded hyperlinks, auto-numbering, active macros, hidden data, fields, comments, and tracked changes; format tables using Word’s table tool rather than tabs.  

For public comments on Regulations.gov, the FAQ says commenters can attach up to 20 files, each up to 10 MB, with valid file types including common document, image, spreadsheet, presentation, text, XML, and PDF formats.  

7. FDA medical-AI product-submission artifacts

For AI-enabled medical-device software, the most important “attachments” are product-regulatory artifacts, not legislative attachments.

FDA’s AI PCCP guidance says a PCCP should describe planned AI-enabled device modifications, the methodology to develop, validate, and implement those modifications, and an impact assessment; FDA reviews the PCCP as part of a marketing submission so changes described in the authorized PCCP can be implemented without separate marketing submissions for each modification.  

FDA’s PCCP framework breaks that into three core pieces: Description of Modifications, Modification Protocol, and Impact Assessment. The Modification Protocol includes verification and validation activities, predefined acceptance criteria, and step-by-step implementation methods.  

For AI data, FDA distinguishes training, tuning, and test data, and expects test data to characterize performance, be independent of training/tuning data, and generally come from multiple sites different from training/tuning sources.  

The Modification Protocol should address data management, re-training practices, performance evaluation protocols, update procedures, communications/transparency to users, and real-world monitoring where applicable. FDA also describes data-management practices such as how data will be collected, annotated, curated, stored, retained, controlled, and used.  

FDA eSTAR technical requirements include using the dynamic PDF template, downloading rather than opening in-browser, using supported PDF software, keeping attachment names under 124 characters, respecting file-size limits, avoiding zip files, and using appropriate attachments such as Word documents, Excel sheets, MP4s, PDFs, images, DICOM/CDISC packages where applicable, and other supporting files.  

8. Prior laws and medical-AI examples: what resources were included?

Law/bill	What the text did	Resources included with/around text	Source-code attached?
21st Century Cures Act §3060	Amended FD&C Act software/device definitions and excluded certain software functions from “device” status	Statutory text, FDA guidance, examples, docket materials; FDA says §3060 amended FD&C Act §520 and removed certain software functions from device definition	No  
FDORA / CAA 2023 §3308	Added FD&C Act §515C for Predetermined Change Control Plans	Statutory text, FDA PCCP guidance, marketing-submission documentation: modifications, methodology, impact assessment	No  
FD&C Act §524B cyber-device requirements	Requires cybersecurity information for cyber-device premarket submissions	SBOM, vulnerability monitoring, update/patch processes, architecture views, risk controls	Source code maintained/escrowed, not submitted  
CA AB 3030	Requires AI-generated patient communications to include an AI disclaimer and instructions for direct communication with a health care provider	Bill text, legislative digest, compliance/disclaimer language	No  
CA SB 1120	Regulates AI/algorithm/software in health-plan utilization review; requires individual clinical information, no sole group-dataset reliance, no supplanting provider decisionmaking, audit access, policies, performance review, and licensed professional medical-necessity decisions	Bill text, policies/procedures, audit/compliance materials, periodic performance/outcome review	No direct source-code submission requirement stated in the cited text  
CO SB24-205	General high-risk AI consumer-protection law; may affect health contexts depending on deployment	Developer documentation, impact assessments, risk management program, notices, appeals/human review where feasible	No source-code attachment in bill summary  
Utah SB149	AI amendments with bill text, fiscal note, transmittal letters, committee amendments, hearing/debate materials	Official page includes introduced/amended/enrolled bill text plus related documents like fiscal note and amendments	No  
H.R. 238 Healthy Technology Act of 2025	Proposed FD&C Act amendment on AI/ML as eligible practitioner for prescribing if state-authorized and FDA-authorized	PDF, text, XML, metadata, ZIP; U.S. Code reference	No  
S. 1399 Health Tech Investment Act	Proposed Medicare payment changes for algorithm-based healthcare services	PDF, text, XML, metadata, ZIP; Social Security Act/U.S. Code reference	No  
H.R. 7381 HEALTH AI Act	Proposed NIH grant program for generative AI in health care	PDF, text, XML, metadata, ZIP; code references to existing statutes	No  
H.R. 6077 Healthcare Education in AI Literacy Act	Proposed PHSA amendment for AI education/training in medical profession	PDF, text, XML, metadata, ZIP; U.S. Code reference	No  

Practical answer

A U.S. medical-AI law can be legally dependent on statutory cross-references, defined terms, agency regulations, incorporated standards, and later FDA/CMS/HHS submissions. It is not normally dependent on a hidden or attached computer program. The deeper technical “attachments” appear after enactment: SBOMs, validation reports, risk assessments, data-management protocols, PCCPs, cybersecurity architecture diagrams, labeling, policies/procedures, audit materials, and public-comment dockets. Source code is usually controlled by the manufacturer, not submitted as legislative text.
