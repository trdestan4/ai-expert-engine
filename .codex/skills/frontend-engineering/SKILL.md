---
name: frontend-engineering
description: Owns framework-neutral production frontend implementation across semantic HTML, CSS architecture, TypeScript, components, state/data/forms, responsive behavior, localization, accessibility baseline, performance discipline, security hygiene, and testability; framework-specific behavior routes to verified adapters or `react-nextjs`.
---

# Purpose
Build maintainable, resilient frontend code from approved product/UX requirements while keeping semantics, state ownership, responsive behavior, localization and failure states explicit.

## Use when
- implementing frontend structure, semantic HTML/CSS/TypeScript, forms, state/data flow or responsive behavior;
- translating a design system into reusable components/tokens;
- internationalization, locale behavior, RTL or localization resilience affects implementation;
- Vue/Nuxt, Svelte/SvelteKit, Astro, Remix/React Router or Vite-based code needs framework-aware frontend guidance;
- a feature needs production frontend quality gates independent of one framework runtime.

## Do not use when
- React/Next.js runtime, RSC, App Router, Server Actions or Next caching is primary (`react-nextjs`);
- visual/UX design rather than implementation is primary (`ux-ui-design` and creative skills);
- HTTP/browser-platform semantics are primary (`web-platform`);
- formal security/performance/accessibility review is primary.

## Inputs
Use approved flows/layouts, actual content ranges, repository/framework versions, locale requirements, browser/device constraints, API/data contracts, accessibility/performance/security requirements, and existing tokens/components. Repository evidence outranks remembered framework defaults.

## Workflow
### 1. Establish boundaries
Identify route/page shell, feature modules, reusable primitives, domain components, data adapters, form/URL/client/server state, validation/error boundaries, styling/tokens and tests.

### 2. Start semantic
Use native elements and browser behavior before custom abstractions. Buttons act; links navigate. Preserve landmarks, headings, labels, tables, dialogs and media semantics.

### 3. Implement styling as a system
Translate design into semantic tokens, layout/container rules, responsive behavior and state variants. Prefer logical CSS properties where direction can change; avoid positional hacks and English-only width assumptions.

### 4. Make TypeScript express valid states
Use narrow props, discriminated unions, explicit nullability and schema-derived contracts where trustworthy. Runtime trust boundaries still require validation.

### 5. Assign state correctly
Local interaction → local state; shareable navigation → URL; remote authority → server-state/data layer; form draft/errors → form state; durable cross-feature client state → shared store only when justified. Derive values instead of effect-syncing copies.

### 6. Design data and async behavior
Define loading, empty, stale/refetch, pending, success, failure, cancellation/races and optimistic recovery. Avoid duplicate truth across cache, component, URL and form state.

### 7. Treat forms as workflows
Provide field semantics, usable client feedback, authoritative server validation, pending/error/success recovery, autofill and input preservation. Client validation is not a trust boundary.

### 8. Recompose responsively
Decide what wraps, reorders, collapses, scrolls or changes control type. Test narrow widths, touch, dense/empty states, 200% text and long/localized content.

### 9. Make locale behavior explicit when applicable
Define locale authority/routing/fallback, message formatting, date/number/currency/timezone presentation, pseudo-localization and RTL behavior. Coordinate localized metadata/URLs with `seo` and formal accessibility concerns with `accessibility`.

### 10. Apply the verified framework adapter
Use the installed framework version/router/build mode. Do not transfer React/Next assumptions into Nuxt, SvelteKit, Astro or Remix. Keep server/client/private-public boundaries native to the selected framework.

### 11. Complete quality states
Verify semantic/accessibility baseline, type/lint/build correctness, keyboard/focus, responsive and locale integrity, no client secret exposure, no obvious fetch/render waterfalls, and tests at the changed boundary.

## Decision rules
- Native semantics first.
- Component boundaries follow behavior/ownership, not arbitrary size.
- Composition beats configuration-heavy god components.
- URL is state when sharing/reload/history should preserve it.
- Mobile is behavior, not `display:none` for essential content.
- Locale, timezone and currency are separate concepts.
- Do not concatenate translated sentence fragments or assume left-to-right physical layout.
- Framework/version-specific claims require repository evidence.
- Optimize measured bottlenecks without introducing obvious structural waste.

## Reference routing
Load `references/semantic-css-system.md` for semantic HTML, CSS architecture, layout, tokens and design-system implementation.
Load `references/state-data-forms.md` for state ownership, data, forms, validation, mutations and error states.
Load `references/responsive-component-engineering.md` for component boundaries, responsive behavior and content resilience.
Load `references/frontend-quality-baseline.md` before substantial completion/review.
Load `references/i18n-localization-rtl.md` when locale routing, translations, RTL, date/currency/timezone or multilingual resilience is material.
Load `references/framework-adapters.md` for verified Vue/Nuxt, Svelte/SvelteKit, Astro, Remix/React Router or Vite framework behavior.
Use `react-nextjs` for React/Next runtime-specific implementation; use Phase 01 skills when implementation exposes an unresolved design decision.

## Quality gates
- Semantics match interaction meaning.
- State has one authoritative owner and async/form states are complete.
- Responsive behavior survives content/input variation.
- Locale/RTL behavior is deliberate when multilingual scope exists.
- Tokens/components preserve the approved design without brittle duplication.
- Accessibility, security, performance and testing baselines are addressed.
- Framework-specific behavior is verified and routed correctly.

## Failure handling
If design cannot be implemented accessibly/responsively/localizably, preserve intent and return the constraint to `ux-ui-design` instead of shipping a brittle approximation. If state/data authority is ambiguous, resolve it before adding stores/caches. If framework behavior is uncertain, inspect installed versions/docs rather than generalizing from another framework.

## Output contract
Return frontend/module structure, semantics/styling, state/data/form ownership, responsive/localization behavior, relevant framework decisions, failure states, verification performed and unresolved specialist reviews.
