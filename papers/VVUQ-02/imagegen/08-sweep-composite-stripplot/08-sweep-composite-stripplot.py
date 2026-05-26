"""VVUQ-02 figure 08: 32-iteration composite strip plot.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/08-sweep-composite-stripplot.
Grounding: execution section 04 composite_scores.jsonl and the sweep summary.
Depends only on matplotlib and numpy.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Patch, Rectangle

PALETTE = {
    "navy": "#1F3A5F",
    "slate": "#4C72B0",
    "teal": "#2A9D8F",
    "green": "#2E7D32",
    "red": "#C0392B",
    "amber": "#E1A93B",
    "purple": "#6A4C93",
    "rose": "#B5566E",
    "gray": "#6B7280",
    "panel": "#F4F6F8",
    "grid": "#D9DEE3",
    "ink": "#1A1A1A",
}
SECTION = "§"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 11

OUT = "papers/VVUQ-02/imagegen/08-sweep-composite-stripplot/08-sweep-composite-stripplot.png"

SCORES = [
    93.573, 93.519, 93.668, 93.587, 93.537, 93.583, 93.600, 93.622,
    93.515, 93.474, 93.631, 93.527, 93.649, 93.461, 93.715, 93.522,
    93.669, 93.522, 93.482, 93.600, 93.558, 93.594, 93.601, 93.593,
    93.507, 93.417, 93.443, 93.663, 93.611, 93.443, 93.528, 93.574,
]  # fmt: skip


def fit_text(fig, x, y, s, size, max_frac, **kw):
    t = fig.text(x, y, s, fontsize=size, **kw)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    while size > 6.0 and t.get_window_extent(renderer=r).width > max_frac * fig.bbox.width:
        size -= 0.5
        t.set_fontsize(size)
    return t


def add_frame(fig, title, subtitle, footer):
    fit_text(fig, 0.5, 0.965, title, 20, 0.94, ha="center", va="center", fontweight="bold", color=PALETTE["ink"])
    fit_text(fig, 0.5, 0.935, subtitle, 12.5, 0.95, ha="center", va="center", color=PALETTE["ink"])
    fit_text(fig, 0.5, 0.03, footer, 9, 0.97, ha="center", va="center", color=PALETTE["gray"])


def main():
    vals = np.array(SCORES)
    assert len(vals) == 32
    vmin, vmax, vmean = float(vals.min()), float(vals.max()), float(vals.mean())
    assert round(vmin, 3) == 93.417 and round(vmax, 3) == 93.715 and round(vmean, 3) == 93.562

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(3, 1, height_ratios=[1, 3, 2], left=0.10, right=0.95, top=0.88, bottom=0.10, hspace=0.32)
    ax_top = fig.add_subplot(gs[0, 0])
    ax_main = fig.add_subplot(gs[1, 0], sharex=ax_top)
    ax_gate = fig.add_subplot(gs[2, 0], sharex=ax_top)
    xlo, xhi = 93.38, 93.74
    ax_top.set_xlim(xlo, xhi)

    # Top marginal: 12-bin step density outline.
    counts, edges = np.histogram(vals, bins=12, range=(xlo, xhi))
    ax_top.stairs(counts, edges, fill=False, color=PALETTE["teal"], linewidth=1.8, baseline=0)
    ax_top.set_ylim(0, counts.max() + 1)
    ax_top.set_yticks([])
    for sp in ("top", "right", "left"):
        ax_top.spines[sp].set_visible(False)
    ax_top.tick_params(labelbottom=False, length=0)
    ax_top.set_title("Distribution of the 32 composite scores (tight, unimodal)", fontsize=10.5, color=PALETTE["ink"])

    # Main strip plot.
    rng = np.random.default_rng(20260525)
    jitter = 0.5 + rng.uniform(-0.26, 0.26, len(vals))
    ax_main.scatter(vals, jitter, s=70, color=PALETTE["green"], edgecolor="white", linewidth=0.7, zorder=4)
    ax_main.axvline(vmean, color=PALETTE["ink"], linewidth=1.6, zorder=3)
    ax_main.text(
        vmean, 1.05, f"mean {vmean:.3f}", ha="center", va="bottom", fontsize=10, fontweight="bold", color=PALETTE["ink"]
    )
    ax_main.plot(
        vmean,
        0.5,
        marker="D",
        markersize=12,
        markerfacecolor="none",
        markeredgecolor=PALETTE["ink"],
        markeredgewidth=1.6,
        zorder=5,
    )
    # Range bar.
    ax_main.hlines(0.9, vmin, vmax, color=PALETTE["gray"], linewidth=2.0, zorder=3)
    for xv in (vmin, vmax):
        ax_main.vlines(xv, 0.87, 0.93, color=PALETTE["gray"], linewidth=2.0, zorder=3)
    ax_main.text((vmin + vmax) / 2, 0.945, "range 0.298", ha="center", va="bottom", fontsize=9.5, color=PALETTE["gray"])
    ax_main.annotate(
        f"min {vmin:.3f} (iter 25)",
        xy=(vmin, 0.5),
        xytext=(vmin - 0.005, 0.16),
        fontsize=9,
        ha="center",
        color=PALETTE["ink"],
        arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], lw=0.9),
    )
    ax_main.annotate(
        f"max {vmax:.3f} (iter 14)",
        xy=(vmax, 0.5),
        xytext=(vmax + 0.004, 0.16),
        fontsize=9,
        ha="center",
        color=PALETTE["ink"],
        arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], lw=0.9),
    )
    ax_main.set_ylim(0, 1.18)
    ax_main.set_yticks([])
    for sp in ("top", "right", "left"):
        ax_main.spines[sp].set_visible(False)
    ax_main.tick_params(labelbottom=False)
    ax_main.text(
        xlo + 0.006,
        0.05,
        "Spread is about 0.30 of a point across 32 seeded iterations;\nthe gate verdict, not the score, is the decision",
        ha="left",
        va="bottom",
        fontsize=10,
        style="italic",
        color=PALETTE["gray"],
    )
    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=PALETTE["green"],
            markersize=10,
            label="iteration (all gates ACCEPT)",
        ),
        Line2D(
            [0],
            [0],
            marker="D",
            color="none",
            markerfacecolor="none",
            markeredgecolor=PALETTE["ink"],
            markersize=11,
            label="mean",
        ),
        Patch(facecolor=PALETTE["gray"], alpha=0.5, hatch="///", label="withheld on non-ACCEPT"),
    ]
    leg = ax_main.legend(handles=handles, loc="upper right", fontsize=8.5, frameon=True)
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Gating-overlay lane.
    for xv in vals:
        ax_gate.vlines(xv, 0.62, 0.78, color=PALETTE["green"], linewidth=1.6)
    ax_gate.text(
        xlo + 0.006,
        0.84,
        "gates_all_accepted = true  ->  composite reported (this sweep: 32 of 32)",
        ha="left",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["green"],
    )
    ax_gate.add_patch(
        Rectangle(
            (xlo + 0.02, 0.18),
            xhi - xlo - 0.04,
            0.16,
            facecolor=PALETTE["gray"],
            alpha=0.35,
            hatch="///",
            edgecolor=PALETTE["gray"],
            linewidth=1.0,
        )
    )
    ax_gate.plot(93.46, 0.26, "o", color=PALETTE["red"], markersize=8)
    ax_gate.plot(93.50, 0.26, "o", color=PALETTE["amber"], markersize=8)
    ax_gate.text(
        xlo + 0.006,
        0.40,
        "any BLOCK or ESCALATE  ->  composite = null (withheld)",
        ha="left",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["gray"],
    )
    ax_gate.add_patch(
        FancyArrowPatch(
            (xhi - 0.01, 0.70),
            (xhi - 0.01, 0.26),
            arrowstyle="-",
            color=PALETTE["ink"],
            lw=1.2,
            connectionstyle="arc3,rad=0.3",
        )
    )
    ax_gate.text(xhi - 0.004, 0.48, "gating\noverlay\nswitch", ha="left", va="center", fontsize=8, color=PALETTE["ink"])
    ax_gate.set_ylim(0, 1)
    ax_gate.set_yticks([])
    for sp in ("top", "right", "left"):
        ax_gate.spines[sp].set_visible(False)
    ax_gate.set_xlabel("composite score", fontsize=10.5)
    ax_gate.tick_params(axis="x", labelsize=9)

    add_frame(
        fig,
        "32-Iteration Sweep Composite Scores",
        f"All 32 iterations cleared all 10 gates; the score is reported only because every gate ACCEPTs (execution {SECTION}04)",
        f"cancer-automated v1.0.0  |  source: execution {SECTION}04 composite_scores.jsonl, 04-automation README  |  "
        "white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
