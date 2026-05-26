"""VVUQ-02 figure 02: VVUQ gate decision funnel.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/02-vvuq-gate-decision-funnel.
Grounding: codegen/config/vvuq_thresholds.yaml and execution section 03 decision
surface. Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch, Polygon, Rectangle

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

OUT = "papers/VVUQ-02/imagegen/02-vvuq-gate-decision-funnel/02-vvuq-gate-decision-funnel.png"


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


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))


def lerp(c1, c2, t):
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def card(ax, x0, y0, x1, y1, accent, header, body):
    ax.add_patch(
        FancyBboxPatch(
            (x0, y0),
            x1 - x0,
            y1 - y0,
            boxstyle="round,pad=0,rounding_size=0.012",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
            mutation_aspect=0.6,
        )
    )
    ax.add_patch(Rectangle((x0, y0), 0.012, y1 - y0, facecolor=accent, edgecolor="none"))
    ax.text(x0 + 0.028, y1 - 0.022, header, ha="left", va="top", fontsize=9.5, fontweight="bold", color=PALETTE["ink"])
    ax.text(
        x0 + 0.028,
        y1 - 0.05,
        textwrap.fill(body, 32),
        ha="left",
        va="top",
        fontsize=9,
        color=PALETTE["ink"],
    )


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 1, left=0.06, right=0.94, top=0.91, bottom=0.07)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cx, scale = 0.33, 0.052
    y_hi, y_lo = 0.085, 0.855
    bands = [
        ("Verify", "5 in, 4 pass", 5, 4),
        ("Validate", "4 in, 3 pass", 4, 3),
        ("Quantify", "3 in, 2 pass", 3, 2),
        ("Hard predicate", "2 in, 1 pass", 2, 1),
        ("Accept", "1 ships", 1, 1),
    ]
    n = len(bands)
    band_h = (y_lo - y_hi) / n
    mids = []
    for i, (name, counts, top_c, bot_c) in enumerate(bands):
        yt = y_lo - i * band_h
        yb = yt - band_h
        thw, bhw = top_c * scale, bot_c * scale
        color = lerp(PALETTE["navy"], PALETTE["teal"], i / (n - 2)) if i < n - 1 else hex_to_rgb(PALETTE["green"])
        poly = Polygon(
            [(cx - thw, yt), (cx + thw, yt), (cx + bhw, yb), (cx - bhw, yb)],
            closed=True,
            facecolor=color,
            edgecolor="white",
            linewidth=1.5,
        )
        ax.add_patch(poly)
        mids.append((yt + yb) / 2)
        if i < n - 1:
            ax.text(
                cx,
                (yt + yb) / 2 + 0.012,
                name,
                ha="center",
                va="center",
                fontsize=10.5,
                fontweight="bold",
                color="white",
            )
            ax.text(cx, (yt + yb) / 2 - 0.022, counts, ha="center", va="center", fontsize=9, color="white")

    # Accept badge beside the green tip.
    ax.add_patch(
        FancyBboxPatch(
            (0.435, mids[4] - 0.028),
            0.105,
            0.056,
            boxstyle="round,pad=0,rounding_size=0.02",
            facecolor=PALETTE["green"],
            edgecolor="none",
            mutation_aspect=0.6,
        )
    )
    ax.text(0.4875, mids[4], "ACCEPT", ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    ax.text(
        0.4875,
        mids[4] - 0.05,
        "Case A: all 10 gates pass;\ncomposite 93.56",
        ha="center",
        va="top",
        fontsize=9,
        color=PALETTE["ink"],
    )

    # Left gutter: gate evaluation order arrow.
    ax.add_patch(
        FancyArrowPatch(
            (0.045, y_lo), (0.045, y_hi), arrowstyle="-|>", mutation_scale=16, color=PALETTE["gray"], lw=1.6
        )
    )
    ax.text(
        0.028,
        (y_hi + y_lo) / 2,
        "gate evaluation order",
        rotation=90,
        ha="center",
        va="center",
        fontsize=9,
        color=PALETTE["gray"],
    )

    # Right callout cards keyed to the funnel level where each case drops.
    drops = [
        (
            0,
            PALETTE["red"],
            "Case C  -  gate 08 perception",
            "Verify drop: verification fraction 0.80 below 1.0 (4 of 5 structural checks)",
        ),
        (
            1,
            PALETTE["red"],
            "Case D  -  gate 03 balance",
            "Validate drop: agreement 0.00 below 0.98; max relative error 0.500 above 0.03",
        ),
        (
            2,
            PALETTE["amber"],
            "Case E  -  gate 02 finger-force",
            "Quantify escalate: max cv 0.163 above 0.10; escalated to hand-back-to-human",
        ),
        (
            3,
            PALETTE["red"],
            "Case B  -  gate 06 vascular",
            "Hard predicate fail: hard check hard_stop_violations_zero failed",
        ),
    ]
    card_x0, card_x1 = 0.63, 0.99
    for band_i, accent, header, body in drops:
        cyt = mids[band_i] + 0.065
        cyb = mids[band_i] - 0.065
        card(ax, card_x0, cyb, card_x1, cyt, accent, header, body)
        # leader from funnel right edge to card
        thw = bands[band_i][2] * scale
        ax.add_patch(
            FancyArrowPatch(
                (cx + thw, mids[band_i]),
                (card_x0, mids[band_i]),
                arrowstyle="-|>",
                mutation_scale=10,
                color=accent,
                lw=1.2,
                linestyle=(0, (3, 2)),
            )
        )

    # Asymmetry annotation near the top.
    ax.text(
        0.5,
        0.925,
        "Generating each candidate took microseconds; the four-dimension gate is the substantial step",
        ha="center",
        va="center",
        fontsize=10,
        style="italic",
        color=PALETTE["gray"],
    )

    # Legend (lower left).
    handles = [
        Patch(facecolor=PALETTE["green"], edgecolor=PALETTE["green"], label="Accepted"),
        Patch(facecolor=PALETTE["red"], edgecolor=PALETTE["red"], label="Blocked"),
        Patch(facecolor=PALETTE["amber"], edgecolor=PALETTE["amber"], label="Escalated to human"),
    ]
    leg = ax.legend(
        handles=handles,
        loc="lower left",
        bbox_to_anchor=(0.0, 0.0),
        fontsize=9.5,
        frameon=True,
        title="Gate verdict",
        title_fontsize=9.5,
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])
    leg.get_frame().set_facecolor("white")

    add_frame(
        fig,
        "VVUQ Gate Decision Funnel",
        f"Five candidate cases enter, one ships; verify, validate, quantify, hard predicate (execution {SECTION}03)",
        f"cancer-automated v1.0.0  |  source: codegen/config/vvuq_thresholds.yaml, execution {SECTION}03  |  "
        "white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
