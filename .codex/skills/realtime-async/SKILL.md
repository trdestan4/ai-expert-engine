---
name: realtime-async
description: Owns realtime and asynchronous execution architecture across WebSockets, SSE, pub/sub, queues, workers, cron, retries, backoff, dead-letter handling, idempotency, event delivery, eventual consistency, and distributed job lifecycle; it does not own ordinary synchronous API contracts or provider-specific integration semantics.
---

# Purpose

Design realtime and asynchronous workflows that remain correct under retries, duplication, delay, partial failure, worker restarts, disconnects, and out-of-order delivery.

## Use when

- WebSockets, SSE, realtime subscriptions or pub/sub are required;
- work must continue beyond request lifetime using queues/workers/jobs;
- cron/scheduled processing, retries/backoff, DLQ, delayed jobs, fan-out, or event-driven architecture is involved;
- duplicate/out-of-order events or eventual consistency affect correctness.

## Do not use when

- a normal request/response API is enough (`api-engineering`);
- external webhook/provider contract is primary (`integrations`);
- database transaction/schema is primary (`database-data`);
- frontend UI state alone is the concern (`frontend-engineering`).

## Inputs

Establish:

- producer/consumer boundaries and event/job purpose;
- delivery guarantees offered by actual broker/provider;
- ordering requirements and partition/key semantics;
- retryability and idempotency requirements;
- maximum latency, throughput and burst expectations;
- payload size/security/retention constraints;
- acknowledgement/visibility timeout behavior;
- worker concurrency and shutdown model;
- source-of-truth and consistency expectations.

## Workflow

### 1. Decide sync versus async intentionally

Use async when work is long-running, retryable, bursty, fan-out, scheduled, independently scalable, or must survive request termination. Do not introduce a queue to hide an unclear synchronous design.

### 2. Define the durable state transition

Identify what database/state change proves the job/event was accepted and what proves completion. Separate durable business state from transient delivery state.

### 3. Design idempotency before retries

Assume at-least-once delivery unless the provider contract proves stronger behavior. Define stable deduplication keys, unique constraints/state-machine checks, or idempotent operations before enabling automatic retries.

### 4. Classify failures

Retry transient failures with bounded exponential backoff and jitter. Do not endlessly retry validation, permission, malformed payload, permanent not-found, or invariant violations.

### 5. Define dead-letter/recovery path

Poison jobs need terminal state, reason, observability and replay/manual-resolution procedure. A DLQ with no owner/runbook is delayed data loss.

### 6. Handle ordering and concurrency

Only require global ordering if the business truly needs it. Prefer per-entity/partition ordering or version checks. Protect state transitions from duplicate and out-of-order delivery.

### 7. Design realtime transport

Use SSE for server-to-client streams when one-way HTTP streaming fits. Use WebSockets for bidirectional/low-latency sessions. Define reconnect, heartbeat, authorization refresh, resubscription and missed-event recovery.

### 8. Design worker lifecycle

Use bounded concurrency, graceful shutdown, visibility/lease renewal when needed, cancellation semantics, per-job timeouts and backpressure. Do not acknowledge success before required durable effects complete.

### 9. Integrate transactionally

When a database write must emit an event, use an outbox or equivalent durable handoff rather than an unsafe dual-write. Consumers should tolerate replay.

### 10. Observe the pipeline

Track queue depth/age, success/failure/retry/DLQ counts, processing latency, duplicate rate, worker saturation, reconnect churn and stuck jobs.

## Decision rules

- Exactly-once delivery claims do not remove the need for idempotent business effects.
- At-least-once + idempotency is usually safer than assuming no duplicates.
- Retry only failures likely to become successful without changing the payload/business state.
- Queue acceptance is not business completion.
- Cron schedules need overlap/concurrency policy.
- Realtime clients need recovery after disconnect; a socket connection is not durable history.
- Use the database/outbox for durable state transitions, not in-memory event emission alone.
- Preserve correlation/causation IDs across async boundaries.

## Reference routing

Load `references/websocket-sse-realtime.md` for transport selection, connection lifecycle, authorization and missed-event recovery.

Load `references/queues-retries-dlq.md` for broker delivery, acknowledgements, retry classes, backoff, DLQ and worker concurrency.

Load `references/jobs-cron-idempotency.md` for scheduled jobs, deduplication, idempotency, leases and overlap control.

Load `references/events-consistency-outbox.md` for event-driven workflows, outbox/inbox, ordering, versioning and eventual consistency.

Use `integrations` when an external provider/webhook owns the message contract; use `database-data` for transaction/constraint details.

## Quality gates

- Delivery and ordering assumptions match the actual provider.
- Retry policy distinguishes transient from permanent failure.
- Business effects are idempotent or deduplicated.
- DLQ/replay/manual recovery is defined for important jobs.
- Worker shutdown/timeouts/backpressure are explicit.
- Realtime reconnect/missed-event recovery exists where needed.
- Dual-write risk is removed for critical event publication.
- Queue/job observability exposes age, failures and stuck work.

## Failure handling

If broker guarantees are unclear, assume duplicates/delay and inspect provider docs before relying on stronger semantics. If an operation cannot be made idempotent, serialize/protect it with a durable state transition and unique identity. If a realtime connection loses history, recover from authoritative persisted state rather than pretending the stream is complete.

## Output contract

Return:

- transport/job topology;
- delivery/idempotency model;
- retry/DLQ/recovery behavior;
- ordering/concurrency rules;
- realtime reconnect policy;
- durable handoff/state strategy;
- monitoring and tests.