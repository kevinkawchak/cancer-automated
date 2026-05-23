# Section 05: Physical-AI Stage 2 Execution (2030 PDAC, Lights-Off Factory)

This section executes the `physical-ai/` package, the Stage 2 deployment
references. Stage 2 is the mid to long term goal: code that runs physical AI in
lights-off factories, and a hybrid surgery and medicine pilot analogous to the
2030 PDAC 60-second robotic Whipple plus Daraxonrasib simulation. Both modules
are planning and simulation references, disabled by default in
`configs/pipeline_config.yaml`, and any real use requires VVUQ clearance, human
oversight, IRB approval, and regulatory authorization.

The task calls out the Stage 2 2030 60-second PDAC procedure code specifically:
it is executed here for use in a future paper. Two examples were run, and the
full safety-gating surface of the lights-off controller was exercised with a
dedicated capture.

## Hybrid surgery and medicine pilot (2030 PDAC analog)

```bash
python physical-ai/examples-physical-ai/02_hybrid_pilot.py
```

```text
summary: {'surgery': 'Robotic Whipple (60 second)', 'surgery_seconds': 60.0, 'surgery_arms': 8, 'medicine': 'Daraxonrasib (adjuvant)', 'regimen_days': 168, 'events': 7, 'requires_human_oversight': True}
timeline:
  day   0 [surgery] Robotic Whipple (60 second): 8-arm procedure, 60 s
  day  28 [medicine] Daraxonrasib (adjuvant): adjuvant cycle 1
  day  56 [medicine] Daraxonrasib (adjuvant): adjuvant cycle 2
  day  84 [medicine] Daraxonrasib (adjuvant): adjuvant cycle 3
  day 112 [medicine] Daraxonrasib (adjuvant): adjuvant cycle 4
  day 140 [medicine] Daraxonrasib (adjuvant): adjuvant cycle 5
  day 168 [medicine] Daraxonrasib (adjuvant): adjuvant cycle 6
```

The full output is saved in `artifacts/pdac_hybrid_pilot_timeline.txt`.

### What the pilot models

| Element | Value | Meaning |
|---------|-------|---------|
| Surgery | Robotic Whipple (60 second) | the 8-arm robotic resection on day 0 |
| Surgery duration | 60.0 s | the headline 60-second procedure |
| Surgery arms | 8 | concurrent robotic arms |
| Medicine | Daraxonrasib (adjuvant) | the adjuvant systemic regimen |
| Cycles | 6 | adjuvant cycles |
| Cycle length | 28 days | days per cycle |
| Regimen days | 168 | 6 cycles times 28 days |
| Timeline events | 7 | 1 surgery event plus 6 medicine cycles |
| Human oversight | required | the pilot is gated on human oversight |

The arithmetic checks out: `regimen_days = cycles * cycle_days = 6 * 28 = 168`,
and the timeline has `1 + 6 = 7` events. The surgery anchors day 0 and each
adjuvant cycle lands every 28 days through day 168.

```
  day 0        28        56        84       112       140       168
   |---------|---------|---------|---------|---------|---------|
   [Whipple]  [cyc 1]   [cyc 2]   [cyc 3]   [cyc 4]   [cyc 5]   [cyc 6]
   8-arm      adjuvant Daraxonrasib, one cycle every 28 days
   60 s
```

This is the Stage 2 analog: a sub-minute robotic procedure combined with a
multi-month adjuvant medicine regimen, planned as a single timeline. It is the
deliverable type a future paper will build on.

## Lights-off factory controller

```bash
python physical-ai/examples-physical-ai/01_lights_off_cell.py
```

```text
clean run state: dark per_cell: {'cell-a': {'completed': 3, 'faulted': 0}, 'cell-b': {'completed': 3, 'faulted': 0}}
faulted run state: estop faults: 2
```

A clean batch of 6 tasks distributed round-robin across 2 cells (3 each) and the
line returned to the `dark` idle state. A second batch that faulted every third
task exceeded the fault budget of 1 and triggered an emergency stop (`estop`).

