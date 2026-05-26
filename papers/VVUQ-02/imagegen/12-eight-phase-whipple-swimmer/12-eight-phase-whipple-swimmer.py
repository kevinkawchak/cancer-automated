"""VVUQ-02 figure 12: 60-second 8-phase Whipple swimmer plot.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/12-eight-phase-whipple-swimmer.
Grounding: codegen/config/project.yaml phases, execution section 05
eight_phase_timeline.txt, anastomosis ring-tension targets via execution section
02.6. Depends only on matplotlib and numpy.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
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

OUT = "papers/VVUQ-02/imagegen/12-eight-phase-whipple-swimmer/12-eight-phase-whipple-swimmer.png"

# id, full name, short label, start s, end s
PHASES = [
    (1, "Kocher exploration", "Kocher", 0, 6),
    (2, "venous control, dissection", "venous", 6, 16),
    (3, "uncinate, artery first", "uncinate", 16, 24),
    (4, "specimen removal en bloc", "specimen", 24, 32),
    (5, "pancreaticojejunostomy (PJ)", "PJ", 32, 42),
    (6, "hepaticojejunostomy (HJ)", "HJ", 42, 48),
    (7, "gastrojejunostomy (GJ)", "GJ", 48, 54),
    (8, "hemostasis, closure", "closure", 54, 60),
]
MILESTONES = [(42, "PJ 0.45 N grade A", "right"), (48, "HJ 0.50 N", "center"), (54, "GJ 0.60 N", "left")]
PINK = (0.953, 0.835, 0.812)


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


def lerp(c1, c2, t):
    a = tuple(int(c1.lstrip("#")[i : i + 2], 16) / 255 for i in (0, 2, 4))
    b = tuple(int(c2.lstrip("#")[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def rbar(ax, x0, x1, yc, hh, color, edge="white"):
    ax.add_patch(
        FancyBboxPatch(
            (x0, yc - hh),
            x1 - x0,
            2 * hh,
            boxstyle="round,pad=0,rounding_size=0.5",
            facecolor=color,
            edgecolor=edge,
            linewidth=1.4,
            mutation_aspect=0.05,
        )
    )


def main():
    assert sum(e - s for _, _, _, s, e in PHASES) == 60

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 1, left=0.19, right=0.95, top=0.855, bottom=0.135)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(-1, 61)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    bounds = [0, 6, 16, 24, 32, 42, 48, 54, 60]
    ax.set_xticks(bounds)
    ax.set_xticklabels([str(b) for b in bounds], fontsize=9)
    ax.set_xlabel("procedure time (s), reused verbatim from the PDAC 8-arm baseline for comparability", fontsize=10)

    lanes = {"L": 0.88, "R": 0.70, "suture": 0.46, "safety": 0.22}
    hh = 0.07
    phase_colors = [lerp(PALETTE["teal"], PALETTE["navy"], i / 7) for i in range(8)]

    for b in bounds:
        ax.axvline(b, ymin=0.04, ymax=0.92, color=PALETTE["grid"], linestyle=(0, (3, 3)), linewidth=0.8, zorder=1)

    # Hand lanes.
    for pid, full, short, s, e in PHASES:
        col = phase_colors[pid - 1]
        lum = 0.299 * col[0] + 0.587 * col[1] + 0.114 * col[2]
        tcol = "white" if lum < 0.62 else PALETTE["ink"]
        for lane in ("L", "R"):
            rbar(ax, s, e, lanes[lane], hh, col)
            ax.text(
                (s + e) / 2,
                lanes[lane],
                f"P{pid}\n{short}",
                ha="center",
                va="center",
                fontsize=7.6,
                fontweight="bold",
                color=tcol,
                linespacing=0.9,
            )
        ax.text(
            (s + e) / 2,
            lanes["L"] - hh - 0.022,
            f"{e - s} s",
            ha="center",
            va="center",
            fontsize=8,
            color=PALETTE["gray"],
        )

    # Suturing lane.
    rbar(ax, 32, 54, lanes["suture"], 0.05, PALETTE["rose"])
    ax.text(
        37,
        lanes["suture"],
        "needle-driver grasp",
        ha="center",
        va="center",
        fontsize=8.5,
        fontweight="bold",
        color="white",
    )
    for t, lab, align in MILESTONES:
        ax.scatter(
            t, lanes["suture"], marker="D", s=95, color=PALETTE["rose"], edgecolor="white", linewidth=1.0, zorder=5
        )
        tx = t - 1.2 if align == "right" else (t + 1.2 if align == "left" else t)
        ax.text(
            tx,
            lanes["suture"] + 0.085,
            lab,
            ha=align,
            va="bottom",
            fontsize=7.8,
            fontweight="bold",
            color=PALETTE["rose"],
        )

    # Safety surface lane (continuous).
    ax.add_patch(
        Rectangle(
            (0, lanes["safety"] - 0.07), 60, 0.14, facecolor=PINK, edgecolor=PALETTE["red"], linewidth=1.2, zorder=2
        )
    )
    ax.text(
        33,
        lanes["safety"] + 0.028,
        "vascular no-fly, shared-OR collision, fault e-stop active every tick",
        ha="center",
        va="center",
        fontsize=8.3,
        fontweight="bold",
        color=PALETTE["red"],
    )
    for k, gid in enumerate(["06", "09", "10"]):
        ax.scatter(3 + k * 3.2, lanes["safety"] - 0.032, s=110, color=PALETTE["red"], zorder=4)
        ax.text(
            3 + k * 3.2,
            lanes["safety"] - 0.032,
            gid,
            ha="center",
            va="center",
            fontsize=6.5,
            fontweight="bold",
            color="white",
            zorder=5,
        )

    # Phase-name key in the empty left of the suturing lane.
    rows = [(0, 4), (1, 5), (2, 6), (3, 7)]
    for r, (i1, i2) in enumerate(rows):
        yk = 0.515 - r * 0.027
        ax.text(0, yk, f"P{PHASES[i1][0]} {PHASES[i1][1]}", ha="left", va="center", fontsize=6.6, color=PALETTE["ink"])
        ax.text(
            15.5, yk, f"P{PHASES[i2][0]} {PHASES[i2][1]}", ha="left", va="center", fontsize=6.6, color=PALETTE["ink"]
        )

    # Lane labels in the left margin.
    fig.canvas.draw()
    inv = fig.transFigure.inverted()
    lane_names = {
        "L": "Left hand (L)",
        "R": "Right hand (R)",
        "suture": "Suturing window\n(needle driver)",
        "safety": "Catastrophe-gate\nsafety surface\n(06, 09, 10)",
    }
    for key, yc in lanes.items():
        _, fy = inv.transform(ax.transData.transform((0, yc)))
        fig.text(
            0.025, fy, lane_names[key], ha="left", va="center", fontsize=8.8, fontweight="bold", color=PALETTE["ink"]
        )

    # Top legend: phase ramp plus milestone and safety swatches.
    for i in range(8):
        ax.add_patch(
            Rectangle(
                (0 + i * 1.8, 0.965),
                1.7,
                0.03,
                facecolor=phase_colors[i],
                edgecolor="white",
                linewidth=0.6,
                clip_on=False,
            )
        )
    ax.text(0, 0.945, "P1", ha="left", va="top", fontsize=7, color=PALETTE["ink"])
    ax.text(14.4, 0.945, "P8 (teal to navy)", ha="right", va="top", fontsize=7, color=PALETTE["ink"])
    handles = [
        Line2D(
            [0],
            [0],
            marker="D",
            color="none",
            markerfacecolor=PALETTE["rose"],
            markeredgecolor="white",
            markersize=10,
            label="anastomosis milestone",
        ),
        Patch(facecolor=PINK, edgecolor=PALETTE["red"], label="catastrophe gate active"),
    ]
    leg = ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, 0.965), fontsize=8.3, frameon=True, ncol=2)
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    add_frame(
        fig,
        "60-Second 8-Phase Whipple Swimmer",
        f"One autonomous humanoid, two hands active every phase; the catastrophe gates monitor throughout (execution {SECTION}05)",
        f"cancer-automated v1.0.0  |  source: codegen/config/project.yaml phases, execution {SECTION}05 "
        "eight_phase_timeline.txt  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
