# Frontend Framework Adapters

Framework-neutral frontend rules remain authoritative. Verify installed framework/router/build/runtime versions before applying remembered behavior.

## Vue / Nuxt

Prefer explicit Composition API ownership and derived/computed state over watcher chains that synchronize duplicated state. Distinguish server/client execution, composables with request scope, route middleware, Nitro/server routes, payload hydration and browser-only APIs. In Nuxt, verify data-fetch/cache/runtime conventions for the installed version and deployment adapter.

Do not expose private runtime config in public/client keys. Keep SEO/meta/server rendering deliberate for content pages. For forms/mutations, preserve server-authoritative validation and progressive behavior where framework supports it.

## Svelte / SvelteKit

Use the installed reactivity model (stores/runes/etc.) deliberately; do not duplicate derived values into writable state. Distinguish universal `load`, server-only `+page.server`/`+server` logic, form actions, hooks and client navigation. Keep secrets/private env in server-only modules and verify adapter/runtime behavior.

Use form actions/progressive enhancement where it improves resilience. Streaming/data invalidation should follow actual version semantics rather than copied examples.

## Astro

Default to static/server HTML and add islands only where interaction needs client runtime. Choose hydration directives from interaction timing; `client:load` everywhere defeats the islands model. Verify server adapter/output mode for SSR routes and keep per-request state off module globals.

Content collections/MDX/integrations should be version-checked. Marketing sites should protect crawlable semantic content, asset performance and accessibility before adding interactive islands.

## Remix / React Router framework mode

Treat loaders/actions, nested routes, pending/navigation state, redirects/status/headers and progressive forms as first-class HTTP architecture. Keep server-only modules out of browser bundles. Avoid duplicating loader data into client stores unless ownership genuinely changes.

Verify whether the repository uses Remix packages or modern React Router framework mode; APIs/runtime conventions evolve.

## Vite SPA frameworks

Vite is a build/dev tool, not a backend or auth/session architecture. Define API/server ownership, deployment history fallback, base path, asset environment variables and browser storage/security explicitly. Protect deep-link routing at CDN/origin.

## Cross-framework tests

Across all frameworks verify: server/client boundary, request-scoped vs module-global state, URL state, form/error/loading states, hydration/SSR mismatch, secret leakage, semantic/accessibility behavior, production build/adapter, cache freshness and bundle/client-JS budget.

When framework-specific behavior is material, read the installed version's official docs/source before asserting a rule.
