# Shared Operating Room Safety Protocol (VVUQ 06, 09, 10)

These three gates are the immediate-catastrophe gates. They carry a verification
pass fraction of 1.0 and the tightest coefficient-of-variation bounds, because a
1 mm arterial breach, a human collision, or an undetected fall is not recoverable.

## VVUQ 06: vascular no-fly (src/safety/vessel_gate.py)

The gate reads the per-hand tip position at 10 kHz and applies the five vessel
safety zones (config/safety_zones.yaml) per phase, defending in depth behind the
100 kHz vessel proximity sensor that triggers the one-tick (10 microsecond)
hard-stop e-stop.

| Band | Trigger | Velocity scale | Force soft cap (N) | E-stop |
|------|---------|----------------|--------------------|--------|
| clear | distance > no-fly radius | 1.0 | 3.0 | no |
| no_fly | soft-warning < d <= no-fly | 0.5 | 2.5 | no |
| soft_warning | hard-stop < d <= soft-warning | 0.1 | 1.5 | no |
| hard_stop | d <= hard-stop radius | 0.0 | 0.0 | yes |

VVUQ 06 requires zero hard-stop volume breaches over the run.

## VVUQ 09: human-aware collision (src/safety/human_collision.py)

The gate computes the minimum clearance from any humanoid link to any human-actor
keep-out sphere (config/shared_or_actors.yaml) and runs the four-state FSM with
speed-and-separation monitoring per ISO/TS 15066 and ISO 10218.

| State | Clearance | Velocity scale | E-stop |
|-------|-----------|----------------|--------|
| clear | > 300 mm | 1.0 | no |
| proximity | 150 to 300 mm | 0.5 | no |
| contact | 50 to 150 mm | 0.1 | no |
| unsafe | < 50 mm (hard floor) | 0.0 | yes |

VVUQ 09 requires the minimum clearance never to drop below the 50 mm hard floor
and the intrusion-reaction latency to stay within the 3 ms budget.

## VVUQ 10: fault and graceful degradation (src/safety/estop.py)

The unified fault monitor watches balance loss, joint fault, vision dropout,
thermal, and power, and emits a safe-park or a hand-back-to-human response with
the detection latency and the safe-state-reached flag.

| Fault | Detection latency | Action |
|-------|-------------------|--------|
| balance_loss | 50 us | safe_park |
| joint_fault | 50 us | safe_park |
| power | 100 us | safe_park |
| thermal | 100 us | safe_park |
| vision_dropout | 1000 us | hand_back (escalate) |

An ambiguous fault, a vision dropout, or more than one simultaneous fault hands
back to the human by default, the fail-safe behaviour required by IEC 60601-1
single-fault safety, ISO 13849-1, and IEEE 7009-2024. VVUQ 10 is the gate most
likely to ESCALATE.
