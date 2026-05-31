## prompt-instruct-bill

Your goal is to provide comprehensive, high quality, and relevant U.S. medical AI bill and law summaries that will be used to make the prior VVUQ Physical AI Oncology Trial Bill found in kevinkawchak/cancer-automated/tree/main/papers/VVUQ-03/final-paper more a) up to date with today’s medical AI laws and their relevant medical and technology complexities b) grounded with current and mass adopted medical law references and utilizes medical law context more meaningfully, c) relevant to emerging bills as research influences, but the bills won’t be used in the actual bill text (but potentially be used in a memo, appendix, testimony, or research matrix), d) streamlined to the structured law format and visually styled similar to today’s laws (the new bill version will be converted into xml in a future step) (keep all your outputs for this prompt in markdown or .bib). A future prompt will then utilize your markdown files and cancer-automated/tree/main/papers/VVUQ-03/final-paper to generate a new draft bill version.

Only provide effective and machine readable text, ASCII diagrams, mermaid diagrams, numbered lists, bullet points, and tables (no images) in 10 markdown files located in cancer-automated/tree/main/papers/VVUQ-04/instruct-bill. Provide all respective references in 5 .bib files as described below. Consider the LEGAL SOURCES section to make your search understanding comprehensive. Make sure your search includes data through May 31, 2026. Include a README file in VVUQ-04/instruct-bill that provides detail for each md file, as well as key correlations between md files for each md and how all of the separate files correlate to each other (also include the 5 .bib file relationships to the other files). The README must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. 

The new readme will be provided to Claude code opus 4.8 (1M context) Max in a future step to assist it in processing all of the separate markdown and .bib files synergistically along with accessing the prior VVUQ-03/final-paper in order to create the new draft bill version. Return the 10 separate md files, 5 .bib files, and readme in cancer-automated/tree/main/papers/VVUQ-04/instruct-bill. Do not approximate or shorten any of the required steps.

1 commit is required for each markdown file, .bib file, and readme file. Commit to branch after each commit is finished in real time - don’t hold commits until the outputs are finished. Don’t insert all text into one file. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be created within 1 PR. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). This means that each commit needs to be posted to branch in real time, instead of waiting for all files to be finished before added to the branch. The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode. 

Essentially, your new files should provide a significant head start so that a future Claude Code request utilize your output files based on a)-d) from above to ultimately provide a substantially more current and relevant version of the bill.

The 5 .bib files, each of similar length, must include each of the cited sources using the BibTeX format. Please make sure that relevant identifiers such as DOI numbers and actual URLs be included in .bib. Don’t use “howpublished”, and make sure no duplicate links will be produced in later steps.

Make sure to correct all incorrect symbols such as SS into “§” where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper. Utilize consistent black text color and text formatting throughout each of your file outputs. Double check and correct incorrectly spelled law and bill names and numbers.

In later commits, update cancer-automated/blob/main/README.md repository structures, badges, ASCII diagrams and toc, and other affected areas in the repository (this is the only repository that needs to be edited). Add a short summary for this update above the previous summary using a similar number of characters. Don’t include any images, mermaid diagrams, or colored images for main/README.

Inside cancer-automated/tree/main/papers/VVUQ-04/instruct-bill: Create a prompt-instruct-bill.md that uses a “## prompt-instruct-bill” heading followed by this entire prompt word-for-word. Create a separate output-instruct-bill.md that uses a “## output-instruct-bill” heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

“PRIORBILL”
@misc{kawchak_2026_20454870,
  author       = {Kawchak, Kevin},
  title        = {VVUQ Physical AI Oncology Trial Bill},
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20454870},
  url          = {https://doi.org/10.5281/zenodo.20454870},
}
“PRIORBILL”

“LEGAL SOURCES”
Federal: U.S. Code + eCFR + Federal Register
State: the official code/regulation site for the specific state
Agencies: HHS, CMS, FDA, CDC, OCR, DEA depending on the topic
Official Federal Statutes: GovInfo.gov. 
Federal Regulations: Federal Register.
Departmental Guidelines: The U.S. Department of Health and Human Services 
Legal Databases: Cornell's Legal Information Institute.
State Health Laws: National Conference of State Legislatures (NCSL) database.
“LEGAL SOURCES”

Include GitHub documentation headings and release notes. Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v2.0.0).

"FORMAT"
Release title
v2.0.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes
“FORMAT”
