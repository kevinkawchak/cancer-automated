# Lint and Format Verification

This tree is kept green so the cancer-automated repository CI
(`.github/workflows/ci.yml`, job `lint-and-format` on Python 3.10 / 3.11 / 3.12)
passes. The repository CI runs `ruff check .` and `ruff format --check .` from the
repository root, which lint every Python file in this tree. A nested
`pyproject.toml` `[tool.ruff]` block scopes the lint rules to this tree via ruff
hierarchical config discovery.

## Verified locally before the final push

| Check | Command | Result |
|-------|---------|--------|
| Ruff lint | `ruff check .` (repo root) | All checks passed |
| Ruff format | `ruff format --check .` (repo root) | all files already formatted |
| Yamllint (CI scope) | `yamllint -d relaxed configs/ .github/` | clean |
| Yamllint (codegen) | `yamllint -c .yamllint config/` | clean (document-end enabled) |
| Python compile | `python -m py_compile` on all codegen .py | OK |
| Test suite | `pytest tests -q` | all passing |

## Why the prior 3 lint-and-format failures will not recur

The failures `CI / lint-and-format (3.10 / 3.11 / 3.12)` were ruff failures. This
tree avoids them by:

- writing ruff-format-clean Python (double quotes, lf endings, trailing commas in
  multiline collections) and verifying with `ruff format --check .` from the root;
- scoping F401 (unused import) exemptions to the guarded-optional-import packages
  in the nested `pyproject.toml` per-file-ignores, and otherwise removing unused
  imports;
- guarding every optional heavy import (anthropic, ollama, openai, numpy, pandas,
  pyarrow, matplotlib, requests) so the core imports cleanly with no installs;
- excluding generated and non-Python directories (data, outputs, results,
  releases, notebooks) from ruff in the nested config;
- targeting Python 3.10 and using `from __future__ import annotations` so modern
  type syntax is never evaluated at runtime.
