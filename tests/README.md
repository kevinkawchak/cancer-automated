## Cancer-Automated Tests

Files Included:
### conftest.py  
- Shared fixtures and helpers for the cancer-automated test suite.

- Several source modules live in directories with hyphens (for example
``physical-ai/``) which cannot be imported with a normal ``import`` statement.
The ``load_module`` helper uses ``importlib.util`` to load any source file by
path. When a module depends on a package that is not installed (for example
anthropic, requests, pypdf, mujoco) the test is skipped rather than errored,
which keeps CI green when only core dependencies are available.

### test_chunking.py  
- Tests for autochunking and reconstruction READMEs.

### test_foundation.py
- Foundation tests: repository invariants and configuration integrity.

- These tests use only the standard library so they pass on the minimal CI
install (pytest plus pyyaml).

### test_ingestion.py
- Tests for robust web search and PDF processing.

### test_physical_ai.py
- Tests for the Stage 2 deployment references.

### test_pipeline.py
- Tests for the daily-deliverable pipeline (the five established methods).

- Modules are loaded by file path through the conftest ``load_module`` helper, so
the hyphen-free ``pipeline/`` modules import cleanly without packaging.

### test_scheduler.py
- Tests for the non-stop commit scheduler.

### test_simulation.py
- Tests for triple simulation and consensus.

### test_vvuq.py
- Tests for the VVUQ framework and gate.
