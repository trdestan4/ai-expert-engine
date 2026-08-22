# WCAG 2.2, Semantics, Keyboard and Focus

WCAG 2.2 is the current W3C Recommendation and preferred baseline for new work unless a product/jurisdiction specifies otherwise. Aim for AA for normal production web experiences where feasible, while treating actual user task accessibility as the goal rather than checklist theater.

Use semantic HTML headings, landmarks, lists, buttons, links, tables and form controls before ARIA. Custom widgets must implement expected roles/states/keyboard behavior and should be avoided when a native control fits.

All interactive functions must work from keyboard. Keep DOM/focus order logical and avoid positive tabindex. Provide visible focus and ensure sticky headers/overlays do not obscure focused elements; WCAG 2.2 adds explicit focus-not-obscured criteria.

Support reflow/zoom without losing content/function. Ensure pointer targets meet applicable minimum-size/spacing expectations or provide equivalent alternatives. Drag-only actions need an alternative input method.

Use meaningful page titles, heading hierarchy, skip/landmark navigation and predictable focus restoration for dialogs and major context changes.