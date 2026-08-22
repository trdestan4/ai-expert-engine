# Next.js Runtime, Hydration, and Performance

## Hydration

Hydration mismatch means the initial server markup and client render disagree. Common classes:

- browser-only values read during initial render;
- time/random/locale differences;
- invalid HTML nesting;
- unstable external data;
- client persistence changing initial state;
- DOM mutation by extensions/third parties.

Fix the causal difference. Use hydration-warning suppression only for a small intentionally divergent node whose behavior is understood.

## Images

Prefer the repository's Next image pipeline when compatible. Define intrinsic dimensions/aspect ratio, meaningful `sizes` for responsive layouts, correct crop behavior, and loading priority based on actual above-the-fold/LCP role.

Do not mark every image priority/eager. Configure remote sources narrowly and keep user-controlled URLs within the application's trust model.

## Fonts

Use Next font facilities or established local strategy to avoid unnecessary external blocking requests and layout shift. Load only required families/weights/subsets. Map typography design tokens to font variables/classes rather than duplicating font declarations across components.

## Scripts and third parties

Load third-party scripts according to when they are needed. Defer analytics/support/marketing code when it is not required for initial interaction. Keep consent/privacy requirements separate and explicit.

## Bundle discipline

Prefer direct imports over heavyweight barrels when package structure makes that materially smaller. Dynamically/conditionally load large client-only features that are not needed initially. Avoid moving server-capable libraries/components into the client graph through an overly broad `'use client'` boundary.

## Metadata and social assets

Use static metadata when values are static; dynamic generation only when content actually varies. Reuse already-available server data to avoid duplicate fetches. Verify canonical/social asset routes in production-like builds.

## Runtime/build

A development server is not proof of production behavior. For meaningful changes run the production build and inspect warnings/errors relating to route prerendering, dynamic APIs, server/client imports, bundle/runtime compatibility, and metadata.

For self-hosting or alternate runtimes, verify framework-supported output mode, filesystem/cache assumptions, image optimization, and multi-instance cache behavior rather than assuming Vercel defaults.

## Performance priority

Fix in this order unless profiling says otherwise:

1. async/data waterfalls;
2. unnecessary client JS/boundary size;
3. oversized eager media/third parties;
4. server serialization/data duplication;
5. rerender/render hot paths;
6. low-level JS micro-optimizations.

Measure Core Web Vitals and route-level behavior in the later performance phase for formal optimization/audit.

## Verification

Check production build, hydration console, network/bundle behavior, direct navigation, image/font loading, slow-network interaction, and JS-disabled/server-rendered baseline where the product requires it.
