# Frontend Framework Adapters

Framework-neutral frontend rules remain authoritative. Apply framework-specific patterns only after installed versions and router/build mode are verified.

## Vue / Nuxt
Keep Composition API state ownership explicit; avoid watchers as a default synchronization mechanism. In Nuxt, distinguish server/client execution, route middleware, server routes, payload hydration and cache/runtime behavior. Keep browser-only APIs behind client boundaries.

## Svelte / SvelteKit
Use stores/runes/reactivity to model ownership rather than duplicate derived state. In SvelteKit, distinguish load functions, server-only modules, form actions, endpoint handlers and client navigation. Do not leak private environment values into public modules.

## Astro
Prefer server/static HTML with islands only where interaction requires client runtime. Choose island hydration directives intentionally; do not convert a content site into a client SPA by habit. Verify adapter/runtime behavior for SSR targets.

## Remix / React Router framework mode
Treat loaders/actions, nested route boundaries, navigation state and progressive forms as first-class. Keep server-only code separate from browser bundles and preserve HTTP semantics rather than recreating them in client state.

## Vite SPA frameworks
Define server/API ownership explicitly because Vite is a build tool, not an application backend. URL state, auth/session boundaries, caching and deployment fallback routing still need deliberate architecture.

## Cross-framework quality
Across all frameworks: native semantics first, one authoritative state owner, complete async/error states, runtime validation at trust boundaries, accessible interaction, measurable performance, repository-version-aware behavior and minimal client JavaScript.
