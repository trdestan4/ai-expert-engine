---
name: motion-direction
description: Defines purposeful, performant, accessible motion systems for web experiences, including transitions, scroll behavior, feedback, choreography, spatial continuity, intensity, timing, and reduced-motion behavior; it is the motion-design authority and hands implementation mechanics to `animation-engineering` or 3D runtime specialists.
---

# Purpose
Use motion to clarify hierarchy, continuity, feedback, narrative, and brand character while protecting usability, performance and accessibility. Define how movement should feel and why it exists; do not conflate this with library/API implementation.

## Use when
- a site needs a motion language, scroll storytelling, transitions, micro-interactions or signature choreography;
- animation feels random, excessive, slow, generic, or disconnected from hierarchy;
- a creative direction requires cinematic/spatial behavior;
- desktop/mobile motion behavior must be adapted;
- reduced-motion and performance constraints need design treatment.

## Do not use when
- the issue is ordinary static layout (`ux-ui-design`);
- the whole creative direction is unresolved (`creative-director` first);
- GSAP/ScrollTrigger/CSS/WAAPI/View Transition/Lottie/Rive implementation mechanics are the task (`animation-engineering`);
- camera/mesh/render-loop motion inside Three.js is primary (`threejs-webgl`).

## Inputs
Use creative/brand direction, information hierarchy and user flow, interaction types, device/input context, content length, browser/performance constraints, asset availability, and accessibility/reduced-motion requirements.

## Workflow
### 1. Assign motion jobs
Classify each proposed motion as feedback, state change, spatial continuity, hierarchy/reveal, orientation/navigation, narrative emphasis, or branded signature. Remove motion that has no job.

### 2. Define motion character
Choose tempo, distance, easing character, overlap/stagger, dimensionality and continuity. Describe emotional intent in a way an implementation specialist can encode rather than handing over arbitrary duration numbers without context.

### 3. Build intensity hierarchy
Use **micro**, **sectional**, and rare **signature** levels. Signature motion must remain scarce enough to retain impact.

### 4. Design choreography
Define entry/exit order, anticipation, handoff between visual anchors, whether elements move together or independently, what should remain calm, and how interaction interruption resolves. Avoid generic fade-up/stagger everywhere.

### 5. Design scroll behavior
Choose normal flow, sticky narrative, pinned sequence, parallax/depth, horizontal segment, or progressive transformation only where it improves narrative/orientation. Native scrolling remains authoritative.

### 6. Preserve reading and control
Do not delay content needed for comprehension, create gesture traps, add perpetual ambient movement near forms/checkout, or use large spatial movement merely for spectacle.

### 7. Recompose for mobile
Reduce distance, layers, pinned duration and simultaneous motion where small screens/touch make desktop choreography unsuitable. Mobile may use a different sequence while preserving the motion character.

### 8. Design reduced motion
Every non-essential spatial/parallax/auto-motion pattern gets an equivalent preserving hierarchy/state. Remove pin-only geometry and autoplay/perpetual movement that would remain problematic even at zero duration.

### 9. Hand implementation to the correct owner
`animation-engineering` implements web motion timelines/triggers/assets. `threejs-webgl` owns scene/camera/object runtime motion. `realtime-shaders` owns time-driven GPU effect code. The direction includes enough start/end/trigger/easing/intensity information for implementation without prescribing unnecessary technology.

## Decision rules
- Motion must explain, connect, confirm, orient, or meaningfully express.
- Scroll effects are not quality by themselves.
- Important content should not wait on animation.
- Strong signature motion should be surrounded by calm UI.
- Mobile motion is adapted, not blindly scaled.
- Reduced motion is a designed state, not “disable everything and hope.”
- Implementation technology follows the motion job, not the reverse.

## Reference routing
Load `references/motion-system.md` for timing, easing, choreography, intensity hierarchy, scroll patterns, performance, interruption, mobile and reduced-motion rules.
Use `anti-generic-design` if motion is mainly generic fade-up/stagger/parallax without a concept. Hand implementation to `animation-engineering` after the design contract is clear.

## Quality gates
- Every motion pattern has a job.
- Choreography and intensity hierarchy prevent animation saturation.
- Scroll behavior preserves control and comprehension.
- Mobile adaptation is explicit.
- Reduced-motion behavior preserves information and removes spatial traps.
- Performance risk is bounded at the design level.
- Signature motion supports the creative thesis.
- Implementation owner receives explicit states/triggers/relationships rather than vague adjectives.

## Failure handling
If motion adds complexity without UX/brand value, remove it. If a signature effect is too expensive/inaccessible, simplify the expression while preserving narrative intent. If mobile cannot support the desktop sequence cleanly, redesign it rather than forcing parity. If implementation constraints reveal a new motion-design decision, resolve it here rather than letting a library default decide.

## Output contract
Return motion intent/character, motion job map, micro/sectional/signature hierarchy, choreography, scroll/transition rules, timing/easing guidance, mobile adaptation, reduced-motion behavior, performance constraints, and implementation handoff owners.
