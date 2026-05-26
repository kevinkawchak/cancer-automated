"""VVUQ-02 figure 09: composite score weighting waterfall.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/09-composite-weighting-waterfall.
Grounding: codegen/config/project.yaml composite_score_weights and execution
section 04 gated composite. Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle

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

OUT = "papers/VVUQ-02/imagegen/09-composite-weighting-waterfall/09-composite-weighting-waterfall.png"

COMPONENTS = [
    ("Quality", 0.30, PALETTE["navy"], "largest weight"),
    ("Time", 0.20, PALETTE["slate"], "carries the structural time-dimension caveat"),
    ("Cost", 0.15, PALETTE["teal"], "the cost half of the thesis"),
    ("Safety", 0.15, "#D98077", "the 3 catastrophe gates feed here"),
    ("Anastomosis quality", 0.15, PALETTE["rose"], "graded against the Fistula Risk Score (VVUQ 07)"),
    ("Patient experience", 0.05, PALETTE["gray"], "smallest weight"),
]


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


def card(ax, x0, y0, x1, y1, accents, header, body):
    ax.add_patch(
        FancyBboxPatch(
            (x0, y0),
            x1 - x0,
            y1 - y0,
            boxstyle="round,pad=0,rounding_size=0.015",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
            mutation_aspect=0.35,
        )
    )
    h = (y1 - y0) / len(accents)
    for i, a in enumerate(accents):
        ax.add_patch(Rectangle((x0, y0 + i * h), 0.018, h, facecolor=a, edgecolor="none"))
    ax.text(
        x0 + 0.05,
        (y0 + y1) / 2 + 0.16,
        header,
        ha="left",
        va="center",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    ax.text(
        x0 + 0.05,
        (y0 + y1) / 2 - 0.13,
        textwrap.fill(body, 80),
        ha="left",
        va="center",
        fontsize=9,
        color=PALETTE["ink"],
    )


def main():
    weights = np.array([c[1] for c in COMPONENTS])
    assert abs(weights.sum() - 1.0) < 1e-9
    tops = np.cumsum(weights)
    bases = tops - weights

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], left=0.12, right=0.95, top=0.88, bottom=0.10, hspace=0.30)
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])

    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-0.26, 1.10)
    ax.set_ylabel("cumulative composite weight", fontsize=10.5)
    ax.set_xticks([])
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.axhline(0, color=PALETTE["grid"], linewidth=1.0)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.grid(axis="y", color=PALETTE["grid"], linewidth=0.6)

    w = 0.62
    for i, (name, weight, color, note) in enumerate(COMPONENTS):
        ax.add_patch(
            Rectangle((i - w / 2, bases[i]), w, weight, facecolor=color, edgecolor="white", linewidth=1.4, zorder=3)
        )
        if i < len(COMPONENTS) - 1:
            ax.plot(
                [i + w / 2, i + 1 - w / 2],
                [tops[i], tops[i]],
                linestyle=(0, (4, 3)),
                color=PALETTE["gray"],
                linewidth=1.0,
                zorder=2,
            )
        lum = sum(int(color.lstrip("#")[k : k + 2], 16) / 255 * c for k, c in [(0, 0.299), (2, 0.587), (4, 0.114)])
        if weight >= 0.08:
            ax.text(
                i,
                (bases[i] + tops[i]) / 2,
                f"{weight:.2f}",
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
                color="white" if lum < 0.6 else PALETTE["ink"],
            )
        else:
            ax.text(
                i,
                tops[i] + 0.012,
                f"{weight:.2f}",
                ha="center",
                va="bottom",
                fontsize=11,
                fontweight="bold",
                color=PALETTE["ink"],
            )
        ax.text(
            i,
            1.055,
            textwrap.fill(name, 12),
            ha="center",
            va="top",
            fontsize=9.5,
            fontweight="bold",
            color=PALETTE["ink"],
        )
        ax.text(
            i + w / 2 + 0.04, tops[i], f"{tops[i]:.2f}", ha="left", va="center", fontsize=8.5, color=PALETTE["gray"]
        )
        ax.text(i, -0.04, textwrap.fill(note, 16), ha="center", va="top", fontsize=7.8, color=PALETTE["ink"])

    # Total bar.
    ax.add_patch(
        Rectangle((6 - w / 2, 0), w, 1.0, facecolor=PALETTE["navy"], edgecolor="white", linewidth=1.6, zorder=3)
    )
    ax.text(6, 0.5, "1.00", ha="center", va="center", fontsize=14, fontweight="bold", color="white")
    ax.text(
        6,
        1.055,
        "Full composite\nweight",
        ha="center",
        va="top",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["navy"],
    )
    ax.text(6, -0.04, "the complete\n6-component weighting", ha="center", va="top", fontsize=7.8, color=PALETTE["ink"])
    ax.plot([5 + w / 2, 6 - w / 2], [1.0, 1.0], linestyle=(0, (4, 3)), color=PALETTE["gray"], linewidth=1.0, zorder=2)

    handles = [
        Patch(facecolor=c, edgecolor="white", label=f"{n.replace(chr(10), ' ')} {wt:.2f}") for n, wt, c, _ in COMPONENTS
    ]
    leg = ax.legend(
        handles=handles,
        loc="lower left",
        bbox_to_anchor=(0.40, 0.26),
        fontsize=8.3,
        frameon=True,
        title="Frozen weights",
        title_fontsize=9,
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Gating-overlay terminal cards.
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.text(
        0.5,
        0.97,
        "Gating overlay on the 1.00-weight composite (the gate verdict is the switch)",
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    card(
        ax2,
        0.0,
        0.48,
        1.0,
        0.86,
        [PALETTE["green"]],
        "all 10 gates ACCEPT  ->  composite reported",
        "this sweep 32 of 32, mean 93.56, range 93.417 to 93.715.",
    )
    card(
        ax2,
        0.0,
        0.04,
        1.0,
        0.42,
        [PALETTE["amber"], PALETTE["red"]],
        "any BLOCK or ESCALATE  ->  composite = null",
        "the gating overlay withholds the score; the number is never reported on a non-ACCEPT verdict.",
    )

    add_frame(
        fig,
        "Composite Score Weighting and the Gating Overlay",
        f"Six frozen weights sum to 1.00; the score is reported only when all 10 gates ACCEPT (project.yaml, execution {SECTION}04)",
        f"cancer-automated v1.0.0  |  source: codegen/config/project.yaml composite_score_weights, execution {SECTION}04  |  "
        "white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
