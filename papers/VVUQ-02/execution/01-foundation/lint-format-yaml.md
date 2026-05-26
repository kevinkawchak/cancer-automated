# Lint, Format, and YAML

These are the exact checks the CI `lint-and-format` job runs across Python 3.10,
3.11, and 3.12. The job is the one most likely to fail a pull request, so it was
run verbatim on this host both before and after the execution artifacts were
added, to guarantee the single pull request stays green. Static analysis is part
of the verification dimension (IEC 62304 software verification, ASME V&V 40-2018
§8).

## CI checks at the repository root (as CI runs them)

```bash
ruff check .
ruff format --check .
yamllint -d relaxed configs/ .github/
```

| Check | Command | Result |
|-------|---------|--------|
| Lint | `ruff check .` | All checks passed |
| Format | `ruff format --check .` | 110 files already formatted |
| YAML lint | `yamllint -d relaxed configs/ .github/` | clean, exit 0 |

The repository root uses `ruff.toml` (line length 120, rules E, F, W). The
`codegen/` tree carries its own `pyproject.toml` `[tool.ruff]` block (line length
100, rules E, F, W, I, UP, B, C4, with `data`, `outputs`, `results`, `releases`,
and `notebooks` excluded). Ruff resolves the nearest configuration per file, so a
single `ruff check .` from the root applies the stricter codegen rules to the
codegen sources and the root rules to everything else. Both came back clean.

## Codegen-local checks

```bash
cd papers/VVUQ-02/codegen
ruff check .
yamllint -d relaxed config/
```

| Check | Result |
|-------|--------|
| `ruff check .` (codegen pyproject rules) | All checks passed |
| `yamllint -d relaxed config/` | exit 0 (two non-fatal line-length warnings on long regulatory strings) |

The only yamllint output is two relaxed-profile warnings for long lines in
`config/vvuq_thresholds.yaml`, where a standards designation string is more
readable left unsplit. Relaxed yamllint treats these as warnings, not errors, and
the job exits 0. CI yamllint only targets `configs/` and `.github/` at the
repository root, so these warnings do not affect the gate.

## Execution-directory additions are lint-safe by construction

Every file added under `papers/VVUQ-02/execution/` is Markdown, plain text,
JSON, or JSONL. Ruff lints Python and notebook files only, and CI yamllint
targets only `configs/` and `.github/`. No Python module or notebook was added
to the repository outside the already-clean `codegen/` tree, so the execution
record cannot introduce a new lint or format failure. This was a deliberate
choice to keep the single pull request green; driver code is shown as fenced
code blocks in the section reports rather than as committed `.py` files.

## ASCII view of the foundation gate

```
  codegen/ source tree (172 tests, 14 wired standards)
        |
        v
  +-----------------------------+
  | pytest tests -q             |  verification floor: 172 passed, 0 skipped
  +-----------------------------+
        |
        v
  +-----------------------------+
  | ruff check .                |  lint: all checks passed
  | ruff format --check .       |  format: 110 files already formatted
  | yamllint configs/ .github/  |  yaml: clean, exit 0
  +-----------------------------+
        |
        v
  foundation green -> proceed to pipeline, vvuq, automation, deployment
```

All foundation checks passed, so the execution proceeded to the pipeline section.
