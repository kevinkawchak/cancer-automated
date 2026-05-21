# physical-ai/ - Stage 2 Deployment References

Stage 2 is the mid to long term goal: code runs physical AI in lights-off
factories, and the first hybrid surgery and medicine pilot ships. These modules
are planning and simulation references. They are disabled by default in
`configs/pipeline_config.yaml`, and any real deployment must pass the VVUQ gate,
human oversight, and your institution's safety, IRB, and regulatory review.

```
  Lights-off factory                      Hybrid surgery and medicine pilot
  +-----------------------------+         +-----------------------------------+
  | interlocks satisfied?       |         | day 0   robotic surgery phase     |
  |   estop, perimeter, VVUQ,   |         | day 28  adjuvant medicine cycle 1 |
  |   remote human oversight    |         | day 56  adjuvant medicine cycle 2 |
  | run cells autonomously,     |         | ...                               |
  | emergency-stop on faults    |         | analogous to 2030 PDAC Whipple    |
  +-----------------------------+         |   plus Daraxonrasib simulation    |
                                          +-----------------------------------+
```

## Modules

| File | Stage 2 goal | Responsibility |
|------|--------------|----------------|
| `lights_off_factory.py` | Lights-off factory | Safety-gated autonomous batch runner across cells |
| `hybrid_surgery_medicine.py` | Hybrid pilot | Combined surgery and medicine timeline and summary |

## Usage

```python
import os, sys
sys.path.insert(0, os.path.abspath("physical-ai"))
from lights_off_factory import LightsOffFactory
from hybrid_surgery_medicine import default_pilot

factory = LightsOffFactory(cell_ids=["cell-a", "cell-b"])
report = factory.run_batch(tasks=list(range(8)), executor=lambda cell, task: True)
print(report.state, report.per_cell)

pilot = default_pilot()
print(pilot.summary())
```

See `examples-physical-ai/` for runnable examples.
