# VVUQ-02 image-instruct (placeholder)

Reserved for the 10 figure specifications (one per VVUQ gate), authored in the
same shape as `papers/VVUQ-01/image-instruct/`. Each figure specification will
live at `image-instruct/NN-name/README.md` and map to a non-basic chart family
and a gated VVUQ.

| No. | Figure slug | Chart family | Gated VVUQ |
|-----|-------------|--------------|------------|
| 01 | ten-vvuq-gate-funnel | Funnel | all |
| 02 | handeye-accuracy-radial | Radial / polar scatter | 01 |
| 03 | finger-force-ridgeline | Ridgeline | 02 |
| 04 | balance-zmp-support-polygon | Support polygon + ZMP trace | 03 |
| 05 | autonomy-plan-swimlane | Swimlane | 04 |
| 06 | vessel-no-fly-heatmap | Proximity heatmap | 06 |
| 07 | bimanual-suture-tension-stream | Streamgraph | 07 |
| 08 | perception-dice-treemap | Treemap | 08 |
| 09 | shared-or-clearance-statemap | State diagram + clearance bands | 09 |
| 10 | fault-escalation-sankey | Sankey | 10 |

The figure set is a separate downstream pull request, one commit per figure,
exactly as VVUQ-01 separates `image-instruct` from `imagegen`. No images, Mermaid
diagrams, or colored images are committed in this repository.
