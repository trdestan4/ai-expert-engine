# Browser Runtime, Storage, and Workers

## Execution context

Before using a browser API establish whether code runs during server render/build, in a worker, or in the window/document context. `window`, `document`, DOM nodes, Web Storage, observers, media APIs, and many device APIs are unavailable outside their intended context.

Prefer capability checks and delayed browser-only access over broad environment hacks.

## DOM and events

Use native elements/behavior where possible. Understand event target/currentTarget, capture/bubble, default actions, focus, and form submission before adding global listeners or `preventDefault` broadly.

Global listeners should have clear ownership and cleanup. Use passive listeners for high-frequency scrolling/touch events when the handler never cancels the event.

## Navigation and URL state

History/back-forward behavior is part of UX. State belongs in the URL when sharing, bookmarking, reload persistence, or navigation history is expected. Do not mirror URL state into another store unless a synchronization requirement is explicit.

## Storage choices

- In-memory component/store state: current app lifetime.
- `sessionStorage`: tab/session-scoped script-readable persistence.
- `localStorage`: origin-scoped script-readable persistence.
- IndexedDB: larger structured client data/offline workflows.
- Cache Storage: request/response caching, commonly with service workers.
- Cookies: request-coupled small state governed by cookie attributes.

Choose by lifetime, size, ownership, synchronization, trust, and offline needs. Script-readable storage is not a secret store.

Version persistent client schemas when application updates can outlive stored data.

## Observers and browser APIs

Use Intersection/Resize/Mutation observers only for behaviors that need observation, and disconnect them when ownership ends. Prefer CSS for layout/responsiveness before JS measurement.

Feature-detect optional APIs and define fallback behavior. Avoid user-agent sniffing unless working around a proven platform defect with a bounded removal plan.

## Workers and service workers

Web Workers are for off-main-thread computation without DOM access. Service Workers are network/event workers that can intercept requests and enable offline/caching/push patterns.

A service worker introduces:

- installation/activation lifecycle;
- version/update behavior;
- separate cache state;
- offline failure modes;
- another debugging surface.

Introduce it only for a clear product requirement, not as a generic performance badge.

## Verification

Test direct load, reload, back/forward, multiple tabs when state sharing matters, storage migration/corruption behavior, offline/online transitions when supported, and cleanup of listeners/observers/workers.
