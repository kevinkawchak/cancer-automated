"""Value Proposition Matrix (Image 09).

Renders a portrait, full page, 300 dpi 2 by 2 strategic positioning matrix that
places the autonomous cloud run against a conventional high-end server, plus a
structured better, different, worse summary and a net verdict banner.

Grounding: papers/VVUQ-01/execution/README.md, the section comparing this
autonomous cloud run with conventional high-end server processing (code
execution v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

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
    gs = GridSpec(
        3, 1, height_ratios=[2.0, 1.6, 0.4], left=0.07, right=0.93, top=0.90, bottom=0.07, hspace=0.26, figure=fig
    )

    add_frame(
        fig,
        "Value Proposition Matrix",
        "Autonomous cloud run versus conventional high-end server",
        "cancer-automated v0.3.0  |  source: execution README, autonomous cloud versus conventional server  |  white background, 300 dpi, portrait",
    )

    # Top region: 2 by 2 matrix.
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    x0, x1, y0, y1 = 0.14, 0.99, 0.14, 0.97
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    quads = [
        (x0, y0, mx, my, PALETTE["panel"]),
        (mx, y0, x1, my, PALETTE["panel"]),
        (x0, my, mx, y1, PALETTE["panel"]),
        (mx, my, x1, y1, "#E4F1E5"),
    ]
    for qx0, qy0, qx1, qy1, color in quads:
        ax.add_patch(
            Rectangle((qx0, qy0), qx1 - qx0, qy1 - qy0, facecolor=color, edgecolor="white", linewidth=1.5, zorder=2)
        )
    ax.plot([mx, mx], [y0, y1], color=PALETTE["grid"], linewidth=1.0, linestyle=(0, (4, 3)), zorder=3)
    ax.plot([x0, x1], [my, my], color=PALETTE["grid"], linewidth=1.0, linestyle=(0, (4, 3)), zorder=3)

    # Axis arrows and titles.
    ax.add_patch(
        FancyArrowPatch(
            (x0, 0.075), (x1, 0.075), arrowstyle="-|>", mutation_scale=16, color=PALETTE["gray"], linewidth=1.6
        )
    )
    ax.text(
        (x0 + x1) / 2,
        0.025,
        "Cost and setup efficiency, low to high",
        ha="center",
        va="center",
        fontsize=10.5,
        color=PALETTE["ink"],
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.075, y0), (0.075, y1), arrowstyle="-|>", mutation_scale=16, color=PALETTE["gray"], linewidth=1.6
        )
    )
    ax.text(
        0.03,
        (y0 + y1) / 2,
        "Live backend capability, low to high",
        ha="center",
        va="center",
        rotation=90,
        fontsize=10.5,
        color=PALETTE["ink"],
    )

    # Quadrant corner labels.
    ax.text(
        x0 + 0.02,
        y1 - 0.03,
        "Full live backends,\nheavier setup",
        ha="left",
        va="top",
        fontsize=10,
        color=PALETTE["gray"],
    )
    ax.text(
        x1 - 0.02,
        y1 - 0.03,
        "Ideal future target,\nboth at once",
        ha="right",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["green"],
    )
    ax.text(
        x0 + 0.02,
        y0 + 0.03,
        "Manual and\nunassured baseline",
        ha="left",
        va="bottom",
        fontsize=10,
        color=PALETTE["gray"],
    )
    ax.text(
        x1 - 0.02,
        y0 + 0.03,
        "Fast, cheap,\nreproducible assurance",
        ha="right",
        va="bottom",
        fontsize=10,
        color=PALETTE["gray"],
    )

    # Markers.
    ax.scatter([0.33], [0.74], s=620, marker="o", color=PALETTE["slate"], edgecolors="white", linewidths=1.6, zorder=5)
    ax.text(
        0.33,
        0.655,
        "Conventional\nhigh-end server",
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["slate"],
        zorder=5,
    )
    ax.scatter([0.78], [0.45], s=620, marker="o", color=PALETTE["teal"], edgecolors="white", linewidths=1.6, zorder=5)
    ax.text(
        0.78,
        0.365,
        "Autonomous cloud run\nOpus 4.7 1M",
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["teal"],
        zorder=5,
    )

    # Middle region: three summary cards.
    axm = fig.add_subplot(gs[1, 0])
    axm.set_xlim(0, 1)
    axm.set_ylim(0, 1)
    axm.axis("off")
    columns = [
        (
            "Better",
            PALETTE["green"],
            [
                "Near zero setup, ran before any heavy install",
                "One integrated loop, run, observe, document, lint, commit",
                "Systematic assurance beyond the shipped tests, surfaced the multibyte limitation",
                "Self verifying documentation, every command and output recorded",
            ],
        ),
        (
            "Different",
            PALETTE["slate"],
            [
                "Ephemeral and commit driven, nothing persists unless pushed",
                "Real time per section commits, a finer granularity",
                "Cross version testing delegated to the CI matrix",
            ],
        ),
        (
            "Worse",
            PALETTE["amber"],
            [
                "No live heavy backends, no agentic model, web, PDF, or physics",
                "No display or GPU, no Isaac Sim, no graphics, no LaTeX render",
                "No persistent caches, each session starts cold",
            ],
        ),
    ]
    cw, cgap = 0.313, 0.0305
    for i, (head, color, points) in enumerate(columns):
        cx = 0.005 + i * (cw + cgap)
        axm.add_patch(
            FancyBboxPatch(
                (cx, 0.02),
                cw,
                0.96,
                boxstyle="round,pad=0.004,rounding_size=0.03",
                facecolor=PALETTE["panel"],
                edgecolor=PALETTE["grid"],
                linewidth=1.1,
            )
        )
        axm.add_patch(
            FancyBboxPatch(
                (cx, 0.86), cw, 0.12, boxstyle="round,pad=0.004,rounding_size=0.03", facecolor=color, edgecolor="none"
            )
        )
        axm.text(cx + cw / 2, 0.92, head, ha="center", va="center", fontsize=13, fontweight="bold", color="white")
        py = 0.80
        for pt in points:
            wrapped = textwrap.fill(pt, width=30)
            n_lines = wrapped.count("\n") + 1
            axm.add_patch(Rectangle((cx + 0.022, py - 0.012), 0.016, 0.016, facecolor=color, edgecolor="none"))
            axm.text(cx + 0.05, py, wrapped, ha="left", va="top", fontsize=9.5, color=PALETTE["ink"])
            py -= n_lines * 0.052 + 0.028

    # Bottom region: verdict banner.
    axv = fig.add_subplot(gs[2, 0])
    axv.set_xlim(0, 1)
    axv.set_ylim(0, 1)
    axv.axis("off")
    axv.add_patch(
        FancyBboxPatch(
            (0.0, 0.1),
            1.0,
            0.8,
            boxstyle="round,pad=0.004,rounding_size=0.08",
            facecolor=PALETTE["navy"],
            edgecolor="none",
        )
    )
    verdict = (
        "Net: faster, cheaper, and more reproducible for standard library assurance; "
        "a provisioned server does more for live model, network, and physics backends"
    )
    axv.text(0.5, 0.5, textwrap.fill(verdict, width=82), ha="center", va="center", fontsize=11, color="white")

    fig.savefig(
        "papers/VVUQ-01/imagegen/09-value-proposition-matrix/09-value-proposition-matrix.png",
        dpi=300,
        facecolor="white",
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
