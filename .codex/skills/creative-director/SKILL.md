---
name: creative-director
description: Converts product and brand context into a distinctive, coherent creative direction for web experiences across layout, composition, visual language, imagery, typography, color, motion, and emotional tone; it coordinates creative and Creative Engineering specialists without replacing their implementation expertise.
---

# Purpose
Create a project-specific art and experience direction that feels intentionally designed rather than assembled from fashionable AI/UI patterns, then hand technically ambitious moments to the correct Phase 10 specialist without turning technology into the concept.

## Use when
- a site needs a new or materially revised visual direction;
- the request contains goals such as premium, elegant, bold, trustworthy, editorial, playful, technical, calm, spatial or cinematic;
- design/creative-engineering specialists need one coherent north star;
- multiple visual directions are plausible and must be evaluated;
- the existing design feels generic, inconsistent or trend-chasing.

## Do not use when
- the creative direction is locked and only implementation is needed;
- only palette/type/motion behavior is needed (use the narrow Phase 01 specialist);
- a reference merely needs evidence reconstruction (`design-reconstruction`);
- GSAP/Three/shader implementation is the task (Phase 10 owner);
- product goals are unresolved (`product-strategy` first).

## Inputs
Use product outcome/audience, brand position/personality, content/product characteristics, category conventions, emotional qualities, references where authorized, asset availability, accessibility/performance constraints, implementation stack and content volume.

## Workflow
### 1. Translate adjectives into criteria
Never map “premium/luxury/modern/cinematic” directly to black-gold, glass, gradients, 3D, parallax or other clichés. Define what the adjective means for this audience/product.

### 2. Identify category codes
Separate expected codes for trust/comprehension, overused codes causing sameness, and ownable opportunities the brand can credibly use.

### 3. Generate direction hypotheses when needed
Each direction specifies strategic idea, emotional tone, composition, type, color, imagery/material language, surface geometry, motion character, differentiation, signature moments, responsive behavior and execution risks. Directions differ conceptually, not merely by palette.

### 4. Choose one direction
Evaluate product outcome, audience trust, brand credibility, differentiation, content scalability, responsive behavior, accessibility/performance feasibility, asset cost and implementation realism.

### 5. Define visual grammar
Set density/whitespace, grid, hierarchy, geometry, surface/material treatment, image cropping, typography roles, palette roles, icon/illustration character, and motion intensity.

### 6. Define 1–3 signature moments
Examples include product reveal, spatial hero, scroll narrative, navigation transition, interactive comparison or editorial product grid. Each moment must have a narrative/product job and a fallback concept. Do not make every section a demo.

### 7. Validate originality
Route to `anti-generic-design` before finalizing major direction. Replace choices justified only by trend familiarity.

### 8. Hand off by design/engineering boundary
Use `brand-design`, `color-intelligence`, `typography-intelligence`, `visual-art-direction`, `motion-direction`, and `ux-ui-design` for detailed design systems. Use `design-reconstruction` for evidence extraction, `creative-frontend` for advanced CSS/composition, `animation-engineering` for motion runtime, `threejs-webgl` for browser 3D, `realtime-shaders` for custom GPU effects, `three-d-asset-pipeline` for DCC→web 3D assets, and `visual-qa` for fidelity evidence.

## Decision rules
- Concept precedes decoration and technology.
- Distinctiveness must remain credible to the product category.
- One strong visual thesis beats a collage of trends.
- Familiar UX patterns may coexist with distinctive expression.
- A 3D/shader/GSAP effect is not a direction by itself.
- Signature moments must have responsive, reduced-motion, capability and performance fallback thinking.
- Mobile is recomposed, not reduced to a desktop poster.

## Reference routing
Load `references/creative-direction-framework.md` for direction construction and comparison.
Load `references/originality-evidence.md` when differentiation is weak or competitor/category similarity is a concern.
Use the shared design policy at `../../../engine/policies/design-quality.md` and Phase 10 creative-engineering policy when implementation crosses those boundaries.

## Quality gates
- Direction is rooted in product/audience context.
- Adjectives became criteria, not clichés.
- Category convention and differentiation are separated.
- Visual grammar covers more than palette/hero styling.
- Signature moments are limited, purposeful and feasible.
- Responsive/accessibility/performance/content scalability are credible.
- Phase 10 handoffs are activated only for real specialist boundaries.
- `anti-generic-design` can explain why the result is not a stock AI composition.

## Failure handling
If the direction feels generic, return to category-code analysis before decoration. If brand evidence is weak, choose a credible provisional direction rather than inventing heritage. If a visually strong choice harms comprehension or exceeds realistic budgets, preserve the thesis with a simpler expression. If a technology starts driving arbitrary design decisions, return ownership to creative/motion intent.

## Output contract
Return creative thesis, audience/emotional intent, category codes, visual grammar, type/color/image/motion direction, signature moments, anti-generic rationale, Phase 10 handoffs, responsive/reduced-motion/fallback intent, and implementation/accessibility/performance constraints.
