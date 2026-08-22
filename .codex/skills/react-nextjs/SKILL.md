---
name: react-nextjs
description: Owns React and Next.js implementation/runtime decisions across component composition, hooks, Server/Client Component boundaries, App Router, Server Actions, Route Handlers, rendering, Suspense/streaming, caching, metadata, images/fonts, hydration, bundle behavior, and framework-specific testing; it detects installed versions before applying version-sensitive patterns.
---

# Purpose

Implement React/Next.js features using the repository's actual framework version and runtime model, preserving correct server/client boundaries, predictable data flow, efficient rendering, and production-safe framework behavior.

## Use when

- React component/hook/composition behavior is the primary implementation concern;
- Next.js App Router, layouts/routes, Server Components, Client Components, Server Actions, Route Handlers, proxy/middleware, metadata, caching/revalidation, runtime, images/fonts, or deployment behavior is involved;
- hydration, Suspense, streaming, RSC serialization, or framework bundle behavior needs reasoning;
- a Next.js version change affects APIs/conventions;
- frontend engineering needs a framework-specific implementation owner.

## Do not use when

- the issue is framework-independent semantic/CSS/state structure (`frontend-engineering`);
- the root problem is HTTP/cookie/CORS/browser behavior (`web-platform`);
- the task is visual design (`ux-ui-design`/creative skills);
- backend/API/database/security architecture is the primary concern rather than Next.js's framework boundary.

## Inputs

Verify before making version-sensitive decisions:

- installed `next`, `react`, and `react-dom` versions from manifests/lockfile;
- App Router versus Pages Router and any migration state;
- relevant route/layout/component tree;
- existing caching/data-fetching conventions;
- target runtime/deployment constraints;
- framework config and TypeScript settings;
- reproduction/build output for framework-specific failures.

Repository evidence outranks remembered defaults.

## Workflow

### 1. Detect framework mode and version

Determine installed versions and whether the target uses App Router, Pages Router, or a mixed migration. Do not apply current App Router conventions blindly to legacy Pages Router code.

For version-sensitive APIs (for example async request APIs, proxy/middleware conventions, Cache Components, experimental/stable flags), confirm repository/version support before editing.

### 2. Choose the server/client boundary

Default to server-rendered/server components for content and data that do not require browser interactivity. Add a Client Component boundary only when required by:

- state/effects;
- browser-only APIs;
- event-driven client interaction;
- client-specific libraries.

Keep the client boundary as narrow as practical. Do not add `'use client'` at a high tree level just to fix one interactive child.

### 3. Design component/data composition

Prefer server-side composition when data is naturally available on the server. Avoid serializing large/unnecessary objects across the RSC boundary. Props crossing server → client must be serializable unless the framework explicitly supports the transferred value.

Use React composition to keep responsibilities local; avoid effects for values/behavior that can be derived during render or handled by events.

### 4. Choose the correct request/mutation primitive

Use framework primitives by intent:

- Server Component data read → server-side data access/fetch;
- mutation initiated by UI → Server Action when it fits the app contract;
- external/public HTTP endpoint, webhook, non-React consumer, or explicit method surface → Route Handler/API owner;
- client-side remote state → client data library only when browser-side revalidation/interactivity requires it.

Authenticate/authorize server mutations like any other server entry point. A Server Action is not trusted because it originated from your UI.

### 5. Control concurrency and waterfalls

Start independent work early and await as late as useful. Parallelize independent reads; use Suspense/streaming boundaries around meaningful independently-resolving regions rather than one global spinner.

Do not create component hierarchies that serialize independent fetches unnecessarily.

### 6. Handle caching/revalidation deliberately

Identify which cache is involved before choosing a fix. Separate:

- request-level/per-render deduplication;
- Next framework/data/cache semantics supported by the installed version;
- explicit `'use cache'` / Cache Components when available/configured;
- browser/CDN/application caches.

Define freshness from product requirements. Do not “fix” stale data by globally disabling caching without understanding the source.

