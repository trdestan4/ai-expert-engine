# WCAG 2.2, Semantics, Keyboard and Focus

WCAG 2.2 is the current W3C Recommendation baseline in this reference. Aim for appropriate conformance (commonly AA for production web) where required, but treat successful user tasks as the goal rather than checklist theater. Verify current standard/jurisdiction when a claim is compliance-critical.

## Semantics

Use native HTML headings, landmarks, lists, links, buttons, tables, labels and form controls before ARIA. Custom widgets inherit keyboard/name/role/state obligations; use them only when native controls cannot meet the interaction.

“No ARIA” is better than incorrect ARIA. ARIA changes accessibility-tree semantics, not behavior. A `div role=button` still needs keyboard activation/focus and usually should just be `<button>`.

## Accessible names

Names must communicate the visible purpose and remain stable enough for speech input. Avoid hidden labels that contradict visible text. Icon-only controls need meaningful names; decorative icons should not create duplicate announcements.

## Keyboard and focus

All core functions must be keyboard-operable without traps. Keep DOM/focus order logical; avoid positive tabindex. Focus must be visible and not obscured by sticky headers/overlays. Dialogs/menus/popovers need deliberate initial focus, containment only when the pattern requires it, escape/close and restoration.

Do not move focus for routine dynamic updates unless it helps orientation. Route/page transitions may need heading/title/focus strategy depending on app model.

## Reflow and zoom

Support zoom/text resize/reflow without clipped controls, hidden content or forced two-dimensional scrolling except where genuinely necessary (e.g. complex data tables). Test 200% text/zoom and narrow equivalent viewport. Responsive breakpoints alone do not prove reflow.

## Pointer and drag

Meet applicable target-size/spacing requirements and provide alternative input for drag-only actions where needed. Hover-only information must also be available to keyboard/touch.

## Forced colors/high contrast

Test Windows forced-colors/high-contrast for custom controls, focus, icons and status. Do not rely on background images/box shadows as the only boundary/selection indicator.
