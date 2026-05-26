"""Multimodal perception fusion for the surgical scene (VVUQ 08 input).

Fuses head stereo RGB, NIR indocyanine green (800 nm), ultrasound B-mode, and
bile spectrophotometry into a per-structure confidence map. The fused confidence
biases the segmentation in ``segment.py`` and is what lets the perception gate
recover usable masks under blood and smoke.

Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

# Per-structure modality weights: which sensing modality most informs each
# structure. Rows sum to 1.0 so the fused confidence is a convex combination.
MODALITY_WEIGHTS = {
    "vessel": {"rgb": 0.20, "nir_icg": 0.45, "us_b_mode": 0.30, "bile": 0.05},
    "pancreatic_duct": {"rgb": 0.15, "nir_icg": 0.20, "us_b_mode": 0.60, "bile": 0.05},
    "bile_duct": {"rgb": 0.10, "nir_icg": 0.25, "us_b_mode": 0.20, "bile": 0.45},
    "tumor_margin": {"rgb": 0.25, "nir_icg": 0.40, "us_b_mode": 0.30, "bile": 0.05},
    "instrument": {"rgb": 0.70, "nir_icg": 0.10, "us_b_mode": 0.15, "bile": 0.05},
}


@dataclass(frozen=True)
class FusedScene:
    """Per-structure fused confidence in [0, 1]."""

    confidence: dict[str, float]

    def usable(self, threshold: float = 0.5) -> list[str]:
        """Structures whose fused confidence is at or above a threshold."""
        return [s for s, c in self.confidence.items() if c >= threshold]


def _channel_quality(values: list[float]) -> float:
    """Map a channel vector to a [0, 1] quality scalar by its mean magnitude."""
    if not values:
        return 0.0
    mean = sum(abs(v) for v in values) / len(values)
    return max(0.0, min(1.0, mean))


def fuse(
    rgb: list[float],
    nir_icg: list[float],
    us_b_mode: list[float],
    bile: list[float],
) -> FusedScene:
    """Fuse the four modalities into per-structure confidence.

    Each argument is a normalized channel vector in [0, 1]. The fused confidence
    for a structure is the modality-weighted combination of channel qualities.
    """
    quality = {
        "rgb": _channel_quality(rgb),
        "nir_icg": _channel_quality(nir_icg),
        "us_b_mode": _channel_quality(us_b_mode),
        "bile": _channel_quality(bile),
    }
    confidence: dict[str, float] = {}
    for structure, weights in MODALITY_WEIGHTS.items():
        confidence[structure] = round(sum(weights[m] * quality[m] for m in weights), 4)
    return FusedScene(confidence=confidence)
