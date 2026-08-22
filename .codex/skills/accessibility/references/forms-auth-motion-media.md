# Forms, Authentication, Motion, Media and Complex Interaction Accessibility

## Forms and errors

Provide persistent labels, purpose/instructions before input, programmatic relationships and clear required/format hints. Associate field errors; for large forms provide an error summary that can move focus to the problem. Preserve entered values after server errors.

Do not use placeholder as the only label or color as the only error signal. Announce async validation/status only when useful; avoid noisy live regions on every keystroke.

## Authentication

Avoid cognitive-function tests that force transcription/memorization without alternatives where WCAG requirements apply. Support password managers/paste and passkey flows. MFA/recovery must remain accessible across devices/input methods; visual CAPTCHAs require accessible alternatives/provider support.

## Motion

Honor reduced-motion preferences. Remove/paraphrase large spatial travel, parallax, autoplay-like loops and vestibular effects while preserving feedback/state comprehension. Avoid flashing content. Essential information must never require watching an animation sequence.

## Media

Provide captions for prerecorded synchronized media as required, transcripts/audio description where applicable to content, accessible player controls and keyboard focus. Autoplay audio/video should be avoided or controlled. Decorative background video needs pause/reduced-motion behavior and must not reduce text readability.

## Dialog/menu/combobox

Use native elements where possible. For custom widgets follow current WAI-ARIA Authoring Practices patterns for role/state/keyboard behavior. A combobox requires much more than `role=combobox`: input/value ownership, popup relation, active option/selection and keyboard navigation must match the chosen pattern.

## Data tables

Use actual tables for tabular relationships, correct header associations and captions/context. Complex responsive alternatives must preserve row/column meaning. Sorting controls need accessible names/state; do not make an entire row a non-semantic clickable div.

## Mobile and speech

Check touch target, orientation/zoom restrictions, virtual keyboard/viewport behavior and accessible names that match visible labels for voice control. Screen-reader rotor/landmark/headings should expose useful navigation on long pages.
