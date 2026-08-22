# Next.js Data, Cache, Rendering, and Delivery

Use repository/version evidence before applying a specific cache API.

## Data reads

Place server-owned data reads close to the server component/use case that owns them while keeping persistence/integration logic reusable outside React when appropriate.

Parallelize independent reads. Parent/child component structure must not accidentally serialize unrelated data.

## Rendering strategy

Choose rendering from product freshness and interactivity rather than labels such as “SSR is better.” Consider:

- static/prebuilt content when data can be safely reused;
- dynamic server rendering when request-specific or fresh data requires it;
- streaming/Suspense for independently resolving regions;
- client fetching when browser-driven revalidation or client-only context is genuinely required.

The installed Next version may infer/cache these differently; verify actual behavior.

## Cache layers

Before changing caching identify the owner:

- React/request-level deduplication;
- Next framework render/data cache;
- Cache Components / `'use cache'` where supported and enabled;
- explicit application cache;
- client query cache;
- HTTP/CDN/browser/service-worker cache.

A “no cache” change at one layer may not invalidate another.

## Freshness contract

For each cached read define:

- what key/identity makes entries equivalent;
- acceptable staleness;
- invalidation/revalidation trigger;
- user/tenant/privacy scope;
- whether failure can serve stale data;
- whether personalized data may ever be shared.

Do not cache request/user-specific data in a shared scope accidentally.

## Revalidation

Use the installed framework's supported tag/path/cache invalidation primitives only after establishing which data/view they own. Prefer precise invalidation over global revalidation.

Mutations should update or invalidate the authoritative affected data, not merely force a client reload to mask stale state.

## Suspense and streaming

Place boundaries around useful user-visible units that can resolve independently. Avoid one huge blocking boundary and avoid excessive tiny boundaries that create visual noise.

Fallbacks should preserve layout and communicate meaningful progress. Streaming does not excuse data waterfalls inside a segment.

## Client data libraries

Use SWR/query libraries where browser-side cache/revalidation/optimistic interaction needs them. Do not duplicate server-rendered authoritative data into a separate client fetch solely by habit.

## Verification

Test cold direct load, warm navigation, post-mutation freshness, user/tenant isolation, relevant revalidation timing, failure behavior, and production build/runtime mode. If caching differs between dev and production, verify production-like execution before concluding.
