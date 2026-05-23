"""Schedule Acceleration Waterfall (Image 02).

Renders a portrait, full page, 300 dpi figure bridging the conventional 30 day
baseline down to the automated 12 day schedule, decomposed by the contribution
of each of the three simulation runs, with an audit panel reproducing the model.

Grounding: pipeline/codegen_stage.py formula automated_days = 30.0 / (1.0 +
runs * 0.5), configs/pipeline_config.yaml simulate_runs: 3 (code generation
v0.1.0) and papers/VVUQ-01/execution/02-pipeline/README.md (code execution
v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch, Patch

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
    """Reduce a text object font size until it fits max_frac of the figure."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    max_w = max_frac * fig.bbox.width
    size = text_obj.get_fontsize()
    while size > floor and text_obj.get_window_extent(renderer=renderer).width > max_w:
        size -= 0.5
        text_obj.set_fontsize(size)


def add_frame(fig, title, subtitle, footer):
    """Place the shared header, subtitle, and two line footer in their bands."""
    fig.text(0.5, 0.965, title, ha="center", va="center", fontsize=20, fontweight="bold", color=PALETTE["ink"])
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
    gs = GridSpec(2, 1, height_ratios=[2.4, 1.0], left=0.06, right=0.94, top=0.91, bottom=0.07, hspace=0.28, figure=fig)

    add_frame(
        fig,
        "Schedule Acceleration Waterfall",
        "30 baseline days to 12 automated days, a 2.5x acceleration",
        "cancer-automated v0.3.0  |  source: pipeline/codegen_stage.py, configs/pipeline_config.yaml, execution §02  |  white background, 300 dpi, portrait",
    )

    # Model evaluated at runs 0, 1, 2, 3.
    days = [30.0 / (1.0 + r * 0.5) for r in range(4)]  # 30, 20, 15, 12
    changes = [days[i] - days[i + 1] for i in range(3)]  # 10, 5, 3
    factors = [days[0] / days[k + 1] for k in range(3)]  # 1.5, 2.0, 2.5

    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(-0.7, 5.6)
    ax.set_ylim(0, 32)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=PALETTE["grid"], linewidth=0.8)
    ax.set_ylabel("Schedule, days", fontsize=11, color=PALETTE["ink"])
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(PALETTE["grid"])
    ax.spines["bottom"].set_color(PALETTE["grid"])
    ax.tick_params(colors=PALETTE["ink"])

    width = 0.6
    # Total bars from zero.
    ax.bar(0, 30, width=width, color=PALETTE["navy"], zorder=3)
    ax.bar(4, 12, width=width, color=PALETTE["green"], zorder=3)
    # Floating decrement bars.
    for k in range(3):
        top = days[k]
        bottom = days[k + 1]
        ax.bar(k + 1, top - bottom, bottom=bottom, width=width, color=PALETTE["teal"], zorder=3)

    # Connectors between consecutive bars at the running total.
    levels = [30, 20, 15, 12]
    for k in range(4):
        ax.plot(
            [k + width / 2, k + 1 - width / 2],
            [levels[k], levels[k]],
            color=PALETTE["gray"],
            linewidth=1.1,
            linestyle=(0, (5, 3)),
            zorder=2,
        )

    # Total bar value labels.
    ax.text(0, 30.7, "30 days", ha="center", va="bottom", fontsize=12, fontweight="bold", color=PALETTE["navy"])
    ax.text(4, 12.7, "12 days", ha="center", va="bottom", fontsize=12, fontweight="bold", color=PALETTE["green"])
    # Decrement labels: change inside the bar, cumulative factor above it.
    for k in range(3):
        mid = (days[k] + days[k + 1]) / 2
        ax.text(
            k + 1,
            mid,
            f"-{int(changes[k])}",
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color="white",
            zorder=4,
        )
        ax.text(k + 1, days[k] + 0.5, f"{factors[k]:.1f}x", ha="center", va="bottom", fontsize=9, color=PALETTE["gray"])

    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(
        ["Baseline", "Sim run 1", "Sim run 2", "Sim run 3", "Automated"], fontsize=10, color=PALETTE["ink"]
    )

    # Accept green reference line at 12 days.
    ax.axhline(12, xmin=0.02, xmax=0.80, color=PALETTE["green"], linewidth=1.3, linestyle=(0, (6, 4)), zorder=2)
    ax.text(4.55, 12, "Automated\ntarget 12 days", ha="left", va="center", fontsize=9, color=PALETTE["green"])

    ax.legend(
        handles=[
            Patch(facecolor=PALETTE["navy"], label="Baseline"),
            Patch(facecolor=PALETTE["teal"], label="Per run reduction"),
            Patch(facecolor=PALETTE["green"], label="Automated"),
        ],
        loc="upper right",
        frameon=True,
        fontsize=10,
        edgecolor=PALETTE["grid"],
    )

    # Lower audit panel.
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.add_patch(
        FancyBboxPatch(
            (0.0, 0.02),
            1.0,
            0.96,
            boxstyle="round,pad=0.005,rounding_size=0.02",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.2,
        )
    )
    ax2.text(
        0.04,
        0.88,
        "Audit: how the model derives each level",
        ha="left",
        va="center",
        fontsize=12,
        fontweight="bold",
        color=PALETTE["navy"],
    )
    # Formula in a monospace box.
    ax2.add_patch(
        FancyBboxPatch(
            (0.04, 0.66),
            0.55,
            0.13,
            boxstyle="round,pad=0.01",
            facecolor="white",
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
        )
    )
    ax2.text(
        0.065,
        0.725,
        "automated_days = 30.0 / (1.0 + runs * 0.5)",
        ha="left",
        va="center",
        fontsize=11,
        family="monospace",
        color=PALETTE["ink"],
    )

    # Three row table.
    cols_x = [0.07, 0.22, 0.38, 0.50]
    headers = ["runs", "denominator", "days", "factor"]
    for x, head in zip(cols_x, headers):
        ax2.text(x, 0.52, head, ha="left", va="center", fontsize=10, fontweight="bold", color=PALETTE["gray"])
    rows = [("1", "1.5", "20", "1.5x"), ("2", "2.0", "15", "2.0x"), ("3", "2.5", "12", "2.5x")]
    row_y = [0.40, 0.28, 0.16]
    for ry, row in zip(row_y, rows):
        ax2.plot([0.05, 0.60], [ry + 0.06, ry + 0.06], color=PALETTE["grid"], linewidth=0.8)
        for x, val in zip(cols_x, row):
            ax2.text(x, ry, val, ha="left", va="center", fontsize=10.5, color=PALETTE["ink"])

    # Bold callout on the right.
    ax2.add_patch(
        FancyBboxPatch((0.66, 0.16), 0.30, 0.58, boxstyle="round,pad=0.01", facecolor=PALETTE["navy"], edgecolor="none")
    )
    ax2.text(0.81, 0.62, "18 days saved", ha="center", va="center", fontsize=13, fontweight="bold", color="white")
    ax2.text(0.81, 0.45, "60 percent shorter", ha="center", va="center", fontsize=12, color="white")
    ax2.text(0.81, 0.29, "2.5x", ha="center", va="center", fontsize=18, fontweight="bold", color="#9FD8CE")

    fig.savefig(
        "papers/VVUQ-01/imagegen/02-acceleration-waterfall/02-acceleration-waterfall.png", dpi=300, facecolor="white"
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
