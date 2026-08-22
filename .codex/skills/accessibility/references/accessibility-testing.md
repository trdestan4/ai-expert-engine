# Accessibility Testing and Assistive Technology

Automation cannot prove accessibility. Use layered evidence.

## Automated checks

Run semantic/contrast/name/ARIA-rule tools in CI or component tests where useful. Treat violations as defects but review false positives/context. Automated tools miss focus order, meaningful names, cognitive clarity, screen-reader interaction, voice control and many custom-widget failures.

## Keyboard pass

Test every critical flow with keyboard only: entry, skip/navigation, controls, dialogs/menus, validation/errors, dynamic content, destructive confirmation and exit. Verify visible focus, logical order, no traps and restoration.

## Screen reader

Use targeted combinations appropriate to support policy—commonly VoiceOver/Safari on Apple platforms and NVDA/Firefox or Chrome on Windows. Test headings/landmarks, form names/descriptions/errors, tables, dialogs, menus/comboboxes and dynamic status. Do not expect identical speech across AT/browser pairs; verify task success and correct semantics.

## Other modalities

For products/audiences that warrant it, test Windows forced-colors, magnification/zoom, speech input/voice control, switch/keyboard-only navigation and mobile screen readers. Cognitive accessibility review should inspect language, consistency, error prevention, time limits and memory burden.

## Test matrix

Select critical flows × interaction modalities × representative viewport/locale/state. Include long text, 200% zoom/reflow, reduced motion and error/empty/loading states. Do not mechanically test every page if shared components and representative flows give stronger evidence.

## Regression

Add automated regression for specific bugs when possible (accessible name, focus return, keyboard handling, error association). Complex AT behavior may require documented manual verification in release evidence. A green automated accessibility scan never means “WCAG complete.”
