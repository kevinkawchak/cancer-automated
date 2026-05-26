# 2025 Dutch Nationwide Robotic Pancreatoduodenectomy Cohort (Human Baseline)

This file summarizes the human-surgeon comparator used in the 4-entrant
tournament (`codegen/src/llm/compare_agent.py`). It is a public-literature
outcome baseline, not a model output.

## Baseline figures used

- Cohort: approximately 1000 robotic pancreatoduodenectomies, Dutch nationwide,
  reported circa 2025.
- Ideal outcome rate: about 47 percent (a composite of no major complication, no
  conversion, and acceptable length of stay).
- Five-year overall survival for pancreatic ductal adenocarcinoma remains below
  about 13 percent in the United States, motivating the durable-survival framing.
- Typical operative duration for an open or robotic Whipple is on the order of 4
  to 8 hours.

## Structural time-dimension caveat (preserved everywhere)

The simulated 60-second robotic Whipple is compared against a multi-hour human
operation. The time component of the composite score is therefore dominated by an
orders-of-magnitude duration delta. Every Round 3 (robot vs human) rationale in
the tournament must carry this caveat, exactly as the PDAC baseline does. The
robot entrants are themselves simulations, so all comparisons are
simulation-against-simulation except for these human baseline figures.
