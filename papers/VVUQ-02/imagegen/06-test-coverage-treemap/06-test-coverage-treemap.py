"""VVUQ-02 figure 06: 172-test coverage treemap.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/06-test-coverage-treemap.
Grounding: execution section 01 test-suite.md (172 tests across 15 modules).
Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Patch, Rectangle

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

OUT = "papers/VVUQ-02/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.png"

# (subsystem, color, [(module, count, subject)]) sorted descending by count.
SUBSYSTEMS = [
    (
        "Assurance harness",
        PALETTE["navy"],
        [
            ("test_vvuq_gates.py", 64, "the 10-gate registry, thresholds, decision surface"),
            ("test_vvuq_framework.py", 9, "verify, validate, uncertainty, composition"),
            ("test_standards_corpus.py", 3, "the wired external-standards binding"),
        ],
    ),
    (
        "Behavior models",
        PALETTE["teal"],
        [
            ("test_safety.py", 12, "estop, human-collision FSM, vessel no-fly"),
            ("test_suturing.py", 11, "bimanual suture, ring tension, RMSE"),
            ("test_hands.py", 11, "fingertip force, bimanual caps, grasp, handover"),
            ("test_kinematics.py", 9, "DH forward kinematics, joint-limit clamp"),
            ("test_perception.py", 8, "segmentation, Dice, NIR/US/bile fusion"),
            ("test_balance.py", 8, "ZMP, support-polygon margin, recovery"),
            ("test_autonomy.py", 8, "LLM intent, deterministic compile, concordance"),
            ("test_sensors.py", 7, "per-tick per-hand sensor record synthesis"),
        ],
    ),
    (
        "Integration and harness",
        PALETTE["slate"],
        [
            ("test_llm.py", 7, "the 4-entrant tournament agent and caveats"),
            ("test_simulation.py", 6, "the 32-iteration Latin hypercube sweep"),
            ("test_metrics.py", 5, "the 6-component composite and gating overlay"),
            ("test_zenodo.py", 4, "L0 pointer JSON and cross-iteration manifest"),
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


def text_on(rgb):
    lum = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    return "white" if lum < 0.56 else PALETTE["ink"]


def main():
    total = sum(c for _, _, mods in SUBSYSTEMS for _, c, _ in mods)
    assert total == 172

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 1, left=0.06, right=0.94, top=0.90, bottom=0.07)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    tx0, tx1 = 0.0, 0.78
    ty0, ty1 = 0.135, 0.875
    span = tx1 - tx0
    height = ty1 - ty0

    x = tx0
    for sub_name, color, mods in SUBSYSTEMS:
        sub_total = sum(c for _, c, _ in mods)
        col_w = span * sub_total / total
        header_x = 0.87 if sub_name.startswith("Integration") else x + col_w / 2
        ax.text(
            header_x,
            ty1 + 0.018,
            f"{sub_name} {sub_total}",
            ha="center",
            va="bottom",
            fontsize=10.5,
            fontweight="bold",
            color=color,
        )
        y = ty1
        for rank, (mod, count, subject) in enumerate(mods):
            tile_h = height * count / sub_total
            yb = y - tile_h
            fill = tint(color, min(0.07 * rank, 0.42))
            ax.add_patch(Rectangle((x, yb), col_w, tile_h, facecolor=fill, edgecolor="white", linewidth=1.5, zorder=2))
            txt = text_on(fill)
            cx = x + col_w / 2
            cy = (y + yb) / 2
            is_int = sub_name.startswith("Integration")
            if mod == "test_vvuq_gates.py":
                ax.add_patch(
                    Rectangle(
                        (x + 0.012, yb + 0.012),
                        col_w - 0.024,
                        tile_h - 0.024,
                        facecolor="none",
                        edgecolor=PALETTE["green"],
                        linewidth=2.0,
                        zorder=3,
                    )
                )
            if is_int:
                # Narrow column: count big inside, label via right-margin leader.
                ax.text(cx, cy, str(count), ha="center", va="center", fontsize=15, fontweight="bold", color=txt)
                lx = 0.815
                ax.add_patch(
                    FancyArrowPatch((x + col_w, cy), (lx - 0.006, cy), arrowstyle="-", color=PALETTE["gray"], lw=0.8)
                )
                ax.text(
                    lx,
                    cy,
                    f"{mod} ({count})\n{textwrap.fill(subject, 26)}",
                    ha="left",
                    va="center",
                    fontsize=8,
                    linespacing=0.95,
                    color=PALETTE["ink"],
                )
            elif tile_h < 0.05:
                ax.text(
                    cx, cy, f"{mod} ({count})", ha="center", va="center", fontsize=8.2, fontweight="bold", color=txt
                )
            else:
                size_name = 12 if count == 64 else 9.5
                size_count = 22 if count == 64 else 13
                noff = min(tile_h * 0.28, 0.06)
                ax.text(cx, cy + noff, mod, ha="center", va="center", fontsize=size_name, fontweight="bold", color=txt)
                ax.text(cx, cy, str(count), ha="center", va="center", fontsize=size_count, fontweight="bold", color=txt)
                if tile_h >= 0.075:
                    ax.text(
                        cx,
                        cy - min(tile_h * 0.30, 0.075),
                        textwrap.fill(subject, 34),
                        ha="center",
                        va="center",
                        fontsize=8,
                        linespacing=0.95,
                        color=txt,
                    )
            y = yb
        x += col_w

    # Annotation (lower band).
    fig.text(
        0.06,
        0.105,
        textwrap.fill(
            "Assurance carries 76 of 172 tests, more than a third in the single gate suite alone (green keyline).", 60
        ),
        ha="left",
        va="center",
        fontsize=10,
        style="italic",
        color=PALETTE["ink"],
    )

    # Legend.
    handles = [
        Patch(facecolor=PALETTE["navy"], edgecolor="white", label="Assurance harness (76)"),
        Patch(facecolor=PALETTE["teal"], edgecolor="white", label="Behavior models (74)"),
        Patch(facecolor=PALETTE["slate"], edgecolor="white", label="Integration and harness (22)"),
    ]
    leg = fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.052), ncol=3, fontsize=9, frameon=True)
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    add_frame(
        fig,
        "172-Test Coverage Treemap",
        f"15 modules, 3 subsystems; the 10-gate suite carries 64 of 172 (execution {SECTION}01)",
        f"cancer-automated v1.0.0  |  source: execution {SECTION}01 test-suite.md  |  "
        "white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
