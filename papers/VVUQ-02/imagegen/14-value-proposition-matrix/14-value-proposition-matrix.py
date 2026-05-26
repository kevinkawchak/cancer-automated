"""VVUQ-02 figure 14: value proposition matrix.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/14-value-proposition-matrix.
Grounding: execution README thesis and this-run-versus-conventional, execution
section 03, codegen/config/standards_map.yaml and inputs/. Depends only on
matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Rectangle

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

OUT = "papers/VVUQ-02/imagegen/14-value-proposition-matrix/14-value-proposition-matrix.png"

PILLARS = [
    (
        "Faster",
        PALETTE["teal"],
        "one integrated autonomous loop; generation in microseconds; 172 tests in about 1.38 s; commit-per-section in real time",
    ),
    (
        "Less expensive",
        PALETTE["green"],
        "standard-library tree with guarded imports; no human tool cycling; assurance breadth in a single pass",
    ),
    (
        "More beneficial\nto patients",
        PALETTE["rose"],
        "10 gates bound to real standards; 3 catastrophe hard predicates; hand-back-to-human default; recorded human review before ship",
    ),
]
STAKEHOLDERS = [
    ("Trial sponsor", "faster, cheaper, reproducible assurance evidence for a submission"),
    ("Surgeon and care team", "a single autonomous humanoid gated to defined safety bounds with human hand-back"),
    ("Patient", "safety measures proportional to the concentrated risk of one body, before any non-simulated use"),
    ("Regulator", "each decision traceable to a published consensus standard (ASME V&V 40, IEC, ISO, UL, IEEE, FDA)"),
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


def tint(hexcolor, t):
    h = hexcolor.lstrip("#")
    rgb = tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return tuple(c + (1 - c) * t for c in rgb)


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(
        3, 1, height_ratios=[3.1, 1.5, 1.7], left=0.12, right=0.95, top=0.88, bottom=0.08, hspace=0.42
    )
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[2, 0])

    # Quadrant.
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.add_patch(Rectangle((0.5, 0.5), 0.5, 0.5, facecolor=tint(PALETTE["green"], 0.86), edgecolor="none", zorder=0))
    ax.axvline(0.5, color=PALETTE["grid"], linewidth=1.2, zorder=1)
    ax.axhline(0.5, color=PALETTE["grid"], linewidth=1.2, zorder=1)
    ax.text(
        0.75,
        0.965,
        "faster and defensible",
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
        color=PALETTE["green"],
    )
    for qx, qy, qlab in [
        (0.25, 0.965, "credible but slow"),
        (0.75, 0.035, "fast but ungated"),
        (0.25, 0.035, "neither"),
    ]:
        ax.text(qx, qy, qlab, ha="center", va="center", fontsize=8.5, color=PALETTE["gray"])

    approaches = [
        (0.82, 0.86, "VVUQ-02 autonomous\nassurance", PALETTE["green"], True),
        (0.22, 0.84, "Conventional\nmanual V&V", PALETTE["slate"], False),
        (0.85, 0.22, "Raw LLM code\ngeneration", PALETTE["gray"], False),
        (0.30, 0.33, "Ad hoc\nspot checks", PALETTE["gray"], False),
    ]
    for x, y, lab, color, star in approaches:
        if star:
            ax.scatter(x, y, s=900, marker="*", color=color, edgecolor="white", linewidth=1.0, zorder=5)
            ax.scatter(x, y, s=2400, marker="o", facecolor="none", edgecolor=color, linewidth=2.0, zorder=4)
            ax.text(x, y - 0.11, lab, ha="center", va="top", fontsize=9, fontweight="bold", color=color, zorder=6)
        else:
            ax.scatter(x, y, s=420, color=color, edgecolor="white", linewidth=1.0, alpha=0.9, zorder=5)
            ax.text(x, y - 0.085, lab, ha="center", va="top", fontsize=8.5, color=PALETTE["ink"], zorder=6)

    ax.set_xticks([0.04, 0.96])
    ax.set_xticklabels(["low", "high"], fontsize=9)
    ax.set_yticks([0.04, 0.96])
    ax.set_yticklabels(["low", "high"], fontsize=9)
    ax.set_xlabel("verification efficiency (cost and time)  ->", fontsize=10.5)
    ax.set_ylabel("assurance credibility  ->", fontsize=10.5)

    handles = [
        Line2D(
            [0],
            [0],
            marker="*",
            color="none",
            markerfacecolor=PALETTE["green"],
            markersize=18,
            label="VVUQ-02 autonomous assurance (featured)",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=PALETTE["gray"],
            markersize=11,
            label="alternative approach",
        ),
    ]
    leg = ax.legend(
        handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8.3, frameon=True
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Value pillars.
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.text(
        0.0,
        1.04,
        "Three value pillars (thesis)",
        ha="left",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    pw, gap = 0.313, 0.03
    for i, (title, color, body) in enumerate(PILLARS):
        x0 = i * (pw + gap)
        ax2.add_patch(
            FancyBboxPatch(
                (x0, 0.05),
                pw,
                0.9,
                boxstyle="round,pad=0,rounding_size=0.02",
                facecolor=tint(color, 0.85),
                edgecolor=color,
                linewidth=1.4,
                mutation_aspect=0.4,
            )
        )
        ax2.add_patch(Rectangle((x0, 0.78), pw, 0.17, facecolor=color, edgecolor="none"))
        ax2.text(
            x0 + pw / 2,
            0.865,
            title,
            ha="center",
            va="center",
            fontsize=9.5,
            fontweight="bold",
            color="white",
            linespacing=0.9,
        )
        ax2.text(
            x0 + pw / 2, 0.40, textwrap.fill(body, 34), ha="center", va="center", fontsize=7.8, color=PALETTE["ink"]
        )

    # Stakeholder panel.
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis("off")
    ax3.text(
        0.0,
        1.02,
        "Value delivered to each stakeholder",
        ha="left",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    rh = 0.235
    for i, (who, val) in enumerate(STAKEHOLDERS):
        y0 = 0.94 - (i + 1) * rh
        fill = PALETTE["panel"] if i % 2 == 0 else "white"
        ax3.add_patch(
            FancyBboxPatch(
                (0.0, y0),
                1.0,
                rh - 0.02,
                boxstyle="round,pad=0,rounding_size=0.01",
                facecolor=fill,
                edgecolor=PALETTE["grid"],
                linewidth=0.8,
                mutation_aspect=0.25,
            )
        )
        ax3.add_patch(Rectangle((0.0, y0), 0.01, rh - 0.02, facecolor=PALETTE["navy"], edgecolor="none"))
        ax3.text(
            0.025,
            y0 + (rh - 0.02) / 2,
            who,
            ha="left",
            va="center",
            fontsize=8.8,
            fontweight="bold",
            color=PALETTE["navy"],
        )
        ax3.text(
            0.30,
            y0 + (rh - 0.02) / 2,
            textwrap.fill(val, 70),
            ha="left",
            va="center",
            fontsize=8.3,
            color=PALETTE["ink"],
        )

    add_frame(
        fig,
        "Value Proposition Matrix",
        "Higher-standard VVUQ, run autonomously: faster, less expensive, more beneficial to patients (thesis, execution README)",
        f"cancer-automated v1.0.0  |  source: execution README thesis and this-run-versus-conventional, execution {SECTION}03, "
        "codegen/config/standards_map.yaml  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
