"""Lights-Off Factory Safety State Machine (Image 07).

Renders a portrait, full page, 300 dpi state diagram of the lights off factory
safety controller, the four default interlocks, and the four exercised cases.

Grounding: physical-ai/lights_off_factory.py and physical-ai/README.md (code
generation v0.1.0) and papers/VVUQ-01/execution/05-physical-ai-stage2/README.md
(code execution v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

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
    fig.text(0.5, 0.965, title, ha="center", va="center", fontsize=20, fontweight="bold", color=PALETTE["ink"])
    sub = fig.text(0.5, 0.935, subtitle, ha="center", va="center", fontsize=12.5, color=PALETTE["ink"])
    _shrink_to_width(fig, sub, 0.88, 10.0)
    parts = [p.strip() for p in footer.split("|")]
    f1 = fig.text(
        0.5, 0.040, parts[0] + "  |  " + parts[1], ha="center", va="center", fontsize=9, color=PALETTE["gray"]
    )
    f2 = fig.text(0.5, 0.020, parts[2], ha="center", va="center", fontsize=9, color=PALETTE["gray"])
    _shrink_to_width(fig, f1, 0.90, 7.5)
    _shrink_to_width(fig, f2, 0.90, 7.5)


def draw_check(ax, x, y, color):
    ax.plot(
        [x, x + 0.006, x + 0.017],
        [y, y - 0.008, y + 0.01],
        color=color,
        linewidth=2.2,
        solid_capstyle="round",
        zorder=6,
    )


def node(ax, cx, cy, w, h, label, color):
    ax.add_patch(
        FancyBboxPatch(
            (cx - w / 2, cy - h / 2),
            w,
            h,
            boxstyle="round,pad=0.004,rounding_size=0.02",
            facecolor=color,
            edgecolor="white",
            linewidth=1.5,
            zorder=4,
        )
    )
    ax.text(cx, cy, label, ha="center", va="center", fontsize=14, fontweight="bold", color="white", zorder=5)


def tag(ax, x, y, letter, color):
    ax.add_patch(Circle((x, y), 0.018, facecolor=color, edgecolor="white", linewidth=1.0, zorder=7))
    ax.text(x, y, letter, ha="center", va="center", fontsize=9, fontweight="bold", color="white", zorder=8)


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(
        3, 1, height_ratios=[0.7, 2.2, 1.1], left=0.06, right=0.94, top=0.90, bottom=0.07, hspace=0.22, figure=fig
    )

    add_frame(
        fig,
        "Lights-Off Factory Safety State Machine",
        "Runs only when every interlock is satisfied, emergency stops past the fault budget",
        "cancer-automated v0.3.0  |  source: physical-ai/lights_off_factory.py, execution §05  |  white background, 300 dpi, portrait",
    )

    # Interlock panel (top).
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)
    ax0.axis("off")
    interlocks = ["estop_armed", "perimeter_clear", "vvuq_gate_online", "human_oversight_remote"]
    pw, pg = 0.235, 0.017
    for i, name in enumerate(interlocks):
        px = 0.005 + i * (pw + pg)
        highlight = name == "vvuq_gate_online"
        ax0.add_patch(
            FancyBboxPatch(
                (px, 0.45),
                pw,
                0.34,
                boxstyle="round,pad=0.006,rounding_size=0.06",
                facecolor="white",
                edgecolor=PALETTE["navy"] if highlight else PALETTE["grid"],
                linewidth=2.5 if highlight else 1.2,
            )
        )
        draw_check(ax0, px + 0.016, 0.70, PALETTE["green"])
        ax0.text(
            px + pw / 2, 0.56, name, ha="center", va="center", fontsize=9, family="monospace", color=PALETTE["ink"]
        )
        if highlight:
            ax0.text(
                px + pw / 2,
                0.28,
                "Stage 1 VVUQ wired into Stage 2 safety",
                ha="center",
                va="center",
                fontsize=8,
                style="italic",
                color=PALETTE["navy"],
            )
    ax0.text(
        0.005,
        0.90,
        "Default interlocks, all satisfied at start",
        ha="left",
        va="center",
        fontsize=10,
        fontweight="bold",
        color=PALETTE["gray"],
    )

    # State machine (middle).
    ax = fig.add_subplot(gs[1, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    nw, nh = 0.20, 0.13
    dark = (0.20, 0.80)
    running = (0.60, 0.60)
    fault = (0.20, 0.20)
    estop = (0.80, 0.22)
    gate = (0.38, 0.71)

    # Pre run gate diamond.
    gdx, gdy = 0.052, 0.05
    ax.add_patch(
        Polygon(
            [(gate[0], gate[1] + gdy), (gate[0] + gdx, gate[1]), (gate[0], gate[1] - gdy), (gate[0] - gdx, gate[1])],
            closed=True,
            facecolor="white",
            edgecolor=PALETTE["amber"],
            linewidth=2.2,
            zorder=4,
        )
    )
    ax.text(
        gate[0],
        gate[1],
        "gate",
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=PALETTE["navy"],
        zorder=5,
    )

    arrow = dict(arrowstyle="-|>", mutation_scale=16, color=PALETTE["gray"], linewidth=1.8, zorder=3)
    # DARK to gate.
    ax.add_patch(FancyArrowPatch((dark[0] + 0.07, dark[1] - 0.055), (gate[0] - 0.03, gate[1] + 0.035), **arrow))
    # gate to RUNNING.
    ax.add_patch(FancyArrowPatch((gate[0] + 0.04, gate[1] - 0.02), (running[0] - nw / 2, running[1] + 0.03), **arrow))
    ax.text(0.50, 0.70, "interlocks satisfied", ha="center", va="center", fontsize=9.5, color=PALETTE["gray"])
    # gate to FAULT.
    ax.add_patch(FancyArrowPatch((gate[0] - 0.02, gate[1] - 0.045), (fault[0] + 0.02, fault[1] + nh / 2), **arrow))
    ax.text(
        0.225, 0.47, "interlock\nunsatisfied,\nblocked", ha="center", va="center", fontsize=9, color=PALETTE["gray"]
    )
    # RUNNING to DARK (curved return).
    ax.add_patch(
        FancyArrowPatch(
            (running[0] - nw / 2, running[1] + 0.04),
            (dark[0] + nw / 2, dark[1] - 0.04),
            connectionstyle="arc3,rad=0.32",
            **arrow,
        )
    )
    ax.text(0.47, 0.89, "batch within budget", ha="center", va="center", fontsize=9.5, color=PALETTE["gray"])
    # RUNNING to ESTOP.
    ax.add_patch(
        FancyArrowPatch((running[0] + 0.06, running[1] - nh / 2), (estop[0] - 0.02, estop[1] + nh / 2), **arrow)
    )
    ax.text(0.80, 0.45, "faults exceed\nbudget", ha="center", va="center", fontsize=9.5, color=PALETTE["gray"])

    node(ax, dark[0], dark[1] + 0.012, nw, nh, "DARK", PALETTE["gray"])
    node(ax, running[0], running[1], nw, nh, "RUNNING", PALETTE["teal"])
    node(ax, fault[0], fault[1], nw, nh, "FAULT", PALETTE["amber"])
    node(ax, estop[0], estop[1], nw, nh, "ESTOP", PALETTE["red"])
    ax.text(
        dark[0],
        dark[1] - 0.038,
        "(idle)",
        ha="center",
        va="center",
        fontsize=9,
        style="italic",
        color="#E2E5E9",
        zorder=5,
    )

    # Case tags on the transitions they take.
    tag(ax, 0.40, 0.835, "A", PALETTE["green"])
    tag(ax, 0.44, 0.835, "D", PALETTE["green"])
    tag(ax, 0.715, 0.44, "B", PALETTE["red"])
    tag(ax, 0.30, 0.45, "C", PALETTE["amber"])

    # Case table (bottom).
    axt = fig.add_subplot(gs[2, 0])
    axt.set_xlim(0, 1)
    axt.set_ylim(0, 1)
    axt.axis("off")
    cols = [0.02, 0.19, 0.57, 0.72, 0.85]
    headers = ["Case", "Setup", "End state", "Blocked", "Faults"]
    state_color = {"DARK": PALETTE["gray"], "ESTOP": PALETTE["red"], "FAULT": PALETTE["amber"]}
    table = [
        ("A clean run", "6 tasks, all succeed, budget 1", "DARK", "no", "0"),
        ("B over budget", "9 tasks, every 3rd faults, budget 1", "ESTOP", "no", "2"),
        ("C interlock off", "perimeter_clear unsatisfied", "FAULT", "yes", "not applicable"),
        ("D within budget", "9 tasks, every 4th faults, budget 3", "DARK", "no", "3"),
    ]
    row_h = 0.165
    y_head = 0.92
    axt.add_patch(Rectangle((0.0, y_head - row_h / 2), 1.0, row_h, facecolor=PALETTE["navy"], edgecolor="none"))
    for x, head in zip(cols, headers):
        axt.text(x, y_head, head, ha="left", va="center", fontsize=10.5, fontweight="bold", color="white")
    for r, (case, setup, end, blocked, faults) in enumerate(table):
        ry = y_head - (r + 1) * row_h
        if r % 2 == 0:
            axt.add_patch(Rectangle((0.0, ry - row_h / 2), 1.0, row_h, facecolor=PALETTE["panel"], edgecolor="none"))
        axt.text(cols[0], ry, case, ha="left", va="center", fontsize=10, color=PALETTE["ink"])
        axt.text(cols[1], ry, setup, ha="left", va="center", fontsize=10, color=PALETTE["ink"])
        axt.text(cols[2], ry, end, ha="left", va="center", fontsize=10, fontweight="bold", color=state_color[end])
        axt.text(cols[3], ry, blocked, ha="left", va="center", fontsize=10, color=PALETTE["ink"])
        axt.text(cols[4], ry, faults, ha="left", va="center", fontsize=10, color=PALETTE["ink"])
    axt.text(
        0.02,
        0.02,
        "Case A cells: 3 plus 3 completed, 0 faulted. Case B halted mid batch after the second fault (budget 1).",
        ha="left",
        va="center",
        fontsize=8.5,
        style="italic",
        color=PALETTE["gray"],
    )

    fig.savefig(
        "papers/VVUQ-01/imagegen/07-lights-off-state-machine/07-lights-off-state-machine.png",
        dpi=300,
        facecolor="white",
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
