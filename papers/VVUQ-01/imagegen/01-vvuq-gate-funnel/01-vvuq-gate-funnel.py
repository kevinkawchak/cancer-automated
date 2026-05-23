"""VVUQ Gate Decision Funnel (Image 01).

Renders a portrait, full page, 300 dpi figure showing six candidate
deliverables entering the VVUQ gate and only one surviving to ship, with each
drop labeled by the dimension that blocked it.

Grounding: vvuq/vvuq_gate.py, configs/vvuq_thresholds.yaml (code generation
v0.1.0) and papers/VVUQ-01/execution/03-vvuq/README.md (code execution v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch, Polygon

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


def best_text_color(hex_fill):
    """Return white or near black text for legible contrast on a fill."""
    r = int(hex_fill[1:3], 16) / 255
    g = int(hex_fill[3:5], 16) / 255
    b = int(hex_fill[5:7], 16) / 255
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "#FFFFFF" if luminance < 0.55 else PALETTE["ink"]


def _shrink_to_width(fig, text_obj, max_frac, floor):
    """Reduce a text object font size until it fits max_frac of the figure."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    max_w = max_frac * fig.bbox.width
    size = text_obj.get_fontsize()
    while size > floor and text_obj.get_window_extent(renderer=renderer).width > max_w:
        size -= 0.5
        text_obj.set_fontsize(size)


def add_frame(fig, title, subtitle, footer):
    """Place the shared header, subtitle, and two line footer in their bands."""
    fig.text(0.5, 0.965, title, ha="center", va="center", fontsize=20, fontweight="bold", color=PALETTE["ink"])
    sub = fig.text(0.5, 0.935, subtitle, ha="center", va="center", fontsize=12.5, color=PALETTE["ink"])
    _shrink_to_width(fig, sub, 0.88, 10.0)
    parts = [p.strip() for p in footer.split("|")]
    line1 = parts[0] + "  |  " + parts[1]
    line2 = parts[2]
    f1 = fig.text(0.5, 0.040, line1, ha="center", va="center", fontsize=9, color=PALETTE["gray"])
    f2 = fig.text(0.5, 0.020, line2, ha="center", va="center", fontsize=9, color=PALETTE["gray"])
    _shrink_to_width(fig, f1, 0.90, 7.5)
    _shrink_to_width(fig, f2, 0.90, 7.5)


