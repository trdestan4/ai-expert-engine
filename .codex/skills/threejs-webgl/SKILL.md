---
name: threejs-webgl
description: Owns production Three.js and browser 3D runtime engineering across renderer and scene architecture, cameras, lighting, PBR materials, glTF loading, interaction, post-processing, resize/DPR/render loops, WebGL/WebGPU capability choices, explicit resource disposal, context resilience, and graceful non-3D fallbacks.
---

# Purpose
Build 3D web experiences that remain correct, responsive, memory-bounded, and integrated with the surrounding product instead of functioning only as isolated demos.

## Use when
- Three.js scene/camera/lighting/material/runtime code is required;
- glTF/GLB models, textures, environment maps, raycasting, controls, post-processing, or 3D scroll interactions are implemented;
- a 3D page leaks GPU memory, duplicates render loops, breaks on resize, or performs poorly;
- WebGL versus WebGPU/renderer capability and fallback strategy must be decided;
- React/SPA lifecycle must safely own Three.js resources.

## Do not use when
- the 3D asset itself needs DCC/export/compression work (`three-d-asset-pipeline`);
- the task is primarily custom shader mathematics (`realtime-shaders`);
- only DOM/CSS perspective is needed (`creative-frontend`);
- the spatial/motion concept is unresolved (`creative-director` / `motion-direction`).

## Inputs
Use repository/library versions, visual direction, model/texture inventory, camera/framing requirements, interaction/motion map, viewport/device matrix, performance budgets, asset compression format, color-management requirements, fallback/poster, and lifecycle boundaries.

## Workflow
### 1. Define runtime ownership
Choose one renderer/canvas owner, scene lifecycle, animation loop policy, resize observer/window behavior, route/component mount/unmount, and asset cache ownership. Multiple accidental render loops are a correctness bug.

### 2. Establish renderer and capability path
Select WebGL/WebGPU support according to the installed Three.js version and project requirements. Configure pixel ratio with an explicit cap appropriate to device/budget, size the drawing buffer deliberately, and provide a non-3D fallback for unsupported/failed initialization.

### 3. Build scene graph intentionally
Use stable scene hierarchy, meaningful object groups, calibrated world scale, appropriate camera near/far planes, and lighting/environment consistent with PBR assets. Avoid extreme near/far ranges that waste depth precision.

### 4. Load assets through a controlled pipeline
Use glTF as runtime delivery when appropriate; configure DRACO/Meshopt/KTX2 support only for assets that use them. Report loading/progress/error states and avoid blocking essential page content on optional 3D readiness.

### 5. Implement interaction and motion ownership
Raycast only against relevant objects, normalize pointer/touch coordinates correctly, and keep UI/business state separate from raw scene objects. Scroll/timeline orchestration may be owned by `animation-engineering`; define a clear bridge rather than two loops fighting over camera/object transforms.

### 6. Add post-processing only with a visual job
Compose passes deliberately, preserve color/tone mapping, size render targets with the viewport/budget, and dispose pass resources. Full-screen effects can dominate GPU cost.

### 7. Manage lifecycle and disposal
Removing an object from a scene does not automatically free geometry, material, texture, render target, controls, pass, or loader resources. Track ownership and call relevant dispose/close methods when resources are no longer reusable. Verify route/reload cycles and context behavior.

### 8. Measure and degrade
Inspect CPU/GPU frame behavior, draw calls, triangles, texture memory proxies, renderer info, loading bytes, shader compilation hitches, and mobile thermals where material. Reduce DPR, post effects, texture resolution, model detail, update frequency, or animation complexity before sacrificing core UX.

## Decision rules
- Asset bytes, GPU memory, draw calls, shader cost, and CPU update cost are different budgets.
- Explicit disposal is part of SPA correctness.
- A single stable render loop beats competing requestAnimationFrame owners.
- Use compressed textures/geometry based on measured transfer/runtime trade-offs, not slogans.
- 3D must have a meaningful fallback/poster path.
- Scroll-driven 3D must preserve native page control and reduced-motion behavior.
- Version-sensitive Three.js APIs require installed-version/official-doc verification.

## Reference routing
Load `references/scene-runtime-lifecycle.md` for scene graph, renderer, loop, resize, DPR, ownership, disposal, context, and SPA integration.
Load `references/loading-postprocessing-interaction.md` for glTF/loaders, compression runtime, PBR, interaction, post-processing, color, and performance diagnostics.

## Quality gates
- Renderer/canvas/loop/lifecycle ownership is explicit.
- Resize, DPR cap, camera framing, and loading/error state are handled.
- Assets use the configured decoder/transcoder path only when required.
- Route teardown/revisit does not accumulate GPU resources/listeners/loops.
- Interaction targets are bounded and state ownership is clear.
- Post-processing has a purpose and bounded render-target cost.
- Reduced-motion and non-3D fallback are coherent.
- Representative mobile/desktop performance evidence exists for material scenes.

## Failure handling
If an effect exceeds the budget, first simplify render scale, post passes, texture/model detail, lights, and update frequency while preserving the visual thesis. If browser capability is missing or initialization fails, show the designed fallback instead of blocking the page. If asset defects are the root cause, route to `three-d-asset-pipeline` rather than compensating with runtime hacks.

## Output contract
Return renderer/scene architecture, asset-loader configuration, camera/light/material plan, interaction and animation bridge, loop/resize/lifecycle/disposal strategy, capability/fallback path, performance evidence, and specialist escalations.
