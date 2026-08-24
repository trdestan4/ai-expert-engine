# Scroll Experience, Media, and Rendering Cost

Scroll storytelling should use the page's natural scroll position as a source of progress, not replace user control. Separate three responsibilities: document/layout conditions (`creative-frontend`), motion timelines (`animation-engineering`), and 3D/shader rendering (`threejs-webgl` / `realtime-shaders`).

## Scroll structures
- **Normal flow reveal:** content enters normally; motion is optional enhancement.
- **Sticky narrative:** one visual region remains sticky while adjacent text progresses.
- **Pinned sequence:** a controlled section maps scroll range to a timeline. Keep duration proportional and provide non-pinned mobile/reduced-motion modes when needed.
- **Horizontal segment:** use only when the content relationship genuinely benefits; preserve keyboard/touch access and clear orientation.
- **Depth/parallax:** treat as a secondary spatial cue, not a requirement for reading.

Avoid wheel/touch interception that changes expected scrolling unless the product has a compelling interaction reason and an accessible alternative. Sticky/pinned sections must not trap users or create enormous dead travel on small screens.

## Stable geometry
Reserve dimensions before media loads. Scroll measurements depend on stable layout; late fonts, images, dynamic banners, or async content can invalidate trigger positions. Coordinate refresh/recalculation with `animation-engineering` only after the layout source of truth is correct.

## Image delivery
Use responsive source selection and modern codecs according to tooling/browser policy. Preserve focal point and art direction. Preload only an image proven critical to initial rendering; over-preloading competes for bandwidth. Below-fold images should usually be lazy loaded, but do not lazy-load the likely LCP image. Decode/size behavior should be verified in the real page.

## Video
Use video when time-based content contributes product/brand value. Provide a poster/fallback, explicit geometry, muted autoplay only when appropriate and allowed, pause controls where required, and a reduced-motion/static path. Consider mobile network/power costs. Do not ship a huge cinematic loop as a background merely because it looks premium.

## Compositing
Transforms and opacity are often compositor-friendly, but performance depends on layer size, count, device, filters, texture upload, and main-thread work. Avoid assuming “GPU accelerated” equals cheap. Large fixed layers, backdrop filters, masks, and video combined with 3D can exceed mobile memory/bandwidth quickly.

## Loading choreography
A creative page should not hide useful content behind a long loader waiting for every visual asset. Prioritize shell/content and progressively activate expensive effects. 3D can display a poster or lightweight state before model/texture readiness. Failed optional media should degrade without blocking navigation or purchase/contact actions.

## Responsive and reduced motion
Shorten scroll ranges, remove unnecessary pins, simplify parallax, reduce simultaneous layers, and substitute static keyframes on small devices or reduced-motion preference. Reduced motion should preserve the story and state transitions, not merely turn CSS duration to zero while leaving unusable pinned geometry.

## Evidence
For material creative pages capture performance traces or metrics on representative mobile and desktop devices, visual states at key scroll positions, reduced-motion behavior, and resize/orientation changes. Validate LCP/CLS/INP with the complete media/animation stack, not a stripped development page.
