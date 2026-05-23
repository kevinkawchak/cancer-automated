"""FDA Cost-Efficiency Bridge and Credibility Assessment (Image 08).

Renders a portrait, full page, 300 dpi figure: a top financial bridge that
attributes an illustrative cost reduction to each automation lever, and a bottom
credibility bullet assessment using the measured compliance scores.

Honesty: the cost bridge is an illustrative planning index, not measured
dollars. The credibility scores are measured values.

Grounding: papers/VVUQ-01/execution/README.md comparison, pipeline and
vvuq/vvuq_gate.py levers (v0.1.0 and v0.2.0), and the input corpus under
papers/VVUQ-01/inputs/ (FDA §VI.B credibility, ASME V&V 40, Verification 81.9,
Validation 85.75).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch, Rectangle

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
    _shrink_to_width(fig, sub, 0.88, 10.0)
    parts = [p.strip() for p in footer.split("|")]
    f1 = fig.text(
        0.5, 0.040, parts[0] + "  |  " + parts[1], ha="center", va="center", fontsize=9, color=PALETTE["gray"]
    )
    f2 = fig.text(0.5, 0.020, parts[2], ha="center", va="center", fontsize=9, color=PALETTE["gray"])
    _shrink_to_width(fig, f1, 0.90, 7.5)
    _shrink_to_width(fig, f2, 0.90, 7.5)


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(2, 1, height_ratios=[1.7, 1.2], left=0.08, right=0.94, top=0.90, bottom=0.08, hspace=0.30, figure=fig)

    add_frame(
        fig,
        "FDA Cost-Efficiency Bridge and Credibility Assessment",
        "An illustrative cost index with measured VVUQ credibility scores",
        "cancer-automated v0.3.0  |  source: execution README comparison, pipeline and vvuq levers, inputs corpus (FDA §VI.B, ASME V&V 40)  |  white background, 300 dpi, portrait",
    )

    # Top panel: cost bridge.
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(-62, 108)
    ax.set_ylim(-0.7, 6.7)
    ax.set_yticks([])
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xticklabels(["0", "20", "40", "60", "80", "100"], fontsize=9, color=PALETTE["ink"])
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, color=PALETTE["grid"], linewidth=0.8)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(PALETTE["grid"])
    ax.set_xlabel(
        "Relative effort index (baseline 100, illustrative planning model)", fontsize=10.5, color=PALETTE["ink"]
    )

    names = [
        "Conventional verification",
        "AI text protocol generation",
        "AI Python model generation",
        "Automated execution and log capture",
        "Automated VVUQ gate vs manual review",
        "Autonomous cloud loop, no provisioning",
        "Automated VVUQ cost",
    ]
    ys = [6, 5, 4, 3, 2, 1, 0]
    bh = 0.6
    # Baseline and endpoint full bars.
    ax.barh(6, 100, height=bh, color=PALETTE["navy"], zorder=3)
    ax.barh(0, 30, height=bh, color=PALETTE["green"], zorder=3)
    ax.text(101.5, 6, "100", ha="left", va="center", fontsize=11, fontweight="bold", color=PALETTE["navy"])
    ax.text(31.5, 0, "30", ha="left", va="center", fontsize=11, fontweight="bold", color=PALETTE["green"])
    # Reductions: (y, left, width, label).
    reductions = [(5, 82, 18, "-18"), (4, 66, 16, "-16"), (3, 54, 12, "-12"), (2, 40, 14, "-14"), (1, 30, 10, "-10")]
    for y, left, width, lab in reductions:
        ax.barh(y, width, left=left, height=bh, color=PALETTE["teal"], zorder=3)
        ax.text(
            left + width / 2,
            y,
            lab,
            ha="center",
            va="center",
            fontsize=10.5,
            fontweight="bold",
            color="white",
            zorder=4,
        )
        ax.text(left - 1.5, y, str(left), ha="right", va="center", fontsize=9, color=PALETTE["gray"])
    # Connectors at running indices.
    boundary = [(6, 5, 100), (5, 4, 82), (4, 3, 66), (3, 2, 54), (2, 1, 40), (1, 0, 30)]
    for ya, yb, x in boundary:
        ax.plot(
            [x, x], [ya - bh / 2, yb + bh / 2], color=PALETTE["gray"], linewidth=1.0, linestyle=(0, (4, 3)), zorder=2
        )
    # Category labels in the left gutter.
    for y, name in zip(ys, names):
        ax.text(-60, y, name, ha="left", va="center", fontsize=9, color=PALETTE["ink"])
    # 3.3x headline pill near the endpoint.
    ax.add_patch(
        FancyBboxPatch(
            (37, -0.27),
            34,
            0.54,
            boxstyle="round,pad=0.1,rounding_size=0.3",
            facecolor=PALETTE["green"],
            edgecolor="none",
            zorder=4,
        )
    )
    ax.text(54, 0, "about 3.3x", ha="center", va="center", fontsize=10.5, fontweight="bold", color="white", zorder=5)
    ax.text(74, 0, "70 percent lower\nthan baseline", ha="left", va="center", fontsize=8.5, color=PALETTE["gray"])
    ax.text(
        -60,
        6.62,
        "Illustrative planning index, not measured dollars; pending a cost study",
        ha="left",
        va="center",
        fontsize=9,
        style="italic",
        color=PALETTE["red"],
    )

    # Bottom panel: credibility bullets.
    axb = fig.add_subplot(gs[1, 0])
    axb.set_xlim(-66, 104)
    axb.set_ylim(0, 1)
    axb.set_yticks([])
    axb.set_xticks([0, 20, 40, 60, 80, 100])
    axb.set_xticklabels(["0", "20", "40", "60", "80", "100"], fontsize=9, color=PALETTE["ink"])
    for spine in ("top", "right", "left"):
        axb.spines[spine].set_visible(False)
    axb.spines["bottom"].set_color(PALETTE["grid"])
    axb.set_xlabel("Measured credibility score, 0 to 100", fontsize=10.5, color=PALETTE["ink"])

    bands = [
        (0, 60, "#D7DCE1", "weak"),
        (60, 80, "#E1E5E9", "fair"),
        (80, 90, "#EAEEF1", "good"),
        (90, 100, "#F4F6F8", "strong"),
    ]
    rows = [
        (0.70, "Verification overall score", "81.9 of 100, FDA §VI.B", 81.9),
        (0.30, "Validation tests final score", "85.75 of 100, ASME V&V 40, FDA §VI.B", 85.75),
    ]
    band_h = 0.20
    for ry, name, ref, value in rows:
        for x0, x1, color, _ in bands:
            axb.add_patch(
                Rectangle(
                    (x0, ry - band_h / 2), x1 - x0, band_h, facecolor=color, edgecolor="white", linewidth=0.8, zorder=2
                )
            )
        axb.add_patch(Rectangle((0, ry - 0.05), value, 0.10, facecolor=PALETTE["navy"], edgecolor="none", zorder=4))
        axb.plot(
            [80, 80], [ry - band_h / 2 - 0.02, ry + band_h / 2 + 0.02], color=PALETTE["red"], linewidth=2.2, zorder=5
        )
        axb.text(
            value + 1.5,
            ry,
            f"{value}",
            ha="left",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=PALETTE["navy"],
            zorder=6,
        )
        axb.text(-64, ry + 0.055, name, ha="left", va="center", fontsize=10.5, fontweight="bold", color=PALETTE["ink"])
        axb.text(-64, ry - 0.075, ref, ha="left", va="center", fontsize=9, color=PALETTE["gray"])
    # Band names along the top and target marker label.
    for x0, x1, _, label in bands:
        axb.text((x0 + x1) / 2, 0.93, label, ha="center", va="center", fontsize=8.5, color=PALETTE["gray"])
    axb.text(80, 0.99, "target 80", ha="center", va="center", fontsize=8.5, fontweight="bold", color=PALETTE["red"])
    axb.text(
        -64,
        0.05,
        "Uncertainty margin, max cv 0.0068 against the 0.10 bound, ample headroom",
        ha="left",
        va="center",
        fontsize=9,
        style="italic",
        color=PALETTE["gray"],
    )

    fig.savefig(
        "papers/VVUQ-01/imagegen/08-fda-cost-efficiency-bridge/08-fda-cost-efficiency-bridge.png",
        dpi=300,
        facecolor="white",
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
