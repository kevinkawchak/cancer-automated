"""VVUQ-02 figure 07: validation parity scatter.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/07-validation-parity-scatter.
Grounding: execution section 03 vvuq_decisions.json and the four adversarial cases,
codegen/config/vvuq_thresholds.yaml. Depends only on matplotlib and numpy.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Rectangle

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

OUT = "papers/VVUQ-02/imagegen/07-validation-parity-scatter/07-validation-parity-scatter.png"


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


def card(ax, x0, y0, x1, y1, accent, header, body):
    ax.add_patch(
        FancyBboxPatch(
            (x0, y0),
            x1 - x0,
            y1 - y0,
            boxstyle="round,pad=0,rounding_size=0.02",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.0,
            mutation_aspect=0.4,
        )
    )
    ax.add_patch(Rectangle((x0, y0), 0.02, y1 - y0, facecolor=accent, edgecolor="none"))
    ax.text(x0 + 0.05, y1 - 0.12, header, ha="left", va="top", fontsize=10, fontweight="bold", color=PALETTE["ink"])
    ax.text(x0 + 0.05, y1 - 0.42, textwrap.fill(body, 44), ha="left", va="top", fontsize=9, color=PALETTE["ink"])


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], left=0.12, right=0.95, top=0.88, bottom=0.08, hspace=0.24)
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])

    lo, hi = 0.4, 1.25
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.set_xlabel("independent reference value (normalized)", fontsize=10.5)
    ax.set_ylabel("observed value (normalized)", fontsize=10.5)
    ax.grid(True, color=PALETTE["grid"], linewidth=0.6)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    # Pass corridor and the y = x line.
    xs = np.array([lo, hi])
    ax.fill_between(xs, xs - 0.04, xs + 0.04, color=PALETTE["green"], alpha=0.12, zorder=1)
    ax.plot(xs, xs, linestyle=(0, (6, 4)), color=PALETTE["gray"], linewidth=1.5, zorder=2)
    ax.text(
        1.18,
        1.205,
        "perfect validation (y = x)",
        rotation=45,
        ha="center",
        va="center",
        fontsize=9,
        color=PALETTE["gray"],
    )

    # Off-diagonal blocks with drop lines.
    for cx, cy, head, reason, lx, ly in [
        (1.0, 0.50, "Case D, 03 balance", "agreement 0.00; rel err 0.500\nabove 0.03  ->  BLOCK", 0.47, 0.5),
        (1.0, 0.80, "Case C, 08 perception", "verification fraction 0.80\nbelow 1.0  ->  BLOCK", 0.47, 0.78),
    ]:
        ax.plot([cx, cx], [cy, lo], linestyle=(0, (1, 2)), color=PALETTE["red"], linewidth=1.0, alpha=0.7, zorder=2)
        ax.scatter(cx, cy, s=150, marker="D", facecolor=PALETTE["red"], edgecolor="white", linewidth=1.0, zorder=5)
        ax.annotate(
            f"{head}\n{reason}",
            xy=(cx, cy),
            xytext=(lx, ly),
            fontsize=8.5,
            va="center",
            ha="left",
            color=PALETTE["ink"],
            arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], lw=0.9),
        )

    # Nominal cluster.
    ax.scatter(1.0, 1.0, s=210, facecolor=PALETTE["green"], edgecolor="white", linewidth=1.2, zorder=5)
    ax.annotate(
        "Nominal: 10 gates\nobserved = reference\nagreement 1.0  ->  ACCEPT",
        xy=(1.0, 1.0),
        xytext=(1.07, 1.16),
        fontsize=8.5,
        va="center",
        ha="left",
        color=PALETTE["ink"],
        arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], lw=0.9),
    )

    # Case E: on the line, dispersion escalates.
    ax.errorbar(
        1.06,
        1.0,
        yerr=0.20,
        fmt="o",
        markersize=10,
        color=PALETTE["amber"],
        ecolor=PALETTE["amber"],
        elinewidth=1.8,
        capsize=5,
        zorder=6,
    )
    ax.annotate(
        "Case E, 02 finger-force\nruns 0.80 to 1.20\ncv 0.163  ->  ESCALATE",
        xy=(1.06, 1.2),
        xytext=(1.12, 0.74),
        fontsize=8.5,
        va="center",
        ha="left",
        color=PALETTE["ink"],
        arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], lw=0.9),
    )

    # Case B: on the line but hard predicate fails.
    ax.scatter(0.92, 1.0, s=170, facecolor=PALETTE["green"], edgecolor=PALETTE["green"], alpha=0.5, zorder=5)
    ax.scatter(0.92, 1.0, s=150, marker="x", color=PALETTE["red"], linewidth=2.6, zorder=7)
    ax.annotate(
        "Case B, 06 vascular\nhard predicate fails\n->  BLOCK",
        xy=(0.92, 1.0),
        xytext=(0.55, 1.14),
        fontsize=8.5,
        va="center",
        ha="left",
        color=PALETTE["ink"],
        arrowprops=dict(arrowstyle="-", color=PALETTE["gray"], lw=0.9),
    )

    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=PALETTE["green"],
            markersize=11,
            label="ACCEPT (on diagonal)",
        ),
        Line2D(
            [0],
            [0],
            marker="D",
            color="none",
            markerfacecolor=PALETTE["red"],
            markersize=10,
            label="BLOCK (off diagonal or hard predicate)",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            markerfacecolor=PALETTE["amber"],
            markersize=11,
            label="ESCALATE (dispersion)",
        ),
        Line2D([0], [0], linestyle=(0, (6, 4)), color=PALETTE["gray"], label="y = x"),
    ]
    fig.canvas.draw()
    pos = ax.get_position()
    leg = fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.535, pos.y0 - 0.008),
        ncol=2,
        fontsize=8.5,
        frameon=True,
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Annotation cards.
    ax2.set_xlim(0, 2)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    card(
        ax2,
        0.0,
        0.05,
        0.97,
        0.98,
        PALETTE["amber"],
        "Case E sits on the line yet does not ship",
        "Its three runs spread 80 to 120 percent of the reference; max cv 0.163 exceeds the 0.10 bound, "
        "so the gate ESCALATEs to hand-back-to-human.",
    )
    card(
        ax2,
        1.03,
        0.05,
        2.0,
        0.98,
        PALETTE["red"],
        "Case B sits on the line yet does not ship",
        "It matches the reference on every continuous metric, but the hard predicate hard_stop_violations "
        "is non-zero, so the catastrophe gate BLOCKs anyway.",
    )

    add_frame(
        fig,
        "Validation Parity: Observed versus Independent Reference",
        f"On the y = x line passes validation; off the line blocks; dispersion escalates (execution {SECTION}03)",
        f"cancer-automated v1.0.0  |  source: execution {SECTION}03 vvuq_decisions.json, "
        "codegen/config/vvuq_thresholds.yaml  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
