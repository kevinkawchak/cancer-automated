# Perception Stack Specification (VVUQ 08)

The H2-Surgical 1.0 perceives the surgical scene through head stereo RGB, NIR
indocyanine green at 800 nm, an endoscopic and ultrasound fusion path, and bile
spectrophotometry, augmented with wrist and palm cameras the 8-arm baseline does
not carry. Parameters are in `config/perception_model.yaml`.

## Modalities and what they resolve

| Modality | Primary structures | Channels |
|----------|--------------------|----------|
| Head stereo RGB | instruments, gross anatomy | 2 cameras |
| NIR ICG (800 nm) | vessels, tumor margin perfusion | 4 |
| Ultrasound B-mode | pancreatic duct, deep vessels | 8 elements |
| Bile spectrophotometry | bile duct, leak detection | 4 (410 470 532 600 nm) |
| Vessel proximity (confocal) | vessel surface distance | 1 at 100 kHz |
| Wrist and palm cameras | close-in fingertip context | 4 |

## Fusion to segmentation

`src/perception/fuse_nir_us.py` fuses the four primary modalities into a
per-structure confidence using a fixed modality-weight matrix (rows sum to 1.0),
then `src/perception/segment.py` produces five binary masks (vessel, pancreatic
duct, bile duct, tumor margin, instrument). The masks are compared by the Dice
coefficient against the labeled reference at
`data/reference/scene_masks_reference.json`.

## Degradation under blood and smoke

Segmentation quality degrades with the occlusion fraction, one of the five sweep
free parameters. As occlusion rises, true mask cells drop out and false positives
appear at the occluded boundary. VVUQ 08 validates that the mean Dice across the
five structures stays at or above the gate agreement threshold and that the
coefficient of variation across seeded runs stays inside the gate bound.
