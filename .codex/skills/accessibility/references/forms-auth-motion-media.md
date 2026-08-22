# Forms, Authentication, Motion and Media Accessibility

Forms need persistent labels, programmatic associations, clear instructions and errors tied to the field and summary where useful. Preserve valid entered data after errors. Required/format expectations should not rely only on color or placeholder text.

WCAG 2.2 adds accessible-authentication criteria: avoid requiring users to solve cognitive-function tests such as remembering/transcribing passwords or puzzles without an accessible mechanism/alternative where the criterion applies. Support password managers, paste and modern authentication rather than blocking them unnecessarily.

Respect `prefers-reduced-motion` for nonessential animation and avoid motion that causes loss of context when reduced. Never make animation the only carrier of meaning. Avoid unsafe flashing.

Images need text alternatives based on purpose; decorative images should be ignored by assistive technology. Video/audio require captions/transcripts/audio description as applicable to content and conformance target.

Status, validation and async completion messages should be perceivable without stealing focus unnecessarily; use appropriate live-region/status semantics sparingly.