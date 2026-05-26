# Section 01: Foundation Execution

This section establishes that the `papers/VVUQ-02/codegen/` tree is healthy on
the execution host before any humanoid behavior, gate decision, sweep, or safety
case is run. It is the verification floor of the VVUQ process: environment,
deterministic reproducibility, automated tests, and static analysis must all be
green first.

## Contents

| File | What it records |
|------|-----------------|
| environment-and-verification.md | Host, Python version, dependency posture, and the byte-for-byte determinism check |
| test-suite.md | The full `pytest tests` run, 172 tests across 15 modules |
| lint-format-yaml.md | `ruff check`, `ruff format --check`, and `yamllint`, the CI lint-and-format checks |

## Summary of outcomes

| Check | Command | Result |
|-------|---------|--------|
| Interpreter | `python3 --version` | CPython 3.11.15 |
| Determinism | regenerate sensor CSV, comparison, sweep index | all reproduced exactly |
| Test suite | `python -m pytest tests -q` | 172 passed, 0 skipped |
| Lint | `ruff check .` | all checks passed |
| Format | `ruff format --check .` | 110 files already formatted |
| YAML lint | `yamllint -d relaxed configs/ .github/` | clean, exit 0 |

## ASCII view of the foundation gate

```
  codegen/ source tree
        |
        v
  +-------------------------------+
  | interpreter + dependencies    |  CPython 3.11.15; numpy, click, pyyaml, jsonschema
  +-------------------------------+
        |
        v
  +-------------------------------+
  | determinism check             |  sensor CSV byte-identical; comparison + sweep identical
  +-------------------------------+
        |
        v
  +-------------------------------+
  | pytest tests (172 tests)      |  verification floor: all pass
  +-------------------------------+
        |
        v
  +-------------------------------+
  | ruff check + ruff format      |  static analysis: clean
  | yamllint configs/ .github/    |
  +-------------------------------+
        |
        v
  foundation green -> proceed
```

All foundation checks passed, including a byte-for-byte determinism check that is
the credibility floor under NASA-STD-7009A and ASME V&V 40-2018, so the execution
proceeded to the pipeline section next.

## External standards anchored here

The foundation is where the external-standards framing begins, and that framing
is what gives the study credibility a reviewer or regulator can examine.
Recording the host, the exact dependency versions, and a deterministic
reproduction is the minimum NASA-STD-7009A asks for before a model and
simulation result is credible, and the automated test and static-analysis floor
is the IEC 62304 software-verification expectation. Every later section builds on
this base.
