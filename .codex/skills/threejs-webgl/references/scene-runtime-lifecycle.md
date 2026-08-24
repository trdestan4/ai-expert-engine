# Three.js Scene Runtime and Lifecycle

Production Three.js begins with ownership. One application surface should have a clear canvas/renderer owner and a deliberate render-loop policy. In a continuously animated hero, one requestAnimationFrame loop may be appropriate. In mostly static scenes, render-on-demand can save power. Do not let components independently create loops that continue after navigation.

## Renderer and sizing
Size the CSS canvas and drawing buffer intentionally. Cap device pixel ratio according to visual requirement and performance evidence; rendering a full-screen scene at a very high mobile DPR can multiply fragment work dramatically. Update renderer size and camera aspect on meaningful container changes without creating resize feedback loops.

Near/far camera planes should tightly enclose the useful scene to preserve depth precision. Keep world scale consistent with model authoring where possible. Build scene groups around logical ownership so visibility, transforms, and cleanup can be managed coherently.

## Resource ownership
JavaScript garbage collection does not automatically free all GPU resources created through WebGL. When no longer reusable, dispose geometries, materials, textures, render targets, controls, post-processing passes, and loaders that expose disposal. Texture ownership matters because multiple materials may share one texture; a resource manager/cache should know when shared resources are safe to release.

Removing a Mesh from `scene` is not disposal. For bitmap-backed textures, CPU-side image resources may also need explicit closing depending on how they were created. Inspect the current Three.js API because disposal capabilities vary by class/addon.

## SPA and component integration
Create scene resources in a well-defined mount/init phase and tear them down on route/component exit. Remove event listeners/observers and cancel the render loop. Development double-mount behavior should not leave a hidden renderer running. If assets are cached across routes, distinguish intentional reusable cache memory from a leak.

## Time
Use elapsed/delta time deliberately and cap or handle huge delta after hidden-tab/background pauses. Do not base animation speed on assumed 60 Hz. If GSAP owns a camera/object property, establish whether the render loop simply renders current state or also updates it; avoid two authorities.

## Context loss
WebGL context loss can occur. Decide the product behavior: recover/reinitialize when feasible or replace the 3D surface with a fallback. Do not let a failed canvas make navigation/content unusable.

## Diagnostics
Three.js renderer information can help inspect geometries, textures, programs, draw calls, triangles, and related runtime counts, but internal cached resources may remain for legitimate reuse. Compare counts over repeated mount/unmount cycles and controlled scene changes rather than demanding absolute zero.

Use browser performance/memory tooling and real-device observation for heavy scenes. CPU profiles reveal excessive raycasting/object traversal or JS updates; GPU/render symptoms may require reducing draw calls, fragments, post-processing, texture load, or DPR.

## Quality baseline
A robust scene can mount, resize, pause/background, navigate away, navigate back, fail asset load, and switch to reduced-motion/fallback behavior without duplicate loops or unbounded resource growth.
