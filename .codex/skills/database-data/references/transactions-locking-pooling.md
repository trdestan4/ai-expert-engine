# Transactions, Locking and Pooling

## Transaction boundaries

Wrap the smallest set of database operations that must succeed or fail together to preserve a business invariant. Do not keep transactions open across slow external network calls when an outbox/workflow pattern can separate them.

## Isolation and races

Understand the application's anomaly risk: lost updates, non-repeatable reads, phantoms, write skew and uniqueness races. Prefer constraints/atomic updates/upserts and row locks for narrow invariants before escalating isolation globally.

Handle retryable serialization/deadlock failures explicitly when the selected strategy can produce them. Retry the complete transaction with bounded backoff, not only the failing statement.

## Locks

Keep lock acquisition order predictable in high-contention flows. Avoid user interaction or arbitrary external I/O while holding database locks. Use `SELECT ... FOR UPDATE` or advisory locks only when ownership/concurrency semantics justify them.

## Optimistic concurrency

Version columns/timestamps/compare-and-swap updates can protect collaborative or lower-contention updates without long-held locks. A failed version match is a business conflict, not a generic 500.

## Connections

Determine provider connection limits and deployment concurrency. Long-lived servers may use normal pools; serverless/edge deployments often need provider poolers or constrained client pools. Avoid creating a new pool per request.

Pool size is not throughput by itself. Account for total instances × pool size, transaction duration and database capacity.

## Tests

Exercise simultaneous creates/updates, unique races, inventory/balance-like decrements, deadlock/retry paths, pool exhaustion, transaction rollback and external-side-effect ordering.