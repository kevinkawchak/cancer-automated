# Instruction Set: Automated trial acceleration estimate

Deliverable ID: DAILY-0001
Topic: Physical AI oncology trial throughput

## Inputs

- national-platform paper
- four-simulation paper

## Ordered Steps (the five established methods)

1. Generate this instruction set.
2. Generate code from the instructions.
3. Execute the generated code and capture outputs.
4. Assemble a paper from the executed results.

## Production Constraints

- Use single dashes in prose. Reserve triple dashes for Markdown rules and YAML separators.
- Keep every committed file at or under 200000 bytes.
- Autochunk any oversized code or document and emit a README per chunk.
- Guard heavy or optional imports so modules stay importable.

## Acceptance Criteria

- The deliverable passes the VVUQ gate (verification, validation, uncertainty).
- The three simulation runs agree within the configured coefficient of variation.
- A human review is recorded before any clinical use.
