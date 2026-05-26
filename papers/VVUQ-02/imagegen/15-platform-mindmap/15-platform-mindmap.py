"""VVUQ-02 figure 15: platform mind map.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/15-platform-mindmap. A central assurance
hub with six branches (platform, codegen modules, 10 gates, standards, execution,
lineage), each carrying its leaf nodes. Grounding: codegen/config/project.yaml,
execution README source-executed table, execution section 03,
codegen/config/standards_map.yaml. Depends only on matplotlib and numpy.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Patch

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

OUT = "papers/VVUQ-02/imagegen/15-platform-mindmap/15-platform-mindmap.png"

# name, color, center (x, y), (w, h), ncols, leaves (leaf may carry a trailing * for catastrophe)
BRANCHES = [
    (
        "Platform",
        PALETTE["navy"],
        (0.0, 0.73),
        (0.50, 0.30),
        1,
        ["H2-Surgical 1.0 (2030)", "71 total DOF", "2 x 7-DOF arms", "2 x 20-DOF hands", "60 s 8-phase Whipple"],
    ),
    (
        "10 VVUQ gates",
        PALETTE["teal"],
        (0.74, 0.40),
        (0.50, 0.34),
        2,
        [
            "01 handeye",
            "02 finger-force",
            "03 balance",
            "04 plan",
            "05 grasp-hand",
            "06 vasc no-fly*",
            "07 suturing",
            "08 perception",
            "09 OR collision*",
            "10 fault e-stop*",
        ],
    ),
    (
        "External standards",
        PALETTE["purple"],
        (0.73, -0.42),
        (0.52, 0.40),
        2,
        [
            "ASME V&V 40",
            "NASA-STD-7009A",
            "IEC 80601-2-77",
            "IEC 60601-1",
            "ISO 13482",
            "ISO/TS 15066",
            "ISO 10218-1",
            "ISO 9283",
            "IEC 62304",
            "ISO 14971",
            "ISO 13849-1",
            "UL 4600",
            "IEEE 7009",
            "FDA CM&S",
            "Fistula Risk Score",
        ],
    ),
    (
        "Execution record (v0.8.0)",
        PALETTE["amber"],
        (0.0, -0.74),
        (0.66, 0.28),
        1,
        [
            "01 foundation (172 tests)",
            "02 pipeline (concordance 1.000)",
            "03 vvuq (5-case surface)",
            "04 automation (sweep, tournament)",
            "05 deployment (60 s, 1000 rows)",
        ],
    ),
    (
        "Lineage",
        PALETTE["rose"],
        (-0.74, -0.42),
        (0.44, 0.28),
        1,
        ["instructions", "codegen v0.7.0", "execution v0.8.0", "image-instruct v0.9.0"],
    ),
    (
        "Codegen modules (v0.7.0)",
        PALETTE["slate"],
        (-0.76, 0.40),
        (0.56, 0.34),
        2,
        [
            "autonomy",
            "kinematics",
            "perception",
            "hands",
            "balance",
            "suturing",
            "safety",
            "vvuq",
            "simulation",
            "metrics",
            "llm",
            "zenodo",
            "sensors",
        ],
    ),
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
    gs = fig.add_gridspec(1, 1, left=0.05, right=0.95, top=0.905, bottom=0.075)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.15, 1.15)
    ax.set_aspect("equal")
    ax.axis("off")

    # Connectors hub to each branch (drawn first, under the nodes).
    for _, color, (cx, cy), (w, h), _, _ in BRANCHES:
        ax.add_patch(
            FancyArrowPatch(
                (0.20 * np.sign(cx) if cx else 0, 0.11 * np.sign(cy) if cy else 0),
                (cx, cy),
                arrowstyle="-",
                color=color,
                lw=2.0,
                connectionstyle="arc3,rad=0.18",
                zorder=1,
            )
        )

    # Hub.
    ax.add_patch(Circle((0, 0), 0.255, facecolor=PALETTE["navy"], edgecolor="white", linewidth=2.0, zorder=4))
    ax.text(
        0,
        0,
        "VVUQ-02\nH2-Surgical\nassurance",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        color="white",
        zorder=5,
    )

    # Branch cards.
    for name, color, (cx, cy), (w, h), ncols, leaves in BRANCHES:
        x0, y0 = cx - w / 2, cy - h / 2
        ax.add_patch(
            FancyBboxPatch(
                (x0, y0),
                w,
                h,
                boxstyle="round,pad=0,rounding_size=0.02",
                facecolor=tint(color, 0.9),
                edgecolor=color,
                linewidth=1.6,
                zorder=3,
            )
        )
        hh = 0.062
        ax.add_patch(
            FancyBboxPatch(
                (x0, y0 + h - hh),
                w,
                hh,
                boxstyle="round,pad=0,rounding_size=0.02",
                facecolor=color,
                edgecolor=color,
                zorder=3,
            )
        )
        ax.text(
            cx,
            y0 + h - hh / 2,
            name,
            ha="center",
            va="center",
            fontsize=8.0,
            fontweight="bold",
            color="white",
            zorder=5,
        )
        # Leaves in ncols columns.
        per_col = -(-len(leaves) // ncols)
        body_top = y0 + h - hh - 0.018
        row_step = (body_top - (y0 + 0.02)) / max(per_col - 1, 1) if per_col > 1 else 0
        for idx, leaf in enumerate(leaves):
            col = idx // per_col
            row = idx % per_col
            lx = x0 + (col + 0.5) * (w / ncols)
            ly = body_top - row * row_step if per_col > 1 else cy - hh / 2
            cat = leaf.endswith("*")
            txt = leaf[:-1] if cat else leaf
            if cat:
                ax.plot(lx - (w / ncols) * 0.45, ly, "o", color=PALETTE["red"], markersize=4.5, zorder=5)
            ax.text(
                lx,
                ly,
                txt,
                ha="center",
                va="center",
                fontsize=6.6,
                color=PALETTE["red"] if cat else PALETTE["ink"],
                fontweight="bold" if cat else "normal",
                zorder=5,
            )

    # Legend.
    handles = [Patch(facecolor=c, edgecolor="white", label=nm) for nm, c, *_ in BRANCHES]
    handles.append(
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=PALETTE["red"],
            markersize=8,
            label="immediate-catastrophe gate",
        )
    )
    leg = ax.legend(
        handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.05), ncol=4, fontsize=8.0, frameon=True
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    add_frame(
        fig,
        "VVUQ-02 Platform Mind Map",
        "One-page overview: platform, code, 10 gates, standards, execution, lineage",
        f"cancer-automated v1.0.0  |  source: codegen/config/project.yaml, execution README source-executed table, "
        f"execution {SECTION}03, codegen/config/standards_map.yaml  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
