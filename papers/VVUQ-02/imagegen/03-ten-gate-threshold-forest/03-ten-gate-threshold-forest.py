"""VVUQ-02 figure 03: ten-gate threshold forest plot.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/03-ten-gate-threshold-forest.
Grounding: codegen/config/vvuq_thresholds.yaml and execution section 03 threshold
table. Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

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

OUT = "papers/VVUQ-02/imagegen/03-ten-gate-threshold-forest/03-ten-gate-threshold-forest.png"

GATES = [
    {"id": "01", "slug": "bimanual-handeye-servo", "agreement": 0.97, "rel_err": 0.050, "cv": 0.08, "cat": False},
    {"id": "02", "slug": "dexterous-finger-force", "agreement": 0.95, "rel_err": 0.050, "cv": 0.10, "cat": False},
    {"id": "03", "slug": "whole-body-balance", "agreement": 0.98, "rel_err": 0.030, "cv": 0.06, "cat": False},
    {"id": "04", "slug": "autonomous-plan-correctness", "agreement": 0.95, "rel_err": 0.050, "cv": 0.10, "cat": False},
    {"id": "05", "slug": "instrument-grasp-handover", "agreement": 0.96, "rel_err": 0.050, "cv": 0.10, "cat": False},
    {"id": "06", "slug": "vascular-no-fly-hand", "agreement": 1.00, "rel_err": 0.010, "cv": 0.05, "cat": True},
    {
        "id": "07",
        "slug": "bimanual-suturing-anastomosis",
        "agreement": 0.96,
        "rel_err": 0.050,
        "cv": 0.08,
        "cat": False,
    },
    {
        "id": "08",
        "slug": "perception-scene-understanding",
        "agreement": 0.95,
        "rel_err": 0.050,
        "cv": 0.10,
        "cat": False,
    },
    {"id": "09", "slug": "shared-or-human-collision", "agreement": 1.00, "rel_err": 0.020, "cv": 0.06, "cat": True},
    {
        "id": "10",
        "slug": "fault-estop-graceful-degradation",
        "agreement": 1.00,
        "rel_err": 0.020,
        "cv": 0.05,
        "cat": True,
    },
]
HARD = {
    "06": "hard_stop_violations == 0",
    "09": "min_clearance_mm >= 50.0",
    "10": "safe_state_success_rate == 1.0",
}


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


def draw_panel(ax, key, default, xlim, fmt, decimals):
    ax.set_xlim(*xlim)
    ax.set_ylim(-1.4, 9.5)
    ax.invert_yaxis()
    ax.set_yticks(range(10))
    ax.set_yticklabels([])
    ax.grid(axis="x", color=PALETTE["grid"], linewidth=0.6, zorder=0)
    ax.axvline(default, color=PALETTE["gray"], linestyle=(0, (5, 3)), linewidth=1.3, zorder=2)
    ax.text(
        default,
        -1.05,
        f"default {default:.{decimals}f}",
        ha="center",
        va="center",
        fontsize=8.5,
        color=PALETTE["gray"],
    )
    for i, g in enumerate(GATES):
        v = g[key]
        color = PALETTE["red"] if g["cat"] else PALETTE["slate"]
        ax.hlines(i, min(default, v), max(default, v), color=color, linewidth=1.4, zorder=3)
        ax.plot(v, i, "o", markersize=7.5, color=color, zorder=4)
        off = (xlim[1] - xlim[0]) * 0.03
        right = v + off if key == "agreement" else v + off
        ax.annotate(fmt(v), (right, i), fontsize=8.5, va="center", ha="left", color=PALETTE["ink"])
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="x", labelsize=8.5)


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 3, left=0.175, right=0.76, top=0.815, bottom=0.13, wspace=0.4)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[0, 2])

    draw_panel(ax1, "agreement", 0.95, (0.94, 1.012), lambda v: f"{v:.2f}", 2)
    draw_panel(ax2, "rel_err", 0.05, (0.0, 0.058), lambda v: f"{v:.3f}", 2)
    draw_panel(ax3, "cv", 0.10, (0.04, 0.11), lambda v: f"{v:.2f}", 2)
    ax1.set_title("Validation\nagreement (>=)", fontsize=11, fontweight="bold", color=PALETTE["ink"])
    ax2.set_title("Max relative\nerror (<=)", fontsize=11, fontweight="bold", color=PALETTE["ink"])
    ax3.set_title("CV bound (<=)", fontsize=11, fontweight="bold", color=PALETTE["ink"])

    fig.canvas.draw()
    inv = fig.transFigure.inverted()
    # Row labels (once, at the far left) and catastrophe hard-predicate notes (far right).
    for i, g in enumerate(GATES):
        _, fy = inv.transform(ax1.transData.transform((0.94, i)))
        label = textwrap.fill(f"{g['id']} {g['slug']}", 15)
        fig.text(
            0.015,
            fy,
            label,
            ha="left",
            va="center",
            fontsize=8,
            fontweight="bold" if g["cat"] else "normal",
            color=PALETTE["red"] if g["cat"] else PALETTE["ink"],
        )
        if g["id"] in HARD:
            note = f"{g['id']} hard predicate:\n{HARD[g['id']]}"
            fig.add_artist(
                Rectangle(
                    (0.775, fy - 0.02),
                    0.006,
                    0.04,
                    transform=fig.transFigure,
                    facecolor=PALETTE["red"],
                    edgecolor="none",
                )
            )
            fig.text(0.788, fy, note, ha="left", va="center", fontsize=7.8, color=PALETTE["ink"])

    # Verification band under the subtitle.
    tint = tuple(c + (1 - c) * 0.78 for c in (0.18, 0.49, 0.20))
    fig.add_artist(
        Rectangle(
            (0.05, 0.902),
            0.90,
            0.024,
            transform=fig.transFigure,
            facecolor=tint,
            edgecolor=PALETTE["green"],
            linewidth=1.0,
        )
    )
    fig.text(
        0.5,
        0.914,
        "All 10 gates also require verification fraction == 1.0 (a single failed check blocks)",
        ha="center",
        va="center",
        fontsize=9,
        color=PALETTE["ink"],
    )

    # Legend at the bottom.
    handles = [
        Line2D(
            [0], [0], marker="o", color="none", markerfacecolor=PALETTE["slate"], markersize=9, label="standard gate"
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=PALETTE["red"],
            markersize=9,
            label="immediate-catastrophe gate",
        ),
        Line2D([0], [0], color=PALETTE["gray"], linestyle=(0, (5, 3)), linewidth=1.3, label="default bound"),
    ]
    leg = fig.legend(
        handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.058), ncol=3, fontsize=9.5, frameon=True
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    add_frame(
        fig,
        "Ten VVUQ Gate Thresholds",
        f"Bounds tighten with model risk; the three catastrophe gates are strictest (execution {SECTION}03)",
        f"cancer-automated v1.0.0  |  source: codegen/config/vvuq_thresholds.yaml, execution {SECTION}03  |  "
        "white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