### 7. Implement routing and request APIs correctly

For App Router, use route segments/layouts/special files according to the installed version. Treat `params`, `searchParams`, cookies/headers, proxy/middleware APIs as version-sensitive when the project spans recent Next versions.

Use redirects/not-found/error boundaries as control-flow primitives only according to framework semantics; do not catch and swallow framework control-flow exceptions.

### 8. Protect hydration correctness

When server and client output can differ, identify why:

- time/randomness;
- browser-only state;
- locale/environment;
- invalid HTML nesting;
- external mutation/extensions;
- unstable IDs/data.

Fix the source of mismatch. Suppress hydration warnings only for intentionally divergent, bounded content.

### 9. Use framework optimizations intentionally

Use Next image/font/script/metadata facilities when they improve correctness/performance and are supported by the version. For images, provide responsive sizing and avoid loading everything eagerly. For fonts, control subsets/weights and layout stability. For third-party scripts, choose loading strategy based on interaction and performance impact.

### 10. Verify at framework boundaries

Run the relevant type/lint/tests/build. For significant route/runtime changes verify:

- server/client compilation;
- navigation/direct load;
- action/handler behavior;
- error/not-found paths;
- cache/freshness behavior;
- hydration/console output;
- bundle/client boundary impact where material.

## Decision rules

- Installed versions and repository conventions beat generic “latest Next.js” memory.
- Server Components are not a ban on Client Components; use the smallest correct client boundary.
- Do not fetch your own Route Handler from a Server Component merely to reach server data that can be called directly.
- Server Actions are mutation entry points and require authentication, authorization, validation, and error discipline.
- Derive state during render when possible; avoid effects that only synchronize derived values.
- Independent async work should not be serialized without dependency.
- Suspense boundaries should map to useful loading/reveal units, not arbitrary component depth.
- Treat framework cache, browser cache, CDN cache, and client cache as separate until proven otherwise.
- Avoid barrel imports and unnecessary client-only libraries on hot paths when direct imports/conditional loading reduce bundle cost.
- Hydration fixes must preserve SSR correctness; `suppressHydrationWarning` is not a general repair tool.

## Reference routing

Load `references/react-component-runtime.md` for component composition, hooks/state/effects, render behavior, concurrency, and client performance patterns.

Load `references/next-app-router.md` for file conventions, RSC boundaries, routing, request APIs, Server Actions, Route Handlers, errors, and runtime selection.

Load `references/next-data-cache-rendering.md` for data flow, waterfalls, Suspense/streaming, cache/revalidation, rendering and freshness decisions.

Load `references/next-runtime-error-performance.md` for hydration, bundling, images/fonts/scripts, metadata, runtime/build and production verification.

Use `repository-intelligence` when framework version/migration state is unclear. Use `debugging` for unexplained runtime failures rather than guessing a Next-specific cause.

## Quality gates

- Installed framework/version and router mode are verified.
- Server/client boundaries are minimal and justified.
- Async work avoids unnecessary waterfalls.
- Data/mutation primitive matches the consumer and trust boundary.
- Cache/freshness behavior is explicit rather than accidental.
- RSC props/serialization and hydration are valid.
- Framework optimizations do not hide correctness/accessibility issues.
- Build/runtime/navigation/error paths are verified proportionally to the change.
- Version-sensitive APIs are not asserted without evidence.

## Failure handling

If the repository uses a framework version whose behavior is uncertain, inspect installed docs/types/config and current official guidance before editing. If the issue reduces to HTTP/browser semantics, route to `web-platform`; if it is general frontend structure, route to `frontend-engineering`. If a build passes but runtime behavior is wrong, return to `debugging` with the exact route, execution boundary, and evidence.

## Output contract

Return:

- detected React/Next/router/version context;
- server/client and data/mutation architecture;
- routing/rendering/cache decisions;
- framework-specific implementation constraints;
- performance/hydration/error considerations;
- verification performed and unresolved version-sensitive assumptions.
