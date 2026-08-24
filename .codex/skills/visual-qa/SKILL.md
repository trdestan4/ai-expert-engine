---
name: visual-qa
description: Owns evidence-based visual and motion verification for web experiences using deterministic screenshot/state capture, viewport/browser matrices, reference and regression comparison, typography/media/load stabilization, measurable layout deltas, animation key-state inspection, and explicit tolerance/masking without claiming pixel-perfect fidelity from incomplete evidence.
---

# Purpose
Prove that an implemented experience matches its approved design/reference across meaningful states and devices, and detect visual regressions without confusing rendering noise with product defects.

## Use when
- implementation must be compared with screenshots/design exports/reference baselines;
- visual regression tests or screenshot baselines are needed;
- spacing, typography, alignment, responsive composition, media crop, or theme fidelity must be reviewed;
- scroll/animation/3D sequences need key-state and cross-device visual QA;
- a “pixel-perfect” claim needs evidence and defined tolerance.

## Do not use when
- the visual direction itself must be created (`creative-director`);
- reference rules still need reconstruction (`design-reconstruction`);
- functional test strategy is primary (`testing-qa`);
- accessibility/performance conformance is primary, though their evidence may be coordinated.

## Inputs
Use approved design DNA/reference set, exact baseline viewport/state where known, implementation URL/build, fonts/assets, deterministic test data, theme/locale, target browser/device matrix, motion keyframes/scroll states, dynamic regions to stabilize, and acceptance tolerance.

## Workflow
### 1. Define the comparison contract
List what is authoritative: design export, reference screenshot, approved implementation baseline, or design DNA rule. Record viewport/DPR/theme/locale/data and whether exact assets/fonts are available.

### 2. Stabilize capture
Wait for relevant fonts and critical media, use deterministic data/time when possible, disable or freeze unrelated dynamic content, and ensure loading overlays are in the intended state. Do not mask a region merely because it is failing.

### 3. Capture representative matrix
Include composition-changing viewports, not every width. Add themes/locales/content extremes when material. For 3D/video, capture defined readiness/key states or use deterministic camera/timeline positions where feasible.

### 4. Compare at multiple levels
Use automated pixel/perceptual diff for regression signal where appropriate, but also inspect semantic visual relationships: container geometry, hierarchy, text wrapping, baseline/alignment, spacing rhythm, radii/borders/shadows, crop/focal point, overflow, and state visibility.

### 5. Classify differences
Separate rendering noise (font rasterization/subpixel/antialiasing), expected dynamic variance, acceptable implementation adaptation, and real defect. Every tolerance or mask needs a reason and scope.

### 6. Verify motion key states
Capture start/mid/end and critical scroll positions, interruption/resume, resize, and reduced-motion variant. Smoothness belongs to performance evidence too; visual QA checks choreography/state/fidelity.

### 7. Close with reproducible evidence
Report baseline/candidate IDs, environment, captures, measured deltas, accepted tolerances, defects with owner, and missing evidence. Update baselines only after intentional design change is reviewed.

## Decision rules
- A single desktop screenshot cannot prove responsive fidelity.
- “Pixel-perfect” requires identical authoritative assets/fonts/environment plus explicit comparison criteria; otherwise use high-fidelity/measured language.
- Never update a baseline simply to make a failing test green.
- Masks/tolerances must be narrow and documented.
- Visual diff complements, not replaces, accessibility, functional, and performance testing.
- Dynamic 3D/motion requires deterministic key states when exact frame comparison is desired.

## Reference routing
Load `references/visual-regression-method.md` for baseline contracts, deterministic capture, pixel/perceptual comparison, typography/layout deltas, masks, and triage.
Load `references/motion-cross-device-qa.md` for motion/scroll/3D state capture, responsive matrices, reduced motion, browser/device differences, and evidence reporting.

## Quality gates
- Authority/baseline and capture environment are explicit.
- Target matrix covers actual composition changes.
- Fonts/media/data are stabilized or their uncertainty is stated.
- Differences are classified with evidence, not taste.
- Tolerances/masks are justified and scoped.
- Motion/3D signature states and reduced-motion variant are inspected when applicable.
- Baseline updates require intentional-change evidence.
- Findings route to the correct implementation/design owner.

## Failure handling
If the baseline is ambiguous, stop short of a pass/fail claim and request/derive a clearer contract. If browser rasterization creates noisy diffs, use structural/perceptual thresholds or environment-specific baselines rather than huge masks. If a motion state cannot be deterministically captured, document a manual/video QA protocol instead of pretending frame-level automation is reliable.

## Output contract
Return baseline/candidate/environment, capture matrix, comparison method/tolerance, visual findings and measurements, motion/3D key-state results, accepted variance, baseline-update status, missing evidence, and owners for remediation.
