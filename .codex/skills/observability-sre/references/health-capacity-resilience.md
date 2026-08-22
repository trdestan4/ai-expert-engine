# Health, Capacity and Resilience

## Health checks

Liveness asks whether process is irrecoverably stuck; readiness asks whether it should receive traffic. Do not make liveness depend on every downstream service and cause restart storms. Startup probes/initial delays may protect slow initialization.

## Capacity

Track traffic, latency, errors and saturation plus workload-specific limits: CPU/memory, DB connections/locks, queue depth/age, thread/event-loop lag, provider quotas, storage and cache. Forecast growth/seasonality where lead time for capacity is material.

## Resilience

Use timeouts, bounded retries/backoff/jitter, circuit/admission controls, bulkheads/concurrency limits and graceful degradation based on failure mode. Every retry consumes budget/capacity; avoid synchronized retry storms.

## Dependency failure

Define what can degrade safely vs must fail closed. Auth/payment/data integrity often require fail-closed; recommendations/analytics may degrade. Cache fallback must respect freshness/security.

## Disaster recovery

Backups are assumptions until restore tested. Define RPO/RTO and recovery ownership for critical data/services. Multi-region/replication does not replace backup and can replicate corruption.

## Game days

For high-impact systems, controlled failover/restore/chaos exercises can validate assumptions. Define steady state, blast radius and abort criteria before the exercise.
