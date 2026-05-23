# Foundation Execution: Environment and Verification

This is the first execution section. It records the runtime environment, the
dependency posture, and the output of the repository self-check script
`scripts/verify_installation.py`. Every later section in this execution run was
produced on the same environment described here.

## Execution host

The execution was performed by Claude Code Opus 4.7 (1M context) inside a
managed remote execution container, not on a developer workstation. The
relevant facts of the host are below.

| Property | Value |
|----------|-------|
| Runner | Claude Code Opus 4.7 (1M context), managed cloud container |
| Operating system | Linux 6.18.5 x86_64 |
| Python | 3.11.15 (CPython) |
| Working directory | /home/user/cancer-automated |
| Repository ref | branch claude/friendly-hamilton-xnjku at v0.1.0 baseline |
| Execution date | 2026-05-23 |

The repository targets Python 3.10, 3.11, and 3.12 in CI. The container provides
3.11.15, which sits in the middle of that support window, so the results below
are representative of the supported range. Python 3.10 and 3.12 were not
separately available in the container; the cross-version behavior is instead
covered by the GitHub Actions matrix described in the lint and test section.

## Dependency posture

The core daily-deliverable engine is pure Python standard library. The two
declared core dependencies are `numpy` and `pyyaml`. Every heavy or optional
dependency is imported through a `try/except` guard in the module that uses it,
so the package stays importable when the dependency is absent. This guarded
design is what lets the same code run unchanged on a fully provisioned server
and on a minimal CI runner.

The container was provisioned with the core dependencies plus the linting and
test tooling. Optional agentic, PDF, and physics backends were intentionally
left absent so that the guarded import paths were exercised for real rather than
mocked.

| Package | Role | Status during this run |
|---------|------|------------------------|
| numpy | core | available (2.4.6) |
| pyyaml | core | available (6.0.1) |
| requests | optional, ingestion web search | available (2.33.1) |
| anthropic | optional, agentic instruction and code generation | not installed |
| openai | optional, agentic backend | not installed |
| mcp | optional, Model Context Protocol | not installed |
| pypdf | optional, PDF text extraction | not installed |
| bs4 | optional, HTML parsing | not installed |
| mujoco | optional, physics simulation backend | not installed |
| tqdm | optional, progress reporting | not installed |
| pytest | test harness | available (9.0.3) |
| ruff | lint and format | available (0.15.8) |
| yamllint | YAML lint | available (1.38.0) |

Because `anthropic` and `openai` are absent, the instruction and code generation
stages ran on their deterministic offline templates rather than a live model
backend. Because `requests` is present but the container network policy does not
expose live web search HTML, the web search client exercised its bounded retry
envelope and then degraded to the labeled offline stub. Because `pypdf` is
absent, the PDF processor reported a clean non-fatal status and the chunk
estimate ran on plain text. Each of these is the intended guarded behavior and
is documented in the relevant section.

## verify_installation.py output

The repository ships a self-check at `scripts/verify_installation.py`. It probes
core and optional packages without importing them (using
`importlib.util.find_spec`) and confirms the two configuration files parse. The
verbatim output of the run is below.

```text
================================================================
cancer-automated environment verification
================================================================
Core packages
  [ok] numpy: available
  [ok] yaml: available

Optional packages (guarded at import)
  [--] anthropic: not installed
  [--] openai: not installed
  [--] mcp: not installed
  [ok] requests: available
  [--] pypdf: not installed
  [--] bs4: not installed
  [--] mujoco: not installed
  [--] tqdm: not installed

Configuration files
  [ok] configs/pipeline_config.yaml: present and parseable
  [ok] configs/vvuq_thresholds.yaml: present and parseable

Summary
  core packages present:     2/2
  optional packages present: 1/8
  config files present:      2/2

Core environment is ready.
```

The `[--]` markers in the script output are the script's own two-character
status glyph for an absent package. They are not prose dashes.

## What this section establishes

- The core environment is ready: both core packages and both config files are
  present and parseable.
- The optional backends are absent by design, so the guarded import paths are
  the live paths for this run.
- The host is a managed cloud container running Python 3.11.15 on Linux, which
  is the reference point for the convention-versus-conventional notes recorded
  in the top-level execution README.
