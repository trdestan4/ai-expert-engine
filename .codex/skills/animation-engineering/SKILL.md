---
name: animation-engineering
description: Implements production web motion from an approved motion system using GSAP and ScrollTrigger, CSS/WAAPI, View Transitions, SVG, Lottie, Rive, or framework adapters with deterministic timelines, lifecycle cleanup, responsive/reduced-motion variants, scroll stability, and testable state ownership.
---

# Purpose
Turn motion direction into reliable code. Own timeline/trigger mechanics, animation lifecycle, responsive setup/teardown, and integration with component/router state while preserving native scrolling, accessibility, and performance.

## Use when
- GSAP timelines, ScrollTrigger, scrub/pin/snap, stagger, SVG, FLIP-like continuity, or complex sequencing are being implemented;
- CSS/WAAPI or View Transitions need orchestration beyond ordinary styling;
- Lottie/Rive/motion assets must be driven by UI or scroll state;
- animation leaks, duplicate triggers, resize problems, hydration issues, or component cleanup must be fixed;
- motion behavior differs by viewport, input capability, or reduced-motion preference.

## Do not use when
- the motion concept/timing hierarchy is unresolved (`motion-direction` first);
- only static creative layout is needed (`creative-frontend`);
- the animation is primarily a Three.js render loop/camera/scene concern (`threejs-webgl`);
- the core effect is custom shader math (`realtime-shaders`).

## Inputs
Use the motion job map, start/end states, timing/easing character, scroll ranges, responsive variants, reduced-motion behavior, component/router lifecycle, actual DOM geometry, target browsers, and performance constraints. Inspect installed library versions before API-specific claims.

## Workflow
### 1. Choose the simplest capable runtime
Use CSS transitions/keyframes for local state where sufficient; WAAPI when imperative browser animation fits; View Transitions for supported state/navigation continuity; GSAP for complex sequencing/scroll choreography; Lottie/Rive for authored assets/state machines. Avoid multiple animation authorities controlling the same property.

### 2. Define ownership and lifecycle
Every timeline/trigger belongs to a component/page scope with explicit creation, refresh conditions, and cleanup/revert. In framework environments, account for mount/unmount, development double invocation, route changes, suspense/loading, and DOM replacement.

### 3. Build deterministic timelines
Prefer named labels and explicit relationships over chains of magic delays. Separate state transitions from scroll-progress timelines. Use transforms/opacity where appropriate but animate the property that best represents the interaction, not a blanket rule.

### 4. Engineer ScrollTrigger deliberately
Define trigger, start/end, pin/scrub/snap only when the motion direction requires them. Keep pinned geometry stable, understand pin spacing, and refresh after legitimate layout changes. Do not animate the pinned element in ways that invalidate its measured position without a deliberate structure.

### 5. Implement responsive variants
Use runtime/media-query mechanisms that create and revert the right animations per composition mode. Mobile may replace a pinned desktop narrative with shorter reveals. Avoid accumulating triggers when breakpoints change.

### 6. Implement reduced motion as a variant
Remove large spatial travel, parallax, perpetual motion, and long scroll-mapped sequences while preserving state feedback and content order. A reduced-motion route must also remove unnecessary pinned/hidden states.

### 7. Integrate authored motion assets
For Lottie/Rive/SVG, control loading, state/event ownership, canvas/SVG sizing, offscreen behavior, loop policy, and fallback/poster. Do not autoplay decorative motion indefinitely near reading or forms.

### 8. Verify cleanup and stability
Test route revisit, resize, orientation, content changes, fast scroll, back/forward navigation, reduced-motion toggles when practical, and component teardown. Inspect for duplicate listeners/triggers and long tasks.

## Decision rules
- Motion design and motion implementation are separate ownership boundaries.
- One property should have one clear animation authority at a time.
- Native scrolling remains authoritative unless an explicit product requirement says otherwise.
- Responsive setup must be reversible, not layered repeatedly.
- Cleanup is part of correctness.
- Timeline complexity must correspond to user/brand value.
- Version-sensitive GSAP/framework APIs must be verified from installed versions and current official docs.

## Reference routing
Load `references/gsap-scrolltrigger-production.md` for GSAP lifecycle, timelines, ScrollTrigger, responsive setup, cleanup, and common production failures.
Load `references/web-motion-runtimes.md` for CSS/WAAPI/View Transitions, SVG, Lottie, Rive, framework integration, reduced motion, and runtime selection.

## Quality gates
- Motion implements an approved job/hierarchy from `motion-direction`.
- Timeline/trigger ownership and cleanup are explicit.
- Scroll geometry remains stable across load/resize/content changes.
- Responsive variants revert cleanly.
- Reduced-motion state preserves content and interaction.
- Route revisit does not duplicate animations/listeners.
- Authored motion assets have loading/offscreen/fallback policy.
- Performance and visual QA evidence exists for signature sequences.

## Failure handling
If a requested effect requires scroll-jacking or brittle geometry, return the constraint to motion/creative direction and preserve the intent with a safer sequence. If lifecycle duplication occurs, fix ownership/cleanup rather than hiding symptoms with global kill calls. If an animation library feature is version-dependent, inspect the installed version before choosing an API.

## Output contract
Return runtime choice, timeline/trigger structure, component lifecycle and cleanup, responsive/reduced-motion variants, asset integration, scroll geometry assumptions, verification performed, and unresolved performance/accessibility/visual-QA risks.
