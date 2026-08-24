# Compression, Textures, LOD, and Web 3D Budgets

Optimization has multiple independent targets: network bytes, decode time, CPU memory, GPU vertex/index memory, GPU texture memory, draw calls, shader cost, and visual quality.

## Texture budget
Uncompressed GPU texture cost depends on dimensions, format, mip levels, and array/cube usage, not the compressed source-file size. A visually simple 4K JPEG can still become expensive GPU memory. Choose resolution from maximum on-screen texel need and camera distance. Reuse textures where appropriate, atlas only when it helps the draw/material architecture, and avoid unique high-resolution maps for tiny objects.

KTX2 can carry GPU-oriented textures, and Basis Universal supercompression enables runtime transcoding to formats supported by the device. In a Three.js pipeline this can reduce transfer and GPU footprint, but requires the KTX2 transcoder/runtime setup. Validate visual artifacts, alpha, normal/data texture treatment, and transcoding support.

## Geometry compression
Draco and Meshopt can reduce geometry transfer. Compare compression ratio, decoder download/caching, decode time, worker behavior, runtime support, and whether progressive/streaming characteristics matter. A tiny static model may not justify extra decoder complexity. Keep optimization deterministic and versioned.

## Geometry detail
Reduce polygons based on silhouette, curvature, shading, deformation, and camera distance. Baking normal/AO/detail maps can move detail from geometry to textures, which shifts rather than erases cost. Balance the two budgets.

## LOD
Use LOD when camera distance or device constraints produce meaningful savings. Define switch distances/hysteresis and avoid visible popping; crossfade only if the extra overlap cost is justified. LOD assets should share consistent materials/UV/animation assumptions where needed.

## Instancing
Repeated identical geometry/material transforms are candidates for instancing. Keep per-instance attributes minimal and understand interaction implications. Instancing is a runtime architecture decision coordinated with `threejs-webgl`, but asset structure should enable it.

## Baking
Bake expensive procedural material/light/detail into textures when the visual is largely static and the texture budget is acceptable. Do not bake information that must react dynamically to runtime lighting or product customization.

## Delivery tiers
For ambitious experiences consider asset tiers: full and constrained variants with lower texture resolution/model detail. A fallback poster/image should be designed for no-3D or failed-load conditions. Avoid user-agent model lists where capability/performance measurement can make a better decision.

## Verification
Measure final compressed bytes and load/decode time, inspect GPU/runtime behavior, compare visual parity at intended camera positions, and test on representative mobile hardware. Optimization is complete when the asset meets visible-quality and runtime budgets together—not when a compressor reports the smallest file.
