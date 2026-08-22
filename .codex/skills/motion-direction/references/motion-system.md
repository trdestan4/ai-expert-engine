# Motion System

Motion must provide feedback, communicate state, preserve spatial continuity, reveal hierarchy, orient navigation, explain a process, emphasize narrative or express a rare branded signature. If none apply, static is usually better.

## Layers

- **Micro:** control feedback/local state; immediate, low amplitude.
- **Structural:** navigation, overlay, reorder, expand/collapse, route/spatial transitions.
- **Sectional:** reveal/recomposition supporting content hierarchy.
- **Signature:** rare high-attention narrative/brand moments.

Keep surrounding UI calm around signature sequences.

## Timing and easing

Shorter for direct feedback; longer only for meaningful spatial/narrative transitions. Match easing to physical/brand character and distance. Avoid identical stagger curves on every list. Continuity matters more than decorative overshoot.

## Scroll storytelling

Default to native document flow. Sticky/pinned/parallax/horizontal sequences require narrative/spatial value and user control. Define entry, progress, exit, reverse-scroll behavior and what happens when viewport height is short. Avoid scroll-jacking, giant pinned dead zones and essential information that only exists at one animation frame.

For complex sequences, storyboard states and content beats before implementation. Decide whether CSS scroll-driven animations, Motion/GSAP or pre-rendered media is justified by browser support, control and performance; verify installed stack rather than choosing by trend.

## Spatial transitions

Use shared geometry, origin and direction to explain where content came from/went. Dialog/drawer/menu transitions should reinforce focus and hierarchy without delaying interaction. Route transitions must not disguise loading or block navigation.

## Performance

Prefer compositor-friendly transform/opacity where possible; avoid layout-triggering animation in hot loops. Bound simultaneous layers, filters, blur, masks, huge images/canvases and continuous JavaScript work. Measure on lower-end mobile. Heavy 3D/video sequences need asset/network/memory budgets and fallback behavior.

## Accessibility

`prefers-reduced-motion` is a design branch, not “set duration to 0 everywhere.” Preserve state feedback and comprehension while removing non-essential movement, parallax, large spatial travel or autoplay-like effects. Avoid vestibular triggers and flashing. Never hide required content behind animation completion.

## Mobile adaptation

Redesign complex desktop motion for touch/viewport constraints: shorten narrative, replace pinned horizontal with native vertical sequence, use alternate crops, reduce layers or choose a static signature. Do not simply scale the desktop scene.

## Motion tokens and governance

Define a small duration/easing vocabulary only where repeated. Signature sequences can use custom timing. Document purpose and reduced-motion equivalent. Review actual interaction recordings at representative devices, not only design-tool prototypes.
