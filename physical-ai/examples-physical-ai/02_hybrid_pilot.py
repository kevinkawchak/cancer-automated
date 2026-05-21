"""Example: build the hybrid surgery and medicine pilot timeline.

Run from the repository root:
    python physical-ai/examples-physical-ai/02_hybrid_pilot.py

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys

PAI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PAI_DIR)

from hybrid_surgery_medicine import default_pilot  # noqa: E402


def main() -> None:
    pilot = default_pilot()
    print("summary:", pilot.summary())
    print("timeline:")
    for event in pilot.timeline():
        print(f"  day {event.day:>3} [{event.phase}] {event.description}")


if __name__ == "__main__":
    main()
