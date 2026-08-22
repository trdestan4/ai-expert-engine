# SVG, Icons and Illustration

Use SVG when vector scalability, crisp geometry, themeability or small procedural graphics justify it. Keep a deliberate `viewBox`, predictable coordinate system and minimal groups/paths. Remove editor metadata, hidden layers, unused definitions and excessive decimals when they add no value.

SVG is executable-like markup. Sanitize untrusted SVG before browser use; reject scripts, event handlers, unsafe external references and unexpected embedded content. Do not inline third-party SVG blindly into privileged application DOM.

Icon systems require shared geometry: canvas/keyline, optical size, stroke/fill model, corner language, terminal style and baseline alignment. Avoid mixing unrelated icon libraries or stroke weights inside one interface without a deliberate reason.

Prefer simple shapes and semantic consistency over decorative detail at small sizes. Test icons at actual 16–24 px use, high-DPI screens and both light/dark surfaces. Filled/outlined variants should preserve recognizable silhouette.

Illustrations should inherit the established art direction: perspective, depth, palette, line/shadow, texture and human/brand character. A generated illustration set that changes rendering language between sections is a system failure even if each image looks attractive alone.

Do not encode important translatable copy inside paths. When SVG text is required, consider font availability, localization and accessibility. Decorative SVG should be hidden appropriately from assistive technology; meaningful diagrams require accessible labeling/description coordinated with `accessibility`.

Optimize only after visual correctness. Simplify paths and symbols while preserving curves and alignment; keep editable masters separate from optimized delivery SVGs.