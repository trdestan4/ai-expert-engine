# GSAP and ScrollTrigger Production Engineering

Treat GSAP as an animation runtime, not the design system. The approved motion job, hierarchy, and reduced-motion behavior come from `motion-direction`; GSAP owns deterministic execution.

## Registration and version evidence
Use the installed GSAP version and the plugins actually available to the project. Register plugins explicitly where the module setup requires it. Do not assume a plugin is included, licensed, or configured simply because an example uses it.

## Timeline structure
Use one timeline per coherent sequence with labels for semantic moments. Prefer relative positions/labels over scattered delays and independent tweens that fight over the same property. Set intentional initial state so content does not flash or remain hidden if JavaScript fails. Avoid `from()` surprises by understanding current/computed state and immediate rendering behavior.

## Component lifecycle
Animations must be scoped to their owning DOM/component. In React-like runtimes use a scope/context pattern that can revert animations created during the component lifecycle. Development remounts, route transitions, and conditional rendering must not duplicate timelines, listeners, or ScrollTriggers. Cleanup should revert only the owned work rather than globally destroying unrelated animations.

## Responsive behavior
Modern GSAP media-query orchestration can create animations only while a query matches and revert them when it stops matching. Use this to implement different desktop/mobile compositions and reduced-motion variants. Responsive changes must rebuild from clean state; do not stack a second ScrollTrigger on top of the first.

## ScrollTrigger
ScrollTrigger supports trigger positions, callbacks, vertical/horizontal behavior, scrub, pin, snap, and custom scrollers. Define start/end based on stable layout anchors. Development markers are useful for diagnosing geometry but do not belong in production.

For pinning, keep a stable wrapper/trigger structure. Animating transforms on the same element whose position is used for pin measurement can create confusing results; separate the pinned container from animated children when appropriate. Understand pin spacing and how sticky/fixed ancestors, transforms, and custom scrollers affect behavior.

Use `scrub` only when continuous progress should map to scroll. A simple reveal should usually trigger once rather than bind every frame to scroll. Use snap only when it improves navigation/meaning, not as decoration.

## Refresh and dynamic content
Scroll positions are recalculated on resize, but late font/media/layout changes and application state can still require coordinated refresh. Fix the source of unstable geometry first. Do not spam refresh on every scroll event.

## Smooth scrolling
ScrollTrigger itself does not require scroll hijacking. If another smooth-scroll system is introduced, establish a single scroll authority and integrate through documented mechanisms. Test touch, keyboard, browser navigation, focus scrolling, reduced motion, and anchor links.

## Cleanup and diagnostics
Verify route revisit, breakpoint switches, orientation changes, and removed sections. Inspect active triggers during debugging and confirm counts return to expected levels. Global `killAll()` is an emergency/application-level operation, not a substitute for correct component ownership.

## Performance
Avoid hundreds of independent triggers when a smaller architecture can express the sequence. Keep per-update callbacks light, avoid layout reads/writes in hot paths, and coordinate with `performance` when scroll effects coexist with video, filters, or WebGL. Measure on mobile hardware, not only desktop devtools.
