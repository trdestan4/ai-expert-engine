# Rendering, Caching, and Delivery Boundaries

## Rendering boundary

Separate what produces HTML from what enhances it. Server rendering can supply initial content; browser JavaScript can hydrate/enhance interaction; purely client-rendered regions depend on JS/data after load. Choose based on content, personalization, interactivity, latency, and failure requirements.

Do not assume a framework label describes the entire route—modern pages can contain mixed server/client regions.

## Cache ownership map

When data/content is stale, identify each possible owner:

1. origin application/persistence;
2. application/framework data cache;
3. rendered output cache;
4. reverse proxy/CDN/shared HTTP cache;
5. browser HTTP cache;
6. service-worker Cache Storage;
7. client query/state cache.

Record the key, scope, freshness, invalidation mechanism, and privacy boundary for the layer actually involved.

## HTTP freshness

Where standard HTTP caching is used, reason about explicit freshness and validators rather than “hard refresh fixed it.” Shared caches require extra care for personalized/authenticated responses and representation variance.

`Vary` changes cache identity by request headers; misuse can fragment cache or leak incorrect representations. Private/user-specific content must not accidentally enter a shared reusable cache.

## Preload/prefetch

Preloading increases priority; prefetching speculatively acquires future resources. Use only for likely/critical resources. Aggressive prefetch can consume bandwidth/data and compete with current-page work.

Framework navigation prefetch may produce requests the user did not explicitly initiate; GET endpoints and loaders should therefore avoid unsafe side effects.

## Compression and formats

Content encoding, modern image formats, font subsets, and streaming affect delivery but belong to different layers. Do not solve an application-rendering bottleneck by blindly changing transport compression, or vice versa.

## Offline behavior

If offline support is required, define which routes/assets/data work offline and how conflicts/staleness are handled. “Cache everything” is not an offline strategy.

## Verification

Use network evidence across cold/warm loads, direct/client navigation, logged-in/logged-out states when applicable, and post-mutation refresh. Inspect response/cache headers and service-worker state before changing unrelated application code.
