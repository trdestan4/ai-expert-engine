# Loading, PBR, Interaction, and Post-processing

## glTF loading
Use glTF/GLB for runtime 3D delivery when it fits the asset type. Keep model transformation hierarchy intact unless optimization explicitly changes it. Loading should expose useful progress/error state where the wait is visible, but essential HTML content should not depend on optional 3D success.

If the asset uses Draco geometry compression, configure the corresponding decoder. Compression reduces transfer bytes but adds decode work, so use it based on model/network/device evidence. If the asset uses Meshopt compression, configure the decoder supported by the installed loader/runtime. Do not enable decoders merely because they exist.

KTX2/Basis textures can reduce transfer and GPU texture footprint by transcoding to device-supported compressed formats. Configure the KTX2 transcoder path and detect renderer support before use according to the installed Three.js API. Texture compression is often more important to mobile memory than geometry compression.

## PBR and color
Physically based materials depend on correct texture roles, color-space handling, environment lighting, roughness/metalness, normal orientation, and sensible exposure/tone mapping. Avoid “fixing” an incorrectly authored material with arbitrary lights before checking texture/color/export settings.

Environment maps can provide both lighting and reflections. Use appropriate preprocessing/runtime path and resolution; very large environment textures can cost substantial memory.

## Interaction
Raycasting each frame against an entire complex scene can be unnecessary. Restrict pickable objects/layers, raycast on relevant pointer events or only when pointer interaction is active, and consider simpler proxy geometry for complex meshes. Normalize coordinates relative to the actual canvas bounds, not assumed full viewport.

Separate scene state from product state. A clicked mesh may emit a semantic product event; the checkout/router should not depend on a raw Three.js object reference.

## Post-processing
An EffectComposer-style pipeline renders through one or more passes and intermediate render targets. Every full-screen pass adds work and often memory. Add bloom, depth effects, distortion, color grading, anti-aliasing, or custom passes only when the art direction requires them. Understand pass ordering and keep final color/tone conversion correct for the renderer/version in use.

Resize composer/render targets with the scene and dispose them on teardown. Reduce render scale or pass count on constrained devices when the effect is nonessential.

## Loading/compilation hitches
Large textures, model parsing, shader compilation, and first-use material programs can cause visible stalls. Progressive activation, prewarming only where justified, smaller assets, and avoiding a huge burst of simultaneous uploads can improve the experience. Do not hide a ten-second initialization behind an elaborate loader if a useful HTML page can appear immediately.

## Performance triage
First identify whether the limit is transfer/decode, CPU update, draw-call/geometry submission, vertex work, fragment/fill-rate, post-processing, texture memory, or shader compilation. Different causes require different fixes. Coordinate asset changes with `three-d-asset-pipeline`, shader cost with `realtime-shaders`, and end-to-end measurement with `performance`.
