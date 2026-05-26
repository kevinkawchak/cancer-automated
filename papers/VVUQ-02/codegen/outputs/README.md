# Outputs

Generated outputs from a run of the codegen tree.

- `diagrams/` ASCII diagrams (no images, no Mermaid, no colored images).
- `metrics/` per-iteration gated composite records (`composite_scores.jsonl`).
- `logs/` per-script log files (git-ignored; this README keeps the directory).

The headline composite per iteration is reported only when all 10 VVUQ gates
ACCEPT, so these outputs always carry the gate roll-up alongside any score.
