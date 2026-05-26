"""VVUQ-02 figure 10: four-entrant comparison box plot.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/10-four-entrant-comparison-violin.
Grounding: codegen/results/comparison.json and execution section 04
comparison_analysis.txt and comparison_leaderboard.md. Depends only on matplotlib
and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
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

OUT = "papers/VVUQ-02/imagegen/10-four-entrant-comparison-violin/10-four-entrant-comparison-violin.png"

# rank, name, morphology, n, min, max, mean, spread, win_rate, total_wins, color
ENTRANTS = [
    (1, "PancreSpeed 1.0", "8-arm cart", 64, 92.764, 94.730, 93.782, 1.966, 0.875, 56, PALETTE["slate"]),
    (2, "H2-Surgical 1.0", "humanoid", 96, 92.468, 94.417, 93.334, 1.949, 0.75, 72, PALETTE["teal"]),
    (3, "da Vinci successor", "2030 teleop", 64, 82.928, 84.832, 83.970, 1.904, 0.0, 0, PALETTE["gray"]),
    (4, "Dutch human", "2025 cohort", 32, 66.911, 68.884, 67.885, 1.973, 0.0, 0, PALETTE["rose"]),
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


def main():
    assert sum(e[3] for e in ENTRANTS) == 256

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], left=0.12, right=0.95, top=0.88, bottom=0.10, hspace=0.30)
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])

    ax.set_xlim(-0.7, 3.9)
    ax.set_ylim(64, 97)
    ax.set_ylabel("composite score", fontsize=10.5)
    ax.set_xticks([])
    ax.grid(axis="y", color=PALETTE["grid"], linewidth=0.6)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)

    bw = 0.5
    for i, (rank, name, morph, n, vmin, vmax, mean, spread, _wr, _tw, color) in enumerate(ENTRANTS):
        body_lo, body_hi = mean - spread / 4, mean + spread / 4
        feat = name.startswith("H2")
        ax.vlines(i, vmin, vmax, color=PALETTE["ink"], linewidth=1.2, zorder=3)
        for yv in (vmin, vmax):
            ax.hlines(yv, i - 0.12, i + 0.12, color=PALETTE["ink"], linewidth=1.2, zorder=3)
        ax.add_patch(
            Rectangle(
                (i - bw / 2, body_lo),
                bw,
                body_hi - body_lo,
                facecolor=color,
                edgecolor=PALETTE["green"] if feat else "white",
                linewidth=2.4 if feat else 1.2,
                zorder=4,
            )
        )
        ax.plot(
            i,
            mean,
            marker="D",
            markersize=9,
            markerfacecolor="white",
            markeredgecolor=PALETTE["ink"],
            markeredgewidth=1.4,
            zorder=6,
        )
        lx = i - 0.34 if i == 0 else i + 0.32
        lha = "right" if i == 0 else "left"
        ax.text(lx, mean, f"mean {mean:.3f}", ha=lha, va="center", fontsize=8.5, color=PALETTE["ink"])
        ax.text(lx, vmax, f"max {vmax:.3f}", ha=lha, va="center", fontsize=7.5, color=PALETTE["gray"])
        ax.text(lx, vmin, f"min {vmin:.3f}", ha=lha, va="center", fontsize=7.5, color=PALETTE["gray"])
        ax.text(
            i,
            64.6,
            f"{name}\n({morph})\nrank {rank}, n={n}",
            ha="center",
            va="bottom",
            fontsize=8.5,
            fontweight="bold" if feat else "normal",
            color=PALETTE["ink"],
        )
        if feat:
            ax.add_patch(
                FancyBboxPatch(
                    (i - 0.26, vmax + 0.45),
                    0.52,
                    1.2,
                    boxstyle="round,pad=0,rounding_size=0.1",
                    facecolor=PALETTE["green"],
                    edgecolor="none",
                    zorder=6,
                )
            )
            ax.text(
                i,
                vmax + 1.05,
                "rank 2",
                ha="center",
                va="center",
                fontsize=9,
                fontweight="bold",
                color="white",
                zorder=7,
            )

    # Separation guides between the two leaders (drawn in the gap between the boxes).
    for mean in (93.782, 93.334):
        ax.hlines(mean, 0.28, 0.72, color=PALETTE["gray"], linestyle=(0, (4, 3)), linewidth=1.0, zorder=2)
    ax.annotate(
        "", xy=(0.5, 93.782), xytext=(0.5, 93.334), arrowprops=dict(arrowstyle="<->", color=PALETTE["ink"], lw=1.3)
    )
    ax.text(0.5, 91.4, "delta about\n0.45 of a point", ha="center", va="center", fontsize=8, color=PALETTE["ink"])

    handles = [
        Patch(
            facecolor=e[10],
            edgecolor=PALETTE["green"] if e[1].startswith("H2") else "white",
            linewidth=1.5,
            label=f"rank {e[0]} {e[1]} (mean {e[6]:.2f})",
        )
        for e in ENTRANTS
    ]
    leg = ax.legend(handles=handles, loc="center right", bbox_to_anchor=(0.99, 0.62), fontsize=8.3, frameon=True)
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Win-rate panel and caveat band.
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.text(
        0.0, 0.95, "Win rate and total wins", ha="left", va="top", fontsize=10, fontweight="bold", color=PALETTE["ink"]
    )
    ys = [0.74, 0.55, 0.36, 0.17]
    x0, scale = 0.16, 0.32
    for (rank, name, morph, n, vmin, vmax, mean, spread, wr, tw, color), y in zip(ENTRANTS, ys):
        ax2.text(0.0, y, name, ha="left", va="center", fontsize=8.5, color=PALETTE["ink"])
        ax2.plot([x0, x0 + wr * scale], [y, y], color=color, linewidth=2.6)
        ax2.plot(x0 + wr * scale, y, "o", color=color, markersize=8)
        ax2.text(
            x0 + wr * scale + 0.01,
            y,
            f"win rate {wr:.3f}, {tw} wins",
            ha="left",
            va="center",
            fontsize=8,
            color=PALETTE["ink"],
        )
    ax2.text(
        0.0,
        0.02,
        "The humanoid has more total wins (72) because it appears in 3 of 4 rounds; win rate normalizes for appearances.",
        ha="left",
        va="bottom",
        fontsize=8.3,
        style="italic",
        color=PALETTE["gray"],
    )

    # Caveat card (right).
    ax2.add_patch(
        FancyBboxPatch(
            (0.66, 0.12),
            0.34,
            0.8,
            boxstyle="round,pad=0,rounding_size=0.02",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
            mutation_aspect=0.5,
        )
    )
    ax2.add_patch(Rectangle((0.66, 0.12), 0.012, 0.8, facecolor=PALETTE["amber"], edgecolor="none"))
    ax2.text(
        0.69, 0.86, "Caveats (verbatim)", ha="left", va="top", fontsize=8.6, fontweight="bold", color=PALETTE["ink"]
    )
    ax2.text(
        0.69,
        0.74,
        textwrap.fill(
            "The H2-Surgical 1.0 is a hypothetical 2030 platform; this comparison is simulation against simulation.", 40
        ),
        ha="left",
        va="top",
        fontsize=7.6,
        color=PALETTE["ink"],
    )
    ax2.text(
        0.69,
        0.42,
        textwrap.fill(
            "Structural time-dimension caveat: a 1-minute robot run against a multi-hour human baseline; the time component dominates the delta.",
            40,
        ),
        ha="left",
        va="top",
        fontsize=7.6,
        color=PALETTE["ink"],
    )

    add_frame(
        fig,
        "Four-Entrant Comparison: the Humanoid in Second Place",
        f"Composite score across 128 verdicts in the 1790-line comparison.json; H2-Surgical 1.0 is rank 2 (execution {SECTION}04)",
        f"cancer-automated v1.0.0  |  source: codegen/results/comparison.json, execution {SECTION}04 "
        "comparison_analysis.txt and comparison_leaderboard.md  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
