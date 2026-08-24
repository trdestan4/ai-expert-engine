# Visual Regression Method

Visual testing begins by defining authority. A Figma/export screenshot, production-approved baseline, or reconstructed design DNA can each be authoritative for different questions. Record which one governs each surface.

## Deterministic capture
Control viewport, browser engine/version where practical, DPR, theme, locale, timezone, data fixtures, feature flags, fonts, image/video readiness, and animation state. Disable unrelated blinking cursors, timestamps, rotating ads, or randomized data through test fixtures—not broad masks that hide layout defects.

Wait for the fonts actually used by the target text and for critical images before capture. A fallback font changes glyph metrics, line wrapping, vertical rhythm, and therefore many downstream pixels.

## Comparison layers
Use three layers together:
1. **Pixel/perceptual diff** — sensitive regression detector under controlled rendering.
2. **Measured geometry** — bounding boxes, spacing, container widths, text wrapping, crop/aspect, visibility/overflow.
3. **Design-system inspection** — hierarchy, semantic token/state, repeated component consistency, and intentional responsive behavior.

Pixel diff alone can over-report antialiasing while missing a systemic token mistake hidden by a broad threshold.

## Tolerance
Define tolerance based on known rendering variability and importance. Exact icons/vector blocks may deserve tight thresholds; text rasterization across platforms may need perceptual or structural comparison. Never choose a threshold after seeing a regression merely to force a pass.

Masks should be narrow, named, and tied to truly nondeterministic content. A masked area must still receive separate functional/design coverage when it contains meaningful UI.

## Reference fidelity
When reproducing an external/reference screenshot, exact equality may be impossible because fonts, media, dynamic content, or browser rendering differ. Report measurable deltas in container geometry, type scale/wrapping, color roles, spacing, component shape, media crop, and signature effects. Use “pixel-perfect” only if the environment and assets support that claim.

## Baseline governance
A baseline is code-like evidence. Store enough metadata to know which version/environment created it. Intentional design changes require baseline review/update. Never automatically accept new screenshots after every run because that converts regression testing into screenshot archiving.

## Triage
Classify failures:
- functional/state failure rendered visually;
- layout/responsive defect;
- typography/font load;
- token/style regression;
- media/crop/asset mismatch;
- browser rasterization/noise;
- intended design change;
- nondeterministic capture defect.

Route the first five to the owning engineering/design skill, fix capture defects in the test harness, and require approval for intended baseline changes.
