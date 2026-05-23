"""File Generation Sankey (Image 10).

Renders a portrait, full page, 300 dpi Sankey flowing the 13 generated files
(54127 bytes) from the single execution run, through the five numbered sections,
into the four future paper roles, with ribbon widths proportional to bytes.

Grounding: papers/VVUQ-01/execution/README.md File generation outcomes table
(code execution v0.2.0) and the pipeline artifacts (code generation v0.1.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path

PALETTE = {
    "navy": "#1F3A5F",
    "slate": "#4C72B0",
    "teal": "#2A9D8F",
    "green": "#2E7D32",
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


def ribbon(ax, xl_t, xr_t, y_top, xl_b, xr_b, y_bot, color, alpha=0.55):
    ymid = (y_top + y_bot) / 2
    verts = [
        (xl_t, y_top),
        (xl_t, ymid),
        (xl_b, ymid),
        (xl_b, y_bot),
        (xr_b, y_bot),
        (xr_b, ymid),
        (xr_t, ymid),
        (xr_t, y_top),
        (xl_t, y_top),
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.LINETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.CLOSEPOLY,
    ]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=color, edgecolor="none", alpha=alpha, zorder=2))


def bar(ax, x0, x1, y0, h, color, inset=0.003):
    ax.add_patch(
        FancyBboxPatch(
            (x0 + inset, y0),
            (x1 - x0) - 2 * inset,
            h,
            boxstyle="round,pad=0,rounding_size=0.006",
            facecolor=color,
            edgecolor="white",
            linewidth=1.0,
            zorder=5,
        )
    )


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(1, 1, left=0.06, right=0.94, top=0.90, bottom=0.07, figure=fig)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    add_frame(
        fig,
        "File Generation Sankey",
        "13 generated files, 54127 bytes, flowing into four future paper roles",
        "cancer-automated v0.3.0  |  source: execution README file generation outcomes, pipeline artifacts  |  white background, 300 dpi, portrait",
    )

    total = 54127
    x_start = 0.10
    s = 0.80 / total

    sections = [
        ("01 Foundation", 17304, PALETTE["navy"]),
        ("02 Pipeline", 10659, PALETTE["slate"]),
        ("03 VVUQ", 8812, PALETTE["teal"]),
        ("04 Stage 1", 9152, PALETTE["green"]),
        ("05 Physical-AI", 8200, PALETTE["amber"]),
    ]
    roles = [("Methods", 6893), ("Verification", 10411), ("Core Results", 8812), ("Results", 28011)]
    sec_color = {name: color for name, _, color in sections}

    # Compute edge to edge x ranges.
    sec_x, cx = {}, x_start
    for name, b, _ in sections:
        sec_x[name] = (cx, cx + b * s)
        cx += b * s
    role_x, cx = {}, x_start
    for name, b in roles:
        role_x[name] = (cx, cx + b * s)
        cx += b * s

    y_src, y_sec, y_role = 0.80, 0.50, 0.19
    h = 0.04

    # Source to section ribbons (aligned, one per section).
    for name, b, color in sections:
        xl, xr = sec_x[name]
        ribbon(ax, xl, xr, y_src, xl, xr, y_sec + h, color)

    # Section to role ribbons with offset tracking.
    flows = [
        ("01 Foundation", "Methods", 6893),
        ("01 Foundation", "Verification", 10411),
        ("02 Pipeline", "Results", 10659),
        ("03 VVUQ", "Core Results", 8812),
        ("04 Stage 1", "Results", 9152),
        ("05 Physical-AI", "Results", 8200),
    ]
    sec_off = {name: sec_x[name][0] for name, _, _ in sections}
    role_off = {name: role_x[name][0] for name, _ in roles}
    for sec, role, b in flows:
        w = b * s
        sl = sec_off[sec]
        sec_off[sec] = sl + w
        rl = role_off[role]
        role_off[role] = rl + w
        ribbon(ax, sl, sl + w, y_sec, rl, rl + w, y_role + h, sec_color[sec])

    # Source node and label.
    bar(ax, x_start, x_start + total * s, y_src, h, PALETTE["navy"])
    ax.text(
        (x_start + x_start + total * s) / 2,
        y_src + h / 2,
        "VVUQ-01 Execution Run, 13 files, 54127 bytes",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="white",
        zorder=6,
    )

    # Section nodes and labels.
    for name, b, color in sections:
        xl, xr = sec_x[name]
        bar(ax, xl, xr, y_sec, h, color)
        ax.text(
            (xl + xr) / 2,
            y_sec - 0.035,
            f"{name}\n{b}",
            ha="center",
            va="top",
            fontsize=9,
            color=PALETTE["ink"],
            zorder=6,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.2),
        )

    # Role nodes and labels.
    for name, b in roles:
        xl, xr = role_x[name]
        bar(ax, xl, xr, y_role, h, PALETTE["gray"])
        ax.text(
            (xl + xr) / 2,
            y_role - 0.03,
            f"{name}\n{b}",
            ha="center",
            va="top",
            fontsize=9.5,
            fontweight="bold",
            color=PALETTE["ink"],
            zorder=6,
        )

    # Legend, upper right.
    ly = 0.985
    for name, b, color in sections:
        ax.add_patch(Rectangle((0.80, ly - 0.016), 0.022, 0.022, facecolor=color, edgecolor="none", zorder=6))
        ax.text(0.83, ly - 0.005, name, ha="left", va="center", fontsize=9, color=PALETTE["ink"], zorder=6)
        ly -= 0.03

    # Inventory note, lower left.
    note = (
        "Three saved pipeline artifacts (instructions, execution log, paper) plus the chunk "
        "reconstruction README and the PDAC timeline are the primary generated deliverables."
    )
    ax.text(0.0, 0.10, textwrap.fill(note, width=58), ha="left", va="top", fontsize=9, color=PALETTE["gray"])

    fig.savefig(
        "papers/VVUQ-01/imagegen/10-file-generation-sankey/10-file-generation-sankey.png", dpi=300, facecolor="white"
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
