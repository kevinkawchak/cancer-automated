## prompt-full-bill

Use the kevinkawchak/cancer-automated/tree/main/papers/VVUQ-04/draft-bill directory based on bracketed instructions, directory names, and file names to generate the full bill LaTeX files and corresponding zip file into cancer-automated/tree/main/papers/VVUQ-04/full-bill. (Do not process output-draft-bill.md and prompt-draft-bill.md). Your outputs should be in a single LaTeX zip of all files that will compile correctly as a pdf in Overleaf.

The main goal is to comprehensively populate, refine, and make polished the new .tex files, .bib, .sty, and README. Your outputs for the LaTeX zip in cancer-automated/tree/main/papers/VVUQ-04/full-bill need to compile correctly as a pdf in Overleaf (Also create the corresponding GitHub VVUQ-04/full-bill directory README with doi badges, tables, and ASCII diagrams to reflect the new changes made).

The bill should have its own 2026 specific H. R. 9510 name. The legislation should look like teams of top human authors wrote it, with comprehensive key points connecting throughout the bill. Do not approximate or shorten any of the required steps. Double check and correct incorrect bill and law names. Do not generate or include any images throughout the bill.

The new bill must be very clear to lawmakers exactly what Claude Code has changed, and how to implement the new bill as new law. Provide a statement that covers relevant v2.0.0-v2.3.0 developments (likely towards the end of the bill) which provides transparency, and assists in the physical ai oncology trials implementation process. Make sure to be concise while providing required development information for this new AI bill generation process. As this is likely the first AI generated bill at scale for physical ai oncology trial implementation, include a brief statement in the cover page, if appropriate.

Issue: You need to abbreviate headers at the top of some of the pages, as text from at least two fields are overlapping, Example: 1 Verification Before Generation Act of 2026 (Draft)SECTION 1. SHORT TITLE; TABLE OF CONTENTS. Limit the number of header characters for all affected cases.

Issue: Should this same statement be mentioned twice on the cover paper for both House and Senate? Modify the statment(s) if necessary.
"To amend the Federal Food, Drug, and Cosmetic Act to require an automated verification, validation, and uncertainty quantification process to clear robot-patient interaction code before that code is generated or executed in a Physical AI oncology clinical investigation, and for other purposes."

Issue: Fix URLs that extend off the right side of the page in references.

Your bill must be a) up to date with today's medical AI laws and implement their relevant medical and technology complexities b) grounded with current and mass adopted medical law references and utilizes medical law context meaningfully, c) relevant to emerging bills as research influences, but the bills won't be used in the actual bill text (but potentially be used in a memo, appendix, testimony, or research matrix), d) streamlined to the structured amendment format.

In later commits, update cancer-automated/blob/main/README.md repository structures, badges, ASCII diagrams and toc, and other affected areas in the repository (this is the only repository that needs to be edited). Add a short summary for this update above the previous summary using a similar number of characters. Don't include any images, mermaid diagrams, or colored images for main/README.

It is important that your bill specify a comprehensive amount of context for each section. Legislation should look like teams of top human authors wrote them. Do not approximate or shorten any of the required steps. Double check and correct incorrect bill and law names.

Make sure your final bill is readable and effective for human interpretation of the pharmaceutical and AI industries. Make sure all tables (if present) are the width of the body text. Make sure the majority of the file names are primarily designated in tables (if present), without dominating text throughout the bill.

1 commit is required for each of the following (main.tex, .sty, .bib, and README); and 1 commit is required for each of the paper's .tex sections (1 .tex file per section) that each correspond to main.tex. Commit to branch after each commit is finished in real time - don't hold commits until the draft paper is finished. Don't insert all text into one file. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be created within 1 PR.

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). This means that each commit needs to be posted to branch in real time, instead of waiting for all sections of the paper to be finished before added to the branch. The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode.

Do not approximate or shorten any of the required steps. Do not overwrite or change anything from the input cancer-automated/tree/main/papers/VVUQ-04/draft-bill. It is important that you follow the file names and directories in each section's instructions. You also must make sure that each section is ultimately correct, professional, and adheres to the goals of the bill.

The README in cancer-automated/tree/main/papers/VVUQ-04/full-bill must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

For your full paper: avoid large white empty spaces without text. Where large spacing between words exist throughout the body of text.: modify \raggedright spacing to make positioning between words look equally and properly spaced. Make sure text doesn't run off the right side of the page anywhere. Include instructions to avoid lines with a single or two words. All tables need to use a similar format for each column width as in this example: The contents of every table cell must be properly left aligned using the example format:{>{\raggedright\arraybackslash}p{2cm}. Every width value must have a prepended \raggedright\arraybackslash to ensure no big gaps between words in tables. It is also important that tables match the exact width of the body of the text.

Avoid single lines separate from the main paragraph on the next page. Perform the final formatting steps that a senior author would take by correcting white space formatting and removing and/or adding relevant text to make each section and page look properly formatted and self standing by itself. (Don't overcrowd the page with text, some white space formatting is ok). Make sure to correct all incorrect symbols such as SS into "§" where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper. Utilize the same text color formatting as in the paper draft.

Inside cancer-automated/tree/main/papers/VVUQ-04/full-bill: Create a prompt-full-bill.md that uses a "## prompt-full-bill" heading followed by this entire prompt word-for-word. Create a separate output-full-bill.md that uses a "## output-full-bill" heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v2.3.0).

"FORMAT"
Release title
v2.3.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude

## Notes
"FORMAT"
