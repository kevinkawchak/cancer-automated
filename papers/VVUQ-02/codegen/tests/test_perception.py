"""Tests for the perception segmentation and fusion (VVUQ 08 inputs).

LICENSE: MIT
"""

from __future__ import annotations

from src.perception.fuse_nir_us import MODALITY_WEIGHTS, fuse
from src.perception.segment import (
    STRUCTURES,
    dice,
    mean_dice,
    per_structure_dice,
    reference_masks,
    segment,
)


def test_dice_identical_and_disjoint():
    a = frozenset({(0, 0), (1, 1), (2, 2)})
    assert dice(a, a) == 1.0
    assert dice(a, frozenset({(9, 9)})) == 0.0
    assert dice(frozenset(), frozenset()) == 1.0


def test_reference_masks_deterministic_and_nonempty():
    r1 = reference_masks()
    r2 = reference_masks()
    assert r1 == r2
    assert all(r1.coverage(s) > 0 for s in STRUCTURES)


def test_zero_occlusion_recovers_reference():
    ref = reference_masks()
    pred = segment(occlusion_fraction=0.0)
    assert mean_dice(pred, ref) == 1.0


def test_occlusion_degrades_dice():
    ref = reference_masks()
    clear = mean_dice(segment(occlusion_fraction=0.0), ref)
    occluded = mean_dice(segment(occlusion_fraction=0.5), ref)
    assert occluded < clear


def test_per_structure_keys():
    ref = reference_masks()
    scores = per_structure_dice(segment(occlusion_fraction=0.1), ref)
    assert set(scores.keys()) == set(STRUCTURES)


def test_modality_weights_rows_sum_to_one():
    for weights in MODALITY_WEIGHTS.values():
        assert abs(sum(weights.values()) - 1.0) < 1e-9


def test_fuse_confidence_bounds():
    fused = fuse([1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0] * 8, [1.0] * 4)
    assert set(fused.confidence.keys()) == set(STRUCTURES)
    assert all(0.0 <= c <= 1.0 for c in fused.confidence.values())
    assert "vessel" in fused.usable(threshold=0.5)


def test_fuse_zero_signal_low_confidence():
    fused = fuse([0.0, 0.0], [0.0] * 4, [0.0] * 8, [0.0] * 4)
    assert all(c == 0.0 for c in fused.confidence.values())
    assert fused.usable(threshold=0.5) == []
