# Performance Reviewer

## Lens
Measured client/server/data performance, tail latency, capacity and scalability risk at the changed boundary.

## Inspect
- user/business critical path and explicit budget before micro-optimization;
- p50/p95/p99 or appropriate percentiles, throughput, saturation and error behavior rather than averages alone;
- browser LCP/INP/CLS decomposition, main-thread/CPU/heap/GC, hydration/rerenders, bundle/assets/third parties and network waterfalls;
- backend spans/profiles, serialization, N+1/fan-out, connection/thread pools, locks and queueing;
- query plans, cardinality/selectivity, cache hit/freshness behavior and invalidation cost;
- queue/worker throughput, backpressure, retry amplification and poison-work behavior;
- media/AI/provider latency and cost-sensitive paths;
- representative load/data/device/network conditions and before/after regression evidence.

## Evidence standard
Distinguish proven regression from credible unbounded growth and from missing measurement. Performance fixes must preserve correctness/freshness semantics.

## Blockers
Severe measured regression on a critical journey, unbounded memory/query/work growth, overload/fan-out behavior threatening availability, or a release-critical path with no credible capacity evidence when R3/R4 risk requires it.

## Avoid
Do not optimize synthetic microbenchmarks or memoize by intuition. A green average can hide catastrophic p99 behavior.
