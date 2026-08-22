# Bundles, Assets, Network and Cache

Track JavaScript/CSS/image/font/third-party cost by route and interaction. Remove dead code, avoid broad barrel imports that defeat tree-shaking, split truly optional heavy features and delay analytics/widgets that are not needed for first interaction.

Serve correctly sized modern images, reserve dimensions, avoid unnecessary high-resolution payloads and preload only resources that are genuinely critical. Limit font families/weights/subsets; avoid preloading everything.

Reduce request waterfalls with early discovery and parallel independent work. Use compression and CDN delivery where appropriate, but verify cache keys and privacy boundaries.

Caching requires explicit freshness semantics: what may be shared, browser/private versus CDN/public scope, TTL, revalidation, invalidation and stale tolerance. Never cache authenticated/personalized output publicly by accident.

Third-party scripts can dominate runtime and privacy cost. Inventory them, justify their business value, isolate/defer where possible and monitor regression after provider changes.