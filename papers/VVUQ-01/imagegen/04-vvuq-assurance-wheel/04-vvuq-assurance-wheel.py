"""VVUQ Assurance Wheel (Image 04).

Renders a portrait, full page, 300 dpi polar radar showing six normalized
assurance spokes, the gate threshold ring, the accepted deliverable that clears
every spoke, and the worst failing marker per spoke.

Grounding: configs/vvuq_thresholds.yaml and the vvuq/ modules (code generation
v0.1.0) and papers/VVUQ-01/execution/03-vvuq/README.md (code execution v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch

PALETTE = {
    "navy": "#1F3A5F",
    "slate": "#4C72B0",
    "teal": "#2A9D8F",
    "green": "#2E7D32",
    "red": "#C0392B",
    "amber": "#E1A93B",
    "gray": "#6B7280",
    "panel": "#F4F6F8",
    "grid": "#D9DEE3",
    "ink": "#1A1A1A",
}


def _shrink_to_width(fig, text_obj, max_frac, floor):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    max_w = max_frac * fig.bbox.width
    size = text_obj.get_fontsize()
    while size > floor and text_obj.get_window_extent(renderer=renderer).width > max_w:
        size -= 0.5
        text_obj.set_fontsize(size)


def add_frame(fig, title, subtitle, footer):
    t = fig.text(0.5, 0.965, title, ha="center", va="center", fontsize=20, fontweight="bold", color=PALETTE["ink"])
    _shrink_to_width(fig, t, 0.92, 15.0)
    sub = fig.text(0.5, 0.935, subtitle, ha="center", va="center", fontsize=12.5, color=PALETTE["ink"])
    _shrink_to_width(fig, sub, 0.88, 10.0)
    parts = [p.strip() for p in footer.split("|")]
    f1 = fig.text(
        0.5, 0.040, parts[0] + "  |  " + parts[1], ha="center", va="center", fontsize=9, color=PALETTE["gray"]
    )
    f2 = fig.text(0.5, 0.020, parts[2], ha="center", va="center", fontsize=9, color=PALETTE["gray"])
    _shrink_to_width(fig, f1, 0.90, 7.5)
    _shrink_to_width(fig, f2, 0.90, 7.5)


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(2, 1, height_ratios=[2.6, 1.0], left=0.08, right=0.92, top=0.86, bottom=0.07, hspace=0.16, figure=fig)

    add_frame(
        fig,
        "VVUQ Assurance Wheel",
        "The gate accepts only when every spoke clears the threshold ring",
        "cancer-automated v0.3.0  |  source: configs/vvuq_thresholds.yaml, vvuq/ modules, execution §03  |  white background, 300 dpi, portrait",
    )

    spokes = [
        "Verification\nfraction",
        "Validation\nagreement",
        "Validation\nprecision",
        "Uncertainty\nconsensus",
        "Consensus\nruns",
        "Human\nreview",
    ]
    threshold = [1.00, 0.95, 0.95, 0.90, 1.00, 1.00]
    accepted = [1.00, 1.00, 1.00, 0.9932, 1.00, 1.00]
    failing = [0.83, 0.00, 0.40, 0.6354, 0.667, 0.00]
    fail_labels = ["Case 6\n0.83", "Case 4\n0.00", "Case 4\n0.40", "Case 3\n0.6354", "Case 5\n0.667", "Case 2\n0.00"]
    fail_colors = [PALETTE["red"], PALETTE["red"], PALETTE["red"], PALETTE["amber"], PALETTE["red"], PALETTE["red"]]

    angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
    ang_c = np.concatenate([angles, angles[:1]])
    thr_c = threshold + threshold[:1]
    acc_c = accepted + accepted[:1]

    ax = fig.add_subplot(gs[0, 0], projection="polar")
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 1.06)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8", "1.0"], fontsize=8, color=PALETTE["gray"])
    ax.set_xticks(angles)
    ax.set_xticklabels(spokes, fontsize=11, color=PALETTE["ink"])
    ax.tick_params(axis="x", pad=10)
    ax.set_rlabel_position(108)
    ax.grid(color=PALETTE["grid"], linewidth=0.9)
    ax.spines["polar"].set_color(PALETTE["grid"])
    ax.set_facecolor("white")

    ax.plot(ang_c, thr_c, color=PALETTE["gray"], linewidth=2, linestyle=(0, (5, 3)), label="Gate threshold", zorder=4)
    ax.plot(ang_c, acc_c, color=PALETTE["green"], linewidth=2.5, label="Accepted deliverable (Case 1)", zorder=5)
    ax.fill(ang_c, acc_c, color=PALETTE["green"], alpha=0.18, zorder=3)

    for ang, val, color, lab in zip(angles, failing, fail_colors, fail_labels):
        ax.scatter([ang], [val], s=90, color=color, edgecolors="white", linewidths=1.2, zorder=6)
        label_r = val - 0.16 if val > 0.32 else val + 0.13
        ax.text(ang, label_r, lab, ha="center", va="center", fontsize=8.5, color=color, fontweight="bold", zorder=7)

    # Lower notes panel.
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.add_patch(
        FancyBboxPatch(
            (0.0, 0.05),
            1.0,
            0.9,
            boxstyle="round,pad=0.005,rounding_size=0.03",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.2,
        )
    )
    ax2.plot([0.5, 0.5], [0.14, 0.86], color=PALETTE["grid"], linewidth=1.0)

    ax2.text(0.05, 0.80, "Series", ha="left", va="center", fontsize=11, fontweight="bold", color=PALETTE["navy"])
    series = [
        ("Gate threshold ring", PALETTE["gray"], "dashed"),
        ("Accepted deliverable (Case 1)", PALETTE["green"], "solid"),
        ("Worst failing marker per spoke", PALETTE["red"], "marker"),
    ]
    sy = 0.62
    for label, color, kind in series:
        if kind == "marker":
            ax2.scatter([0.09], [sy], s=80, color=color, edgecolors="white", linewidths=1.0)
            ax2.scatter([0.13], [sy], s=80, color=PALETTE["amber"], edgecolors="white", linewidths=1.0)
        else:
            ax2.plot([0.05, 0.16], [sy, sy], color=color, linewidth=2.4, linestyle="--" if kind == "dashed" else "-")
        ax2.text(0.19, sy, label, ha="left", va="center", fontsize=10, color=PALETTE["ink"])
        sy -= 0.17
    ax2.text(
        0.05,
        0.13,
        "Rule: block on any failure, escalate on divergence",
        ha="left",
        va="center",
        fontsize=9.5,
        style="italic",
        color=PALETTE["gray"],
    )

    ax2.text(0.55, 0.80, "Reading", ha="left", va="center", fontsize=11, fontweight="bold", color=PALETTE["navy"])
    reading = (
        "Accepted clears all six spokes. Every blocked\n"
        "case fails exactly the spoke shown, and one\n"
        "failing spoke is enough to block. The amber\n"
        "uncertainty marker (Case 3) also escalates to\n"
        "a human; the other four markers are blocks."
    )
    ax2.text(0.55, 0.50, reading, ha="left", va="center", fontsize=10, color=PALETTE["ink"])

    fig.savefig(
        "papers/VVUQ-01/imagegen/04-vvuq-assurance-wheel/04-vvuq-assurance-wheel.png", dpi=300, facecolor="white"
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
