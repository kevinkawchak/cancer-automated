## prompt-draft-bill

Write new amendment instructions based on kevinkawchak/cancer-automated/tree/main/papers/VVUQ-04/template-bill/LaTeX (includes select Public Law 119-93 (05/19/2026) Title 21 - Food and Drugs sections relevant to new physical ai oncology trials) that is based on cancer-automated/tree/main/papers/VVUQ-03/final-paper (for the prior bill context) and cancer-automated/tree/main/papers/VVUQ-04/instruct-bill (for additional law context). Do not include output-template-bill and prompt-template-bill. Output the new amendment instruction LaTeX files into cancer-automated/tree/main/papers/VVUQ-04/draft-bill, with a corresponding README. Each relevant current LaTeX file needs to be modified with your new instructions.

Each existing section from cancer-automated/tree/main/papers/VVUQ-04/template-bill/LaTeX must include the original text, with your instructions and exact directories/file names added directly under each section (each of the section tex files will increase in size).

Your instructions must ensure the new amendment will be a) up to date with today's medical AI laws and implement their relevant medical and technology complexities b) grounded with current and mass adopted medical law references and utilizes medical law context meaningfully, c) relevant to emerging bills as research influences, but the bills won't be used in the actual bill text (but potentially be used in a memo, appendix, testimony, or research matrix), d) streamlined to the structured amendment format.

Essentially, your new files should provide a significant head start so that a future Claude Code request utilizes your output files based on a)-d) from above to ultimately provide a current and substantially relevant amendment.

In later commits, update cancer-automated/blob/main/README.md repository structures, badges, ASCII diagrams and toc, and other affected areas in the repository (this is the only repository that needs to be edited). Add a short summary for this update above the previous summary using a similar number of characters. Don't include any images, mermaid diagrams, or colored images for main/README.

Each section must provide instructions in [brackets] that includes the exact cancer-automated repository directories and file names: what to process, how to process, how to use files together synergistically, etc. for future Claude Code Opus 4.8 1M Max processing. Do not process your own instructions for each of the paper sections, instead only provide the exact instructions, directories, and file names needed for Claude Code to process and provide an updated section for each instruction set in a future prompt. Do not generate or include any images.

It is important that your instructions specify that a comprehensive amount of context for each section be implemented, should exactly match standard amendment requirement instructions. In other words, the amendment instructions should ultimately yield a future publication quality amendment, and provide instructions that are not general or vague. Legislation instructions should look like a top human author wrote them. Do not approximate or shorten any of the required steps.

1 commit is required for each of the following (main.tex, .sty, .bib, and README); and 1 commit is required for each of the paper's .tex sections (1 .tex file per section) that each correspond to main.tex. Commit to branch after each commit is finished in real time - don't hold commits until the draft paper is finished. Don't insert all text into one file. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be created within 1 PR.

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode.

Again, you are not processing any of the files in the attached directories, but setting up the amendment and sections, then including bracketed instructions for each section, along with exact directory and file names for AI to process in the future. Make sure your new draft follows the exact requirements to be accepted as an amendment. It is ok to modify the existing template-bill format. To come up with the most correct amendment format: use discretion when implementing AMENDMENT INSTRUCTIONS from below.

Your outputs should be in a single LaTeX zip of all files that will compile correctly as a pdf in Overleaf. Don't compile the pdf on your own. Only provide the LaTeX zip file to cancer-automated/tree/main/papers/VVUQ-04/draft-bill.

Essentially, your new LaTeX amendment draft should provide a significant head start so that a future Claude Code request can focus on processing the instructions in brackets using the files in the current repository specified by you. In this new amendment draft output, you have to specify exact files and folders to make downstream processing steps as accurate and efficient as possible. Do not stall, ask questions, or go into plan mode.

