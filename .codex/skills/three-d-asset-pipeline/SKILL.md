---
name: three-d-asset-pipeline
description: Owns web 3D asset preparation from DCC source to validated glTF/GLB delivery, including scale/transforms, topology, UVs, PBR materials, baking, animation clips, texture resolution and KTX2/Basis compression, Draco/Meshopt trade-offs, LOD/instancing strategy, naming, provenance, and runtime handoff budgets.
---

# Purpose
Turn source 3D content into predictable web assets that load fast, render correctly, fit GPU memory, and preserve required visual detail. Runtime hacks should not compensate for broken export, uncontrolled textures, or unnecessary geometry.

## Use when
- Blender/DCC assets must be prepared for Three.js/web delivery;
- GLB/glTF export, transforms, scale, materials, UVs, animation, texture packing, or naming are unreliable;
- geometry/texture compression, Meshopt/Draco/KTX2/Basis, LOD, instancing, or baking decisions are needed;
- a 3D experience is heavy because of asset structure rather than runtime code;
- asset provenance/source/master and optimization reproducibility matter.

## Do not use when
- scene/camera/renderer/interaction code is primary (`threejs-webgl`);
- custom shader runtime is primary (`realtime-shaders`);
- static raster/vector/video assets dominate (`asset-production`);
- visual direction/model concept has not been approved (`visual-art-direction`).

## Inputs
Use source file and license/provenance, target visual quality, physical scale/orientation, animation requirements, expected camera distance, runtime engine/version, device/network budget, material model, texture source resolution, repeated objects, and whether geometry/material variants must be interactive.

## Workflow
### 1. Normalize source
Establish units, axes/orientation, transforms, object origins/pivots, hierarchy, naming, hidden/unneeded objects, modifiers, and animation ranges. Apply/bake transforms only when it preserves intended animation/instancing behavior.

### 2. Optimize geometry by visibility
Remove unseen/redundant geometry, merge or instance repeated assets where runtime usage allows, preserve silhouette/normal quality, and reduce topology based on camera distance rather than arbitrary polygon targets. Keep separate meshes when interaction/material/animation requires it.

### 3. Build web PBR materials
Map source materials to glTF-compatible PBR when possible. Consolidate materials, fix texture color roles, normal orientation, UVs, alpha mode, double-sided use, emissive/metal/roughness behavior, and bake unsupported procedural networks.

### 4. Budget textures
Choose resolution from on-screen texel need. Pack channels where the format/workflow supports it, generate mipmaps appropriately, and compress web textures using KTX2/Basis when runtime support/budget benefits. Remember a small JPEG/PNG file can expand to large GPU memory.

### 5. Optimize geometry transfer
Evaluate Meshopt or Draco according to runtime support, decode cost, caching, and model characteristics. Compression should be reproducible in the build pipeline; keep an uncompressed master.

### 6. Prepare animation
Trim clips, remove unused tracks, validate root/pivot behavior, loop boundaries, interpolation, skeleton/skin weights, and morph targets. Avoid exporting editor-only animation baggage.

### 7. Validate glTF output
Check asset with validator/viewer/runtime, inspect warnings/extensions, bounding boxes, scale, normals/tangents, material parity, animation names, texture links, and compressed extension support before handoff.

### 8. Handoff budgets and contract
Provide final bytes, approximate geometry counts, texture dimensions/formats, extensions/decoders required, clip names, variant semantics, LOD strategy, source/master provenance, and fallback/poster needs to `threejs-webgl`.

## Decision rules
- Optimize for the visible experience, not an arbitrary triangle number.
- Texture memory often dominates mobile 3D; file byte size alone is misleading.
- Compression adds decode/transcode complexity and must be justified by end-to-end evidence.
- Preserve an editable master and make optimization reproducible.
- Do not merge meshes that must animate, pick, hide, recolor, or instance independently.
- Validate export in the actual target runtime, not only the DCC viewport.

## Reference routing
Load `references/gltf-production-pipeline.md` for DCC cleanup, transforms, materials, UVs, animation, glTF validation, naming, and runtime handoff.
Load `references/compression-textures-lod.md` for KTX2/Basis, geometry compression, texture/GPU budgets, LOD, instancing, baking, and optimization trade-offs.

## Quality gates
- Source/master provenance and reproducible export path are known.
- Scale/orientation/pivots/hierarchy are intentional.
- Materials and texture color roles match runtime PBR expectations.
- Texture resolutions/formats reflect actual screen need.
- Required compression extensions/decoders are documented.
- Animation clips and interaction-relevant mesh boundaries are preserved.
- glTF output is validated and tested in the target runtime.
- Runtime receives measurable asset budgets and fallback requirements.

## Failure handling
If visual parity fails, identify whether the source material is unsupported, color/normal/UV data is wrong, or runtime lighting differs before adding custom shaders. If asset weight is high, optimize textures and invisible/repeated geometry before destroying silhouette quality. If an extension cannot be supported in the deployed runtime, re-export with a compatible path.

## Output contract
Return source normalization, glTF export contract, geometry/material/texture/animation plan, compression/LOD/instancing decisions, validation evidence, measured asset inventory, provenance, and Three.js runtime handoff.
