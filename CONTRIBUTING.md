# Contributing

Contributions are welcome from engineers building automated Physical AI systems for oncology clinical trial settings. This repository turns established methods for generating instructions, generating code, executing code, and creating papers into a single repeatable daily-deliverable pipeline, then layers verification, validation, and uncertainty quantification (VVUQ) on top.

## What We Accept

| Contribution Type | Examples |
|-------------------|----------|
| Pipeline stages | Instruction, code generation, execution, or paper assembly improvements |
| VVUQ tooling | New verification checks, validation references, uncertainty estimators, gate criteria |
| Automation | Commit scheduling, triple-simulation, ingestion, and autochunking utilities |
| Physical AI | Lights-off factory and hybrid surgery and medicine deployment references |
| Bug fixes | Corrections to existing code, configs, or documentation |

## Requirements for All Contributions

1. Recency: referenced frameworks and tools must have been updated within the last 3 months.
2. Oncology relevance: changes must have a clear application to oncology clinical trials.
3. Reproducibility: code must include configurations and instructions sufficient for reproduction.
4. Assurance first: a deliverable that automates a clinical workflow must pass a VVUQ gate before it is accepted. VVUQ is held to a higher standard than code generation.

## Development Workflow

### 1. Fork and Branch

```bash
git clone https://github.com/<your-fork>/cancer-automated.git
cd cancer-automated
git checkout -b your-branch-name
```

### 2. Install Development Tools

```bash
pip install ruff yamllint pytest
```

### 3. Make Changes

- Follow the existing module structure and naming conventions.
- Guard heavy or optional imports with try/except so modules stay importable.
- Pin dependency versions in `requirements.txt`.
- Do not commit patient data, PHI, credentials, or API keys.

### 4. Lint, Format, and Test

```bash
ruff check .
ruff format .
yamllint -d relaxed configs/ .github/
pytest tests/
```

### 5. Submit a Pull Request

- Fill out the PR template completely, including the safety and compliance checklist.
- Reference any related issues.

## Code Style

- Python: formatted with `ruff format`, linted with `ruff check`.
- YAML: validated with `yamllint -d relaxed`.
- Markdown: standard GitHub-flavored markdown. Use single dashes in prose. Reserve triple dashes for Markdown horizontal rules, table separators, and YAML document separators.

## Safety and Compliance

- Any code that automates clinical workflows must document the required human oversight steps.
- Do not introduce changes that bypass safety gates or remove human-in-the-loop requirements.
- VVUQ, scheduling, and deployment tools are reference implementations. Contributors should not represent them as validated medical device software.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
