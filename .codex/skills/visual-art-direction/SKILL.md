---
name: visual-art-direction
description: Defines a coherent image, photography, illustration, icon, texture, 3D, material, lighting, composition, and asset language for web products so visuals support brand, content, and conversion instead of looking like unrelated generated assets.
---

# Purpose

Create an asset direction that makes every visual feel from the same world and supports the product narrative, hierarchy, and interface rather than acting as decoration.

## Use when

- a site needs photography/image generation direction;
- hero/service/product visuals need one coherent style;
- generated imagery looks inconsistent or synthetic;
- illustration, icon, 3D, texture, or background systems must be defined;
- product photography must work across light/dark UI;
- visual assets need performance/responsive planning.

## Do not use when

- the whole creative thesis is unresolved (`creative-director` first);
- only palette/type is in scope;
- the task is direct asset generation/editing (`asset-production` will own execution later).

## Inputs

Use:

- product/brand/creative direction;
- content hierarchy and asset roles;
- target audience/context;
- current logo/color/type system;
- available source photography/assets;
- implementation, performance, responsive, and accessibility constraints.

## Workflow

### 1. Define visual jobs

Classify assets by purpose:

- product truth/evidence;
- emotional atmosphere;
- explanation/education;
- navigation/category recognition;
- brand signature;
- decorative support.

Decorative assets must never compete with evidence or interaction.

### 2. Choose one governing visual world

Specify:

- realism/stylization level;
- camera/lens perspective or illustration geometry;
- lighting direction/quality;
- depth/material behavior;
- background/environment;
- crop and negative-space rules;
- human presence and authenticity;
- texture/grain/finish;
- color relationship to UI.

### 3. Define medium hierarchy

Choose which mediums dominate and which remain supporting:

- photography;
- product renders;
- editorial collage;
- vector illustration;
- line/filled iconography;
- 3D/CG;
- procedural/abstract graphics;
- texture/pattern.

Avoid mixing mediums merely for variety.

### 4. Define composition rules

Set repeatable constraints for focal placement, scale, crop, horizon, visual weight, empty area for copy, card thumbnails, mobile crops, and image-to-image rhythm.

### 5. Define generated-asset realism rules

When AI-generated imagery is used, avoid common synthetic tells:

- over-perfect symmetry;
- plastic skin/materials;
- impossible reflections/lighting;
- inconsistent product geometry;
- meaningless micro-details/text;
- generic “cinematic” haze;
- excessive depth-of-field;
- unrelated backgrounds across a set.

Generated assets must match a locked visual bible.

### 6. Define UI integration

Specify edge behavior, masks, backgrounds, surface separation, transparent product cutouts, shadow direction, image borders, captions, hover crops, and dark/light adaptation.

### 7. Define responsive asset strategy

Plan alternate crops/ratios, art direction by viewport, focal-point preservation, placeholder behavior, and when to use separate mobile assets.

### 8. Define production constraints

Set source-resolution requirements, preferred formats, transparency needs, compression tolerance, animation/video budget, and alt-text/caption requirements.

## Decision rules

- Visual assets must have a role before a style.
- Consistency comes from shared rules, not identical images.
- Product truth outranks cinematic styling in commerce/high-trust contexts.
- 3D or generated imagery must be justified by explanation, differentiation, or atmosphere—not trend appeal.
- Dark-mode product imagery needs explicit separation and tone control.
- Avoid visual density that reduces text/CTA comprehension.
- Icons should form a system, not a mixed marketplace collection.

## Reference routing

Load `references/art-direction-system.md` for visual bible fields, medium selection, composition, AI-generation consistency, and responsive asset planning.

Use `anti-generic-design` if the direction relies on fashionable abstract 3D/AI imagery without product rationale.

## Quality gates

- Every asset class has a defined job.
- One coherent visual world governs medium, lighting, crop, and finish.
- AI/generated asset consistency rules are explicit when relevant.
- Visuals integrate with UI surfaces and themes.
- Mobile/responsive crops are planned.
- Production/performance/accessibility needs are considered.
- Assets reinforce product/brand truth rather than generic atmosphere.

## Failure handling

If available source assets are inconsistent, define a normalization treatment rather than pretending a perfect set exists. If generated product visuals cannot guarantee geometry/truth, use real photography/render sources for evidence-critical views and reserve generated imagery for atmosphere. If a visual treatment harms readability, preserve the concept in less critical regions.

## Output contract

Return:

- visual thesis;
- asset roles/medium hierarchy;
- visual bible rules;
- composition/crop rules;
- AI-generation consistency rules when applicable;
- UI/theme integration;
- responsive asset behavior;
- production/performance/accessibility constraints.
