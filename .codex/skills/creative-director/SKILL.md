---
name: creative-director
description: Converts product and brand context into a distinctive, coherent creative direction for web experiences across layout, composition, visual language, imagery, typography, color, motion, and emotional tone; it coordinates creative specialists but does not replace them.
---

# Purpose

Create a project-specific art and experience direction that feels intentionally designed rather than assembled from fashionable AI/UI patterns.

## Use when

- a site needs a new or materially revised visual direction;
- the request contains subjective goals such as premium, elegant, bold, trustworthy, editorial, playful, technical, calm, or cinematic;
- design specialists need one coherent north star;
- multiple visual directions are plausible and must be evaluated;
- the existing design feels generic, inconsistent, trend-chasing, or “AI-generated.”

## Do not use when

- the creative direction is already locked and the task is a narrow component implementation;
- only palette selection is needed (`color-intelligence` owns it);
- only typography selection is needed (`typography-intelligence` owns it);
- only motion behavior is being designed (`motion-direction` owns it);
- product goals are unresolved (`product-strategy` first).

## Inputs

Use available evidence from:

- product outcome and audience;
- brand position/personality;
- content/product characteristics;
- market conventions and meaningful differentiation opportunities;
- desired emotional qualities;
- constraints such as accessibility, performance, asset availability, implementation stack, and content volume.

## Workflow

### 1. Translate adjectives into design criteria

Never map adjectives directly to clichés.

Examples:

- “premium” may mean restraint, material detail, editorial confidence, product focus, precision, scarcity, craftsmanship, or service quality depending on context;
- “modern” may mean clarity, reduced friction, strong type hierarchy, contemporary interaction, or technically expressive structure—not automatically gradients/glass;
- “luxury” must be interpreted through audience, price, category, heritage, and proof—not black/gold by default.

### 2. Identify category codes

Separate:

- **expected codes** — patterns users rely on for comprehension/trust;
- **overused codes** — patterns causing category sameness;
- **ownable opportunities** — choices the brand can credibly make distinctive.

Break convention only where comprehension is preserved.

### 3. Generate 2–3 direction hypotheses when needed

Each direction must specify:

- strategic idea;
- emotional tone;
- composition/layout behavior;
- typography character;
- color behavior;
- imagery/material language;
- shape/surface treatment;
- motion character;
- what makes it distinct;
- execution risks.

Directions must differ conceptually, not merely by palette.

### 4. Choose one direction

Evaluate against:

- product outcome;
- audience trust/comprehension;
- brand credibility;
- differentiation;
- content scalability;
- responsive behavior;
- performance/accessibility feasibility;
- implementation realism.

### 5. Define the visual grammar

Set rules, not screenshots:

- density and whitespace rhythm;
- grid behavior;
- hierarchy and scale contrast;
- geometry/edge language;
- surface/material treatment;
- image cropping/composition;
- typography roles;
- palette roles;
- icon/illustration character;
- motion tempo and intensity.

### 6. Define signature moments

Choose 1–3 memorable moments appropriate to the product, such as:

- product reveal;
- scroll narrative;
- distinctive navigation transition;
- editorial product grid;
- interactive comparison;
- spatial hero treatment.

Do not make every section a “wow moment.”

### 7. Run anti-generic review

Route to `anti-generic-design` before finalizing a major direction. Replace choices justified only by trend familiarity.

### 8. Hand off to specialists

Route precise decisions to:

- `brand-design` for identity system;
- `color-intelligence` for palette/token logic;
- `typography-intelligence` for type system;
- `visual-art-direction` for imagery/asset direction;
- `motion-direction` for animation behavior;
- `ux-ui-design` for usable responsive interface structure.

## Decision rules

- Concept precedes decoration.
- Distinctiveness must remain credible to the product category.
- One strong visual thesis beats a collage of trends.
- Restraint can be more premium than ornament.
- Familiar UX patterns may coexist with distinctive visual expression.
- Avoid visual effects without product, narrative, spatial, or feedback purpose.
- The design must remain coherent when expanded beyond the hero section.
- Mobile is not a reduced desktop poster; the direction must survive re-composition.

## Reference routing

Load `references/creative-direction-framework.md` for direction construction and comparison.

Load `references/originality-evidence.md` when differentiation is weak or competitor/category similarity is a concern.

Use the shared design policy at `../../../engine/policies/design-quality.md`.

## Quality gates

- Direction is rooted in product/audience context.
- Adjectives were translated into criteria, not clichés.
- Category conventions and differentiation are explicitly separated.
- Visual grammar covers more than palette and hero styling.
- Signature moments are limited and purposeful.
- Responsive, accessibility, performance, and content scalability are feasible.
- `anti-generic-design` can explain why the result is not a stock AI composition.

## Failure handling

If the direction feels generic, return to category-code analysis before adding decoration. If brand evidence is weak, choose a credible provisional direction rather than fabricating heritage or personality. If a visually strong choice harms comprehension, preserve the concept but simplify its interface expression.

## Output contract

Return:

- creative thesis;
- audience/emotional intent;
- category codes to preserve/avoid;
- visual grammar;
- typography/color/image/motion direction;
- signature moments;
- anti-generic rationale;
- implementation/accessibility/performance constraints.
