"""VVUQ-02 figure 01: platform generation-to-assurance pipeline flow.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG
on a white background, following image-instruct/01-platform-pipeline-flow.
Grounding: execution section 02 pipeline, execution README flow,
codegen/config/project.yaml. Depends only on matplotlib and numpy.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch

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
SECTION = "§"  # U+00A7 section symbol

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 11

OUT = "papers/VVUQ-02/imagegen/01-platform-pipeline-flow/01-platform-pipeline-flow.png"


def fit_text(fig, x, y, s, size, max_frac, **kw):
    """Place figure text, shrinking the font until it fits max_frac of the width."""
    t = fig.text(x, y, s, fontsize=size, **kw)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    while size > 6.0 and t.get_window_extent(renderer=r).width > max_frac * fig.bbox.width:
        size -= 0.5
        t.set_fontsize(size)
    return t


def add_frame(fig, title, subtitle, footer):
    """Draw the shared header title, subtitle, and footer with auto-fit sizing."""
    fit_text(fig, 0.5, 0.965, title, 20, 0.94, ha="center", va="center", fontweight="bold", color=PALETTE["ink"])
    fit_text(fig, 0.5, 0.935, subtitle, 12.5, 0.95, ha="center", va="center", color=PALETTE["ink"])
    fit_text(fig, 0.5, 0.03, footer, 9, 0.97, ha="center", va="center", color=PALETTE["gray"])


def rounded_box(ax, x0, y0, x1, y1, facecolor, edgecolor, lw=1.4, radius=0.012):
    """Add a rounded rectangle in axis coordinates and return its center."""
    patch = FancyBboxPatch(
        (x0, y0),
        x1 - x0,
        y1 - y0,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=lw,
        mutation_aspect=0.75,
    )
    ax.add_patch(patch)
    return (0.5 * (x0 + x1), 0.5 * (y0 + y1))


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(1, 1, left=0.06, right=0.94, top=0.91, bottom=0.07)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # ---- Tier A: generation (thin, fast) ----
    ax.text(0.03, 0.99, "Tier A  Generation", fontsize=11, fontweight="bold", color=PALETTE["purple"], ha="left")
    a1 = rounded_box(ax, 0.04, 0.84, 0.345, 0.955, PALETTE["panel"], PALETTE["purple"], lw=1.8)
    a2 = rounded_box(ax, 0.435, 0.84, 0.74, 0.955, PALETTE["panel"], PALETTE["purple"], lw=1.8)
    ax.text(a1[0], a1[1] + 0.03, "A1  on-prem LLM intent", ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(
        a1[0],
        a1[1] - 0.022,
        "propose_intents()\nphase 1, phase 5\nsource = reference (offline)",
        ha="center",
        va="center",
        fontsize=8.5,
        color=PALETTE["ink"],
    )
    ax.text(a2[0], a2[1] + 0.03, "A2  deterministic compile", ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(
        a2[0],
        a2[1] - 0.022,
        "compile_intents()\n20-DOF finger target, tip frame, grasp\nconcordance 1.000",
        ha="center",
        va="center",
        fontsize=8.5,
        color=PALETTE["ink"],
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.345, 0.895), (0.435, 0.895), arrowstyle="-|>", mutation_scale=18, color=PALETTE["teal"], lw=2.2
        )
    )
    ax.text(
        0.755,
        0.895,
        "generation:\nmicroseconds,\ndeterministic",
        ha="left",
        va="center",
        fontsize=9,
        style="italic",
        color=PALETTE["gray"],
    )

    # ---- Tier B: behavior models ----
    ax.text(
        0.03, 0.822, "Tier B  Behavior models (the act stage)", fontsize=11, fontweight="bold", color=PALETTE["slate"]
    )
    b_nodes = [
        ("kinematics", "tip = (-0.2796,\n-0.2895, 1.8185) m", "gate 01"),
        ("perception", "mean Dice 1.0000\nat 0 occlusion", "gate 08"),
        ("hands", "track 1.84 N;\nbimanual 5.0 N\nwithin hard", "gates 02, 05"),
        ("balance", "ZMP margin\n130.00 mm; stable", "gate 03"),
        ("suturing", "PJ RMSE\n0.00326 N; grade A", "gate 07"),
        ("safety", "vessel, collision,\nfault surfaces", "gates 06, 09, 10"),
    ]
    b_w = 0.143
    centers = np.linspace(0.03 + b_w / 2, 0.97 - b_w / 2, 6)
    b_top, b_bot = 0.785, 0.60
    for cx, (name, result, gate) in zip(centers, b_nodes):
        rounded_box(ax, cx - b_w / 2, b_bot, cx + b_w / 2, b_top, PALETTE["panel"], PALETTE["slate"], lw=1.5)
        ax.text(
            cx, b_top - 0.022, name, ha="center", va="center", fontsize=10.5, fontweight="bold", color=PALETTE["ink"]
        )
        ax.text(cx, b_top - 0.072, result, ha="center", va="center", fontsize=7.8, color=PALETTE["ink"])
        ax.text(cx, b_bot + 0.016, gate, ha="center", va="center", fontsize=8, fontweight="bold", color=PALETTE["teal"])

    # Single teal stem from A2, then thin gray fan into the six B nodes.
    fan_apex = (a2[0], 0.825)
    ax.add_patch(FancyArrowPatch((a2[0], 0.84), fan_apex, arrowstyle="-", color=PALETTE["teal"], lw=2.4))
    for cx in centers:
        ax.add_patch(
            FancyArrowPatch(fan_apex, (cx, b_top), arrowstyle="-|>", mutation_scale=9, color=PALETTE["gray"], lw=0.8)
        )

    # ---- Tier C: assurance (thick, gated) ----
    band_x0, band_x1, band_y0, band_y1 = 0.03, 0.97, 0.135, 0.50
    rounded_box(ax, band_x0, band_y0, band_x1, band_y1, "white", PALETTE["navy"], lw=2.4, radius=0.014)
    ax.add_patch(
        FancyBboxPatch(
            (band_x0 + 0.004, band_y1 - 0.05),
            (band_x1 - band_x0) - 0.008,
            0.046,
            boxstyle="round,pad=0,rounding_size=0.01",
            facecolor=PALETTE["navy"],
            edgecolor=PALETTE["navy"],
            mutation_aspect=0.75,
        )
    )
    ax.text(
        0.5,
        band_y1 - 0.027,
        "Assurance layer (the substantial, decision-bearing stage)",
        ha="center",
        va="center",
        fontsize=13.5,
        fontweight="bold",
        color="white",
    )

    catastrophe = {"06", "09", "10"}
    chip_w, chip_h = 0.155, 0.066
    col_centers = np.linspace(0.135, 0.865, 5)
    row_y = [0.385, 0.295]
    for r in range(2):
        for c in range(5):
            gid = f"{r * 5 + c + 1:02d}"
            cx, cy = col_centers[c], row_y[r]
            color = PALETTE["red"] if gid in catastrophe else PALETTE["teal"]
            rounded_box(ax, cx - chip_w / 2, cy - chip_h / 2, cx + chip_w / 2, cy + chip_h / 2, color, color, lw=0)
            tag = "gate " + gid + ("\ncatastrophe" if gid in catastrophe else "")
            ax.text(cx, cy, tag, ha="center", va="center", fontsize=9.5, fontweight="bold", color="white")

    rounded_box(ax, 0.07, 0.17, 0.93, 0.228, PALETTE["panel"], PALETTE["grid"], lw=1.0)
    ax.text(
        0.5,
        0.199,
        "per gate:  Verify (fraction == 1.0)  ->  Validate (vs independent reference)  ->  Quantify (CV bound)",
        ha="center",
        va="center",
        fontsize=9.5,
        color=PALETTE["ink"],
    )

    # Decision node: three colored segments.
    seg = [("ACCEPT", PALETTE["green"]), ("BLOCK", PALETTE["red"]), ("ESCALATE", PALETTE["amber"])]
    dec_x0, dec_x1, dec_y0, dec_y1 = 0.22, 0.78, 0.028, 0.108
    seg_w = (dec_x1 - dec_x0) / 3
    for i, (label, color) in enumerate(seg):
        sx0 = dec_x0 + i * seg_w
        rounded_box(ax, sx0 + 0.004, dec_y0, sx0 + seg_w - 0.004, dec_y1, color, color, lw=0)
        ax.text(sx0 + seg_w / 2, 0.068, label, ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    ax.text(
        0.5,
        0.004,
        "composite reported only when all 10 gates ACCEPT (sweep mean 93.56)",
        ha="center",
        va="center",
        fontsize=9,
        color=PALETTE["ink"],
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.5, band_y0), (0.5, dec_y1), arrowstyle="-|>", mutation_scale=20, color=PALETTE["teal"], lw=2.6
        )
    )

    # Asymmetry caption in the left gutter.
    ax.text(
        0.012,
        0.34,
        "assurance carries 64 of 172 tests",
        rotation=90,
        ha="center",
        va="center",
        fontsize=10,
        style="italic",
        color=PALETTE["gray"],
    )

    # Connectors from B tier converging into the assurance band.
    converge = (0.5, band_y1 + 0.004)
    for cx in centers:
        ax.add_patch(
            FancyArrowPatch(
                (cx, b_bot - 0.004), converge, arrowstyle="-", color=PALETTE["gray"], lw=0.8, linestyle=(0, (4, 2))
            )
        )

    # Legend (compact, in the gap on the right, clear of the converging lines).
    handles = [
        Patch(facecolor=PALETTE["purple"], edgecolor=PALETTE["purple"], label="on-prem intent"),
        Patch(facecolor=PALETTE["slate"], edgecolor=PALETTE["slate"], label="behavior model"),
        Patch(facecolor=PALETTE["teal"], edgecolor=PALETTE["teal"], label="gate (pass path)"),
        Patch(facecolor=PALETTE["red"], edgecolor=PALETTE["red"], label="immediate-catastrophe gate"),
    ]
    leg = ax.legend(
        handles=handles,
        loc="upper right",
        bbox_to_anchor=(0.999, 0.575),
        fontsize=8.5,
        frameon=True,
        handlelength=1.2,
        labelspacing=0.3,
        borderpad=0.5,
    )
    leg.get_frame().set_edgecolor(PALETTE["grid"])
    leg.get_frame().set_facecolor("white")

    add_frame(
        fig,
        "Platform Pipeline: Generation is Fast, Assurance is the Decision",
        f"One candidate behavior from on-prem intent to a gated ship decision (VVUQ-02 execution {SECTION}02 to {SECTION}03)",
        f"cancer-automated v1.0.0  |  source: execution {SECTION}02 pipeline, execution README flow, "
        "codegen/config/project.yaml  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
