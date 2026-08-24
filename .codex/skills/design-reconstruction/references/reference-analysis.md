# Reference Analysis and Measurement

Treat a visual reference as evidence, not source code. Start by recording the source type, capture date if relevant, viewport width/height, device-pixel ratio when known, scroll position, theme, locale, authentication state, and whether fonts/media were fully loaded. A reference without these facts can still be useful, but confidence must be lower.

## Evidence classes
Use four labels consistently:
- **Observed:** directly visible or measurable in supplied/runtime evidence.
- **Derived:** calculated from multiple observed values, such as an apparent container max width inferred from two wide captures.
- **Hypothesis:** plausible implementation or breakpoint behavior not yet proven.
- **Unknown:** materially relevant information for which evidence is absent.

Do not convert a hypothesis into a fact because it is a common CSS pattern.

## Geometry recovery
Measure stable anchors first: viewport edges, page container, major columns, repeated card widths, text baselines, media bounds, and section starts. Compare normalized ratios across captures. If outer whitespace grows while content width remains stable, a max-width container is likely. If columns scale until a threshold then stack or recompose, describe the observed transition rather than inventing the exact media query.

Record spacing as families where possible. Repeated gaps may reveal a base rhythm; isolated decorative gaps should remain exceptions. Capture alignment relationships such as shared left edges, baseline alignment, optical centering, overlap, or deliberate asymmetry. Include z-order and clipping boundaries for layered compositions.

## Typography
A screenshot rarely proves an exact font. If runtime inspection or supplied design files identify the font, record it as observed. Otherwise describe class, width, contrast, x-height, weight behavior, tracking, line-height, optical size, and fallback risk. Measure line wrapping and text block width because these reveal more about layout fidelity than a guessed family name.

## Color and surfaces
Sample representative areas but account for antialiasing, transparency, gradients, color management, video, and compression. Convert samples into semantic roles: canvas, elevated surface, text-primary, text-muted, border, accent, success/error, overlay, media treatment. Do not create dozens of tokens from every sampled pixel.

## Media and art direction
Record aspect ratio, object fit, focal position, safe area, crop behavior, masking, blend/compositing, lighting/material language, and whether the asset itself changes across breakpoints. A mobile composition may require a different crop or asset, not merely a smaller desktop image.

## Motion evidence
For recordings, identify trigger, duration or scroll range, start/end transform, easing character, overlap/stagger, sticky/pin interval, and how content remains readable. Record whether motion depends on pointer, scroll velocity, hover, or page transition. When only still screenshots exist, motion is unknown.

## Multi-viewport inference
Use at least two materially different widths before asserting fluid behavior, and three or more when reconstructing a complex responsive system. Distinguish structural breakpoints from normal fluid wrapping. A breakpoint is a behavior change, not merely a width number.

## Fidelity criteria
Define what must match: hierarchy, container geometry, type scale/wrapping, media crop, component density, signature interaction, and responsive composition. Exact per-pixel comparison may be inappropriate when dynamic content, rendering engines, font rasterization, or deliberately original assets differ. `visual-qa` should use the same evidence ledger and document tolerated variation.
