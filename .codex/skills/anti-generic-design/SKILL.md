---
name: anti-generic-design
description: Detects and rejects generic AI-generated web design patterns, prestige clichés, trend stacking, weak visual rationales, and template-like composition, then prescribes context-specific alternatives without harming usability or implementation feasibility.
---

# Purpose

Act as an originality and taste gate so finished web experiences feel authored for the product rather than synthesized from familiar AI/UI tropes.

## Use when

- a new creative direction is being approved;
- a design feels “AI-made”, templated, trend-stacked, or interchangeable;
- adjectives such as premium, luxury, modern, futuristic, elegant, minimal, tech, or corporate are driving predictable visuals;
- final design review needs an originality check;
- a section/component is technically polished but visually generic.

## Do not use when

- the task is ordinary usability/accessibility review without originality concerns;
- brand/product context is missing and no meaningful differentiation judgment can be made;
- a conventional pattern is intentionally used for usability and the critique is purely novelty-seeking.

## Inputs

Use:

- product/audience goals;
- brand/creative direction;
- proposed layout, palette, typography, imagery, surfaces, and motion;
- category conventions;
- implementation constraints.

## Workflow

### 1. Identify the rationale for each dominant choice

Ask: does this choice exist because of product/brand/content, or because it is a common generated-design default?

### 2. Scan high-frequency cliché families

Look for combinations such as:

- dark navy + gold = automatic premium;
- black + serif + gold = automatic luxury;
- purple/blue gradient = automatic AI/tech;
- neon cyan on black = automatic futuristic;
- excessive glassmorphism;
- glowing gradient blobs/orbs with no concept;
- every section built from rounded floating cards;
- identical “badge + huge headline + two buttons + floating dashboard” heroes;
- random 3D chrome objects;
- generic Bento grids used without information logic;
- oversized metric cards as decorative filler;
- universal pill buttons and pill navigation;
- arbitrary radial gradients/noise textures;
- repeated reveal-on-scroll animations without hierarchy;
- logo walls/testimonials inserted as empty trust decoration;
- stock gradient icons and indistinguishable line-icon sets;
- generic “About / Services / Why us / Testimonials / CTA” rhythm with no narrative reason.

A pattern is not automatically wrong; the problem is unearned/default use.

### 3. Detect trend stacking

Flag designs combining several fashionable treatments without one governing thesis. More effects do not create more authorship.

### 4. Check composition originality

Evaluate:

- hierarchy shape;
- content pacing;
- grid rhythm;
- section transitions;
- crop/scale relationships;
- use of negative space;
- asymmetry/symmetry decisions;
- signature interaction or graphic device.

A different palette on the same template is not a new direction.

### 5. Check semantic fit

For every expressive choice, identify what it communicates and why that message is credible for the product.

### 6. Preserve useful conventions

Do not reject:

- familiar navigation;
- readable forms;
- standard ecommerce controls;
- established accessibility patterns;
- recognizable interaction affordances

merely to appear original.

Originality belongs mainly in art direction, composition, hierarchy, branded assets, content presentation, and selected interactions.

### 7. Replace, do not merely criticize

For each meaningful generic pattern, propose a replacement strategy based on:

- content/product truth;
- audience expectations;
- brand assets;
- category opportunity;
- real implementation constraints.

### 8. Assign originality status

Use:

- **Pass** — distinctive, coherent, context-earned;
- **Pass with notes** — some generic components but overall authored direction;
- **Revise** — multiple major choices rely on defaults;
- **Reject direction** — identity/composition is fundamentally template-driven.

## Decision rules

- Familiar is not the same as generic.
- Novelty that harms usability is not quality.
- One context-specific device can outperform ten decorative trends.
- “Premium” should usually emerge from proportion, restraint, type, materials/imagery, precision, service proof, and content treatment—not prestige colors alone.
- Avoid swapping one cliché for another.
- Genericness is judged at system level, not by isolated components.

## Reference routing

Load `references/ai-design-cliches.md` for detailed cliché families and diagnostic questions.

Load `references/originality-check.md` for final review scoring.

Use `creative-director` to rebuild the direction when the problem is systemic rather than local.

## Quality gates

- Dominant visual choices have context-specific rationale.
- No prestige/style adjective maps directly to a stock palette/layout.
- Trend stacking is controlled.
- At least one meaningful distinctive system/device exists where appropriate.
- Standard UX conventions are retained when they improve comprehension.
- Replacement recommendations are actionable.

## Failure handling

If there is insufficient context to judge originality, request or infer only the minimum product/brand context. If a design must follow a strict existing design system, judge originality within that constraint rather than forcing deviation. If every proposed alternative becomes more decorative, return to product content and hierarchy instead.

## Output contract

Return:

- originality status;
- strongest context-specific choices;
- generic/cliché findings with rationale;
- what conventions should remain familiar;
- replacement direction for each major issue;
- final anti-generic gate result.
