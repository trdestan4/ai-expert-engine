---
name: accessibility
description: Owns accessible web interaction and WCAG-aligned engineering across semantics, keyboard/focus, screen readers, forms/authentication, contrast, target size, motion, media, responsive zoom/reflow, accessible component patterns, and conformance testing; it complements visual design and frontend implementation.
---

# Purpose

Make interfaces perceivable, operable, understandable and robust for users with disabilities by embedding accessibility into design, components, interaction and verification.

## Use when

- UI components, navigation, forms, authentication, dialogs, tables, drag/drop, media or custom interactions are created/reviewed;
- WCAG conformance, keyboard/screen-reader behavior, focus, contrast or motion needs verification;
- design/frontend work may affect accessibility;
- accessibility regressions or audit findings must be fixed.

## Do not use when

- the task is purely visual art direction with no interaction/output impact (`creative-director`);
- general frontend architecture is primary (`frontend-engineering`, then accessibility review);
- legal accessibility obligations by jurisdiction require current legal interpretation; verify authoritative requirements separately.

## Inputs

Inspect:

- supported user journeys and critical tasks;
- semantic DOM/component implementation;
- keyboard/focus flow;
- labels, names, descriptions and errors;
- color/contrast and non-color cues;
- motion/animation behavior;
- responsive zoom/reflow and touch targets;
- media alternatives/captions/transcripts;
- automated and manual accessibility results;
- target conformance level and jurisdiction/product requirements.

## Workflow

### 1. Prefer native semantics

Use native HTML controls/elements when they express the intended behavior. Add ARIA only where semantics are missing; incorrect ARIA can reduce accessibility.

### 2. Verify keyboard operation

Every interactive function must be reachable and usable by keyboard with logical order and visible focus. Avoid keyboard traps and custom interactions without equivalent keyboard behavior.

### 3. Manage focus intentionally

For dialogs, route changes, errors, dynamic content and menus, move/restore focus only when it reflects user context. Ensure sticky/fixed UI does not obscure focused elements.

### 4. Provide accessible names and states

Controls require stable accessible names; state/role/value must be exposed. Do not use placeholder text or icons alone as required labeling.

### 5. Make forms/auth accessible

Associate labels/instructions/errors, identify fields programmatically, preserve entered data when possible, and avoid authentication tasks that require cognitive-function tests without an accessible alternative where WCAG applies.

### 6. Support perception and reflow

Meet contrast requirements, do not rely only on color, support text zoom/reflow, respect reduced-motion preferences and avoid content that flashes unsafely. Ensure touch/pointer targets and alternatives to dragging meet applicable criteria.

### 7. Make media/data usable

Provide appropriate text alternatives, captions/transcripts, meaningful headings/landmarks, table relationships and status announcements for dynamic updates.

### 8. Test with multiple methods

Automated tools catch only part of accessibility. Combine semantic/axe-like automation with keyboard testing, zoom/reflow, focus inspection and screen-reader checks on critical journeys.

### 9. Gate important regressions

Critical inaccessible authentication, navigation, form submission or core task blockers are release issues, not cosmetic backlog items.

## Decision rules

- Target WCAG 2.2 where practical/current; W3C recommends the latest WCAG version.
- Native semantic elements beat custom ARIA recreations when behavior matches.
- `tabindex` positive values are usually a smell; fix DOM/order instead.
- Focus must be visible and not obscured.
- Information conveyed by color needs another cue.
- Reduced motion should preserve meaning/function while removing unnecessary motion.
- Automated accessibility scores cannot prove conformance.
- Accessibility and visual polish are not opposites; redesign when needed rather than hiding semantics.

## Reference routing

Load `references/wcag22-semantics-focus.md` for WCAG 2.2 structure, semantics, keyboard, focus, target size and reflow.
Load `references/forms-auth-motion-media.md` for forms, accessible authentication, errors, motion and media.
Load `references/accessibility-testing.md` for automated/manual assistive-technology testing and regression gates.

Use `ux-ui-design` for visual/interaction direction and `frontend-engineering`/`react-nextjs` for implementation ownership.

## Quality gates

- Critical journeys are fully keyboard operable.
- Focus order/visibility/restore behavior is intentional.
- Controls have correct semantic roles, names, states and labels.
- Form errors/instructions are programmatically associated and understandable.
- Contrast/non-color cues/reflow/zoom/motion requirements are addressed.
- Critical dynamic updates are perceivable to assistive technology.
- Automated plus manual tests cover important journeys.
- Known critical accessibility blockers prevent release unless explicitly accepted by an accountable owner.

## Failure handling

If custom UI cannot meet native-equivalent accessibility reliably, simplify or replace it with a proven accessible pattern. If conformance depends on jurisdiction/product policy, verify the current requirement rather than guessing. If automated and manual results disagree, reproduce with DOM/accessibility-tree and assistive-technology evidence.

## Output contract

Return:

- accessibility findings by severity;
- WCAG/pattern rationale where relevant;
- required design/implementation changes;
- keyboard/focus/assistive-technology tests;
- release blockers and residual gaps.