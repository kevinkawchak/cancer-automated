# Tables — Oncology Trial VVUQ and Emerging LLM Pipelines

## Table: Trial data tasks vs. LLM pipelines

Emerging LLM workflows shift manual steps into automated models but require *post-hoc* verification (e.g. checking SQL queries, matching outputs). References [20†] and [31†] exemplify such pipelines with published accuracy and error metrics.

| Component | Traditional Process | Emerging LLM-Enhanced Process |
|---|---|---|
| Eligibility Criteria & Query Generation | Human experts write SQL or rule-based queries | LLM translates free-text criteria into SQL (with validation against reference cohorts) |
| Patient Recruitment/Match | Manual chart review or keyword matching | Multimodal LLM patient-trial matching (processes EHR notes, genomic data, etc.) |
| Data Extraction & Cleaning | Manual/NLP pipelines (often brittle/hand-tuned) | LLM parses and normalizes unstructured EHR data, with human oversight to catch hallucinated outputs |
| Report Generation | Analysts write reports and narratives | LLM auto-generates draft summaries and charts (verified by experts before finalization) |
