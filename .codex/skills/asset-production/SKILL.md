---
name: asset-production
description: Owns production-ready visual asset creation across image generation/editing, SVG, icons, illustration, general 3D renders, video/motion assets, responsive derivatives, compression, metadata, provenance, and delivery; specialized interactive web glTF/GLB preparation routes to `three-d-asset-pipeline`.
---

# Purpose
Turn an approved visual direction into coherent, reusable, web-ready assets whose style, technical format, accessibility, rights/provenance and performance remain controlled across the product. Keep general asset production distinct from the specialist DCC→interactive-web-3D pipeline.

## Use when
- website/product images, generated imagery, edits, illustrations, icons or SVGs must be produced;
- rendered 3D, motion/video assets, posters or responsive derivatives are needed;
- asset format, compression, dimensions, transparency, crop/safe area or delivery behavior matters;
- a set of assets needs visual consistency, naming, provenance or production QA.

## Do not use when
- creative/brand direction is undefined (`creative-director`, `brand-design`, `visual-art-direction`);
- layout/component implementation alone is primary (`frontend-engineering`, `ux-ui-design`);
- runtime image optimization alone is primary (`performance`);
- generic file storage/upload architecture is primary (`storage-media`);
- Blender/DCC source must be optimized/exported as interactive glTF/GLB with KTX2/Draco/Meshopt/LOD/runtime contract (`three-d-asset-pipeline`).

## Inputs
Identify creative direction, brand rules, asset role, target surfaces, source material, dimensions/aspect ratios, responsive breakpoints, focal/safe areas, transparency, animation needs, accessibility meaning, target formats, quality/performance budget, licensing/provenance, editing restrictions and reuse/versioning needs.

## Workflow
### 1. Define the asset contract
For every family specify purpose, visual role, source/reference constraints, dimensions/aspect ratios, crop behavior, format, transparency, text/no-text rule and delivery targets.

### 2. Preserve visual-system consistency
Follow approved composition, lighting, palette, material, perspective, icon geometry, stroke weight and image-treatment rules. Do not let individual generations drift.

### 3. Generate or edit non-destructively
Preserve source identity/content constraints when editing. Keep masters separate from delivery derivatives. Retain reproducible prompts/settings/reference notes where practical.

### 4. Clean vectors and icons
Use deliberate viewBox, geometry, stroke/fill conventions and alignment. Remove editor junk, unsafe scripts/external references and unnecessary path complexity.

### 5. Prepare motion/video/rendered 3D
Define camera/lighting/material/motion language, loop boundaries, poster/fallback frames, reduced-motion behavior and realistic budgets before export. If the 3D remains interactive runtime geometry, route source/export optimization to `three-d-asset-pipeline` and runtime to `threejs-webgl`.

### 6. Produce delivery variants
Create aspect-ratio crops, density/responsive variants and appropriate codecs/formats without blindly generating every size. Preserve focal hierarchy across breakpoints.

### 7. Optimize and validate
Balance perceptual quality, transparency, color, dimensions and byte weight. Verify on actual target backgrounds/devices.

### 8. Record provenance and handoff
Store source/master relationship, license/usage constraints, generation/edit provenance, filenames/variants and implementation notes.

## Decision rules
- Creative direction precedes asset generation.
- Do not bake essential UI copy into raster media when live text is needed for accuracy/localization/SEO/accessibility.
- Source edits must not silently exceed requested scope.
- SVG is code-like input and untrusted SVG requires sanitation.
- Responsive variants preserve subject/focal hierarchy rather than blind center crops.
- Meaningful content requires accessible text/caption behavior coordinated with `accessibility`.
- Motion has a static/reduced-motion path when needed.
- Unknown provenance is a release risk, not something to invent.
- General 3D renders belong here; interactive web-3D source/export optimization belongs to `three-d-asset-pipeline`.

## Reference routing
Load `references/image-generation-editing.md` for raster generation/editing/source preservation.
Load `references/svg-icons-illustration.md` for SVG hygiene/icon systems/illustration.
Load `references/three-d-video-motion-assets.md` for rendered 3D, video, loops, posters and motion exports.
Load `references/responsive-formats-delivery.md` for dimensions, crops, codecs, responsive variants and browser delivery.
Load `references/asset-consistency-provenance.md` for continuity, masters, naming, licensing and provenance.
Load `references/web-asset-quality-performance.md` for perceptual QA, compression, metadata, color and performance handoff.

## Quality gates
- Every asset maps to approved creative/product role.
- Asset families remain intentionally consistent.
- Source edits respect lock/preservation constraints.
- SVG/icon output is clean/safe.
- Responsive variants preserve focal intent.
- Meaningful content has accessibility/caption strategy.
- Motion/video has poster/fallback/reduced-motion behavior when applicable.
- Delivery byte/format quality is verified.
- Master/source provenance and usage rights are known or explicitly unresolved.
- Interactive 3D is routed to the specialist pipeline/runtime rather than treated as a generic export.

## Failure handling
If creative direction is missing, route back instead of inventing generic style. If source fidelity cannot be preserved, state the limitation. If provenance is unknown, flag it. If a format/browser capability is uncertain, verify current support. If interactive GLB/glTF performance/export is the problem, route to `three-d-asset-pipeline` rather than iterating generic asset compression blindly.

## Output contract
Return asset inventory/contract, production/editing direction, master/variant plan, format/export decisions, consistency/accessibility rules, provenance/licensing status, optimization evidence, implementation handoff and specialist escalations.
