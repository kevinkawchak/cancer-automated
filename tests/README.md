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


### test_physical_ai.py

### test_pipeline.py

### test_scheduler.py

### test_simulation.py

### test_vvuq.py
