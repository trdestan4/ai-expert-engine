# glTF Production Pipeline

glTF is a runtime delivery format, not the editable master. Keep the original DCC source and a reproducible export/optimization pipeline so quality regressions can be traced.

## Scene normalization
Set expected units and orientation. Confirm origin/pivots for rotating/opening/interactive parts, and preserve hierarchy needed by animation or runtime control. Delete hidden/editor helper objects unless deliberately exported. Freeze/apply transforms only when compatible with rigging, instancing, and animation.

## Geometry
Optimize based on visible silhouette, shading, deformation, and camera distance. Remove internal/unseen surfaces where safe. Repeated rigid objects may be instanced at runtime, but do not merge pieces that need independent interaction or animation. Ensure normals are intentional; generate/tune tangents when normal maps require them.

## UVs and materials
Use UV sets deliberately and avoid accidental overlaps where baked textures need unique space. Translate materials to glTF metallic-roughness PBR when possible. Unsupported procedural nodes should be baked or recreated explicitly. Minimize material count when visual/interaction requirements allow because material boundaries can increase draw calls.

Color/albedo/emissive textures are color data; normal, roughness, metallic, occlusion and many masks are data maps. Preserve the distinction through export and runtime color management. Validate alpha mode and double-sided surfaces; using double-sided everywhere increases work and can hide modeling problems.

## Animation
Export only required actions/clips. Name clips semantically. Validate frame range, interpolation, skeleton hierarchy, skin weights, morph targets, root motion, and loop seam. Remove unused tracks where tooling permits. Test clips in an independent glTF viewer and the actual Three.js runtime.

## Extensions
Record every extension the output relies on. The runtime must configure corresponding decoders/features. Do not adopt an extension merely because an optimizer supports it; compatibility and benefit must be demonstrated.

## Validation
Run a glTF validator where available and treat warnings intentionally. Inspect file structure and bounds, then visually test:
- model scale/orientation/framing;
- normals and mirrored transforms;
- material/texture parity;
- transparency sorting issues;
- animation clip names/timing;
- morph/skin deformation;
- extension/decoder readiness;
- missing external resources if using `.gltf` rather than a self-contained `.glb`.

## Handoff manifest
For each asset record master/source path, output path/hash/version, dimensions/bounds/scale, mesh/material count, approximate triangles/vertices, texture list and dimensions/formats, extensions, clip/variant names, intended camera distance, and license/provenance. This lets runtime engineering distinguish asset defects from scene defects.
