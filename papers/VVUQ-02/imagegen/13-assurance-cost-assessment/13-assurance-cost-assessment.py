"""VVUQ-02 figure 13: assurance cost assessment (autonomous cloud vs conventional).

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/13-assurance-cost-assessment. The bridge
uses an illustrative relative index (conventional baseline 100); the direction of
each step and the strengths and weaknesses are grounded verbatim in
execution/README.md. Depends only on matplotlib and numpy.
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

OUT = "papers/VVUQ-02/imagegen/13-assurance-cost-assessment/13-assurance-cost-assessment.png"

# name, signed step (illustrative), kind, reason
STEPS = [
    (
        "Conventional\nbaseline",
        100,
        "base",
        "human cycles terminal, editor, and git over days; installs the full optional matrix first",
    ),
    ("Near-zero\nsetup", -22, "down", "standard library plus four small guarded-import packages; core ran immediately"),
    (
        "One integrated\nagent loop",
        -20,
        "down",
        "read, run, process, document, lint, commit, push in one loop, no tool switch",
    ),
    (
        "Assurance breadth\nin one pass",
        -18,
        "down",
        "full accept, block, escalate surface plus the safety surface and structural processing",
    ),
    (
        "Self-verifying\nrecord",
        -12,
        "down",
        "every command and verbatim output captured, reproducible rather than trusted",
    ),
    ("Autonomous\ncloud run", 28, "resid", "the lower-cost result the bridge lands on"),
]
BULLETS = [
    ("Setup time", 0.12, 0.85, "lower is better"),
    ("Integration overhead", 0.15, 0.80, "lower is better"),
    ("Assurance breadth per run", 0.85, 0.50, "higher is better"),
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
    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(
        3, 1, height_ratios=[3.0, 1.7, 1.2], left=0.12, right=0.95, top=0.88, bottom=0.085, hspace=0.55
    )
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[2, 0])

    ax.set_xlim(-0.6, 5.6)
    ax.set_ylim(-44, 112)
    ax.set_ylabel("relative cost index\n(illustrative)", fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.grid(axis="y", color=PALETTE["grid"], linewidth=0.6)
    ax.axhline(0, color=PALETTE["grid"], linewidth=1.0)
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)

    running = 100
    levels = [100]
    w = 0.6
    for i, (name, step, kind, reason) in enumerate(STEPS):
        if kind == "base":
            base, top, color = 0, 100, PALETTE["gray"]
        elif kind == "resid":
            base, top, color = 0, 28, PALETTE["green"]
        else:
            top = running
            running = running + step
            base = running
            color = PALETTE["teal"]
            levels.append(running)
        ax.add_patch(
            Rectangle((i - w / 2, base), w, top - base, facecolor=color, edgecolor="white", linewidth=1.3, zorder=3)
        )
        ymid = (base + top) / 2
        tcol = "white" if color != PALETTE["amber"] else PALETTE["ink"]
        if kind == "down":
            ax.text(i, ymid, f"-{abs(step)}", ha="center", va="center", fontsize=11, fontweight="bold", color=tcol)
        else:
            ax.text(i, ymid, str(top), ha="center", va="center", fontsize=13, fontweight="bold", color="white")
        ax.text(i, top + 3, name, ha="center", va="bottom", fontsize=8.6, fontweight="bold", color=PALETTE["ink"])
        ax.text(
            i,
            -6,
            textwrap.fill(reason, 19),
            ha="center",
            va="top",
            fontsize=7.0,
            color=PALETTE["ink"],
            linespacing=0.95,
        )

    # Connectors at the running levels.
    conn = [100, 78, 58, 40, 28]
    for i, lvl in enumerate(conn):
        ax.plot(
            [i + w / 2, i + 1 - w / 2],
            [lvl, lvl],
            linestyle=(0, (4, 3)),
            color=PALETTE["gray"],
            linewidth=1.0,
            zorder=2,
        )

    ax.text(
        2.55,
        20,
        textwrap.fill(
            "faster too: the 172-test suite runs in about 1.38 s and generation is microsecond-scale; "
            "the assurance, not the generation, is where the cost sits",
            48,
        ),
        ha="center",
        va="center",
        fontsize=8.6,
        style="italic",
        color=PALETTE["gray"],
    )

    handles = [
        Patch(facecolor=PALETTE["gray"], edgecolor="white", label="conventional baseline"),
        Patch(facecolor=PALETTE["teal"], edgecolor="white", label="documented reduction"),
        Patch(facecolor=PALETTE["green"], edgecolor="white", label="autonomous cloud run"),
    ]
    leg = ax.legend(handles=handles, loc="upper right", bbox_to_anchor=(1.0, 1.0), fontsize=8.3, frameon=True)
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Bullet comparison.
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.text(
        0.0,
        1.02,
        "Three cost drivers (illustrative index, autonomous bar vs conventional tick)",
        ha="left",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    ys = [0.74, 0.45, 0.16]
    bx0, bw = 0.42, 0.5
    for (driver, auto, conv, better), y in zip(BULLETS, ys):
        ax2.text(0.0, y, driver, ha="left", va="center", fontsize=9, color=PALETTE["ink"])
        ax2.text(0.0, y - 0.08, better, ha="left", va="center", fontsize=7.5, style="italic", color=PALETTE["gray"])
        ax2.add_patch(
            Rectangle((bx0, y - 0.05), bw, 0.1, facecolor=PALETTE["panel"], edgecolor=PALETTE["grid"], linewidth=0.8)
        )
        ax2.add_patch(Rectangle((bx0, y - 0.035), bw * auto, 0.07, facecolor=PALETTE["green"], edgecolor="none"))
        ax2.plot([bx0 + bw * conv, bx0 + bw * conv], [y - 0.07, y + 0.07], color=PALETTE["red"], linewidth=2.6)
        ax2.text(bx0 + bw * auto + 0.01, y, "autonomous", ha="left", va="center", fontsize=7, color=PALETTE["green"])
        ax2.text(bx0 + bw * conv, y + 0.085, "conventional", ha="center", va="bottom", fontsize=7, color=PALETTE["red"])

    # Honesty card.
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis("off")
    ax3.add_patch(
        FancyBboxPatch(
            (0.0, 0.05),
            1.0,
            0.9,
            boxstyle="round,pad=0,rounding_size=0.02",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
            mutation_aspect=0.3,
        )
    )
    ax3.add_patch(Rectangle((0.0, 0.05), 0.014, 0.9, facecolor=PALETTE["amber"], edgecolor="none"))
    ax3.text(
        0.03,
        0.80,
        "What a conventional server still does better",
        ha="left",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    ax3.text(
        0.03,
        0.40,
        textwrap.fill(
            "Live on-prem LLM intent and judging, real Zenodo deposition, and mujoco or Isaac physics need a "
            "provisioned server with GPUs and keys; no display, GPU, or persistent warm cache in the ephemeral container.",
            96,
        ),
        ha="left",
        va="center",
        fontsize=8.6,
        color=PALETTE["ink"],
    )

    add_frame(
        fig,
        "Assurance Cost Assessment",
        "Autonomous cloud VVUQ versus conventional verification; the cost half of the thesis (execution README)",
        "cancer-automated v1.0.0  |  source: execution README this-run-versus-conventional, execution "
        f"{SECTION}01 test-suite.md  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
