---
name: realtime-shaders
description: Owns custom realtime GPU effect engineering for web graphics, including GLSL and supported Three.js shader/node systems, uniforms, coordinate spaces, noise/SDF/distortion, render targets and feedback, GPGPU-style simulation, color/precision correctness, compilation diagnostics, bounded complexity, and accessible/performance fallbacks.
---

# Purpose
Create custom GPU visuals only where standard CSS/materials cannot express the approved effect, while keeping the math explainable, the pipeline measurable, and the product usable when the effect is reduced or unavailable.

## Use when
- ShaderMaterial/custom vertex or fragment shaders are required;
- distortion, displacement, procedural noise, SDF, dissolve, refraction-like, fluid/feedback, particles, or custom post effects need shader logic;
- uniforms/resolution/time/pointer/scroll data must cross CPU→GPU boundaries safely;
- shader compilation, precision, color-space, derivative, render-target, or GPU bottlenecks must be diagnosed;
- Three.js node/TSL or WebGPU-era shader paths are being evaluated for the installed version.

## Do not use when
- standard Three.js materials/post passes solve the requirement (`threejs-webgl`);
- CSS masks/filters/blends are sufficient (`creative-frontend`);
- the effect concept is unresolved (`creative-director` / `visual-art-direction`);
- the main problem is 3D asset export/compression (`three-d-asset-pipeline`).

## Inputs
Use the approved visual effect, renderer/runtime/version, coordinate spaces, mesh/UV data, texture inputs, target devices, color pipeline, precision requirements, interaction/time inputs, performance budget, reduced-motion/fallback behavior, and expected compositing order.

## Workflow
### 1. Define the visual equation
Describe what changes in space/color over time and which data drives it. Separate vertex displacement from fragment shading and post-process screen-space effects. Do not start with random noise snippets.

### 2. Establish spaces and units
Identify object/world/view/clip/screen/UV coordinates explicitly. Transform normals correctly. Normalize resolution/pointer inputs and account for aspect ratio where the effect needs isotropy.

### 3. Design uniforms and update cadence
Keep uniform ownership explicit. Static values should not be rewritten every frame. Time, pointer, scroll, audio, or simulation inputs should update at the minimum useful cadence and from one authoritative loop.

### 4. Build progressively
Start with a diagnostic baseline, then add one effect term at a time. Visualize normals/UV/depth/intermediate values when debugging. Preserve a known-good fallback material/pass.

### 5. Control texture/render-target cost
Choose formats/resolution/filtering deliberately. Feedback/FBO and multi-pass effects multiply bandwidth and memory. Use reduced-resolution targets when perceptually acceptable and dispose them with the runtime lifecycle.

### 6. Protect color and precision
Respect the renderer's color pipeline, texture color spaces, linear-light calculations, tone mapping, and output conversion. Select precision based on device needs; avoid needless high precision in heavy fragment loops while never sacrificing correctness blindly.

### 7. Bound GPU work
Avoid uncontrolled loops/branches, excessive texture samples, huge overdraw, full-resolution multi-pass chains, and expensive noise everywhere. Measure on representative mobile GPUs. Provide quality tiers or a static/standard-material fallback for expensive signature effects.

## Decision rules
- A shader must solve a visual problem that simpler layers cannot solve well.
- Coordinate-space mistakes are logic bugs, not art tweaks.
- More procedural complexity is not automatically more premium.
- Transfer bytes, texture memory, render-target bandwidth, and shader ALU/sample cost are separate concerns.
- Reduced motion may still require disabling time-driven distortion even if frame rate is good.
- Version-specific shader/node APIs require installed-version and official-document verification.

## Reference routing
Load `references/shader-authoring.md` for coordinate spaces, uniforms, vertex/fragment structure, noise/SDF, color, debugging, and maintainable shader design.
Load `references/gpu-effects-performance.md` for render targets, feedback/simulation, particles, post effects, quality tiers, profiling, and fallback strategy.

## Quality gates
- Effect intent and data flow are explicit.
- Spaces/aspect/resolution/color pipeline are correct.
- Uniform/update ownership is bounded.
- Shader can be debugged through intermediate visualization or simplified variants.
- Render targets/textures are lifecycle-managed.
- Mobile/low-power quality or fallback is defined for material effects.
- Reduced-motion behavior addresses time/spatial distortion.
- GPU cost is measured when the effect is significant.

## Failure handling
If compilation or output is wrong, reduce to a diagnostic shader and validate spaces/data before adding artistic terms. If performance fails, lower target resolution/samples/passes/particle count or replace procedural work with baked assets before changing the whole design. If the feature is unsupported, use the designed standard-material/static fallback.

## Output contract
Return shader/pipeline architecture, spaces and uniform contract, texture/render-target plan, color/precision decisions, interaction/update cadence, quality tiers/fallbacks, profiling evidence, and integration requirements for `threejs-webgl` or `animation-engineering`.
