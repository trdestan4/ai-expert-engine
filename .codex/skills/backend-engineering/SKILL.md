---
name: backend-engineering
description: Owns production backend implementation across runtime/framework boundaries, service and domain logic, validation, configuration, error handling, observability, caching, concurrency, background execution, and backend testing; it does not own public API contract design, database schema design, identity policy, or distributed messaging architecture.
---

# Purpose

Build backend code that is correct under failure, explicit about trust and side effects, testable at meaningful boundaries, observable in production, and aligned with the repository's actual runtime/framework rather than generic framework folklore.

## Use when

- server-side business logic, services, controllers/handlers, jobs, configuration, validation, errors, logging, or runtime behavior is the primary implementation concern;
- Node.js, Python, Django, FastAPI, or another backend framework needs production-quality implementation guidance;
- side effects, concurrency, caching, retries, or external dependency calls must be coordinated inside an application service;
- backend tests or service boundaries need design/refactoring;
- frontend/API work requires a backend implementation owner.

## Do not use when

- the primary task is public REST/GraphQL contract design (`api-engineering`);
- database schema, SQL, migrations, RLS, or indexing is the main concern (future `database-data`);
- login/session/roles/permissions are the main concern (future `identity-access`);
- queues, pub/sub, WebSockets, SSE, distributed workers, retry topology, or eventual consistency are the main architecture concern (future `realtime-async`);
- the task is framework-independent browser/HTTP behavior (`web-platform`).

## Inputs

Verify the smallest evidence set that can change implementation:

- installed runtime and framework versions;
- application entry points and request/job execution model;
- local service/module conventions;
- domain invariants and side effects;
- validation/schema library in use;
- persistence/cache/external-service boundaries;
- configuration and environment model;
- current logging/testing conventions;
- operational constraints such as latency, throughput, retries, or memory limits when material.

Repository evidence outranks remembered defaults.

## Workflow

### 1. Identify the execution boundary

Classify the code as request handling, command/service execution, scheduled work, background work, event handling, or library/domain logic. Keep transport/framework concerns at the edge when practical.

### 2. Define trust boundaries and validation

Separate untrusted transport/config/external data from trusted internal representations. Parse and validate once near the boundary, preserve useful field-level errors, and avoid spreading unchecked dictionaries/objects through business logic.

### 3. Preserve domain invariants

Keep business rules independent enough to test without booting the whole framework. Do not bury authorization, money, lifecycle, inventory, or state-transition rules in incidental controller code.

### 4. Make side effects explicit

Identify database writes, cache mutation, external API calls, email/notification calls, filesystem/object-storage operations, and emitted jobs/events. Order them deliberately and define what happens when an intermediate side effect fails.

### 5. Design error semantics

Distinguish expected domain/validation/conflict/not-found failures from programmer, dependency, and infrastructure faults. Do not leak stack traces, secrets, SQL, or internal topology to consumers. Preserve causal context in internal logs/traces.

### 6. Handle concurrency and repeat execution

Ask whether the operation can run twice, overlap, race, time out, or be retried. Use database constraints/transactions, idempotency, optimistic/pessimistic coordination, deduplication, or job semantics as appropriate rather than process-local assumptions.

### 7. Add observability at decisions and boundaries

Use structured logs, stable error/operation identifiers, relevant metrics, and trace context. Do not log secrets, credentials, tokens, or unnecessary PII. Logs should explain what happened without becoming the data model.

### 8. Keep configuration explicit

Validate required configuration at startup or boundary initialization. Separate secret values from source control, avoid environment-specific branching scattered throughout business logic, and define safe defaults only when they are truly safe.

### 9. Design for bounded resource use

Control request/body/file sizes, connection/client reuse, timeouts, concurrency, pagination/batch sizes, memory-heavy transforms, and external call fan-out. Avoid unbounded in-memory queues or fetching whole datasets by default.

### 10. Verify behavior

Prefer tests at the closest meaningful boundary:

- pure/domain unit tests for invariants;
- service tests for orchestration and failure behavior;
- integration tests for framework/database/external contracts;
- targeted concurrency/retry tests where duplication or races matter.

## Decision rules

- Framework handlers should coordinate transport; business rules should not depend on HTTP objects unless the rule is genuinely transport-specific.
- Parse/validate untrusted data before business logic; static typing is not runtime validation.
- A retry is safe only when the operation is safe to repeat or protected by idempotency/deduplication.
- Process memory is not a durable coordination mechanism across instances.
- Cache correctness requires an ownership/invalidation/freshness rule; otherwise do not add cache merely for perceived speed.
- Prefer explicit dependency boundaries over global mutable singletons.
- Preserve causal exceptions internally while mapping them to stable public errors at the API boundary.
- Use installed runtime/framework versions before applying version-sensitive patterns.

## Reference routing

Load only what changes the current decision:

- `references/node-runtime-service-patterns.md` for Node.js runtime/service concerns;
- `references/python-backend-runtime.md` for Python/FastAPI/Django runtime concerns;
- `references/validation-errors-observability.md` for trust boundaries, errors, logging, and config;
- `references/concurrency-jobs-cache.md` for repeat execution, concurrency, local background work, and cache decisions;
- `references/backend-testing-production.md` for backend verification and production readiness.

Route public contract decisions to `api-engineering`; route deeper persistence/identity/async/security concerns to their owning phase skills when available.

## Quality gates

- Runtime/framework assumptions match repository evidence.
- Trust boundaries and runtime validation are explicit.
- Domain invariants have a clear owner and test boundary.
- Side effects and failure order are understood.
- Repeat execution/concurrency behavior is safe or explicitly constrained.
- Public errors do not leak sensitive/internal details.
- Logs/metrics/traces are useful and privacy-conscious.
- Resource use, timeouts, and dependency calls are bounded where material.
- Tests prove success, expected failure, and important retry/race behavior.

## Failure handling

If runtime behavior is unexplained, return diagnosis to `debugging` before stacking fixes. If a change depends on database guarantees, identity policy, distributed queue semantics, or security architecture that is not yet established, identify that boundary instead of inventing a local workaround. If an external dependency is unreliable, define timeout/retry/circuit behavior based on idempotency and business tolerance rather than retrying every error.

## Output contract

Return a compact backend implementation result containing:

- verified runtime/framework context;
- execution/service boundary;
- validation and domain-invariant strategy;
- side effects and failure semantics;
- concurrency/idempotency/cache decisions when relevant;
- observability/config/resource rules;
- implementation/testing evidence;
- unresolved cross-domain risks.