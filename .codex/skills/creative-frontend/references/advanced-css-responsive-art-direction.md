# Advanced CSS and Responsive Art Direction

Creative CSS should remain constraint-based. Begin with normal document flow and explicit container ownership. Use Grid/Flexbox for structural relationships, intrinsic sizing for content, `min()`, `max()`, and `clamp()` for bounded fluid behavior, aspect ratios for reserved media geometry, and container queries when a component's behavior depends on available container space rather than global viewport width.

## Layered composition
Absolute positioning is appropriate for decorative or spatially authored layers when the containing block, stacking context, clipping, and fallback behavior are intentional. Keep essential reading order in the DOM. Use isolation/stacking contexts deliberately so blends, filters, and z-index do not leak across unrelated sections.

Masks, `clip-path`, gradients, pseudo-elements, blend modes, and CSS filters can create distinctive effects without canvas. Treat support and paint cost as part of the decision. Large blur/backdrop-filter regions, animated filters, and full-screen blend stacks can become expensive. `will-change` is a temporary hint, not a blanket performance setting; excessive promoted layers consume memory.

## Fluid systems
A premium responsive system usually has a small set of composition modes plus fluid values inside each mode. Scale type/spacing within safe ranges rather than mapping every viewport width to a unique layout. Prefer content-driven wrap/reflow points over device-brand breakpoints.

## Art direction
Responsive design is not desktop shrunk to mobile. Decide for each major composition:
- hierarchy that must remain dominant;
- media crop/focal point and whether a different source is required;
- elements that move, reorder, condense, or change control type;
- depth/layer count that can be removed without losing the concept;
- maximum readable text measure;
- touch/coarse-pointer behavior and hover alternatives;
- safe areas around sticky navigation and device insets.

Use `<picture>`/source selection or CMS variants when composition truly requires different imagery. Keep width/height or aspect-ratio reservations to avoid layout shift.

## Perspective and transforms
CSS 3D transforms can provide depth for card planes, type, or layered media. Define perspective at a stable ancestor and understand flattening/stacking behavior. Avoid extreme perspective or large parallax near reading content. If a scene needs real camera/occlusion/material/lighting behavior, route to `threejs-webgl` instead of simulating a 3D engine with dozens of DOM layers.

## Typography and localization
Test fluid type with actual font metrics, long strings, different scripts, and text zoom. Do not rely on character counts from English. Use logical properties for direction-sensitive spacing/alignment. Ensure decorative overlaps do not cover text when line count changes.

## Capability strategy
Use progressive enhancement. Baseline layout should work without nonessential modern effects; enhance when APIs are supported. Decide whether the support policy permits newer features rather than assuming latest-browser behavior. Feature queries can be used when needed, but a fallback should express the same hierarchy rather than an unrelated design.

## Verification
At minimum inspect narrow mobile, large mobile/small tablet, common desktop, wide desktop, zoom/reflow, and long/localized content. Check layout shift after fonts/media load, sticky boundaries, overflow, stacking contexts, clipping, pointer behavior, and any state that changes element size. `visual-qa` should capture composition modes, not only one canonical desktop screenshot.
