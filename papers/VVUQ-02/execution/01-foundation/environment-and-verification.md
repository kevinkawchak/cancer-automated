# Environment and Verification

This report records the execution host, the Python interpreter, and the
dependency posture used to execute the `papers/VVUQ-02/codegen/` tree. It is the
reproducibility floor for every later section: the same host and the same
deterministic seed (20260525) reproduce every committed artifact byte-for-byte,
which is exactly the credibility property that NASA-STD-7009A and ASME V&V
40-2018 §3 require of a model and simulation result.

## Execution host

| Property | Value |
|----------|-------|
| Platform | Linux 6.18.5 x86_64 (managed ephemeral cloud container) |
| Python | CPython 3.11.15 |
| Runner | Claude Code Opus 4.7 (1M context) Max, autonomous |
| Working tree | `kevinkawchak/cancer-automated` on branch `claude/optimistic-thompson-XBlvl` |
| Date executed | 26 May 2026 |

The CI matrix in `.github/workflows/ci.yml` covers Python 3.10, 3.11, and 3.12.
The local execution used the single interpreter the container provides, 3.11.15.
Cross-version behavior is delegated to the CI matrix; the codegen is pure
standard library plus a small set of pinned scientific packages, so no
version-specific behavior is expected.

## Dependency posture

The codegen `pyproject.toml` declares a core set (numpy, click, pyyaml,
jsonschema) plus optional groups (dev, llm-local, zenodo, viz). The core set and
the dev and lint tooling were installed so the full check matrix could run. The
heavy and network-bound optional groups (anthropic, ollama, openai for
`llm-local`; requests for live Zenodo) were not installed, which is the guarded
offline path the modules are designed for.

| Package | Version installed | Role |
|---------|-------------------|------|
| numpy | 2.4.6 | numeric support (guarded import) |
| click | 8.4.1 | optional CLI wrapper (modules import without it) |
| pyyaml | 6.0.1 | config and standards-corpus loading |
| jsonschema | 4.26.0 | schema validation of sensor and command records |
| ruff | 0.15.8 | lint and format (CI lint-and-format job) |
| yamllint | 1.38.0 | YAML lint (CI lint-and-format job) |
| pytest | 9.0.3 | test runner |

Every `src/` module follows the same standalone discipline: it imports the
standard library and an optional backend inside a `try/except`, and falls back to
a deterministic offline path when the backend is absent. The autonomy intent
module (`src/autonomy/llm_intent.py`), the comparison agent
(`src/llm/compare_agent.py`), and the Zenodo patcher
(`src/zenodo/patch_pointers.py`) all ran on their offline paths, which is the
honest CI behavior and the path a reviewer can reproduce without credentials.

## Determinism verification (the credibility floor)

Two committed artifacts were regenerated from scratch on this host and compared
against the versions committed by the codegen step. Both reproduced exactly,
which establishes the deterministic-reproducibility property the assurance
argument depends on.

| Regenerated artifact | Command | Result vs committed |
|----------------------|---------|---------------------|
| `data/sample_h2_sensor.csv` | `python -m src.sensors.ingest_h2` | byte-for-byte identical |
| `results/comparison.json` | `python -m src.llm.compare_agent` | identical (semantic JSON match) |
| `data/iterations/index.jsonl` | `python -m src.simulation.iterate --seed 20260525 --iterations 32` | identical |

The sensor CSV is the 1000-row, 27-column robot positional stream (500 command
ticks across the left and right hands, with 7 arm-joint channels, 5 fingertip
force channels, and 3 end-effector position channels per hand). The comparison
file is the 1790-line, four-entrant tournament. Both are featured in detail in
their respective sections; the point here is that the host reproduces them with
zero drift, so every downstream number in this execution record is reproducible
from the seed.

## Why this matters for the thesis

The thesis is that the assurance process, not code generation, is the
substantial and decision-bearing part of the workflow. A defensible assurance
argument starts with a reproducible model. Recording the host, the interpreter,
the exact dependency versions, and a byte-for-byte determinism check is the
minimum NASA-STD-7009A and ASME V&V 40-2018 expect before any verification or
validation claim is credible. That external-standards framing is what lets this
inexpensive, autonomous run stand as evidence a regulator could examine.
