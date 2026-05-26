"""VVUQ-02 figure 04: gate to standard binding matrix.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/04-gate-standard-binding-matrix.
Grounding: codegen/config/standards_map.yaml, inputs/standards/manifest.yaml, and
the external-standards anchoring tables in execution sections 02, 03, and 05.
Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Patch

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

OUT = "papers/VVUQ-02/imagegen/04-gate-standard-binding-matrix/04-gate-standard-binding-matrix.png"

DOMAIN_COLOR = {
    "model credibility": PALETTE["navy"],
    "robotic surgery": PALETTE["teal"],
    "service-robot safety": PALETTE["slate"],
    "software and risk": PALETTE["amber"],
    "autonomy": PALETTE["purple"],
    "regulatory": PALETTE["gray"],
    "clinical": PALETTE["rose"],
}
STANDARDS = [
    ("ASME V&V 40-2018", "model credibility"),
    ("NASA-STD-7009A", "model credibility"),
    ("IEC 80601-2-77:2019", "robotic surgery"),
    ("IEC 60601-1", "robotic surgery"),
    ("ISO/TS 15066:2016", "service-robot safety"),
    ("ISO 13482:2014", "service-robot safety"),
    ("ISO 10218-1:2011", "service-robot safety"),
    ("ISO 9283:1998", "service-robot safety"),
    ("IEC 62304", "software and risk"),
    ("ISO 14971:2019", "software and risk"),
    ("ISO 13849-1:2023", "software and risk"),
    ("UL 4600 (2023)", "autonomy"),
    ("IEEE Std 7009-2024", "autonomy"),
    ("FDA CM&S Credibility 2023", "regulatory"),
    ("Fistula Risk Score", "clinical"),
]
ROWS = [
    ("01", "bimanual-handeye-servo", False, False, [0, 2, 7]),
    ("02", "dexterous-finger-force", False, False, [2, 4]),
    ("03", "whole-body-balance", False, False, [3, 5]),
    ("04", "autonomous-plan-correctness", False, False, [8, 11, 12]),
    ("05", "instrument-grasp-handover", False, False, [2, 7]),
    ("06", "vascular-no-fly-hand", True, False, [2, 9]),
    ("07", "bimanual-suturing-anastomosis", False, False, [2, 14]),
    ("08", "perception-scene-understanding", False, False, [0, 8]),
    ("09", "shared-or-human-collision", True, False, [4, 5, 6]),
    ("10", "fault-estop-graceful-degradation", True, False, [3, 10, 12]),
    ("CC", "cross-cutting (all gates)", False, True, [0, 1, 2, 8, 9, 13]),
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
    bind = np.zeros((len(ROWS), len(STANDARDS)), dtype=int)
    for r, row in enumerate(ROWS):
        for c in row[4]:
            bind[r, c] = 1
    row_counts = bind.sum(axis=1)
    col_counts = bind.sum(axis=0)
    assert row_counts.sum() == 30 and col_counts.min() >= 1

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 1, left=0.0, right=1.0, top=1.0, bottom=0.0)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    nrow, ncol = len(ROWS), len(STANDARDS)
    mx0, mx1, my0, my1 = 0.205, 0.86, 0.28, 0.72
    cw = (mx1 - mx0) / ncol
    rh = (my1 - my0) / nrow

    def col_x(c):
        return mx0 + (c + 0.5) * cw

    def row_y(r):
        return my1 - (r + 0.5) * rh

    # Matrix cells.
    for r in range(nrow):
        for c in range(ncol):
            cx, cy = col_x(c), row_y(r)
            filled = bind[r, c] == 1
            color = DOMAIN_COLOR[STANDARDS[c][1]] if filled else PALETTE["panel"]
            edge = "white" if filled else PALETTE["grid"]
            ax.add_patch(
                FancyBboxPatch(
                    (cx - 0.42 * cw, cy - 0.42 * rh),
                    0.84 * cw,
                    0.84 * rh,
                    boxstyle="round,pad=0,rounding_size=0.006",
                    facecolor=color,
                    edgecolor=edge,
                    linewidth=0.8,
                    mutation_aspect=1.0,
                )
            )

    # Column labels (rotated, colored by domain).
    for c, (desig, domain) in enumerate(STANDARDS):
        ax.text(
            col_x(c),
            my1 + 0.008,
            desig,
            rotation=90,
            ha="center",
            va="bottom",
            fontsize=7.5,
            fontweight="bold",
            color=DOMAIN_COLOR[domain],
        )

    # Row labels (left, wrapped to fit the margin).
    for r, (gid, slug, cat, cross, _) in enumerate(ROWS):
        label = textwrap.fill(f"{gid} {slug}" if not cross else slug, 17)
        ax.text(
            mx0 - 0.012,
            row_y(r),
            label,
            ha="right",
            va="center",
            fontsize=7,
            linespacing=0.95,
            fontweight="bold" if cat else "normal",
            style="italic" if cross else "normal",
            color=PALETTE["red"] if cat else PALETTE["ink"],
        )

    # Row margin (standards per gate, navy horizontal lollipops).
    rscale = 0.0115
    ax.text(mx1 + 0.06, my1 + 0.02, "standards\nper gate", ha="center", va="bottom", fontsize=8, color=PALETTE["navy"])
    for r in range(nrow):
        cy = row_y(r)
        x0 = mx1 + 0.015
        x1 = x0 + row_counts[r] * rscale
        ax.plot([x0, x1], [cy, cy], color=PALETTE["navy"], lw=1.4, zorder=2)
        ax.plot(x1, cy, "o", color=PALETTE["navy"], markersize=6, zorder=3)
        ax.text(x1 + 0.012, cy, str(row_counts[r]), ha="left", va="center", fontsize=8, color=PALETTE["navy"])

    # Column margin (gates per standard, teal vertical lollipops).
    cscale = 0.012
    ax.text(mx0 - 0.02, my0 - 0.05, "gates per\nstandard", ha="right", va="center", fontsize=8, color=PALETTE["teal"])
    for c in range(ncol):
        cx = col_x(c)
        y0 = my0 - 0.015
        y1 = y0 - col_counts[c] * cscale
        ax.plot([cx, cx], [y0, y1], color=PALETTE["teal"], lw=1.4, zorder=2)
        ax.plot(cx, y1, "o", color=PALETTE["teal"], markersize=5, zorder=3)
        ax.text(cx, y1 - 0.014, str(col_counts[c]), ha="center", va="top", fontsize=7.5, color=PALETTE["teal"])

    # Domain legend.
    handles = [Patch(facecolor=DOMAIN_COLOR[d], edgecolor="white", label=d) for d in DOMAIN_COLOR]
    leg = ax.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.135),
        ncol=4,
        fontsize=8.5,
        frameon=True,
        title="Standard domain",
        title_fontsize=9,
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    ax.text(
        0.5,
        0.052,
        "IEC 80601-2-77 and the cross-cutting credibility set (ASME V&V 40, NASA-STD-7009A, FDA CM&S) anchor the most gates",
        ha="center",
        va="center",
        fontsize=8.5,
        style="italic",
        color=PALETTE["ink"],
    )

    add_frame(
        fig,
        "Gate to Standard Binding Matrix",
        f"Every VVUQ gate anchored to published consensus standards; all 15 standards used "
        f"(standards_map.yaml, execution {SECTION}02 {SECTION}03 {SECTION}05)",
        f"cancer-automated v1.0.0  |  source: codegen/config/standards_map.yaml, inputs/standards/manifest.yaml, "
        f"execution {SECTION}02 {SECTION}03 {SECTION}05  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
