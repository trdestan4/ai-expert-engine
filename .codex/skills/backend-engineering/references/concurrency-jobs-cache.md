# Concurrency, Jobs, and Cache Decisions

Use this reference when backend correctness depends on repeat execution, overlap, retries, short-lived background work, or caching.

## Concurrency

Assume two requests/jobs can overlap unless the system proves otherwise. Process-local locks do not coordinate multiple instances. Prefer database uniqueness/transactions, optimistic version checks, distributed locks only when justified, or queue serialization where the operation requires it.

## Repeat execution

Ask whether the operation can be retried after a timeout where the caller does not know whether it succeeded. If duplicate execution would cause harm, require an idempotency/deduplication mechanism at the appropriate boundary.

## Background work

Do not rely on request-lifetime fire-and-forget tasks for durable obligations. Tiny best-effort post-response work may be acceptable only when loss is explicitly tolerable and the deployment runtime supports it. Durable work belongs to the future `realtime-async` queue/worker layer.

## Cache

Before caching, define owner, key, freshness, invalidation, fallback, and consistency tolerance. Cache derived/read-heavy data, not correctness-critical mutable state without a coherent invalidation model. Cache misses and stale reads are normal states, not exceptions.

## Failure

Retries require bounded attempts, backoff/jitter where appropriate, timeout budgets, and an understanding of which failures are transient. Never retry validation/authorization/domain conflicts simply because an exception occurred.