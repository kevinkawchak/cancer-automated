"""VVUQ-02 figure 05: clinical and regulatory standards wheel.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/05-clinical-regulatory-standards-wheel.
Grounding: inputs/README.md, inputs/standards/manifest.yaml, inputs/clinical/, and
codegen/config/project.yaml standards grouping. Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Patch, Rectangle, Wedge

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

OUT = "papers/VVUQ-02/imagegen/05-clinical-regulatory-standards-wheel/05-clinical-regulatory-standards-wheel.png"

# (name, color, list of (designation, body, used_for))
DOMAINS = [
    (
        "model credibility",
        PALETTE["navy"],
        [
            ("ASME V&V 40-2018", "ASME", "credibility vs risk"),
            ("NASA-STD-7009A", "NASA", "uncertainty as first-class"),
            ("FDA CM&S Credibility 2023", "FDA", "regulatory acceptance"),
        ],
    ),
    (
        "robotic surgery",
        PALETTE["teal"],
        [
            ("IEC 80601-2-77:2019", "IEC", "accuracy, force, e-stop"),
            ("IEC 60601-1", "IEC", "single-fault safe state"),
        ],
    ),
    (
        "service-robot safety",
        PALETTE["slate"],
        [
            ("ISO 13482:2014", "ISO", "stability"),
            ("ISO/TS 15066:2016", "ISO", "contact and clearance"),
            ("ISO 10218-1:2011", "ISO", "speed and separation"),
            ("ISO 9283:1998", "ISO", "pose accuracy"),
        ],
    ),
    (
        "software and risk",
        PALETTE["amber"],
        [
            ("IEC 62304", "IEC", "software life cycle"),
            ("ISO 14971:2019", "ISO", "risk management"),
            ("ISO 13849-1:2023", "ISO", "control-path level"),
        ],
    ),
    (
        "autonomy",
        PALETTE["purple"],
        [
            ("UL 4600 (2023)", "UL", "autonomy safety case"),
            ("IEEE Std 7009-2024", "IEEE", "fail-safe default"),
        ],
    ),
    (
        "clinical baselines",
        PALETTE["rose"],
        [
            ("Dutch cohort 2025", "literature", "human comparator"),
            ("Callery Fistula Risk Score", "published score", "anastomosis quality, VVUQ 07"),
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


def upright(deg):
    d = deg % 360
    return deg - 180 if 90 < d < 270 else deg


def main():
    n_seg = sum(len(d[2]) for d in DOMAINS)
    seg_deg = 360.0 / n_seg

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 1, left=0.04, right=0.96, top=0.905, bottom=0.265)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-3.3, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")

    # Hub.
    ax.add_patch(Circle((0, 0), 0.9, facecolor=PALETTE["panel"], edgecolor=PALETTE["navy"], linewidth=2.2, zorder=5))
    ax.text(
        0,
        0,
        textwrap.fill("VVUQ-02 assurance corpus (papers/VVUQ-02/inputs)", 15),
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["navy"],
        zorder=6,
    )

    start = 90.0
    flag_rose = []
    for name, color, segs in DOMAINS:
        k = len(segs)
        d_t1 = start - k * seg_deg
        d_t2 = start
        # inner domain wedge
        ax.add_patch(
            Wedge((0, 0), 1.7, d_t1, d_t2, width=0.8, facecolor=color, edgecolor="white", linewidth=1.6, zorder=3)
        )
        dmid = (d_t1 + d_t2) / 2
        ax.text(
            1.28 * np.cos(np.radians(dmid)),
            1.28 * np.sin(np.radians(dmid)),
            textwrap.fill(name, 12),
            rotation=upright(dmid),
            rotation_mode="anchor",
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color="white",
            zorder=4,
        )
        for j, (desig, body, used) in enumerate(segs):
            t2 = start - j * seg_deg
            t1 = t2 - seg_deg
            ax.add_patch(
                Wedge(
                    (0, 0),
                    3.0,
                    t1,
                    t2,
                    width=1.3,
                    facecolor=tint(color, 0.62),
                    edgecolor="white",
                    linewidth=1.4,
                    zorder=3,
                )
            )
            mid = (t1 + t2) / 2
            block = textwrap.fill(desig, 15) + "\n" + body + "\n" + textwrap.fill(used, 16)
            ax.text(
                2.34 * np.cos(np.radians(mid)),
                2.34 * np.sin(np.radians(mid)),
                block,
                rotation=upright(mid),
                rotation_mode="anchor",
                ha="center",
                va="center",
                fontsize=6.8,
                linespacing=0.95,
                color=PALETTE["ink"],
                zorder=4,
            )
            if desig.startswith("FDA") or name == "clinical baselines":
                flag_rose.append((t1, t2))
        start = d_t1

    # Regulatory and clinical relevancy ticks on the flagged outer segments.
    for t1, t2 in flag_rose:
        ax.add_patch(
            Wedge((0, 0), 3.12, t1 + 1.5, t2 - 1.5, width=0.1, facecolor=PALETTE["rose"], edgecolor="none", zorder=4)
        )

    # Regulatory relevancy callout (fig-level, below the wheel).
    fig.add_artist(
        FancyBboxPatch(
            (0.07, 0.175),
            0.86,
            0.075,
            boxstyle="round,pad=0,rounding_size=0.01",
            transform=fig.transFigure,
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
            mutation_aspect=0.5,
        )
    )
    fig.add_artist(
        Rectangle((0.07, 0.175), 0.012, 0.075, transform=fig.transFigure, facecolor=PALETTE["rose"], edgecolor="none")
    )
    fig.text(
        0.095,
        0.235,
        "Regulatory and clinical relevancy",
        ha="left",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    fig.text(
        0.095,
        0.20,
        textwrap.fill(
            "Deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III clearance, "
            "IRB approval, and regulatory authorization.",
            95,
        ),
        ha="left",
        va="center",
        fontsize=9,
        color=PALETTE["ink"],
    )

    # Domain legend with per-domain segment counts.
    handles = [Patch(facecolor=c, edgecolor="white", label=f"{nm} ({len(s)})") for nm, c, s in DOMAINS]
    leg = fig.legend(
        handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.093), ncol=3, fontsize=8.5, frameon=True
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])
    fig.text(
        0.5,
        0.065,
        "Issuing bodies: ASME, NASA, IEC, ISO, UL, IEEE, FDA, plus published clinical literature",
        ha="center",
        va="center",
        fontsize=9,
        style="italic",
        color=PALETTE["gray"],
    )

    add_frame(
        fig,
        "Clinical and Regulatory Standards Wheel",
        "The wired input corpus: 14 consensus standards and 2 clinical baselines across 6 domains (papers/VVUQ-02/inputs)",
        "cancer-automated v1.0.0  |  source: inputs/README.md, inputs/standards/manifest.yaml, inputs/clinical/, "
        "codegen/config/project.yaml  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
