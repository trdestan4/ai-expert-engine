# Shader Authoring System

A maintainable shader starts with spaces and data flow. Document every varying/uniform by meaning and coordinate space. Common bugs come from mixing object-space normals with world-space light vectors, treating UV coordinates as aspect-correct screen coordinates, or using color values in the wrong transfer space.

## Vertex stage
Use the vertex shader for geometry transformation, displacement, point size, and values that can be interpolated across the primitive. Displacement may affect silhouette and normals; large displacement with unchanged normals produces incorrect lighting. Decide whether normals must be recomputed/approximated or whether the effect intentionally ignores PBR lighting.

## Fragment stage
Use the fragment shader for surface/screen color and per-pixel effects. Track texture samples and full-screen overdraw because fragment work dominates many mobile scenes. Branching is not automatically forbidden, but divergent/heavy branches in hot fragments should be justified and measured.

## Coordinates
For procedural screen effects, derive normalized coordinates from actual render-target resolution and correct aspect ratio. For object effects, understand model/world/view/projection matrices rather than cargo-culting transforms. When depth is sampled, know whether values are nonlinear device depth and whether reconstruction is required.

## Uniforms and varyings
Group stable configuration from per-frame data. Reuse typed vectors/matrices instead of creating garbage every frame. Pass the minimum data needed. Large arrays or frequently recreated uniforms can create CPU-side overhead even if the shader itself is fast.

## Noise and SDF
Procedural noise is a tool, not a visual strategy. Choose complexity/frequency/octaves according to the perceptual role. Fractal noise multiplies cost. Signed distance functions are powerful for procedural shapes/masks but require careful antialiasing and coordinate scaling. Cache/bake textures when a static field gives the same visual result cheaper.

## Color
Perform lighting/blending operations in the expected working space and integrate with the renderer's color management. Do not apply duplicate gamma/tone conversions. Texture roles differ: color/albedo maps and data maps such as normal/roughness typically have different color-space handling.

## Time
Long-running time values can lose precision on some paths; wrap or derive periodic time where useful. Pause or reduce time-driven animation offscreen/hidden when the experience does not need continuous simulation.

## Debugging
Replace the final output with diagnostic colors for UV, normal, depth, mask, texture channel, or intermediate scalar. Simplify control flow and remove texture dependencies until the failure boundary is found. Compiler logs must be surfaced during development. Keep a plain standard material/pass as a comparison path.

## Portability
GLSL language/features, precision, derivatives, texture formats, and WebGL/WebGPU/Three.js node systems differ. Do not assume a ShaderToy fragment can be pasted into a production Three.js material without adapting coordinates, uniforms, lifecycle, color, and browser constraints.
