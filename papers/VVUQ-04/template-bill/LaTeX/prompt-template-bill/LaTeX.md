## prompt-template-bill/LaTeX

Your goal is to utilize the context from kevinkawchak/cancer-automated/tree/main/papers/VVUQ-04/instruct-bill and cancer-automated/tree/main/papers/VVUQ-03/final-paper to prepare a new bill template from cancer-automated/blob/main/papers/VVUQ-04/template-bill/xml_usc21%40119-93.zip (with the same document structure, text, headings, etc. format) by removing irrelevant sections that are not related to VVUQ-04/instruct-bill and VVUQ-03/final-paper. The remaining xml must retain all relevant sections to the physical ai oncology trial context. The remaining xml then needs to be converted in LaTeX that will have the same visual appearance once compiled into a pdf using Overleaf by the author. Each remaining law section needs to have its own .tex file. Include all LaTeX files and a LaTeX zip into cancer-automated/tree/main/papers/VVUQ-04/template-bill/LaTeX.

The priority is to retain the same exact look and feel of the xml pdf in Public Law 119-93 Title 21 - Food and Drugs. The context from VVUQ-03/final-paper and VVUQ-04/instruct-bill are what determines which sections are excluded. You are not adding any bracketed instructions or file names specifically in this update (as with prior repository updates). Instead, you are to exclude non-relevant sections of the existing law to create a new bill template so future AI developments can understand what relevant laws are currently in place. There needs to be enough context so that a future AI model can then have all the information from your bill template, VVUQ-04/instruct-bill, and VVUQ-03/final-paper to then create the required new bill amendment to Public Law 119-93 Title 21 - Food and Drugs. Make sure to include relevant information (and keep their exact formatting) for titles, references, headings, etc.

1 commit is required for each of the following (main.tex, .sty, .bib, and README); and 1 commit is required for each of the paper’s .tex sections (1 .tex file per section that each correspond to main.tex). Commit to branch after each commit is finished in real time - don’t hold commits until the draft paper is finished. Don’t insert all text into one file. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be created within 1 PR.

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode. 

Your outputs need to be in a single LaTeX zip of all files that will compile correctly as a pdf in Overleaf. Provide the LaTeX zip file to cancer-automated/tree/main/papers/VVUQ-04/template-bill/LaTeX. Also keep the individual LaTeX files added to GitHub for separate commits. 

The README in cancer-automated/tree/main/papers/VVUQ-04/template-bill/LaTeX must assist future Claude Code Opus 4.7 1M Max processing steps by including detailed tables that describe the contents of each section, how sections interact with each other, and how all relevant files correlate to a single file. Also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

Inside cancer-automated/tree/main/papers/VVUQ-04/template-bill/LaTeX: Create a prompt-template-bill/LaTeX.md that uses a “## prompt-template-bill/LaTeX” heading followed by this entire prompt word-for-word. Create a separate output-template-bill/LaTeX.md that uses a “## output-template-bill/LaTeX” heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

Include v2.1.0 into GitHub documentation headings and release notes. Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v2.1.0).

"FORMAT"
Release title
v2.1.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes
“FORMAT”
