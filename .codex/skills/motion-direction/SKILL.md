---
name: motion-direction
description: Defines purposeful, performant, accessible motion systems for web experiences, including transitions, scroll behavior, feedback, choreography, spatial continuity, intensity, timing, and reduced-motion behavior; it rejects decorative animation without hierarchy or product value.
---

# Purpose

Use motion to clarify hierarchy, continuity, feedback, narrative, and brand character while protecting usability, performance, and accessibility.

## Use when

- a site needs scroll storytelling, transitions, micro-interactions, or motion language;
- animation feels random, excessive, slow, or disconnected from hierarchy;
- a creative direction requires cinematic/spatial behavior;
- desktop/mobile motion behavior must be adapted;
- reduced-motion and performance rules need definition.

## Do not use when

- the issue is ordinary static layout (`ux-ui-design`);
- the whole creative direction is unresolved (`creative-director` first);
- animation implementation details are the only task (future frontend animation specialist owns code).

## Inputs

Use:

- creative/brand direction;
- information hierarchy and user flow;
- interaction types;
- device/input context;
- expected content length;
- browser/performance constraints;
- accessibility/reduced-motion requirements.

## Workflow

### 1. Assign motion jobs

Classify each proposed motion as one of:

- feedback;
- state change;
- spatial continuity;
- hierarchy/reveal;
- orientation/navigation;
- narrative emphasis;
- branded signature.

Remove motion that has no job.

### 2. Define motion character

Choose restrained properties such as:

- tempo: immediate / brisk / measured / cinematic;
- distance: micro / local / sectional / spatial;
- easing character;
- overlap/stagger behavior;
- dimensionality: flat / layered / perspective;
- continuity: cut / dissolve / transform / shared-element style.

### 3. Build intensity hierarchy

Use three levels:

- **micro** — controls and local feedback;
- **sectional** — reveal/recomposition/scroll relationships;
- **signature** — rare high-attention moments.

Signature motion must remain rare.

### 4. Design scroll behavior deliberately

Decide whether scroll should be:

- normal document flow;
- sticky narrative;
- pinned sequence;
- parallax/depth;
- horizontal segment;
- progressive transformation.

Never hijack normal scrolling or create inaccessible gesture dependence without strong reason.

### 5. Preserve reading and control

Avoid:

- delayed content needed for comprehension;
- long entrance animations on repeated elements;
- scroll-jacking;
- excessive spring/bounce;
- motion on every hover;
- perpetual ambient movement near reading/checkout/forms;
- large transforms that cause layout instability or nausea.

### 6. Define mobile adaptation

Reduce distance, layers, pinned duration, and simultaneous motion where screens/input make desktop choreography unsuitable. Mobile can use a different composition while keeping the same motion character.

### 7. Define reduced-motion behavior

Every non-essential transform/parallax/auto-motion must have a reduced-motion equivalent preserving hierarchy and state information.

### 8. Set performance constraints

Favor transform/opacity when appropriate, avoid layout-thrashing animation, limit simultaneous animated layers, and define video/canvas/3D budgets before implementation.

## Decision rules

- Motion must explain, connect, confirm, or meaningfully express.
- Scroll effects are not quality by themselves.
- The most important content should not wait on animation.
- Use continuity where state/layout changes would otherwise feel abrupt.
- Strong signature motion should be surrounded by calm UI.
- Mobile motion is adapted, not blindly scaled.
- Reduced-motion is a designed state, not “disable everything and hope.”

## Reference routing

Load `references/motion-system.md` for timing, easing, motion hierarchy, scroll patterns, performance, and reduced-motion rules.

Use `anti-generic-design` if motion is mainly generic fade-up/stagger/parallax without a concept.

## Quality gates

- Every motion pattern has a job.
- Intensity hierarchy prevents animation saturation.
- Scroll behavior preserves control and comprehension.
- Mobile adaptation is explicit.
- Reduced-motion behavior preserves information.
- Performance risk is bounded.
- Signature motion supports the creative thesis.

## Failure handling

If motion adds complexity without measurable UX/brand value, remove it. If a signature effect is too expensive or inaccessible, simplify the implementation while preserving spatial/narrative intent. If mobile cannot support the desktop sequence cleanly, redesign the sequence rather than forcing parity.

## Output contract

Return:

- motion intent/character;
- motion job map;
- micro/sectional/signature hierarchy;
- scroll/transition rules;
- timing/easing guidance;
- mobile adaptation;
- reduced-motion behavior;
- performance constraints.
