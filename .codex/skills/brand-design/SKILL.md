---
name: brand-design
description: Defines or extends a coherent brand identity system for digital products, including positioning expression, logo/mark logic, visual identity principles, identity assets, consistency rules, and digital application guidance; it does not independently choose the full website UX.
---

# Purpose

Translate brand strategy into a scalable identity system that remains recognizable, credible, and consistent across web interfaces and supporting assets.

## Use when

- a brand identity must be created, refreshed, or formalized;
- a logo/mark, identity language, or digital brand application needs direction;
- existing brand materials are inconsistent or incomplete;
- UI decisions need a stable identity layer;
- a site must feel specific to the organization rather than visually interchangeable.

## Do not use when

- product strategy is unresolved (`product-strategy` first);
- the task is only page usability/layout (`ux-ui-design`);
- the task is only palette or type system (`color-intelligence`, `typography-intelligence`);
- the request is only image/photography treatment (`visual-art-direction`).

## Inputs

Use:

- brand/product purpose;
- audience and market context;
- current identity assets if any;
- brand traits with behavioral meaning;
- competitive/category cues;
- digital and physical use cases;
- constraints such as localization, accessibility, small-size use, dark/light environments, and production formats.

## Workflow

### 1. Separate brand essence from style adjectives

Define 3–5 identity principles that express how the brand should behave visually. Convert adjectives into observable design implications.

### 2. Identify distinctive assets

Determine which elements can create recognition:

- wordmark/mark/monogram;
- typography behavior;
- color relationship;
- framing/shape system;
- image treatment;
- icon/illustration language;
- layout signature;
- motion signature.

Not every brand needs every asset.

### 3. Define logo/mark logic when in scope

Evaluate:

- recognizability;
- simplicity without generic symbolism;
- category fit without literal cliché;
- legibility at favicon/small sizes;
- monochrome viability;
- horizontal/stacked use;
- clear space/minimum size;
- dark/light application.

Avoid forcing initials, shields, crowns, swooshes, globes, teeth, trucks, houses, circuit traces, or other category icons unless the concept genuinely benefits.

### 4. Build identity rules

Document:

- primary/secondary marks;
- color roles (delegate detailed palette to `color-intelligence`);
- type roles (delegate detailed system to `typography-intelligence`);
- image and graphic behavior;
- geometry/surface language;
- spacing/placement principles;
- misuse/anti-patterns.

### 5. Apply to digital surfaces

Show how identity influences:

- header/navigation;
- hero/signature areas;
- cards/product surfaces;
- CTAs and controls;
- editorial/content layouts;
- empty/loading/status states where relevant;
- dark/light modes;
- social/favicons/OG assets when needed.

Identity must support UI; it must not turn controls into brand decoration.

### 6. Test recognition and scalability

Check whether the system still feels branded with:

- logo temporarily hidden;
- a long content page;
- mobile layout;
- dense ecommerce/catalog screens;
- monochrome or reduced-color contexts.

### 7. Run anti-generic review

Use `anti-generic-design` when identity choices are based on common AI/logo tropes or prestige clichés.

## Decision rules

- Distinctive does not mean complicated.
- Brand recognition should come from a system, not logo repetition.
- Category familiarity should support trust, not erase differentiation.
- Never infer premium from gold, luxury from black, technology from neon blue, or healthcare from generic cyan without context.
- Digital accessibility and legibility outrank decorative purity.
- The identity should work with real content volume, not only presentation mockups.

## Reference routing

Load `references/brand-system.md` for identity component coverage and validation.

Use `creative-director` for whole-site creative direction; use specialist color/type/image skills for their detailed systems.

## Quality gates

- Identity principles are specific and usable.
- Distinctive assets are intentional rather than numerous.
- Logo/mark works at realistic digital sizes when applicable.
- System survives mobile, content-heavy, and monochrome/reduced contexts.
- UI usability is not sacrificed to branding.
- Identity cannot be summarized as a generic industry template.

## Failure handling

If the identity depends entirely on one fashionable effect, rebuild recognition from multiple durable cues. If logo concepts become literal/category-generic, return to brand principles and conceptual territory. If current brand assets must be preserved, extend them rather than silently replacing them.

## Output contract

Return:

- identity principles;
- distinctive brand assets;
- logo/mark rules when applicable;
- color/type/image/graphic direction handoffs;
- digital application rules;
- misuse/anti-patterns;
- scalability and recognition checks.
