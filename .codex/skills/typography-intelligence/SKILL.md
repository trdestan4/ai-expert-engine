---
name: typography-intelligence
description: Designs context-specific, readable, performant typography systems for web products by selecting type character, hierarchy, scale, rhythm, pairing, responsive behavior, and loading strategy; it avoids default font choices and prestige typography clichés.
---

# Purpose

Use typography as both a brand voice and an interface system, balancing character, readability, content density, localization, responsiveness, accessibility, and performance.

## Use when

- a site needs font selection or a complete type system;
- typography feels generic, inconsistent, overly fashionable, or detached from brand/product character;
- heading/body pairing, hierarchy, line length, rhythm, or responsive scale is weak;
- an existing brand font must be adapted for UI;
- performance/localization constraints affect font strategy.

## Do not use when

- whole-site creative direction is unresolved (`creative-director` first);
- only logo lettering/wordmark construction is in scope (`brand-design`);
- the issue is primarily layout hierarchy rather than typography (`ux-ui-design`).

## Inputs

Use:

- brand/creative direction;
- audience and reading context;
- content density and language set;
- UI vs editorial balance;
- available/licensed font assets;
- performance constraints;
- accessibility/legibility requirements;
- target devices and responsive range.

## Workflow

### 1. Define typographic job

State what type must communicate and support: precision, warmth, authority, speed, craft, editorial depth, technical clarity, playful energy, etc. Connect each trait to observable type characteristics.

### 2. Choose functional roles

Define only necessary roles:

- display/hero;
- heading;
- body;
- UI/control;
- data/mono when justified;
- caption/metadata.

Do not add a second or third family without a clear job.

### 3. Select by characteristics, not popularity

Evaluate:

- x-height;
- width/condensation;
- stroke contrast;
- terminals/geometry;
- optical size/variable axes;
- numeral quality;
- weight range;
- punctuation/symbol support;
- language coverage;
- small-size clarity;
- loading footprint.

Avoid defaulting to Inter, Poppins, Montserrat, Playfair, DM Sans, or any fashionable family merely because it is familiar.

### 4. Build hierarchy

Define scale from information priority, not decorative size. Control:

- font size;
- weight;
- line height;
- letter spacing;
- line length;
- case;
- spacing before/after text blocks.

Hierarchy should remain readable without relying on color alone.

### 5. Design responsive behavior

Use fluid or breakpoint-based scale where appropriate. Recompose large display treatments on narrow screens instead of only shrinking them. Protect line length and avoid oversized hero type that pushes all useful content below the fold.

### 6. Validate pairing

When pairing families, require complementary contrast rather than arbitrary difference. One family with variable styles may be stronger and cheaper than a fashionable serif/sans pairing.

### 7. Handle localization

Check glyph/language support, fallback metric compatibility, text expansion, punctuation, numeral formats, and line breaking. Do not build identity around characters missing from target languages.

### 8. Define font performance strategy

Prefer minimal families/weights, variable fonts where beneficial, subset only when safe, preload selectively, use appropriate `font-display`, and avoid blocking critical rendering with decorative weights.

## Decision rules

- Typography must fit content behavior, not only screenshots.
- “Luxury” does not automatically require high-contrast serif display type.
- “Modern” does not automatically require geometric sans.
- Display personality can be strong while body/UI typography remains quiet.
- Fewer weights/styles improve hierarchy discipline and performance.
- Readability and language coverage outrank novelty.
- Large typography needs responsive composition rules, not just `clamp()`.

## Reference routing

Load `references/type-decision-system.md` for selection criteria, hierarchy construction, pairing, fluid scale, and performance checks.

Use `anti-generic-design` when typography is selected primarily from trend or prestige association.

## Quality gates

- Every font family/weight has a role.
- Selection rationale is based on characteristics and context.
- Heading/body/UI hierarchy is distinct and coherent.
- Responsive behavior protects reading and composition.
- Localization/glyph requirements are considered.
- Loading strategy is realistic.
- Type system avoids generic prestige mappings.

## Failure handling

If the ideal display family lacks language or web performance support, preserve its character through a compatible alternative or restrict it to non-critical brand assets. If pairing adds no useful contrast, simplify to one family. If a brand font performs poorly in UI, keep it for expressive roles and use a highly compatible interface companion.

## Output contract

Return:

- typographic intent;
- selected family characteristics/options;
- role assignment;
- hierarchy/scale/rhythm rules;
- responsive behavior;
- pairing/fallback logic;
- localization constraints;
- font loading/performance guidance.
