"""Test Suite Coverage Treemap (Image 06).

Renders a portrait, full page, 300 dpi treemap tiling the 51 passing tests
across the 8 test modules, each tile area proportional to its test count with a
sequential teal to navy color by count.

Grounding: papers/VVUQ-01/execution/01-foundation/test-suite.md, 51 of 51
passed, 0 skipped, Python 3.11.15, pytest 9.0.3 (code execution v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

PALETTE = {
    "navy": "#1F3A5F",
    "teal": "#2A9D8F",
    "green": "#2E7D32",
    "gray": "#6B7280",
    "panel": "#F4F6F8",
    "grid": "#D9DEE3",
    "ink": "#1A1A1A",
}

CMAP = LinearSegmentedColormap.from_list("tealnavy", ["#7FC9BE", "#2A9D8F", PALETTE["navy"]])


def best_text_color(rgba):
    lum = 0.2126 * rgba[0] + 0.7152 * rgba[1] + 0.0722 * rgba[2]
    return "#FFFFFF" if lum < 0.55 else PALETTE["ink"]


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


def draw_check(ax, x, y, color):
    ax.plot(
        [x, x + 0.007, x + 0.02],
        [y, y - 0.009, y + 0.011],
        color=color,
        linewidth=2.4,
        solid_capstyle="round",
        zorder=6,
    )


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(2, 1, height_ratios=[3.2, 0.5], left=0.06, right=0.94, top=0.90, bottom=0.07, hspace=0.14, figure=fig)

    add_frame(
        fig,
        "Test Suite Coverage Treemap",
        "51 of 51 tests passed, 0 skipped, across 8 modules",
        "cancer-automated v0.3.0  |  source: execution §01 test-suite.md  |  white background, 300 dpi, portrait",
    )

    total = 51
    rows = [
        [("test_foundation.py", 17, "repository files, configs, verify script")],
        [
            ("test_vvuq.py", 8, "vvuq, verification, validation, uncertainty, gate"),
            ("test_pipeline.py", 5, "pipeline, five established methods"),
            ("test_physical_ai.py", 5, "physical-ai, lights off factory, hybrid pilot"),
        ],
        [
            ("test_simulation.py", 4, "simulation, triple runner, consensus"),
            ("test_ingestion.py", 4, "ingestion, web search, pdf processor"),
            ("test_chunking.py", 4, "chunking, chunker, readme generator"),
            ("test_scheduler.py", 4, "scheduler, commit scheduler"),
        ],
    ]

    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    y_top = 1.0
    for row in rows:
        row_sum = sum(c for _, c, _ in row)
        h = row_sum / total
        y0 = y_top - h
        x_left = 0.0
        for name, count, target in row:
            w = count / row_sum
            x0 = x_left
            color = CMAP((count - 4) / (17 - 4))
            ax.add_patch(Rectangle((x0, y0), w, h, facecolor=color, edgecolor="white", linewidth=2.0))
            tc = best_text_color(color)
            cxm = x0 + w / 2
            cym = y0 + h / 2
            ax.text(cxm, cym + 0.052, name, ha="center", va="center", fontsize=12, fontweight="bold", color=tc)
            ax.text(cxm, cym + 0.012, f"{count} tests", ha="center", va="center", fontsize=11, color=tc)
            wrap_w = max(14, int(w * 60))
            ax.text(
                cxm, cym - 0.045, textwrap.fill(target, width=wrap_w), ha="center", va="center", fontsize=9, color=tc
            )
            mark_color = PALETTE["green"] if tc == PALETTE["ink"] else "#BFEAD8"
            draw_check(ax, x0 + 0.014, y_top - 0.03, mark_color)
            ax.text(
                x0 + 0.042,
                y_top - 0.028,
                "PASSED",
                ha="left",
                va="center",
                fontsize=8.5,
                fontweight="bold",
                color=mark_color,
            )
            x_left += w
        y_top = y0

    # Bottom strip: sequential scale and total readout.
    axb = fig.add_subplot(gs[1, 0])
    axb.set_xlim(0, 1)
    axb.set_ylim(0, 1)
    axb.axis("off")
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    axb.imshow(gradient, extent=(0.02, 0.46, 0.52, 0.82), aspect="auto", cmap=CMAP, zorder=2)
    axb.add_patch(
        Rectangle((0.02, 0.52), 0.44, 0.30, facecolor="none", edgecolor=PALETTE["grid"], linewidth=1.0, zorder=3)
    )
    axb.text(0.02, 0.40, "4", ha="center", va="center", fontsize=9, color=PALETTE["ink"])
    axb.text(0.46, 0.40, "17", ha="center", va="center", fontsize=9, color=PALETTE["ink"])
    axb.text(0.24, 0.20, "tests per module, 4 to 17", ha="center", va="center", fontsize=10, color=PALETTE["ink"])
    axb.text(
        0.98,
        0.62,
        "Total 51 of 51 passed, 0 skipped",
        ha="right",
        va="center",
        fontsize=12,
        fontweight="bold",
        color=PALETTE["navy"],
    )
    axb.text(0.98, 0.30, "Python 3.11.15, pytest 9.0.3", ha="right", va="center", fontsize=10, color=PALETTE["gray"])

    fig.savefig(
        "papers/VVUQ-01/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.png", dpi=300, facecolor="white"
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
