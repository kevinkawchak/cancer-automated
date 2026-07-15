## Cancer-Automated Scripts

#### verify_installation.py
- Verify the cancer-automated environment.

- Reports which core and optional dependencies are available and confirms that
the pipeline configuration files are present and parseable. Heavy and optional
packages are probed through try/except so this script runs on a bare Python
install and never fails the lint-and-format or test CI jobs.

- Usage:
    python scripts/verify_installation.py
