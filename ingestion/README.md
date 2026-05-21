# ingestion/ - Robust Web Search and PDF Processing

Stage 1 calls for robust web search and PDF processing. Robust here means the
ingestion stage tolerates transient failures and missing optional dependencies
without aborting a deliverable.

```
   query / pdf path
        |
        v
  +-----------------------------+      +-----------------------------+
  | WebSearchClient.search      |      | PDFProcessor.extract        |
  | bounded retries with        |      | guarded pypdf backend,      |
  | exponential backoff,        |      | reports pages and the       |
  | offline stub fallback       |      | number of 200K chunks       |
  +-----------------------------+      +-----------------------------+
        |                                      |
        +------------------+-------------------+
                           v
                  handed to chunking/ when over the 200K cap
```

## Modules

| File | Responsibility |
|------|----------------|
| `web_search.py` | Web search with bounded exponential-backoff retries and an offline stub |
| `pdf_processor.py` | PDF text extraction with a guarded backend and 200K chunk estimate |

## Design Notes

- `requests` and `pypdf` are optional and guarded. With neither installed the
  modules still import and return clearly labeled, non-fatal results.
- The retry envelope (not the HTML parser) is the robust contribution of the
  web search module. Callers plug in their preferred parser.

See `examples-ingestion/` for runnable examples.
