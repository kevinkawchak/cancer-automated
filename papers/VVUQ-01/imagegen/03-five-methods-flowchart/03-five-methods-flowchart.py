"""Five Established Methods Pipeline Flowchart (Image 03).

Renders a portrait, full page, 300 dpi process flowchart: one daily deliverable
flowing through the four producing stages, threaded by the orchestrator, and
handed to the optional fifth method, the VVUQ gate.

Grounding: pipeline/orchestrator.py and the four stage modules plus
pipeline/deliverable.py (code generation v0.1.0) and
papers/VVUQ-01/execution/02-pipeline/README.md DAILY-0001 (code execution
v0.2.0).

Self contained: depends only on matplotlib and numpy. Renders headless via Agg.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

PALETTE = {
    "navy": "#1F3A5F",
    "slate": "#4C72B0",
    "teal": "#2A9D8F",
    "deepteal": "#247E6E",
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


def main():
    fig = plt.figure(figsize=(8.5, 11))
    gs = GridSpec(1, 1, left=0.06, right=0.94, top=0.91, bottom=0.07, figure=fig)
    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    add_frame(
        fig,
        "Five Established Methods, One Daily Deliverable",
        "Instruction to code to execution to paper, threaded by the orchestrator, gated by VVUQ",
        "cancer-automated v0.3.0  |  source: pipeline/orchestrator.py and stage modules, execution §02  |  white background, 300 dpi, portrait",
    )

    box_x0, box_w, box_h = 0.22, 0.50, 0.115
    centers_y = [0.85, 0.685, 0.52, 0.355]
    stages = [
        (
            "Method 1  Instruction generation",
            "instruction_stage.py",
            "emits instructions.md  (963 bytes, 0.000010 s)",
            PALETTE["navy"],
        ),
        (
            "Method 2  Code generation",
            "codegen_stage.py",
            "emits generated_deliverable.py  (735 bytes, 0.000008 s)",
            PALETTE["slate"],
        ),
        (
            "Method 3  Code execution",
            "execution_stage.py",
            "emits execution_log.txt  (95 bytes, 0.000197 s)",
            PALETTE["teal"],
        ),
        ("Method 4  Paper assembly", "paper_stage.py", "emits paper.md  (1000 bytes, 0.000010 s)", PALETTE["deepteal"]),
    ]

    # Orchestrator swimlane on the left.
    ax.add_patch(
        FancyBboxPatch(
            (0.035, 0.30),
            0.155,
            0.62,
            boxstyle="round,pad=0.004,rounding_size=0.02",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["navy"],
            linewidth=2.2,
        )
    )
    ax.text(
        0.082,
        0.61,
        "orchestrator.py threads one Deliverable",
        ha="center",
        va="center",
        rotation=90,
        fontsize=12,
        fontweight="bold",
        color=PALETTE["navy"],
    )
    # Navy spine with four ticks aligned to the stage boxes.
    ax.plot([0.16, 0.16], [centers_y[-1], centers_y[0]], color=PALETTE["navy"], linewidth=2.2, zorder=2)
    for cy in centers_y:
        ax.plot([0.16, box_x0], [cy, cy], color=PALETTE["navy"], linewidth=1.6, zorder=2)
        ax.add_patch(
            Polygon(
                [(0.158, cy - 0.006), (0.166, cy), (0.158, cy + 0.006)], facecolor=PALETTE["navy"], edgecolor="none"
            )
        )

    # Four stage boxes.
    for (title, module, emits, accent), cy in zip(stages, centers_y):
        ax.add_patch(
            FancyBboxPatch(
                (box_x0, cy - box_h / 2),
                box_w,
                box_h,
                boxstyle="round,pad=0.004,rounding_size=0.014",
                facecolor=PALETTE["panel"],
                edgecolor=PALETTE["grid"],
                linewidth=1.1,
            )
        )
        ax.add_patch(
            Polygon(
                [
                    (box_x0, cy - box_h / 2),
                    (box_x0 + 0.016, cy - box_h / 2),
                    (box_x0 + 0.016, cy + box_h / 2),
                    (box_x0, cy + box_h / 2),
                ],
                facecolor=accent,
                edgecolor="none",
            )
        )
        ax.text(
            box_x0 + 0.035,
            cy + 0.034,
            title,
            ha="left",
            va="center",
            fontsize=12.5,
            fontweight="bold",
            color=PALETTE["ink"],
        )
        ax.text(
            box_x0 + 0.035, cy + 0.002, module, ha="left", va="center", fontsize=10.5, family="monospace", color=accent
        )
        ax.text(box_x0 + 0.035, cy - 0.032, emits, ha="left", va="center", fontsize=10.5, color=PALETTE["ink"])

    # Down arrows between consecutive stages with forward pass annotations.
    pass_labels = ["instructions", "generated code", "execution log and results"]
    for i in range(3):
        y_from = centers_y[i] - box_h / 2
        y_to = centers_y[i + 1] + box_h / 2
        ax.add_patch(
            FancyArrowPatch(
                (0.47, y_from), (0.47, y_to), arrowstyle="-|>", mutation_scale=16, color=PALETTE["gray"], linewidth=1.8
            )
        )
        ax.text(
            0.50,
            (y_from + y_to) / 2,
            pass_labels[i],
            ha="left",
            va="center",
            fontsize=9,
            style="italic",
            color=PALETTE["gray"],
        )

    # Arrow from paper stage into the VVUQ gate.
    gate_cx, gate_cy, gdx, gdy = 0.47, 0.175, 0.085, 0.06
    ax.add_patch(
        FancyArrowPatch(
            (0.47, centers_y[-1] - box_h / 2),
            (0.47, gate_cy + gdy),
            arrowstyle="-|>",
            mutation_scale=16,
            color=PALETTE["gray"],
            linewidth=1.8,
        )
    )

    # VVUQ gate diamond.
    ax.add_patch(
        Polygon(
            [(gate_cx, gate_cy + gdy), (gate_cx + gdx, gate_cy), (gate_cx, gate_cy - gdy), (gate_cx - gdx, gate_cy)],
            closed=True,
            facecolor="white",
            edgecolor=PALETTE["amber"],
            linewidth=2.5,
        )
    )
    ax.text(gate_cx, gate_cy + 0.016, "Optional method 5", ha="center", va="center", fontsize=9.5, color=PALETTE["ink"])
    ax.text(
        gate_cx,
        gate_cy - 0.014,
        "VVUQ gate",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color=PALETTE["navy"],
    )

    # Gate exits: accept up-right, block down-right.
    ax.add_patch(
        FancyArrowPatch(
            (gate_cx + gdx, gate_cy + 0.012),
            (0.60, 0.215),
            arrowstyle="-|>",
            mutation_scale=14,
            color=PALETTE["green"],
            linewidth=1.8,
        )
    )
    ax.add_patch(
        FancyBboxPatch(
            (0.605, 0.193),
            0.20,
            0.045,
            boxstyle="round,pad=0.004,rounding_size=0.02",
            facecolor=PALETTE["green"],
            edgecolor="none",
        )
    )
    ax.text(0.705, 0.2155, "ACCEPT and ship", ha="center", va="center", fontsize=10.5, fontweight="bold", color="white")

    ax.add_patch(
        FancyArrowPatch(
            (gate_cx + gdx, gate_cy - 0.012),
            (0.60, 0.115),
            arrowstyle="-|>",
            mutation_scale=14,
            color=PALETTE["red"],
            linewidth=1.8,
        )
    )
    ax.add_patch(
        FancyBboxPatch(
            (0.605, 0.093),
            0.12,
            0.045,
            boxstyle="round,pad=0.004,rounding_size=0.02",
            facecolor=PALETTE["red"],
            edgecolor="none",
        )
    )
    ax.text(0.665, 0.1155, "BLOCK", ha="center", va="center", fontsize=10.5, fontweight="bold", color="white")

    ax.text(
        0.705,
        0.06,
        "evaluated in execution §03",
        ha="center",
        va="center",
        fontsize=9,
        style="italic",
        color=PALETTE["gray"],
    )

    # Right rail metrics card.
    ax.add_patch(
        FancyBboxPatch(
            (0.795, 0.40),
            0.20,
            0.50,
            boxstyle="round,pad=0.006,rounding_size=0.02",
            facecolor=PALETTE["panel"],
            edgecolor=PALETTE["grid"],
            linewidth=1.2,
        )
    )
    ax.text(
        0.895, 0.875, "Run metrics", ha="center", va="center", fontsize=11, fontweight="bold", color=PALETTE["navy"]
    )
    metrics = [
        ("Total stage time", "0.000225 s"),
        ("Largest artifact", "paper.md, 1000 bytes"),
        ("Per file cap", "200000 bytes"),
        ("Deliverable runs", "5 of 5 complete"),
        ("Stages per deliverable", "4 of 4"),
    ]
    my = 0.82
    for label, value in metrics:
        ax.text(0.806, my, label, ha="left", va="center", fontsize=9, color=PALETTE["gray"])
        ax.text(0.806, my - 0.032, value, ha="left", va="center", fontsize=9.5, fontweight="bold", color=PALETTE["ink"])
        my -= 0.085

    # Bottom legend.
    legend = [
        ("Instruction", PALETTE["navy"], "sq"),
        ("Code generation", PALETTE["slate"], "sq"),
        ("Code execution", PALETTE["teal"], "sq"),
        ("Paper assembly", PALETTE["deepteal"], "sq"),
        ("VVUQ gate", PALETTE["amber"], "diamond"),
    ]
    lx = 0.02
    ly = 0.02
    for label, color, kind in legend:
        if kind == "sq":
            ax.add_patch(
                Polygon(
                    [(lx, ly), (lx + 0.02, ly), (lx + 0.02, ly + 0.02), (lx, ly + 0.02)],
                    facecolor=color,
                    edgecolor="none",
                )
            )
        else:
            ax.add_patch(
                Polygon(
                    [(lx + 0.01, ly + 0.022), (lx + 0.022, ly + 0.011), (lx + 0.01, ly), (lx - 0.002, ly + 0.011)],
                    facecolor="white",
                    edgecolor=color,
                    linewidth=1.8,
                )
            )
        ax.text(lx + 0.03, ly + 0.011, label, ha="left", va="center", fontsize=8.5, color=PALETTE["ink"])
        lx += 0.045 + 0.011 * len(label)

    fig.savefig(
        "papers/VVUQ-01/imagegen/03-five-methods-flowchart/03-five-methods-flowchart.png", dpi=300, facecolor="white"
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
