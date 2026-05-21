"""Example: validate observed metrics against a reference.

Run from the repository root:
    python vvuq/examples-vvuq/02_validation_against_reference.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

VVUQ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VVUQ_DIR)

from validation import validate  # noqa: E402


def main() -> None:
    reference = {"acceleration_factor": 2.5, "automated_days": 12.0}
    observed = {"acceleration_factor": 2.55, "automated_days": 12.4}
    result = validate(observed, reference, max_relative_error=0.05, human_review=True)
    print("agreement:", round(result.agreement, 3))
    print("max_relative_error:", round(result.max_relative_error, 3))
    print("human_review:", result.human_review)
    for key, err in result.per_key.items():
        print(f"  {key}: relative_error={err:.3f}")


if __name__ == "__main__":
    main()
