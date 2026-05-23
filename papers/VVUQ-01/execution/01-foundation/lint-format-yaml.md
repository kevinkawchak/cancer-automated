# Foundation Execution: Lint, Format, and YAML

This section records the static-analysis half of the foundation execution. These
are the exact checks the CI `lint-and-format` job runs on every pull request and
push to `main`, across Python 3.10, 3.11, and 3.12. Keeping them green is a hard
requirement for this work, so they were run locally before and after every
section was added.

## Checks and commands

The CI `lint-and-format` job runs three commands. Each was reproduced verbatim
on the execution host.

| Check | Command | Tool version |
|-------|---------|--------------|
| Ruff lint | `ruff check .` | ruff 0.15.8 |
| Ruff format | `ruff format --check .` | ruff 0.15.8 |
| YAML lint | `yamllint -d relaxed configs/ .github/` | yamllint 1.38.0 |

The CI workflow invokes `ruff check . --output-format=github` so that findings
annotate the pull request. The plain `ruff check .` form used here applies the
identical rule set and configuration; only the output formatting differs.

## Ruff lint

```bash
ruff check .
```

```text
All checks passed!
```

Ruff is configured by `ruff.toml`: line length 120, target version py310, rule
families `E`, `F`, and `W` selected, with `F841`, `E741`, and `E501` ignored
globally and per-directory ignores for the guarded optional imports
(for example `F401` in `ingestion/**` and `physical-ai/**`). All source files,
including the example scripts, satisfy this configuration.

## Ruff format

```bash
ruff format --check .
```

```text
44 files already formatted
```

Every one of the 44 Python files in the repository is already in Ruff's
canonical format. No file required reformatting.

## YAML lint

```bash
yamllint -d relaxed configs/ .github/
```

The command produced no output and exited 0, which is a clean pass under the
relaxed profile. The linted YAML is the two pipeline configuration files in
`configs/` and the workflow and template files under `.github/`.

| Linted path | Files | Result |
|-------------|-------|--------|
| configs/ | pipeline_config.yaml, vvuq_thresholds.yaml | clean |
| .github/ | workflows/ci.yml and templates | clean |

## Why this matters for the execution outputs

The execution outputs added by this work are Markdown and plain-text files under
`papers/VVUQ-01/execution/`. They are deliberately not Python or YAML, so they
fall outside the surface that `ruff` and `yamllint` inspect. Generated Python
code captured during the pipeline run (for example the codegen artifact) is
embedded inside fenced Markdown code blocks rather than committed as `.py`
files, so it is preserved verbatim for the reader without entering the lint
surface. This is a deliberate choice to guarantee the `lint-and-format` job
stays green after these outputs are committed.

## Combined foundation result

| Foundation check | Outcome |
|------------------|---------|
| verify_installation.py | core ready, 2/2 core packages, 2/2 configs |
| pytest tests/ | 51 passed, 0 skipped |
| ruff check . | all checks passed |
| ruff format --check . | 44 files already formatted |
| yamllint -d relaxed configs/ .github/ | clean, exit 0 |

The foundation is green on every axis. The remaining sections build on this
clean base and re-run these same checks after each one is added.
