# Reliability, Security and Performance Testing

## Failure injection

Test timeouts, connection resets, provider 429/5xx, queue duplicate/redelivery, delayed/out-of-order events, partial transaction failure, worker restart and stale cache/data where the architecture depends on recovery. Inject failures at controlled boundaries rather than randomly breaking everything.

For distributed/async systems, verify idempotency, retry budget, DLQ/reconciliation and graceful shutdown. A successful happy-path queue test does not prove duplicate safety.

## Concurrency/race testing

Exercise simultaneous updates to business invariants such as inventory, balances, quotas, uniqueness and membership. Prefer database constraints/atomic primitives, then write tests that demonstrate lost-update/double-spend/duplicate prevention. Use repeated stress runs only as supporting evidence; deterministic orchestration/locking hooks are better when available.

## Security tests

Negative authorization tests are mandatory for changed high-risk access boundaries. Include cross-tenant IDs, downgraded roles, direct API/object access and background/admin paths. For SSRF/file/parser paths include redirects, special IPs/encodings, oversized/nested/compressed inputs and resource limits.

## Performance tests

Define workload, dataset, environment, warm/cold state, ramp/peak and pass budget before running. Record p50/p95/p99/throughput/error/saturation when relevant. Do not declare success from average latency or a developer laptop microbenchmark.

## Chaos/resilience

Chaos experiments are justified when production architecture has failover/redundancy assumptions worth proving. Establish steady-state hypothesis, blast radius, abort criteria and observability first. Do not run uncontrolled chaos as a substitute for deterministic failure-path tests.

## Flakiness

A flaky test is a defect. Classify timing/race/environment/shared-state/provider causes. Quarantine only with owner/expiry and keep signal visible. “Retry five times until green” masks reliability risk and biases CI toward false pass.
