# Web Vitals and Rendering Performance

Use field metrics for real-user outcomes and lab traces/profiles for diagnosis. Current Core Web Vitals are LCP, INP and CLS. Good targets remain LCP <= 2.5s, INP <= 200ms and CLS <= 0.1 at the 75th percentile; verify current official guidance when these thresholds materially affect policy.

## LCP decomposition

Separate server response/TTFB, resource discovery delay, resource download and element render delay. Optimize the dominant term. Common causes: serialized backend waterfalls, client-only discovery of hero media, oversized/unprioritized image, font blocking, hydration gating and render-blocking scripts/styles.

Do not preload everything. Prioritize only critical resources and verify network contention. Responsive/art-directed media should avoid downloading a desktop asset then hiding it on mobile.

## INP and main thread

Use performance traces to identify long tasks, input delay, expensive event handlers, layout/style work, hydration, rerender cascades, synchronous JSON/data processing and third-party script cost. Break long work, reduce client JavaScript, move non-UI work off the critical path/worker when appropriate, and fix state/component boundaries before memoizing everywhere.

## CLS

Reserve media/ad/embed space, stabilize font metrics, avoid late above-content insertion and understand intentional user-triggered movement. Layout shift score alone does not explain the source; inspect shift clusters.

## CPU, memory and leaks

On long-lived dashboards/editors, profile heap growth, detached DOM, timers/listeners/subscriptions, retained caches and large media buffers. Use heap snapshots/allocation timelines when a leak is suspected. Garbage collection pauses may expose allocation churn even when total memory stabilizes.

## Rendering architecture

Prefer server/static HTML for content that does not need client ownership. Streaming/progressive delivery helps only if it reveals useful content and does not create excessive client work. Hydration/islands boundaries should match interaction needs.

## Measurement

Segment field data by device/network/route/region when sample size allows. Test realistic lower-end mobile and throttled network, not only developer hardware. Lighthouse-style aggregate scores are signals, not product goals. Record before/after evidence and guard against trading one vital for another.
