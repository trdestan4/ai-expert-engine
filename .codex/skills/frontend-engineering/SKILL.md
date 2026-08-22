---
name: frontend-engineering
description: Owns framework-neutral production frontend implementation across semantic HTML, CSS architecture, TypeScript, component boundaries, state/data/forms, responsive behavior, error handling, accessibility baseline, performance discipline, security hygiene, and testability; React/Next-specific runtime decisions route to `react-nextjs`.
---

# Purpose

Turn approved UX/UI and product requirements into maintainable, resilient, responsive frontend code with clear state ownership, predictable data flow, complete UI states, and production-quality browser behavior.

## Use when

- implementing or reviewing frontend architecture independent of a specific framework feature;
- semantic HTML, CSS, TypeScript, components, forms, state ownership, data flow, responsive implementation, or browser-side error handling needs design;
- a design system must become reusable code/tokens/components;
- a page or feature needs production frontend quality gates;
- framework-specific code still benefits from general frontend structure and quality rules.

## Do not use when

- the main decision is React hooks/RSC/App Router/Server Actions/Next caching (`react-nextjs` owns it);
- the task is visual/UX design rather than implementation (`ux-ui-design` and creative specialists);
- the primary problem is HTTP/browser-platform semantics (`web-platform`);
- the primary task is backend/API/database/security/performance audit owned by later phases.

## Inputs

Use:

- approved user flow/layout/component behavior;
- actual content ranges and interaction states;
- repository stack/conventions;
- browser/device constraints;
- API/data contracts when available;
- accessibility/performance/security requirements;
- existing design tokens/components if present.

## Workflow

### 1. Establish frontend boundaries

Identify:

- page/route shell;
- feature modules;
- reusable UI primitives;
- domain-aware components;
- client state versus server state versus URL/form state;
- network/data adapters;
- validation/error boundaries;
- styling/tokens;
- tests.

Avoid one giant “components” layer with no ownership model.

### 2. Start from semantic structure

Use native HTML elements and browser behavior before custom abstractions. Establish heading/order landmarks, forms, buttons/links, lists, tables, dialogs, media, and labels based on meaning.

Do not use clickable generic containers when a native control expresses the action.

### 3. Implement styling as a system

Translate design decisions into:

- semantic design tokens;
- layout/container rules;
- spacing/type/color/surface roles;
- responsive rules;
- state variants;
- component contracts.

Prefer composable layout primitives and local component styles over page-specific positional hacks. Avoid arbitrary values unless they represent a deliberate one-off art-direction decision.

### 4. Design TypeScript boundaries

Use types to express valid states and public contracts, not to suppress compiler warnings. Prefer:

- narrow component props;
- discriminated unions for mutually exclusive UI states;
- schema-derived/request types where reliable;
- explicit nullable/optional semantics;
- exhaustive handling for finite states.

Do not use `any` as a routine escape hatch or mirror server objects blindly into UI props.

### 5. Assign state to the smallest correct owner

Classify state before choosing a library:

- ephemeral interaction state → local component;
- shareable/reload-stable navigation state → URL;
- remote authoritative data → server-state/data layer;
- form draft/validation → form state;
- cross-feature durable client state → shared store only when justified.

Do not promote state globally because two components currently need it.

### 6. Design data flow

Keep fetching/mutation concerns separate from presentation where it improves testability. Define:

- loading strategy;
- empty state;
- stale/refetch behavior;
- optimistic behavior only when recovery is clear;
- mutation pending/success/error states;
- cancellation/race behavior when relevant.

Avoid duplicate sources of truth between cache, component state, URL, and form state.

### 7. Build forms as workflows

Define field semantics, client validation for usability, authoritative server validation, pending/submission behavior, field/form errors, success/recovery, keyboard flow, autofill, and preservation of user input after recoverable failure.

Never rely on placeholder-only labels or client-side validation as a trust boundary.

### 8. Implement responsive behavior intentionally

Translate design breakpoints into behavioral changes rather than device labels. Decide what reflows, wraps, reorders, collapses, becomes scrollable, changes control type, or moves behind progressive disclosure.

Test narrow widths, long text, localization expansion, large text, empty/dense data, and touch input—not only one desktop and one phone viewport.

### 9. Complete states and failure paths

Every meaningful async/interactive surface should account for applicable:

- initial;
- loading/pending;
- success;
- empty;
- partial;
- validation error;
- network/server error;
- permission/unauthorized;
- destructive confirmation/recovery.

Do not render blank regions for unhandled states.

### 10. Apply baseline quality

Before handoff, verify:

- semantic/accessibility baseline;
- type/lint/build correctness;
- keyboard/focus behavior;
- responsive integrity;
- no obvious secret/token exposure;
- no avoidable render/fetch waterfalls introduced by structure;
- test coverage at the changed boundary.

Deeper security/performance/accessibility audits belong to later specialist phases.

## Decision rules

- Use native semantics first; custom behavior must justify replacing them.
- Component boundaries should follow behavior/ownership, not arbitrary file-size rules.
- Prefer composition over configuration-heavy “god components.”
- Keep presentation components ignorant of transport details when practical.
- URL is state when users reasonably expect sharing, reload persistence, or back/forward behavior.
- Derived values should usually be derived, not synchronized through effects/state.
- A design token should encode role/decision, not merely rename a hex or pixel value.
- Mobile behavior must be explicitly designed; `display:none` is not a responsive strategy for essential content.
- Client validation improves feedback; server validation establishes trust.
- Optimize measured bottlenecks, but avoid structural anti-patterns that obviously create waterfalls or huge bundles.

## Reference routing

Load `references/semantic-css-system.md` for semantic HTML, CSS architecture, layout, tokens, and design-system implementation.

Load `references/state-data-forms.md` for state ownership, server/client data, forms, validation, mutations, and error state design.

Load `references/responsive-component-engineering.md` for component boundaries, responsive behavior, content resilience, and reusable APIs.

Load `references/frontend-quality-baseline.md` before substantial frontend completion/review.

Use `react-nextjs` for framework/runtime-specific implementation. Use Phase 01 creative skills only when implementation reveals an unresolved design decision rather than silently redesigning it.

## Quality gates

- Semantics match interaction meaning.
- Component/module ownership is clear.
- State has one authoritative owner.
- Async and form states are complete.
- Type boundaries represent valid UI states.
- Responsive behavior survives content/input variation.
- Tokens/components preserve the approved design system without brittle duplication.
- Accessibility, security, performance, and testing baselines are addressed at the implementation boundary.
- Framework-specific decisions are routed rather than generalized incorrectly.

## Failure handling

If approved design cannot be implemented accessibly/responsively, preserve the product/creative intent and return the specific constraint to `ux-ui-design` instead of shipping a brittle approximation. If state/data requirements are ambiguous, identify the authoritative source before adding a store/cache. If framework behavior causes the conflict, hand the proven issue to `react-nextjs` or `web-platform`.

## Output contract

Return:

- frontend/module/component structure;
- semantic and styling approach;
- state/data/form ownership;
- responsive and interaction behavior;
- important edge/failure states;
- implementation constraints and decisions;
- verification performed and unresolved specialist reviews.
