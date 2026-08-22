---
name: asset-production
description: Owns production-ready visual asset creation across image generation/editing, SVG, icons, illustration, 3D, video/motion assets, responsive derivatives, compression, metadata, provenance, and delivery; it follows creative direction and does not replace brand, UX/UI, accessibility, or frontend ownership.
---

# Purpose

Turn an approved visual direction into coherent, reusable, web-ready assets whose style, technical format, accessibility, rights/provenance and performance remain controlled across the product.

## Use when

- website/product images, generated imagery, edits, illustrations, icons or SVGs must be produced;
- 3D renders, motion/video assets, posters or responsive derivatives are needed;
- asset format, compression, dimensions, transparency, crop/safe area or delivery behavior matters;
- a set of assets needs visual consistency, naming, provenance or production QA.

## Do not use when

- creative direction/brand language has not been defined (`creative-director`, `brand-design`, `visual-art-direction`);
- layout/component implementation alone is primary (`frontend-engineering`, `ux-ui-design`);
- runtime image optimization alone is primary (`performance`);
- generic file storage/upload architecture is primary (`storage-media`).

## Inputs

Identify creative direction, brand rules, asset role, target surfaces, source material, required aspect ratios/dimensions, responsive breakpoints, focal points/safe areas, transparency, animation/motion needs, accessibility meaning, target formats, quality/performance budget, licensing/provenance constraints, editing restrictions and reuse/versioning needs.

## Workflow

### 1. Define the asset contract
For every asset family specify purpose, visual role, source/reference constraints, dimensions/aspect ratios, crop behavior, format, transparency, text/no-text rule and delivery targets.

### 2. Preserve visual-system consistency
Follow approved composition, lighting, palette, material, perspective, icon geometry, stroke weight and image-treatment rules. Do not let individual generations drift into unrelated styles.

### 3. Generate or edit non-destructively
Preserve source identity/content constraints when editing. Keep masters separate from delivery derivatives. For generated work, retain reusable prompts/settings/reference notes where practical so families can be reproduced.

### 4. Clean vectors and icons
Use deliberate viewBox, geometry, stroke/fill conventions and alignment. Remove editor junk, inaccessible embedded text where avoidable, unsafe scripts/external references and unnecessary path complexity.

### 5. Prepare motion/3D/video for the surface
Define camera/lighting/material/motion language, loop boundaries, poster/fallback frames, reduced-motion behavior and realistic performance budgets before export.

### 6. Produce delivery variants
Create aspect-ratio crops, density/responsive variants and appropriate codecs/formats without blindly generating every size. Preserve focal point and visual intent across breakpoints.

### 7. Optimize and validate
Balance perceptual quality, transparency, color, dimensions and byte weight. Verify rendered appearance on actual target backgrounds/devices rather than trusting export settings.

### 8. Record provenance and handoff
Store source/master relationship, license/usage constraints, generation/edit provenance where relevant, filenames/variants and implementation notes needed by frontend/content teams.

## Decision rules

- Creative direction precedes asset generation; prompts are implementation details, not the design strategy.
- Generated text inside imagery should be avoided when live HTML/SVG text is required for accuracy, localization, SEO or accessibility.
- Do not bake essential UI copy into raster images unless the product explicitly requires it.
- Source images supplied for editing must not be silently restyled or structurally changed beyond the requested scope.
- SVG is code-like input: sanitize untrusted SVG and avoid scripts, unsafe external references and accidental secrets/metadata.
- Use raster/vector/video formats according to content characteristics and actual browser/tooling support, not trend.
- Responsive variants must preserve the subject/focal hierarchy rather than use blind center crops.
- Decorative assets need not create noisy alt text; meaningful content requires accessible text/caption behavior coordinated with `accessibility`.
- Motion must provide a non-motion/static path where user preference or product constraints require it.
- Asset optimization must not visibly damage brand-critical/product-detail imagery merely to hit arbitrary byte targets.
- Rights, source, license and generated-asset usage constraints must not be invented; unknown provenance is a release risk.

## Reference routing

Load `references/image-generation-editing.md` for raster generation, editing, source preservation and consistency.
Load `references/svg-icons-illustration.md` for SVG hygiene, icon systems and illustration production.
Load `references/three-d-video-motion-assets.md` for 3D, video, loops, posters and motion exports.
Load `references/responsive-formats-delivery.md` for dimensions, crops, codecs, responsive variants and browser delivery.
Load `references/asset-consistency-provenance.md` for style continuity, masters, naming, licensing and provenance.
Load `references/web-asset-quality-performance.md` for perceptual QA, compression, metadata, color and performance handoff.

## Quality gates

- Every asset maps to an approved creative/product role.
- Asset families maintain intentional visual consistency.
- Source edits respect stated lock/preservation constraints.
- SVG/icon output is structurally clean and safe.
- Responsive variants preserve focal intent and required safe areas.
- Meaningful visual content has an accessibility/caption strategy.
- Motion/video has poster/fallback and reduced-motion behavior where applicable.
- Delivery formats/byte weight are verified against actual use.
- Master/source provenance and usage rights are known or explicitly unresolved.
- Frontend handoff includes dimensions, crop/fit behavior and variant naming.

## Failure handling

If creative direction is missing, route back to the creative specialists rather than invent a generic style. If exact source fidelity cannot be preserved, state the limitation instead of silently changing the subject. If provenance/license is unknown, flag it rather than claiming commercial safety. If a format or browser capability is uncertain, verify current support/tooling before committing the delivery strategy.

## Output contract

Return asset inventory/contract, production or editing direction, master/variant plan, format/export decisions, consistency and accessibility rules, provenance/licensing status, optimization evidence, implementation handoff and specialist escalations.