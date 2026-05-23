"""2030 PDAC Hybrid Pilot Timeline (Image 05).

Renders a portrait, full page, 300 dpi Gantt of the 168 day hybrid surgery and
medicine pilot: a 60 second 8 arm robotic Whipple on day 0 plus six 28 day
Daraxonrasib adjuvant cycles through day 168.

Grounding: physical-ai/hybrid_surgery_medicine.py and physical-ai/README.md
(code generation v0.1.0) and papers/VVUQ-01/execution/05-physical-ai-stage2/
README.md plus the saved pdac_hybrid_pilot_timeline.txt artifact (code execution
v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch

PALETTE = {
    "navy": "#1F3A5F",
    "slate": "#4C72B0",
    "teal": "#2A9D8F",
    "green": "#2E7D32",
    "red": "#C0392B",
    "amber": "#E1A93B",
    "gray": "#6B7280",
    "panel": "#F4F6F8",
    "grid": "#D9DEE3",
    "ink": "#1A1A1A",
}


def best_text_color(rgb):
    lum = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    return "#FFFFFF" if lum < 0.55 else PALETTE["ink"]


def teal_progression(k, n=6):
    light = (159, 216, 206)
    deep = (42, 157, 143)
    t = k / (n - 1)
    return tuple((light[i] + (deep[i] - light[i]) * t) / 255 for i in range(3))


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
    _shrink_to_width(fig, sub, 0.88, 9.5)
    parts = [p.strip() for p in footer.split("|")]
    f1 = fig.text(
        0.5, 0.040, parts[0] + "  |  " + parts[1], ha="center", va="center", fontsize=9, color=PALETTE["gray"]
    )
    f2 = fig.text(0.5, 0.020, parts[2], ha="center", va="center", fontsize=9, color=PALETTE["gray"])
    _shrink_to_width(fig, f1, 0.90, 7.5)
    _shrink_to_width(fig, f2, 0.90, 7.5)


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(
        3, 1, height_ratios=[0.7, 2.6, 0.6], left=0.06, right=0.94, top=0.90, bottom=0.07, hspace=0.22, figure=fig
    )

    add_frame(
        fig,
        "2030 PDAC Hybrid Pilot Timeline",
        "A 60 second 8 arm robotic Whipple on day 0 plus six 28 day Daraxonrasib cycles, 168 regimen days",
        "cancer-automated v0.3.0  |  source: physical-ai/hybrid_surgery_medicine.py, execution §05 artifact pdac_hybrid_pilot_timeline.txt  |  white background, 300 dpi, portrait",
    )

    # Summary strip.
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)
    ax0.axis("off")
    cards = [
        ("Surgery", "60.0 s, 8 arms", None),
        ("Medicine", "Daraxonrasib, 6 cycles", None),
        ("Regimen", "168 days (6 x 28)", None),
        ("Events", "7, human oversight required", PALETTE["amber"]),
    ]
    cw, gap = 0.235, 0.02
    for i, (head, value, accent) in enumerate(cards):
        cx = 0.005 + i * (cw + gap)
        ax0.add_patch(
            FancyBboxPatch(
                (cx, 0.12),
                cw,
                0.76,
                boxstyle="round,pad=0.006,rounding_size=0.04",
                facecolor=PALETTE["panel"],
                edgecolor=PALETTE["grid"],
                linewidth=1.1,
            )
        )
        if accent:
            ax0.add_patch(
                FancyBboxPatch((cx, 0.12), 0.014, 0.76, boxstyle="square,pad=0", facecolor=accent, edgecolor="none")
            )
        ax0.text(
            cx + cw / 2, 0.64, head, ha="center", va="center", fontsize=11.5, fontweight="bold", color=PALETTE["navy"]
        )
        ax0.text(
            cx + cw / 2,
            0.36,
            textwrap.fill(value, width=20),
            ha="center",
            va="center",
            fontsize=10.5,
            color=PALETTE["ink"],
        )

    # Gantt.
    ax = fig.add_subplot(gs[1, 0])
    ax.set_xlim(-74, 194)
    ax.set_ylim(-0.7, 6.7)
    ax.set_xticks([0, 28, 56, 84, 112, 140, 168])
    ax.set_xticklabels(["0", "28", "56", "84", "112", "140", "168"], fontsize=10, color=PALETTE["ink"])
    ax.set_yticks([])
    ax.set_xlabel("Days since surgery", fontsize=11, color=PALETTE["ink"])
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, color=PALETTE["grid"], linewidth=0.8)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(PALETTE["grid"])
    ax.tick_params(colors=PALETTE["ink"])

    row_y = [6, 5, 4, 3, 2, 1, 0]
    labels = [
        "Robotic Whipple (60 second)",
        "Daraxonrasib (adjuvant)",
        "Daraxonrasib (adjuvant)",
        "Daraxonrasib (adjuvant)",
        "Daraxonrasib (adjuvant)",
        "Daraxonrasib (adjuvant)",
        "Daraxonrasib (adjuvant)",
    ]
    for y, lab in zip(row_y, labels):
        ax.text(-72, y, lab, ha="left", va="center", fontsize=10, color=PALETTE["ink"])

    bar_h = 0.5
    for k in range(6):
        start = 28 * k
        rgb = teal_progression(k)
        y = row_y[k + 1]
        ax.add_patch(
            FancyBboxPatch(
                (start + 1.5, y - bar_h / 2),
                25,
                bar_h,
                boxstyle="round,pad=0,rounding_size=2.4",
                facecolor=rgb,
                edgecolor="white",
                linewidth=1.0,
                mutation_aspect=0.12,
            )
        )
        ax.text(
            start + 14,
            y,
            f"cycle {k + 1}",
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=best_text_color(rgb),
        )
        ax.text(start + 28 + 3, y, f"day {28 * (k + 1)}", ha="left", va="center", fontsize=9.5, color=PALETTE["ink"])

    # Surgery point marker at day 0.
    ax.scatter([0], [6], s=320, marker="D", color=PALETTE["navy"], edgecolors="white", linewidths=1.2, zorder=5)
    ax.scatter([0], [6], s=70, marker="D", color=PALETTE["red"], zorder=6)
    ax.text(6, 6, "8 arm, 60 s", ha="left", va="center", fontsize=10, fontweight="bold", color=PALETTE["navy"])

    # Reference lines.
    ax.axvline(0, ymin=0.04, ymax=0.96, color=PALETTE["navy"], linewidth=1.4, linestyle=(0, (5, 3)), zorder=1)
    ax.axvline(168, ymin=0.04, ymax=0.96, color=PALETTE["green"], linewidth=1.6, linestyle=(0, (5, 3)), zorder=1)
    ax.text(
        168,
        6.5,
        "regimen complete, day 168",
        ha="right",
        va="bottom",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["green"],
    )

    # Stage 2 assurance note.
    ax2 = fig.add_subplot(gs[2, 0])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    ax2.add_patch(
        FancyBboxPatch(
            (0.0, 0.08),
            1.0,
            0.84,
            boxstyle="round,pad=0.006,rounding_size=0.06",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.2,
        )
    )
    note = (
        "Stage 2 reference, disabled by default. The lights off line requires the vvuq_gate_online interlock "
        "and this pilot sets requires_human_oversight True. Real use needs VVUQ clearance, human oversight, "
        "IRB approval, and regulatory authorization."
    )
    ax2.text(0.5, 0.5, textwrap.fill(note, width=92), ha="center", va="center", fontsize=10, color=PALETTE["ink"])

    fig.savefig("papers/VVUQ-01/imagegen/05-pdac-pilot-timeline/05-pdac-pilot-timeline.png", dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
