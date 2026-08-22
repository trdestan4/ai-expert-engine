# Backend, Data, Load and Capacity Performance

## Start with the service objective

Identify critical operation, traffic shape, latency/error/throughput target and resource/cost constraints. Use percentiles (p50/p95/p99 as appropriate), not average alone. Tail latency often reveals lock contention, GC, cold starts, downstream outliers or queue saturation.

## Trace the path

Use distributed traces/profiles/log correlations to decompose request time into application CPU, serialization, database, cache, provider calls, queueing and network. Fix dominant waits before local micro-optimizations.

## Database

Use representative query plans/data. Check N+1/fan-out, join/filter/order shape, cardinality/selectivity, index effectiveness, rows scanned/returned, locks, transaction duration and connection pool saturation. A sequential scan can be correct; an index can make writes/cache worse. Database-data owns the actual query/schema change.

## Concurrency and queueing

Bound thread/goroutine/task/worker concurrency to downstream capacity. More concurrency can increase queueing, lock contention and timeout/retry storms. Monitor queue wait separately from service time. Use Little's Law/queueing intuition carefully with stable workloads; real burstiness requires measurement.

## Load models

Model realistic arrival rate, user journeys, hot keys/tenants, payload sizes, data volume, cache warm/cold state, provider dependencies and ramp/burst behavior. A single-endpoint tight loop is not representative capacity evidence unless that endpoint is the actual bottleneck.

Test steady state, expected peak and controlled overload. Observe saturation indicators (CPU, memory, pool utilization, queue depth, lock/wait, event loop lag) and failure mode. A good system degrades predictably rather than accumulating unbounded work.

## Retries and backpressure

Retries multiply load. Use timeouts, retry budgets/backoff/jitter and idempotency. Queues/workers need bounded concurrency, DLQ/recovery and producer backpressure/admission controls. Measure retry amplification during dependency failure.

## Memory/CPU

Use language/runtime profilers for CPU hotspots, allocation/heap/GC and blocking. Serverless cold-start/runtime selection matters when traffic pattern exposes it; do not optimize cold start when warm processing dominates.

## Regression evidence

Record before/after workload, dataset, environment and confidence. Performance optimization must preserve correctness, consistency and cache freshness. If production-like evidence is unavailable for an R3/R4 capacity-sensitive release, report the gap rather than declaring success.
