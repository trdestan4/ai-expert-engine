# Web Motion Runtime Selection

Choose the runtime by interaction semantics and lifecycle cost.

## CSS transitions and keyframes
Use CSS for local state changes, hover/focus feedback, simple entrances, and looping effects that truly need no JavaScript coordination. Keep essential content visible without animation. Prefer custom properties/tokens for shared duration/easing where the design system benefits.

## Web Animations API
WAAPI is useful when JavaScript must create/control browser-native animations, inspect playback state, or coordinate dynamic keyframes without a larger timeline engine. Own and cancel animations with the component lifecycle. Avoid mixing CSS and WAAPI on the same property unless precedence is deliberate.

## View Transitions
The View Transition API can preserve visual continuity between DOM states and, with appropriate browser support/policy, navigation. Treat transition names and snapshot layers as part of state/navigation architecture. Maintain focus, reading position, and accessibility semantics; do not keep duplicate interactive DOM alive merely for visuals. Feature-detect and provide a normal non-transition navigation/state update.

## SVG
SVG is strong for vector morphs, path drawing, masks, icon choreography, and illustrations. Normalize viewBox and path geometry where morphing requires compatible shapes. Large filters/path complexity can be expensive. Keep semantic text as HTML when it must localize, reflow, or remain searchable.

## Lottie
Lottie is an authored animation asset, not a universal UI runtime. Establish renderer choice, intrinsic dimensions, loading/error state, loop/autoplay policy, offscreen pause, and reduced-motion/static fallback. Avoid shipping large JSON/raster payloads for a tiny effect that CSS/SVG can express more cheaply.

## Rive
Rive is valuable when an authored interactive asset/state machine owns meaningful internal states. Define inputs/events and which application state drives them. Keep application business state outside the animation file. Size canvas/runtime correctly, unload when no longer needed, and provide accessible external controls/fallbacks.

## Framework adapters
Motion libraries that integrate with React/Vue/Svelte can be appropriate for component enter/exit/layout continuity. The same rules apply: one owner per property, explicit lifecycle, deterministic state, responsive/reduced-motion variant, and no library choice merely because it is familiar.

## Easing and time
Implementation should consume the motion-direction system. Micro feedback is usually brief; narrative/signature motion may be longer but must not delay required action. Use physically motivated springs only when their overshoot/settling supports the interaction; avoid default springiness across every element.

## Reduced motion
Use media-query/runtime preference as an input to composition. Replace spatial travel/parallax with opacity or immediate state when needed, remove autoplay/perpetual movement, and eliminate pinned geometry that exists only for animation. Essential status feedback may remain with lower intensity.

## Testing
Test interrupted transitions, rapid repeated actions, back/forward navigation, route changes, hidden tabs, resize, reduced-motion, slow asset loading, and focus/keyboard behavior. A visually smooth demo is not production proof if state becomes inconsistent under interruption.
