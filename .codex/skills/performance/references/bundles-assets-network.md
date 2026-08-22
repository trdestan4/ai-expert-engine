# Bundles, Assets, Network and Third-Party Performance

## JavaScript and bundles

Inspect route/chunk composition, duplicated packages, accidental server-to-client imports, heavy libraries, polyfills and dynamic-import boundaries. Bundle size is a proxy; parse/compile/execution on target devices matters. Prefer removing unnecessary client work over micro tree-shaking.

Use code splitting when it delays genuinely non-critical code without creating request waterfalls. Avoid one dynamic import per tiny component. Verify source-map/analyzer evidence rather than guessing from package reputation.

## Images/video/fonts

Choose dimensions/crops from layout, modern formats where supported, responsive sources, compression quality and lazy loading below the fold. Critical/LCP media needs early discovery and priority. Video/3D sequences require poster/fallback, preload policy, memory/network budgeting and mobile adaptation.

Fonts: load used glyphs/weights/axes only, avoid indiscriminate preload, use fallback metrics when CLS matters and verify language coverage before aggressive subsetting.

## Network waterfalls

Inspect DNS/TLS/connect, redirects, server/API waterfalls, resource priority and third-party chains. Start independent requests early and await late. Reduce round trips when latency dominates; batching can help but may increase payload/cache coupling—measure.

## Third-party scripts

Analytics, tag managers, chat, A/B platforms, embeds and fraud/ads can dominate main thread/network. Inventory business owner, loading condition, consent requirement, performance cost and failure behavior. Load after critical interaction when acceptable and remove unused tags.

## CDN/compression/caching

Use immutable content-hashed assets with long cache lifetime. Enable appropriate compression and avoid recompressing already compressed media. Cache HTML/API only with correct personalization/freshness keys. Edge/CDN cache performance never justifies data leakage.

## Budgets

Define route-level budgets for JS, critical media, request count or interaction cost only when they predict user outcomes. CI budgets catch regressions but need periodic field validation.
