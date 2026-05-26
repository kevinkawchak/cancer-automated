# H2-Surgical 1.0 Hand Kinematics (Hypothetical 2030)

Two dexterous hands, five fingers each, four joints per finger, for 20 DOF per
hand and 40 across both. Model parameters are in `config/hand_model.yaml`.

## Per-finger 4-DOF chain

Each finger has four joints: metacarpophalangeal abduction, metacarpophalangeal
flexion, proximal interphalangeal flexion, and distal interphalangeal flexion.

```
  palm --[mcp_abd]--[mcp_flex]--proximal--[pip_flex]--middle--[dip_flex]--fingertip
```

The four long fingers (index, middle, ring, little) share a chain structure; the
thumb opposes with a longer first link and a wider abduction range.

## Tendon coupling

The real H2 hand lineage is under-actuated: distal interphalangeal flexion is
coupled to proximal interphalangeal flexion through a tendon, here modeled with a
fixed coupling ratio of 0.67 and a maximum tendon tension of 40 N. The plan
compiler accounts for this coupling when it emits per-finger joint targets.

## Fingertip frames and the bimanual workspace

Each fingertip carries a 100 kHz force sensor (0.01 N resolution) and a position
frame referenced to the palm. The bimanual workspace is the intersection of the
two arm workspaces in the patient frame; suturing tasks (VVUQ 07) require both
fingertip frames to reach a shared anastomosis ring location.

## Grasp taxonomy

| Grasp | Fingers | Surgical use |
|-------|---------|--------------|
| pinch | thumb + index | fine needle handling, tissue pickup |
| tripod | thumb + index + middle | instrument shaft control |
| power | full enclosure | gross retraction |
| needle_driver | locked tripod | needle-driver handle, suturing |

## Force limiting

Per-fingertip soft cap 2.5 N, hard cap 3.0 N; bimanual cumulative soft cap 5.0 N,
hard cap 6.0 N. These are enforced by `src/hands/finger_force.py` and gated by
VVUQ 02, derived from IEC 80601-2-77 and the ISO/TS 15066 power-and-force-limiting
principle.
