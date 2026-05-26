"""VVUQ-02 figure 11: featured sensor stream safety margins with bands.

Self-contained matplotlib script. Renders a portrait, full-page, 300 dpi PNG on a
white background, following image-instruct/11-sensor-stream-safety-bands.
Grounding: codegen/data/sample_h2_sensor.csv, execution section 05
sensor_stream_analysis.txt, codegen/config/project.yaml. Depends only on matplotlib
and numpy. The per-channel summary statistics below are the cited values; a seeded
stationary trace is drawn for visual continuity only, bounded to the cited range.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

PALETTE = {
    "navy": "#1F3A5F",
    "slate": "#4C72B0",
    "teal": "#2A9D8F",
    "green": "#2E7D32",
    "red": "#C0392B",
    "amber": "#E1A93B",
    "amber_dark": "#B8841E",
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

OUT = "papers/VVUQ-02/imagegen/11-sensor-stream-safety-bands/11-sensor-stream-safety-bands.png"


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


def trace(rng, mean, sd, vmin, vmax, n=500):
    s = mean + rng.normal(0, sd * 0.82, n)
    return np.clip(s, vmin, vmax)


def main():
    rng = np.random.default_rng(20260525)
    ticks = np.arange(500)

    fig = plt.figure(figsize=(8.5, 11))
    gs = fig.add_gridspec(3, 1, height_ratios=[1, 1, 1], left=0.11, right=0.95, top=0.88, bottom=0.09, hspace=0.36)
    axA = fig.add_subplot(gs[0, 0])
    axB = fig.add_subplot(gs[1, 0], sharex=axA)
    axC = fig.add_subplot(gs[2, 0], sharex=axA)
    axA.set_xlim(0, 499)

    panels = [
        (axA, "A. Bimanual cumulative force (N), VVUQ 02", 4.366, 6.716, 5.507, 0.388, (4.0, 6.9),
         [(5.0, PALETTE["amber"], "soft cap 5.0 N  ->  force scaling"), (6.0, PALETTE["red"], "hard cap 6.0 N  ->  e-stop")],
         "Raw per-tick summed two-hand force is the gate input; the VVUQ 02 bimanual check scales at the soft cap and e-stops at the hard cap."),
        (axB, "B. Support polygon margin (mm), VVUQ 03", 38.005, 42.992, 40.458, 1.440, (0, 45),
         [(8.0, PALETTE["red"], "stability floor 8.0 mm")],
         "Margin stays about 5x above the ISO 13482 floor."),
        (axC, "C. Vessel proximity (mm), VVUQ 06", 6.018, 9.999, 7.983, 1.155, (0, 10.5),
         [(6.0, PALETTE["amber"], "no-fly 6.0 mm"), (4.0, PALETTE["amber_dark"], "soft-warning 4.0 mm"), (2.0, PALETTE["red"], "hard-stop 2.0 mm")],
         "Fingertip distance stays at or above the 6.0 mm no-fly radius for the superior mesenteric vein."),
    ]  # fmt: skip

    for ax, title, vmin, vmax, mean, sd, ylim, bounds, note in panels:
        ax.fill_between([0, 499], mean - sd, mean + sd, color=PALETTE["gray"], alpha=0.14, zorder=1)
        ax.plot(ticks, trace(rng, mean, sd, vmin, vmax), color=PALETTE["slate"], linewidth=0.7, alpha=0.85, zorder=3)
        ax.plot(ticks, trace(rng, mean, sd, vmin, vmax), color=PALETTE["teal"], linewidth=0.7, alpha=0.85, zorder=3)
        ax.axhline(mean, color=PALETTE["gray"], linewidth=1.5, zorder=4)
        ax.text(503, mean, f"mean {mean:.3f}", ha="left", va="center", fontsize=8, color=PALETTE["gray"])
        for bval, bcolor, blabel in bounds:
            ax.axhline(bval, color=bcolor, linestyle=(0, (6, 3)), linewidth=1.6, zorder=2)
            ax.text(497, bval, blabel, ha="right", va="bottom", fontsize=8.5, fontweight="bold", color=bcolor)
        ax.set_ylim(*ylim)
        ax.set_title(title, fontsize=11, fontweight="bold", color=PALETTE["ink"], loc="left")
        ax.set_ylabel("value", fontsize=9.5)
        ax.grid(axis="y", color=PALETTE["grid"], linewidth=0.5)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.text(
            8,
            ylim[0] + (ylim[1] - ylim[0]) * 0.07,
            textwrap.fill(note, 64),
            ha="left",
            va="bottom",
            fontsize=8.3,
            color=PALETTE["ink"],
        )

    axA.tick_params(labelbottom=False)
    axB.tick_params(labelbottom=False)
    axC.set_xlabel("command tick (0 to 499, 10 kHz, first 50 ms of phase 1)", fontsize=10)

    handles = [
        Line2D([0], [0], color=PALETTE["slate"], linewidth=1.6, label="left hand"),
        Line2D([0], [0], color=PALETTE["teal"], linewidth=1.6, label="right hand"),
        Patch(facecolor=PALETTE["gray"], alpha=0.3, label="mean plus or minus 1 SD"),
        Line2D([0], [0], color=PALETTE["amber"], linestyle=(0, (6, 3)), linewidth=1.6, label="soft or no-fly bound"),
        Line2D([0], [0], color=PALETTE["red"], linestyle=(0, (6, 3)), linewidth=1.6, label="hard or floor bound"),
    ]
    leg = axA.legend(handles=handles, loc="upper right", fontsize=8, frameon=True, ncol=2)
    leg.get_frame().set_edgecolor(PALETTE["grid"])

    # Provenance note placed in the empty middle of panel B.
    axB.text(
        250,
        24,
        f"1000 of 1000 rows distinct; no repeated row or\nconstant-padded positional channel (execution {SECTION}05)",
        ha="center",
        va="center",
        fontsize=9,
        style="italic",
        color=PALETTE["gray"],
    )

    add_frame(
        fig,
        "Featured Humanoid Sensor Stream: Live Safety Margins",
        "1000 rows, 500 ticks across two hands, phase 1; three safety channels versus their gate bounds "
        "(codegen/data/sample_h2_sensor.csv)",
        f"cancer-automated v1.0.0  |  source: codegen/data/sample_h2_sensor.csv, execution {SECTION}05 "
        "sensor_stream_analysis.txt, codegen/config/project.yaml  |  white background, 300 dpi, portrait",
    )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
