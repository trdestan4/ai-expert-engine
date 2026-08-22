---
name: web-platform
description: Owns framework-independent browser and web-platform behavior across HTTP semantics, URLs, headers, cookies, CORS, browser APIs, navigation, storage, caching, service workers, delivery boundaries, and runtime constraints; it explains platform behavior but routes framework implementation, security policy, and infrastructure ownership elsewhere.
---

# Purpose

Provide reliable browser/network/runtime reasoning beneath every web framework so implementation decisions are based on how the web actually behaves rather than framework folklore.

## Use when

- behavior depends on HTTP methods/status/headers, redirects, content negotiation, caching, cookies, origins, CORS, URL/history semantics, browser storage, events, service workers, or browser capability;
- a frontend/backend boundary is unclear before framework-specific code is chosen;
- SSR/CSR/navigation behavior depends on browser versus server execution;
- a cross-browser/platform limitation affects architecture;
- another skill needs a framework-neutral explanation of the web contract.

## Do not use when

- the task is ordinary React/Next.js implementation (`react-nextjs` owns framework-specific behavior);
- the task is general component/state/CSS/TypeScript engineering (`frontend-engineering`);
- the task is defining security policy or performing a vulnerability review (future `security` owns that, though this skill can explain browser mechanisms);
- CDN, DNS, TLS termination, reverse proxies, or production hosting are the primary operational task (future production/DevOps skills own them);
- API resource/business contract design is the primary task (future `api-engineering`).

## Inputs

Establish only relevant facts:

- browser/client versus server execution context;
- request URL/origin and navigation mode;
- method/status/headers/cookie attributes when applicable;
- cache/storage layer involved;
- installed framework/runtime only when it changes the platform boundary;
- reproduction evidence for cross-browser/runtime issues.

## Workflow

### 1. Identify the boundary

Classify the issue as one or more of:

- URL/navigation;
- request/response;
- origin/cookie/session transport;
- browser state/storage;
- DOM/event/lifecycle;
- cache/revalidation;
- service worker/offline;
- server/browser execution boundary;
- capability/compatibility.

Do not start with framework code until the platform boundary is clear.

### 2. Define the observable contract

State what the browser, server, intermediary, or cache receives and what each is expected to do. Prefer concrete request/response/state transitions over vague statements such as “the browser blocks it.”

### 3. Reason from standards-level semantics

Use the actual mechanism:

- safe/idempotent method semantics where relevant;
- status and redirect behavior;
- request/response headers;
- origin versus site distinction;
- cookie scope and attributes;
- preflight and CORS response requirements;
- cache freshness/validation/vary behavior;
- navigation/history behavior;
- storage lifetime/scope;
- event propagation/lifecycle;
- execution environment availability.

Do not invent browser behavior from memory when repository/runtime evidence can resolve it.

### 4. Separate transport, identity, and authorization

A cookie being sent, a session being recognized, and a user being authorized are different facts. Likewise, CORS is not authentication and same-origin restrictions are not a server-side authorization boundary.

### 5. Separate browser cache layers

Distinguish where relevant:

- memory/disk HTTP cache;
- framework/data cache;
- service worker cache;
- CDN/shared cache;
- application state cache.

Do not prescribe invalidation before identifying which layer owns stale data.

### 6. Handle server/browser execution explicitly

Before using DOM, storage, window, document, media, observer, clipboard, or similar APIs, establish whether execution occurs in a browser context and whether capability detection or deferred access is required.

### 7. Design progressive behavior

For optional browser capabilities, define a baseline path first. Enhance only when support is available. Do not make core navigation/content dependent on fragile optional APIs unless the product requirement justifies it.

### 8. Route implementation to the correct owner

Once the platform mechanism is proven, hand framework implementation to `react-nextjs` or general code structure to `frontend-engineering`. Route security policy, performance audit, or deployment configuration to their owning phases.

## Decision rules

- Distinguish **origin** from **site** before diagnosing CORS/cookie behavior.
- CORS controls browser-readable cross-origin responses; it is not a substitute for server authorization.
- Prefer server-controlled HTTP-only credentials for sensitive session tokens when the identity architecture calls for cookies; do not prescribe storage policy here without the auth/security owner.
- URL state is appropriate when state should be linkable, reload-stable, shareable, or browser-history aware.
- Local/session storage is application state, not a secure secret vault.
- Browser cache directives and framework cache directives are separate systems unless evidence proves otherwise.
- A service worker adds another execution/cache layer and should be introduced only for a clear offline, installability, push, or caching requirement.
- Feature detection is preferable to browser-name branching for capability decisions.
- Use semantic platform primitives before recreating them with JavaScript.

## Reference routing

Load `references/http-browser-runtime.md` for request/response, URL, origin, CORS, cookie, redirect, and execution-boundary reasoning.

Load `references/browser-apis-and-storage.md` for DOM/events, navigation, storage, observers, workers, service workers, and progressive enhancement.

Load `references/rendering-caching-delivery.md` for cache layers, freshness, revalidation, browser/server rendering boundaries, and delivery behavior.

Use `debugging` when the platform mechanism is not yet proven and symptoms require hypothesis testing.

## Quality gates

- The exact web boundary is identified.
- Browser/server/intermediary responsibilities are not conflated.
- Origin/site, transport/auth, and cache layers are distinguished when relevant.
- Optional browser APIs have a graceful baseline or explicit product justification.
- Framework-specific implementation is not invented inside this skill.
- Platform claims are qualified when browser/runtime/version evidence is missing.
- The proposed mechanism preserves normal navigation, accessibility, and security boundaries.

## Failure handling

If platform behavior differs across environments, capture request/response headers, URL/origin, browser/runtime version, storage/cookie state, and service-worker/cache involvement before changing code. If evidence points to framework caching, auth policy, infrastructure, or a browser bug, stop expanding this skill and route to the correct owner with the proven boundary.

## Output contract

Return:

- platform boundary and observable contract;
- relevant browser/HTTP mechanism;
- proven or unresolved cause;
- implementation constraints for the owning specialist;
- compatibility/progressive-enhancement considerations;
- verification steps at the platform boundary.
