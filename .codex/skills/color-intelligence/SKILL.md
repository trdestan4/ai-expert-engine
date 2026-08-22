---
name: color-intelligence
description: Builds context-specific, accessible, production-ready color systems from brand, audience, content, environment, and interaction needs instead of prestige or industry clichés; it defines roles, relationships, states, modes, and token logic rather than merely listing hex values.
---

# Purpose

Choose and structure color as a communication system: distinctive enough to support brand character, controlled enough for real UI, and accessible across states, modes, content, and devices.

## Use when

- a new palette/color system is required;
- a palette feels generic, fashionable without rationale, or poorly balanced;
- brand colors must be translated into UI tokens;
- light/dark themes need coherent behavior;
- interaction/status/data colors need definition;
- contrast or color hierarchy is failing.

## Do not use when

- whole-site creative direction is unresolved (`creative-director` first);
- the task is solely brand positioning/logo design (`brand-design`);
- the issue is only typography/layout.

## Inputs

Use:

- creative/brand direction;
- audience and product context;
- content density and imagery;
- current brand colors if fixed;
- light/dark requirements;
- accessibility constraints;
- semantic states and data visualization needs;
- display/environment constraints where material.

## Workflow

### 1. Define color intent

State what color must accomplish, such as:

- establish recognition;
- create calm/high-trust environment;
- distinguish product categories;
- foreground imagery;
- support dense operational UI;
- create editorial warmth;
- communicate interaction/status clearly.

Do not begin from a favorite hex code.

### 2. Separate brand color from interface color

Define roles:

- brand signature;
- canvas/background;
- surfaces;
- primary/secondary text;
- borders/dividers;
- interactive accent;
- hover/active/focus;
- success/warning/error/info;
- selected/disabled;
- data categories if needed.

Brand color does not need to fill every surface.

### 3. Explore palette families contextually

Evaluate hue families through:

- category expectations;
- differentiation;
- emotional temperature;
- product/material imagery;
- cultural/context implications when relevant;
- contrast feasibility.

Explicitly challenge default mappings such as:

- premium → navy/gold;
- luxury → black/gold;
- healthcare → cyan/teal;
- sustainability → green;
- technology → electric blue/purple;
- finance → dark blue;

Use them only when strategically earned.

### 4. Build tonal architecture

Create sufficient steps for real UI rather than one background + one accent. Preserve perceptual hierarchy between canvas, surface, raised surface, borders, text, and interactive states.

Avoid low-contrast “premium” interfaces that sacrifice readability.

### 5. Design accent discipline

Define where accent may and may not appear. Primary accent should usually signal brand or interaction priority—not decorate every heading/card.

### 6. Handle light/dark modes independently

Dark mode is not color inversion. Rebalance:

- luminance hierarchy;
- chroma/saturation;
- image treatment;
- borders/shadows;
- accent intensity;
- semantic colors.

Product imagery must remain visually separated from dark surfaces.

### 7. Validate accessibility and states

Check text/control contrast, non-color indicators, focus visibility, disabled states, status differentiation, and interactive state progression.

### 8. Produce token roles

Prefer semantic tokens such as:

`bg/canvas`, `bg/surface`, `text/primary`, `text/muted`, `border/subtle`, `action/primary`, `focus/ring`, `status/error`.

Keep raw palette scales separate from semantic roles when implementation needs both.

## Decision rules

- Color choice must have product/brand rationale beyond trend association.
- Contrast is a quality property, not a late compliance patch.
- Fewer disciplined colors usually outperform many equally loud accents.
- Neutral does not mean gray-only; neutrals may carry controlled hue temperature.
- Dark UI needs surface separation; pure black everywhere is rarely optimal.
- Product/photography colors are part of the composition and should influence UI chroma.
- Semantic states must remain understandable without color alone.

## Reference routing

Load `references/color-decision-system.md` for palette construction, tonal roles, dark-mode adaptation, and evaluation.

Use `anti-generic-design` when palette choice is driven by prestige/category cliché.

## Quality gates

- Palette rationale is tied to context.
- Raw colors and semantic roles are distinguishable.
- Canvas/surface/text/interaction hierarchy is complete.
- Light/dark behavior is intentionally adapted.
- Accent use is controlled.
- Contrast and state differentiation are viable.
- Palette does not rely on a default “premium/tech/health” formula.

## Failure handling

If required brand colors have poor UI contrast, preserve them as brand/signature assets while introducing accessible interface variants. If imagery clashes with surfaces, adjust UI temperature/chroma or image treatment rather than forcing brand color everywhere. If a palette is visually attractive but indistinguishable from category competitors, revisit creative direction.

## Output contract

Return:

- color intent;
- palette concept/rationale;
- raw/tonal palette guidance;
- semantic token roles;
- accent discipline;
- light/dark adaptation;
- state/accessibility rules;
- anti-cliché rationale and risks.
