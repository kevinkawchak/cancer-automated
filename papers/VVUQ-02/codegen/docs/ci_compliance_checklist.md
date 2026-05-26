# CI Compliance Checklist

The codegen tree is kept green so the cancer-automated repository CI
(`.github/workflows/ci.yml`, jobs `lint-and-format` on Python 3.10 / 3.11 / 3.12)
stays passing. The repository CI runs `ruff check .` and `ruff format --check .`
from the repository root, so every Python file in this tree must be ruff-clean
and ruff-format-clean. A nested `pyproject.toml` `[tool.ruff]` block scopes the
lint rules to this tree via ruff hierarchical config discovery.

## Gates

| # | Gate | Tool | Scope |
|---|------|------|-------|
| 1 | Ruff format check | `ruff format --check .` | all .py (repo root) |
| 2 | Ruff lint check | `ruff check .` | all .py (repo root) |
| 3 | Yamllint relaxed | `yamllint -d relaxed` | all .yaml / .yml |
| 4 | Markdownlint | `markdownlint -c .markdownlint.yaml` | all .md |
| 5 | Trailing whitespace | pre-commit | all committed files |
| 6 | EOF newline | pre-commit | all committed files |
| 7 | Mixed line ending (fix to lf) | pre-commit | all committed files |
| 8 | File size cap (10 MB) | pre-commit | all committed files |

## Conventions (non-negotiable, inherited)

- Single hyphens only. No em dashes, no double dashes, no triple dashes.
- Section symbol is the U+00A7 character, never the literal "SS".
- Plain GitHub-Flavored Markdown, black text, ASCII for diagrams.
- No images, no Mermaid diagrams, no colored images.
- Committed files under 10 MB; committed Parquet under 5 MB.
- Deterministic seed contract (root seed 20260525); guarded optional imports so
  the core runs with zero heavy installs.
- Per-section / per-commit pushes; all commits in a single pull request.

## Guarded optional imports

Heavy and optional backends (anthropic, ollama, openai, numpy, pandas, pyarrow,
matplotlib, requests) are imported through try/except guards. The core runs on
the Python standard library so the lint-and-format and local test jobs stay green
without heavy installs.
