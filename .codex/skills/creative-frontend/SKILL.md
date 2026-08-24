---
name: creative-frontend
description: Owns advanced visual frontend implementation beyond ordinary component styling, including modern CSS, compositing, masks, fluid layout, responsive art direction, scroll composition, layered media, progressive enhancement, and performance-aware signature effects while delegating timeline animation, 3D runtime, and shaders to their specialists.
---

# Purpose
Implement authored, high-fidelity creative web surfaces without turning the product into a fragile demo. Use the browser's native layout, CSS, media, and compositing capabilities first, then escalate only where the visual concept actually requires animation or GPU rendering.

## Use when
- a design requires advanced CSS, layered compositions, masks, clipping, blending, filters, gradients, perspective, or unusual responsive layout;
- desktop and mobile need different art direction rather than simple stacking;
- scroll sections, sticky narratives, media reveals, or cinematic page composition must be engineered;
- image/video delivery and visual effects must cooperate with Core Web Vitals and accessibility;
- a creative direction must become production frontend code while preserving maintainability.

## Do not use when
- ordinary semantic/component implementation is enough (`frontend-engineering`);
- motion timelines, ScrollTrigger, Lottie/Rive orchestration, or view-transition code are primary (`animation-engineering`);
- Three.js scene/runtime work is primary (`threejs-webgl`);
- custom shader math/pipelines are primary (`realtime-shaders`);
- creative direction is unresolved (`creative-director`).

## Inputs
Use approved design DNA/direction, repository stack, semantic component structure, content ranges, asset inventory, target browsers/devices, reduced-motion behavior, performance budget, accessibility constraints, and signature moments. Establish which effects are essential versus decorative.

## Workflow
### 1. Preserve semantics and document flow
Start from meaningful DOM and usable source order. Creative layers should enhance, not become the only representation of essential content. Keep reading/navigation functional when advanced effects are absent.

### 2. Choose the cheapest capable rendering path
Prefer normal flow/grid/flex/container queries and CSS transforms before JavaScript layout measurement. Use masks/clip-path/filter/blend/pseudo-elements deliberately. Escalate to canvas/WebGL only when CSS cannot express the concept or measured performance is better with another path.

### 3. Engineer composition as constraints
Use intrinsic sizing, `min/max/clamp`, logical properties, aspect-ratio, container queries, subgrid where support policy permits, and bounded absolute positioning for intentional overlays. Avoid viewport-specific coordinate art that collapses with real content.

### 4. Build responsive art direction
Define composition modes, not just breakpoints. Reframe media, change crop/focal point, reduce depth/layers, shorten pinned narratives, reorder proof/content, or substitute assets when mobile requires it. Preserve hierarchy and brand character.

### 5. Engineer scroll architecture
Keep native scrolling authoritative. Decide normal flow, sticky, pin-like composition, progressive reveal, horizontal segment, or depth treatment. Timeline implementation routes to `animation-engineering`; this skill owns DOM/layout conditions that make the sequence stable.

### 6. Treat media as part of layout
Use responsive image/video sources, poster frames, explicit dimensions/aspect ratios, preload only for critical assets, lazy loading for below-fold media, and crop rules from art direction. Avoid background video that damages readability or consumes budget without a role.

### 7. Control compositing and paint cost
Limit large filtered/backdrop-filtered areas, enormous transformed layers, uncontrolled `will-change`, fixed full-screen effects, and repeated paint-heavy shadows. Measure rather than assuming GPU acceleration fixes everything.

### 8. Add progressive fallbacks
Design acceptable states for unsupported APIs, data saver/low power, reduced motion, no hover, coarse pointer, slow network, missing video, and failed asset load. A signature effect may simplify while core content and action remain intact.

### 9. Verify in the real matrix
Coordinate `visual-qa`, `performance`, and `accessibility` for significant creative work. Test viewport extremes, long/localized content, zoom, actual media, touch, keyboard, and reduced motion.

## Decision rules
- Creative frontend is still product software.
- CSS/native browser features are preferred when they express the same intent with less lifecycle cost.
- Absolute positioning is allowed for authored layers, not as a substitute for layout.
- Mobile may use a different composition and media treatment.
- Scroll must remain user-controlled; do not hijack wheel/touch merely to create spectacle.
- Decorative effects must fail soft.
- Visual fidelity does not justify layout instability, unreadable text, inaccessible controls, or unbounded GPU/paint cost.

## Reference routing
Load `references/advanced-css-responsive-art-direction.md` for layout, modern CSS, compositing, masks, fluid systems, and mobile recomposition.
Load `references/scroll-experience-and-media.md` for sticky/scroll architecture, media delivery, progressive enhancement, and rendering-cost decisions.

## Quality gates
- Semantic source order and core actions work without signature effects.
- Layout is resilient to content and viewport variation.
- Mobile has an intentional art-direction mode.
- Scroll behavior preserves native control and reading.
- Media has dimensions, crop/focal, fallback, and delivery strategy.
- Compositing/paint risks are bounded and measured when material.
- Reduced-motion/unsupported-capability paths remain coherent.
- Specialist handoffs are explicit for animation, 3D, shader, performance, accessibility, and visual QA.

## Failure handling
If the approved concept requires brittle layout or unsupported capability, preserve the visual thesis with a simpler responsive expression and report the trade-off. If performance evidence contradicts the chosen effect, reduce layers/resolution/duration before adding complexity. If the layout only works with placeholder copy, return the content-resilience problem to UX/design.

## Output contract
Return DOM/layout architecture, visual-effect implementation strategy, responsive art-direction modes, scroll/media behavior, capability fallbacks, rendering/performance risks, specialist handoffs, and verification evidence.
