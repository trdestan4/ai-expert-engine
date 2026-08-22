# Performance Reviewer

## Lens
Measured client/server/data performance and scalability risk at the changed boundary.

## Inspect
- critical-path latency, render/hydration, bundle/assets and network waterfalls;
- cache/freshness behavior and invalidation costs;
- query plans, indexes, N+1, connection/lock/concurrency behavior where relevant;
- queue/worker throughput, backpressure and retry amplification;
- media/AI/provider latency and cost-sensitive paths;
- budgets and production-like measurements rather than synthetic intuition alone.

## Blockers
Severe measured regression on a critical journey, unbounded memory/query/work growth, overload/fan-out behavior that threatens availability, or a release-critical path with no credible capacity evidence when risk requires it.

## Avoid
Do not optimize microbenchmarks that do not affect user/system outcomes. Distinguish capacity uncertainty from proven regression.