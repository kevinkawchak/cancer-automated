# Support

## Getting Help

This repository is maintained as an open-source resource for engineers building automated Physical AI systems for oncology clinical trials.

### Questions and Discussions

- GitHub Issues: open an issue for bugs, feature requests, or questions about the daily-deliverable pipeline.
- Discussions: use the GitHub Discussions tab (if enabled) for open-ended questions about automation strategy, VVUQ thresholds, or deployment.

### Before Opening an Issue

1. Run `python scripts/verify_installation.py` to confirm your environment.
2. Run `pytest tests/` to confirm the core pipeline imports and passes its checks.
3. Check existing [issues](https://github.com/kevinkawchak/cancer-automated/issues) for similar reports.
4. Include your OS, Python version, and relevant framework versions.

## Related Repositories

The methods packaged here were proven across several prior repositories. For questions about the source developments, see:

| Repository | Focus |
|------------|-------|
| [physical-ai-oncology-trials](https://github.com/kevinkawchak/physical-ai-oncology-trials) | End-to-end Physical AI unification, National Platform paper, four-simulation accelerated prediction |
| [robotic-surgeries](https://github.com/kevinkawchak/robotic-surgeries) | 2030 PDAC 60-second robotic Whipple plus medicine simulation |
| [Clinical-AI-Demos](https://github.com/kevinkawchak/Clinical-AI-Demos) | Multi-stage instruction to code to execution to paper demo projects |

## Regulatory and Clinical Questions

This repository provides reference implementations and tooling for automated Physical AI in oncology trials. It does not provide legal, medical, or regulatory advice. For compliance questions, consult your institution's:

- Regulatory affairs team (FDA, EMA submissions)
- IRB and ethics committee (protocol review)
- Privacy officer (HIPAA, PHI handling)
- Quality management (IEC 62304, 21 CFR Part 11)
