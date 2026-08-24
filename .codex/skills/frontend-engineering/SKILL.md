---
name: frontend-engineering
description: Owns framework-neutral production frontend implementation across semantic HTML, CSS architecture, TypeScript, components, state/data/forms, responsive behavior, localization, accessibility baseline, performance discipline, security hygiene, and testability; advanced creative rendering, animation, 3D and visual-fidelity evidence route to Phase 10 specialists.
---

# Purpose
Build maintainable, resilient frontend code from approved product/UX requirements while keeping semantics, state ownership, responsive behavior, localization and failure states explicit. Remain the default frontend owner instead of sending ordinary UI work to specialist creative runtimes.

## Use when
- implementing frontend structure, semantic HTML/CSS/TypeScript, forms, state/data flow or responsive behavior;
- translating a design system into reusable components/tokens;
- internationalization, locale behavior, RTL or localization resilience affects implementation;
- Vue/Nuxt, Svelte/SvelteKit, Astro, Remix/React Router or Vite-based code needs framework-aware frontend guidance;
- a feature needs production frontend quality gates independent of one framework runtime.

## Do not use when
- React/Next.js runtime/RSC/App Router/Server Actions/Next caching is primary (`react-nextjs`);
- visual/UX design rather than implementation is primary (Phase 01 design skills);
- HTTP/browser-platform semantics are primary (`web-platform`);
- advanced authored CSS/compositing/scroll composition is the main boundary (`creative-frontend`);
- timeline/ScrollTrigger/motion runtime is primary (`animation-engineering`);
- Three.js/custom shader/DCC asset pipeline/visual regression is primary (`threejs-webgl`, `realtime-shaders`, `three-d-asset-pipeline`, `visual-qa`).

## Inputs
Use approved flows/layouts, actual content ranges, repository/framework versions, locale requirements, browser/device constraints, API/data contracts, accessibility/performance/security requirements, existing tokens/components, and any Phase 10 design/implementation contract required by signature surfaces.

## Workflow
### 1. Establish boundaries
Identify route/page shell, feature modules, reusable primitives, domain components, data adapters, form/URL/client/server state, validation/error boundaries, styling/tokens and tests. Identify any truly specialist creative boundary early without outsourcing the whole page.

### 2. Start semantic
Use native elements/browser behavior before custom abstractions. Buttons act; links navigate. Preserve landmarks, headings, labels, tables, dialogs and media semantics.

### 3. Implement styling as a system
Translate design into semantic tokens, layout/container rules, responsive behavior and state variants. Prefer logical properties where direction can change; avoid positional hacks and English-only width assumptions. Ordinary CSS remains here; Phase 10 is for advanced authored visual systems.

### 4. Make TypeScript express valid states
Use narrow props, discriminated unions, explicit nullability and schema-derived contracts where trustworthy. Runtime trust boundaries still require validation.

### 5. Assign state correctly
Local interaction → local state; shareable navigation → URL; remote authority → server-state/data layer; form draft/errors → form state; durable cross-feature state → shared store only when justified.

### 6. Design async/forms completely
Define loading, empty, stale/refetch, pending, success, failure, cancellation/races and optimistic recovery. Forms provide semantic fields, client feedback, authoritative server validation, pending/error/success recovery, autofill and input preservation.

### 7. Recompose responsively
Decide what wraps, reorders, collapses, scrolls or changes control type. Test narrow widths, touch, dense/empty states, 200% text and long/localized content. Advanced media/art-direction compositions can hand off to `creative-frontend` while retaining semantic/source-order ownership here.

### 8. Apply locale and framework adapters
Define locale authority/fallback, messages, date/number/currency/timezone presentation, pseudo-localization and RTL when relevant. Use the installed framework version/router/build mode; do not transfer React/Next assumptions into other stacks.

### 9. Integrate specialist creative runtimes safely
Keep animation/Three/canvas ownership isolated from business state. Ensure component lifecycle provides mount/unmount boundaries and semantic fallbacks. Do not let a visual library become the application state model.

### 10. Complete quality states
Verify semantic/accessibility baseline, type/lint/build, keyboard/focus, responsive/locale integrity, no client secret exposure, no obvious waterfalls, tests at changed boundary, and required Phase 10 visual/lifecycle evidence for signature surfaces.

## Decision rules
- Native semantics first.
- Component boundaries follow behavior/ownership, not arbitrary size.
- URL is state when sharing/reload/history should preserve it.
- Mobile is behavior, not `display:none` for essential content.
- Framework/version-specific claims require repository evidence.
- Ordinary frontend work stays here; specialist activation must be justified.
- A creative runtime never becomes the authority for business/data state merely because it controls visuals.

## Reference routing
Load `references/semantic-css-system.md` for semantic HTML, CSS architecture, layout, tokens and design-system implementation.
Load `references/state-data-forms.md` for state ownership, data, forms, validation, mutations and error states.
Load `references/responsive-component-engineering.md` for component boundaries, responsive behavior and content resilience.
Load `references/frontend-quality-baseline.md` before substantial completion/review.
Load `references/i18n-localization-rtl.md` when locale/RTL/date/currency/timezone is material.
Load `references/framework-adapters.md` for verified Vue/Nuxt, Svelte/SvelteKit, Astro, Remix/React Router or Vite behavior.
Use `react-nextjs` for React/Next runtime specifics; Phase 01 for unresolved design intent; Phase 10 only for advanced creative implementation/evidence boundaries.

## Quality gates
- Semantics match interaction meaning.
- State has one authoritative owner and async/form states are complete.
- Responsive behavior survives content/input variation.
- Locale/RTL behavior is deliberate when applicable.
- Tokens/components preserve approved design without brittle duplication.
- Accessibility/security/performance/testing baselines are addressed.
- Framework behavior is verified.
- Creative runtimes have isolated lifecycle/state ownership and fallbacks when present.

## Failure handling
If design cannot be implemented accessibly/responsively/localizably, preserve intent and return the constraint to design owners. If state/data authority is ambiguous, resolve it before adding stores/caches. If framework behavior is uncertain, inspect installed versions/docs. If an advanced visual implementation exceeds this boundary, route only that boundary to Phase 10 while keeping ordinary frontend ownership here.

## Output contract
Return frontend/module structure, semantics/styling, state/data/form ownership, responsive/localization behavior, relevant framework decisions, Phase 10 integration boundaries when present, failure states, verification performed and unresolved specialist reviews.
