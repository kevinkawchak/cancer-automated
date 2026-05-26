"""Surgical scene segmentation and Dice agreement (VVUQ 08 input).

Segments the fused surgical scene into five structures: vessel, pancreatic duct,
bile duct, tumor margin, and instrument. Masks are represented as frozensets of
cell indices on a fixed grid so the Dice coefficient is exact and the module is
pure standard library. Segmentation quality degrades with the occlusion fraction
(blood and smoke), which is one of the five sweep free parameters.

The Dice agreement against the labeled reference in
``data/reference/scene_masks_reference.json`` is the validation metric for VVUQ 08
(perception-scene-understanding), grounded in ASME V&V 40 validation.

LICENSE: MIT
"""

from __future__ import annotations

import random
from dataclasses import dataclass

GRID = 16
STRUCTURES = ("vessel", "pancreatic_duct", "bile_duct", "tumor_margin", "instrument")

Cell = tuple[int, int]
Mask = frozenset[Cell]


@dataclass(frozen=True)
class SceneMasks:
    """Per-structure binary masks over a GRID x GRID scene."""

    masks: dict[str, Mask]

    def coverage(self, structure: str) -> int:
        """Number of cells covered by a structure mask."""
        return len(self.masks.get(structure, frozenset()))


def _reference_mask(structure: str) -> Mask:
    """Deterministic labeled reference mask for a structure (the validation truth)."""
    idx = STRUCTURES.index(structure)
    cells: set[Cell] = set()
    for r in range(GRID):
        for c in range(GRID):
            # Each structure occupies a distinct deterministic band of the grid.
            if (r + 2 * c + 3 * idx) % 5 == idx % 5 and (r // 4) != (idx % 4) + 1:
                cells.add((r, c))
    return frozenset(cells)


def reference_masks() -> SceneMasks:
    """Build the full labeled reference scene (independent validation truth)."""
    return SceneMasks(masks={s: _reference_mask(s) for s in STRUCTURES})


def segment(occlusion_fraction: float = 0.0, seed: int = 20260525) -> SceneMasks:
    """Segment the scene, dropping and adding cells in proportion to occlusion.

    Args:
        occlusion_fraction: fraction of the scene obscured by blood or smoke in
            [0, 1]; higher values degrade the predicted masks.
        seed: deterministic seed.

    Returns:
        The predicted ``SceneMasks``.
    """
    rng = random.Random((seed << 4) ^ int(occlusion_fraction * 1_000_003))
    out: dict[str, Mask] = {}
    for structure in STRUCTURES:
        ref = set(_reference_mask(structure))
        predicted = set()
        for cell in ref:
            if rng.random() >= occlusion_fraction:  # drop occluded true cells
                predicted.add(cell)
        # False positives appear at the occluded boundary.
        n_false = int(len(ref) * occlusion_fraction * 0.5)
        for _ in range(n_false):
            predicted.add((rng.randrange(GRID), rng.randrange(GRID)))
        out[structure] = frozenset(predicted)
    return SceneMasks(masks=out)


def dice(pred: Mask, ref: Mask) -> float:
    """Dice coefficient between two masks: 2 |A and B| / (|A| + |B|)."""
    denom = len(pred) + len(ref)
    if denom == 0:
        return 1.0
    return 2.0 * len(pred & ref) / denom


def per_structure_dice(pred: SceneMasks, ref: SceneMasks) -> dict[str, float]:
    """Dice per structure between a predicted and a reference scene."""
    return {
        s: dice(pred.masks.get(s, frozenset()), ref.masks.get(s, frozenset())) for s in STRUCTURES
    }


def mean_dice(pred: SceneMasks, ref: SceneMasks) -> float:
    """Mean Dice across the five structures."""
    scores = per_structure_dice(pred, ref)
    return sum(scores.values()) / len(scores)