Only include references in BibTeX if the amendment format supports.
The original xml zip file reference BibTeX:
@online{uscode_download,
  author       = {{Office of the Law Revision Counsel}},
  title        = {Download the United States Code},
  organization = {United States House of Representatives},
  url          = {https://uscode.house.gov/download/download.shtml},
  urldate      = {2026-05-31}
}

The README in cancer-automated/tree/main/papers/VVUQ-04/draft-bill must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

For your template: specify in your instructions to avoid large white empty spaces without text. Where large spacing between words exist throughout the body of text.: modify \raggedright spacing to make positioning between words look equally and properly spaced. Make sure text doesn't run off the right side of the page anywhere. Include instructions to avoid lines with a single or two words. Any table (if allowed for the amendment draft) needs to use a similar format for each column width as in this example: The contents of every table cell must be properly left aligned using the example format:{>{\raggedright\arraybackslash}p{2cm}. Every width value must have a prepended \raggedright\arraybackslash to ensure no big gaps between words in tables.

Specify in your instructions to avoid single lines separate form the main paragraph on the next page. Perform the final formatting steps that a senior author would take by correcting white space formatting and removing and/or adding relevant text to make each section and page look properly formatted and self standing by itself. (Don't overcrowd the page with text, some white space formatting is ok). Make sure to correct all incorrect symbols such as SS into "§" where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper.

Double check and correct incorrect bill and law names (if any). Check to see if differing governance exists, then update titles and content where appropriate.

The following pieces of information should be included: preferably at the end of the amendment, if appropriate.
CEO Kevin Kawchak (Hyperlink: https://orcid.org/0009-0007-5457-8667)
ChemicalQDevice
kevink@chemicalqdevice.com (Hyperlink)
"Notice: This amendment was adapted from original CFR documents in the public domain. The original ICH document is copyrighted and may be used, reproduced, incorporated into other works, adapted, modified, translated or distributed under a public license. This current work is not endorsed or sponsored by CFR, ICH, or FDA."
"Disclaimer: This work is independent and is not endorsed, sponsored, or approved by any trial sponsor, CRO, site, IRB, regulator, or medical society; and was adapted using Claude Code Opus 4.8 (1M context) Max."
10.5281/zenodo.xxxxxxxx (with Hyperlink: https://doi.org/10.5281/zenodo.xxxxxxxx)
San Diego
June 1, 2026

Inside cancer-automated/tree/main/papers/VVUQ-04/draft-bill: Create a prompt-draft-bill.md that uses a "## prompt-draft-bill" heading followed by this entire prompt word-for-word. Create a separate output-draft-bill.md that uses a "## output-draft-bill" heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

"AMENDMENT INSTRUCTIONS" (Utilize where relevant)
Instructions for Drafting an Amendment to Title 21 - Food and Drugs

Important correction:

"Public Law 119-93" is not Title 21 itself. It is the public law through which the current version of Title 21 has been updated. Title 21 is "Food and Drugs" in the United States Code.

To amend federal law involving food and drugs, you should not say that you are amending "Public Law 119-93 Title 21" unless Public Law 119-93 itself is the specific law you intend to change.

Instead, identify the specific section of Title 21 that you want to change and, when possible, identify the underlying Act that created that section. Many provisions in Title 21 come from the Federal Food, Drug, and Cosmetic Act.

General instructions:
	1.	Identify the exact law section being amended.

Use the current United States Code citation, such as:

21 U.S.C. [section number]

If the section is part of the Federal Food, Drug, and Cosmetic Act, identify it like this:

Section [section number] of the Federal Food, Drug, and Cosmetic Act (21 U.S.C. [section number])
	2.	Decide what kind of change is being made.

Common amendment instructions include:

is amended by striking "[old text]" and inserting "[new text]"

is amended by inserting after "[existing text]" the following: "[new text]"

is amended by adding at the end the following: "[new text]"

is amended by redesignating subsection [old subsection] as subsection [new subsection]
	3.	Draft the amendment as a bill.

The bill text is the legally operative document. It tells Congress exactly what existing law to change and exactly what new text to add.
	4.	Include related changes.

Depending on the amendment, include:

Conforming amendments

Clerical amendments

Definitions

Effective date

Implementation deadline

Transition rule

Rule of construction

Agency rulemaking instructions
	5.	Include a comparative print.

The comparative print is the document that shows all changes to existing law.

Use this convention:

Text to delete: [strike: deleted text]

Text to insert: [insert: new text]

Unchanged law: normal plain text

Because Apple Notes can create formatting problems with strikethrough and underlining, use bracket labels instead of visual formatting.

Exact format of the amendment document:

119TH CONGRESS
[__] Session

H. R. ____

To amend [NAME OF UNDERLYING ACT] to [brief purpose], and for other purposes.

IN THE HOUSE OF REPRESENTATIVES

[Month Day, Year]

Mr./Ms. [SPONSOR] introduced the following bill; which was referred to the Committee on [COMMITTEE NAME]

A BILL

To amend [NAME OF UNDERLYING ACT] to [brief purpose], and for other purposes.

Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled,

SECTION 1. SHORT TITLE.

This Act may be cited as the "[SHORT TITLE]".

SEC. 2. AMENDMENT TO [NAME OF UNDERLYING ACT].

(a) In General.-Section [SECTION NUMBER] of the [NAME OF UNDERLYING ACT] (21 U.S.C. [U.S.C. SECTION]) is amended-

(1) in subsection ([SUBSECTION]), by striking "[EXACT TEXT TO DELETE]" and inserting "[EXACT TEXT TO ADD]";

(2) in subsection ([SUBSECTION])-

(A) in paragraph ([PARAGRAPH]), by striking "[EXACT TEXT TO DELETE]"; and

(B) by inserting after paragraph ([PARAGRAPH]) the following:

"([NEW PARAGRAPH]) [NEW HEADING].-[NEW STATUTORY TEXT]."; and

(3) by adding at the end the following:

"([NEW SUBSECTION]) [NEW HEADING].-

"(1) IN GENERAL.-[NEW STATUTORY TEXT].

"(2) REGULATIONS.-Not later than [TIME PERIOD] after the date of enactment of this Act, the Secretary of Health and Human Services shall [ACTION REQUIRED].

"(3) DEFINITIONS.-In this subsection:

"(A) [TERM].-The term '[TERM]' means [DEFINITION].

"(B) [TERM].-The term '[TERM]' means [DEFINITION].".

(b) Clerical Amendment.-The table of contents for the [NAME OF UNDERLYING ACT] is amended by inserting after the item relating to section [SECTION NUMBER] the following:

"Sec. [NEW SECTION NUMBER]. [NEW SECTION HEADING].".

(c) Conforming Amendments.-The [NAME OF UNDERLYING ACT] is amended-

(1) in section [SECTION NUMBER] (21 U.S.C. [U.S.C. SECTION]), by striking "[OLD CROSS-REFERENCE]" and inserting "[NEW CROSS-REFERENCE]"; and

(2) in section [SECTION NUMBER] (21 U.S.C. [U.S.C. SECTION]), by striking "[OLD TERM]" each place it appears and inserting "[NEW TERM]".

(d) Rule of Construction.-Nothing in this Act, or the amendments made by this Act, shall be construed to [RULE OF CONSTRUCTION].

(e) Effective Date.-The amendments made by this section shall take effect on [DATE OR EVENT].

SEC. 3. COMPARATIVE PRINT; CHANGES IN EXISTING LAW.

The following comparative print shows the changes proposed to existing law by this Act.

Matter proposed to be deleted is shown as:

[strike: text to be deleted]

Matter proposed to be inserted is shown as:

[insert: text to be inserted]

Existing law in which no change is proposed is shown as regular text.

CHANGES IN EXISTING LAW MADE BY THE BILL

[NAME OF UNDERLYING ACT]

SEC. [SECTION NUMBER]. [SECTION HEADING].

(a) [Existing subsection heading].-[Existing unchanged text] [strike: TEXT TO BE DELETED] [insert: TEXT TO BE INSERTED] [existing unchanged text].

(b) [Existing subsection heading].-

(1) [Existing unchanged text].

(2) [strike: TEXT TO BE DELETED]

(3) [insert: NEW TEXT TO BE INSERTED]

[insert: (c) New Subsection Heading.-]

[insert: (1) In general.-Full new statutory text.]

[insert: (2) Regulations.-Not later than [time period] after the date of enactment of this Act, the Secretary of Health and Human Services shall [action required].]

TABLE OF CONTENTS

Sec. [existing section]. [existing heading].
[insert: Sec. [new section]. [new heading].]

Plain-text example:

119TH CONGRESS
1ST Session

H. R. ____

To amend the Federal Food, Drug, and Cosmetic Act to require additional labeling for certain food products, and for other purposes.

IN THE HOUSE OF REPRESENTATIVES

[Month Day, Year]

Mr./Ms. [SPONSOR] introduced the following bill; which was referred to the Committee on Energy and Commerce

A BILL

To amend the Federal Food, Drug, and Cosmetic Act to require additional labeling for certain food products, and for other purposes.

Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled,

SECTION 1. SHORT TITLE.

This Act may be cited as the "Food Labeling Transparency Amendment Act".

SEC. 2. AMENDMENT TO THE FEDERAL FOOD, DRUG, AND COSMETIC ACT.

(a) In General.-Section [SECTION NUMBER] of the Federal Food, Drug, and Cosmetic Act (21 U.S.C. [U.S.C. SECTION]) is amended by adding at the end the following:

"([NEW SUBSECTION]) ADDITIONAL LABELING REQUIREMENT.-

"(1) IN GENERAL.-The Secretary shall require that any covered food product bear a label that clearly and conspicuously discloses [required disclosure].

"(2) REGULATIONS.-Not later than 180 days after the date of enactment of this Act, the Secretary shall issue regulations to carry out this subsection.

"(3) DEFINITION.-In this subsection, the term 'covered food product' means [definition].".

(b) Effective Date.-The amendment made by this section shall take effect 1 year after the date of enactment of this Act.

SEC. 3. COMPARATIVE PRINT; CHANGES IN EXISTING LAW.

The following comparative print shows the changes proposed to existing law by this Act.

Matter proposed to be deleted is shown as:

[strike: text to be deleted]

Matter proposed to be inserted is shown as:

[insert: text to be inserted]

Existing law in which no change is proposed is shown as regular text.

CHANGES IN EXISTING LAW MADE BY THE BILL

FEDERAL FOOD, DRUG, AND COSMETIC ACT

SEC. [SECTION NUMBER]. [SECTION HEADING].

[Existing unchanged statutory text.]

[insert: ([NEW SUBSECTION]) ADDITIONAL LABELING REQUIREMENT.-]

[insert: (1) IN GENERAL.-The Secretary shall require that any covered food product bear a label that clearly and conspicuously discloses [required disclosure].]

[insert: (2) REGULATIONS.-Not later than 180 days after the date of enactment of this Act, the Secretary shall issue regulations to carry out this subsection.]

[insert: (3) DEFINITION.-In this subsection, the term "covered food product" means [definition].]

Checklist before finalizing:

Confirm the exact 21 U.S.C. section being amended.

Confirm the underlying Act name.

Use the exact current statutory text.

Make sure every deletion and insertion appears in the comparative print.

Add conforming amendments if cross-references change.

Add an effective date.

Add rulemaking deadlines if an agency must implement the amendment.

Use consistent defined terms.

Avoid amending "Title 21" generally unless the title itself is the correct target.

For most Food and Drugs amendments, draft the bill as an amendment to the underlying Act, such as the Federal Food, Drug, and Cosmetic Act, with the Title 21 U.S.C. citation included in parentheses.
"AMENDMENT INSTRUCTIONS"

Include v2.2.0 in GitHub documentation headings and release notes. Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v2.2.0).

"FORMAT"
Release title
v2.2.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes
"FORMAT"
