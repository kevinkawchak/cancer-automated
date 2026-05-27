## prompt-full-paper

Use the kevinkawchak/cancer-automated/tree/main/papers/VVUQ-02/draft-paper directory based on bracketed instructions, directory names, and file names to generate the full LaTeX files and corresponding zip file into cancer-automated/tree/main/papers/VVUQ-02/full-paper. (The output-draft-paper.md and prompt-draft-paper.md files are not part of the draft paper, but can be considered in other context).

The main goal is to comprehensively populate, refine, and make polished the new .tex files, .bib, .sty, and README. Your outputs for the LaTeX zip in cancer-automated/tree/main/papers/VVUQ-02/full-paper need to compile correctly as a pdf in Overleaf (Also create the corresponding GitHub paper/full-paper directory README with doi badges, tables, and ASCII diagrams to reflect the new changes made).

“THESIS”
The robotic code assurance process, not code generation, is the substantial and decision bearing part of the AI workflow, holding VVUQ to a higher standard than code itself. These safety measures will ensure upcoming physical AI oncology trial developments are faster, less expensive, and more beneficial towards patients than conventional verifications.
“THESIS”

Abstract: Make sure competition results for the 4 robots is discussed, with an explanation regarding why the mobile units received 2nd place versus the prior author PDAC paper. Be sure to highlight the importance of the external standards in regard to the study. Keep abstract under 250 words.

Make sure your final tables are readable and effective for human readers of the pharmaceutical and AI industries. Make sure all tables are the width of the body text. Also be sure the abstract has no citations, and includes properly sized file names. Make sure the majority of the file names are primarily for tables, and do not dominate text throughout paper paragraphs. Be certain each image has a corresponding \autoref in body text.

Use 1 commit for each of the following (main.tex, .sty, .bib, and README); and 1 commit is also required for each of the paper’s .tex sections that each correspond to main.tex. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be contained in a created single PR. 

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). This means that each commit needs to be posted to branch in real time, instead of waiting for all sections of the paper to be finished before added to the branch. The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode. 

Do not approximate or shorten any of the required steps; aiming for 70 total pages. Please note that this new VVUQ process is flexible for the future while ensuring consistent patient benefits.

Do not overwrite or change anything from the input cancer-automated/tree/main/papers/VVUQ-02/draft-paper directory.

It is important that you follow the file names and directories in each section’s instructions. You also must make sure that each section is ultimately correct, professional, and adheres to the goals of the paper.  

The README in cancer-automated/tree/main/papers/VVUQ-02/full-paper must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

In later commits, update cancer-automated/blob/main/README.md repository structures, badges, ASCII diagrams and toc, and other affected areas in the repository (this is the only repository that needs to be edited). Add a short summary for this update above the previous summary. Don’t include any images, mermaid diagrams, or colored images.  

For your full paper: avoid large white empty spaces without text. Where large spacing between words exist throughout the body of text.: modify \raggedright spacing to make positioning between words look equally and properly spaced. Make sure text doesn’t run off the right side of the page anywhere. Include instructions to avoid lines with a single or two words. All tables need to use a similar format for each column width as in this example: The contents of every table cell must be properly left aligned using the example format:{>{\raggedright\arraybackslash}p{2cm}. Every width value must have a prepended \raggedright\arraybackslash to ensure no big gaps between words in tables. It is also important that tables match the exact width of the body of the text.

Avoid single lines separate from the main paragraph on the next page. Perform the final formatting steps that a senior author would take by correcting white space formatting and removing and/or adding relevant text to make each section and page look properly formatted and self standing by itself. (Don’t overcrowd the page with text, some white space formatting is ok). Make sure to correct all incorrect symbols such as SS into “§” where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper. Utilize the same text color formatting as in the paper draft.

Inside cancer-automated/tree/main/papers/VVUQ-02/full-paper: Create a prompt-full-paper.md that uses a “## prompt-full-paper” heading followed by this entire prompt word-for-word. Create a separate output-full-paper.md that uses a “## output-full-paper” heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v1.2.0).

"FORMAT"
Release title
v1.2.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude

## Notes
“FORMAT”