### Safety-gating state machine

The controller is safety-gated. It only runs when every interlock is satisfied,
and it emergency-stops the moment cumulative faults exceed the budget.

```
        +------+   interlocks satisfied   +---------+
        | DARK | -----------------------> | RUNNING |
        +------+                          +---------+
           ^                               |   |
           | batch completes within budget |   | faults > budget
           +-------------------------------+   v
                                           +-------+
   interlock unsatisfied -> FAULT (blocked)| ESTOP |
                                           +-------+
```

### Full safety surface exercised

The shipped example shows the clean and estop paths. The interlock-block path
and the fault-budget behavior were exercised directly:

| Case | Setup | State | Blocked | Faults |
|------|-------|-------|---------|--------|
| A clean run | 6 tasks, all succeed, budget 1 | dark | no | 0 |
| B over budget | 9 tasks, every 3rd faults, budget 1 | estop | no | 2 |
| C interlock off | perimeter_clear unsatisfied | fault | yes | n/a |
| D within budget | 9 tasks, every 4th faults, budget 3 | dark | no | 3 |

Verbatim capture:

```text
##### DEFAULT INTERLOCKS #####
  estop_armed: satisfied=True
  perimeter_clear: satisfied=True
  vvuq_gate_online: satisfied=True
  human_oversight_remote: satisfied=True

##### CASE A: clean run, all interlocks satisfied #####
  ready: True | initial state: dark
  state: dark | blocked: False | faults: 0
  per_cell: {'cell-a': {'completed': 3, 'faulted': 0}, 'cell-b': {'completed': 3, 'faulted': 0}}

##### CASE B: faults exceed budget -> emergency stop #####
  state: estop | blocked: False | faults: 2
  per_cell: {'cell-a': {'completed': 1, 'faulted': 1}, 'cell-b': {'completed': 1, 'faulted': 1}}

##### CASE C: interlock unsatisfied -> run blocked #####
  ready: False | unsatisfied: ['perimeter_clear']
  state: fault | blocked: True | unsatisfied: ['perimeter_clear']

##### CASE D: higher fault budget tolerates faults, stays dark #####
  state: dark | blocked: False | faults: 3
```

The four default interlocks are notable: one of them is `vvuq_gate_online`. The
lights-off line will not start unless the VVUQ gate is reachable, which wires the
Stage 1 assurance machinery directly into the Stage 2 deployment safety chain.
In case B the emergency stop fired after the second fault because the budget was
1; the per-cell tally shows the line halted mid-batch with only 2 tasks
completed. In case C the unsatisfied `perimeter_clear` interlock blocked the run
before any task executed.

## Relationship to the thesis and the future paper

Stage 2 is where the automated VVUQ matters most. A 60-second robotic procedure
and an autonomous factory line leave no time for manual verification in the
loop, so the verification, validation, and uncertainty work has to be done ahead
of time and enforced automatically. The `vvuq_gate_online` interlock and the
`requires_human_oversight` flag are the two places where this execution shows the
Stage 1 assurance reaching into Stage 2. The 2030 PDAC pilot timeline produced
here is the concrete artifact a future paper can extend with real procedure and
regimen data once VVUQ clearance and the required approvals are in place.

## Outcome

| Item | Result |
|------|--------|
| Examples run | 2 of 2, all exit 0 |
| Hybrid pilot | 60 s 8-arm Whipple, Daraxonrasib 6 cycles, 168 regimen days, 7 events |
| Lights-off clean run | returns to dark, all tasks completed |
| Lights-off safety | estop on over-budget faults; blocked on unsatisfied interlock |
| Default interlocks | estop_armed, perimeter_clear, vvuq_gate_online, human_oversight_remote |
| Deployment status | disabled by default; references only, require VVUQ clearance and approvals |

The physical-ai Stage 2 section is fully green. Every safety path behaved as
specified, and the 2030 PDAC pilot timeline is captured for future work.
