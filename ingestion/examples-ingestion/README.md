# examples-ingestion/

Runnable examples for robust web search and PDF processing. Both run without
network access or optional dependencies by degrading to labeled stubs.

| Script | Shows |
|--------|-------|
| `01_web_search.py` | Search with retry and backoff, returning an offline stub when needed |
| `02_pdf_extract.py` | Report PDF extraction status and the 200K chunk estimate |

```bash
python ingestion/examples-ingestion/01_web_search.py
python ingestion/examples-ingestion/02_pdf_extract.py
```
