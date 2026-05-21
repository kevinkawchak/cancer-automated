## Summary

Brief description of changes.

## Change Type

- [ ] New pipeline stage or automation module
- [ ] VVUQ check, gate, or threshold update
- [ ] Bug fix
- [ ] Documentation update
- [ ] Ingestion, chunking, or scheduling tooling
- [ ] Physical AI deployment tooling
- [ ] Benchmark or results update

## Checklist

### Code Quality
- [ ] Code passes `ruff check` with no errors
- [ ] Code passes `ruff format --check` with no errors
- [ ] YAML files are valid (`yamllint -d relaxed configs/ .github/`)
- [ ] New dependencies added to `requirements.txt` with pinned versions

### Documentation
- [ ] Updated the relevant README or module guide
- [ ] Results and benchmark claims include citations or are labeled as illustrative
- [ ] Framework versions and dates are accurate

### Safety and Compliance (if applicable)
- [ ] No PHI, PII, or patient data included in the PR
- [ ] No hardcoded credentials, API keys, or tokens
- [ ] Human oversight requirements documented for any automated clinical workflow
- [ ] A VVUQ gate guards any deliverable that automates a clinical workflow

### Testing
- [ ] `python scripts/verify_installation.py` passes
- [ ] `pytest tests/` passes
- [ ] Example scripts run without error (if modifying examples)

## Related Issues

Closes #