def band_color(level):
    """Navy to teal vertical progression across the three gate bands."""
    navy = (31, 58, 95)
    teal = (42, 157, 143)
    t = level / 2.0
    return tuple((navy[i] + (teal[i] - navy[i]) * t) / 255 for i in range(3))


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(1, 1, left=0.06, right=0.94, top=0.91, bottom=0.07, figure=fig)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    add_frame(
        fig,
        "VVUQ Gate Decision Funnel",
        "Six candidate deliverables enter, one ships, five are blocked",
        "cancer-automated v0.3.0  |  source: vvuq/vvuq_gate.py, configs/vvuq_thresholds.yaml, execution §03  |  white background, 300 dpi, portrait",
    )

    ax.text(
        0.5,
        0.978,
        "Generation of all six candidates took under 1 ms of stage time; the gate is the substantial step",
        ha="center",
        va="center",
        fontsize=10,
        style="italic",
        color=PALETTE["gray"],
    )

    # Funnel geometry. bands = (top count, bottom count) top to bottom.
    bands = [(6, 5), (5, 3), (3, 1), (1, 1)]
    labels = ["Verification", "Validation", "Uncertainty", "Accept"]
    counts_text = ["6 in, 5 pass", "5 in, 3 pass", "3 in, 1 pass", "1 in, 1 ship"]
    cx = 0.40
    scale = 0.032  # count to half width
    heights = [0.215, 0.215, 0.215, 0.135]
    y_top = 0.90

    level_mid_y = []
    level_right_x = []
    y = y_top
    for i, (top_c, bot_c) in enumerate(bands):
        h = heights[i]
        yb = y - h
        htw = top_c * scale
        hbw = bot_c * scale
        if i < 3:
            fill = band_color(i)
            fill_hex = "#%02X%02X%02X" % tuple(int(round(c * 255)) for c in fill)
        else:
            fill = PALETTE["green"]
            fill_hex = PALETTE["green"]
        ax.add_patch(
            Polygon(
                [(cx - htw, y), (cx + htw, y), (cx + hbw, yb), (cx - hbw, yb)],
                closed=True,
                facecolor=fill,
                edgecolor="white",
                linewidth=1.5,
                zorder=3,
            )
        )
        tc = best_text_color(fill_hex)
        if i < 3:
            ax.text(
                cx,
                y - 0.30 * h,
                labels[i],
                ha="center",
                va="center",
                fontsize=11.5,
                fontweight="bold",
                color=tc,
                zorder=6,
            )
            ax.text(cx, y - 0.55 * h, counts_text[i], ha="center", va="center", fontsize=10.5, color=tc, zorder=6)
        level_mid_y.append((y + yb) / 2)
        level_right_x.append(cx + (htw + hbw) / 2)
        y = yb

    # Left gutter: gate evaluation order arrow.
    ax.annotate(
        "", xy=(0.10, 0.16), xytext=(0.10, 0.86), arrowprops=dict(arrowstyle="-|>", color=PALETTE["gray"], linewidth=2)
    )
    ax.text(
        0.072, 0.51, "Gate evaluation order", ha="center", va="center", rotation=90, fontsize=9, color=PALETTE["gray"]
    )

    # Right callout cards for the five dropped or escalated cases.
    cards = [
        ("Case 6", "verification fraction 0.83 below 1.0 (artifact exceeds 200K cap)", PALETTE["red"], 0),
        ("Case 2", "human review not recorded", PALETTE["red"], 1),
        ("Case 4", "validation agreement 0.00 below 0.95; max relative error 0.600 above 0.05", PALETTE["red"], 1),
        ("Case 3", "max cv 0.365 above 0.1, escalated to human", PALETTE["amber"], 2),
        ("Case 5", "only 2 runs, need 3", PALETTE["red"], 2),
    ]
    card_x = 0.64
    card_w = 0.345
    card_h = 0.135
    gap = 0.0275
    top0 = 0.90
    for j, (name, reason, accent, level) in enumerate(cards):
        cy_top = top0 - j * (card_h + gap)
        cy = cy_top - card_h / 2
        ax.add_patch(
            FancyBboxPatch(
                (card_x, cy_top - card_h),
                card_w,
                card_h,
                boxstyle="round,pad=0.006,rounding_size=0.012",
                facecolor=PALETTE["panel"],
                edgecolor=PALETTE["grid"],
                linewidth=1.0,
                zorder=4,
            )
        )
        ax.add_patch(
            Polygon(
                [
                    (card_x, cy_top - card_h),
                    (card_x + 0.012, cy_top - card_h),
                    (card_x + 0.012, cy_top),
                    (card_x, cy_top),
                ],
                closed=True,
                facecolor=accent,
                edgecolor="none",
                zorder=5,
            )
        )
        tag = "BLOCK" if accent == PALETTE["red"] else "ESCALATE"
        ax.text(
            card_x + 0.028,
            cy_top - 0.026,
            f"{name}  {tag}",
            ha="left",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=accent,
            zorder=6,
        )
        ax.text(
            card_x + 0.028,
            cy_top - 0.052,
            textwrap.fill(reason, width=38),
            ha="left",
            va="top",
            fontsize=9.5,
            color=PALETTE["ink"],
            zorder=6,
        )
        ax.annotate(
            "",
            xy=(card_x, cy),
            xytext=(level_right_x[level], level_mid_y[level]),
            arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], linewidth=0.9, linestyle=(0, (4, 3))),
            zorder=2,
        )

    # Accept badge beside the green tip, with the verbatim accept scores.
    ax.add_patch(
        FancyBboxPatch(
            (0.115, 0.205),
            0.17,
            0.044,
            boxstyle="round,pad=0.004,rounding_size=0.02",
            facecolor=PALETTE["green"],
            edgecolor="none",
            zorder=5,
        )
    )
    ax.text(0.20, 0.227, "ACCEPT", ha="center", va="center", fontsize=11, fontweight="bold", color="white", zorder=6)
    ax.annotate(
        "",
        xy=(0.368, 0.215),
        xytext=(0.285, 0.227),
        arrowprops=dict(arrowstyle="-|>", color=PALETTE["green"], linewidth=1.6),
    )
    ax.text(
        0.20,
        0.188,
        textwrap.fill("verification 1.0, agreement 1.0, rel err 0.0, max cv 0.0068, n=3", width=30),
        ha="center",
        va="top",
        fontsize=9,
        color=PALETTE["ink"],
    )

    # Legend in a horizontal row at the lower left of the content band.
    legend_items = [
        ("Accepted", PALETTE["green"]),
        ("Blocked", PALETTE["red"]),
        ("Escalated to human", PALETTE["amber"]),
    ]
    lx = 0.02
    for label, color in legend_items:
        ax.add_patch(
            Polygon(
                [(lx, 0.02), (lx + 0.022, 0.02), (lx + 0.022, 0.042), (lx, 0.042)],
                facecolor=color,
                edgecolor="none",
                zorder=5,
            )
        )
        ax.text(lx + 0.03, 0.031, label, ha="left", va="center", fontsize=9, color=PALETTE["ink"])
        lx += 0.045 + 0.013 * len(label)

    fig.savefig("papers/VVUQ-01/imagegen/01-vvuq-gate-funnel/01-vvuq-gate-funnel.png", dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
