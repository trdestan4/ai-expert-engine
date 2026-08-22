---
name: backend-engineering
description: Owns production backend implementation across runtime/framework boundaries, service and domain logic, validation, configuration, error handling, observability, caching, concurrency, background execution, resource limits and backend testing; public API contracts, persistence architecture, identity policy and distributed messaging remain separate owners.
---

# Purpose
Build backend code that remains correct under failure, explicit about trust and side effects, observable and testable, while following the repository's actual runtime/framework rather than framework folklore.

## Use when
- server-side business logic, services, handlers, jobs, configuration, validation, errors, logging or runtime behavior is primary;
- Node.js, Python/FastAPI/Django, Go, Spring Boot/JVM, ASP.NET Core, Rails or another backend runtime needs production guidance;
- concurrency, caching, retries or external dependency calls must be coordinated inside application logic;
- backend tests/service boundaries need design or refactoring.

## Do not use when
- public REST/GraphQL contract design is primary (`api-engineering`);
- schema, SQL, migrations, RLS or indexing is primary (`database-data`);
- login/session/roles/permissions are primary (`identity-access`);
- queues/pubsub/WebSockets/SSE/distributed workers are primary (`realtime-async`);
- formal threat review is primary (`security`).

## Inputs
Verify installed runtime/framework versions, execution entry points, local module conventions, domain invariants, validation library, persistence/cache/external boundaries, configuration/environment model, logging/testing conventions and material latency/throughput/resource constraints.

## Workflow
### 1. Identify execution boundary
Classify request handling, service/command execution, scheduled/background/event work or pure domain/library logic. Keep transport/framework concerns at edges when practical.

### 2. Validate trust boundaries
Parse untrusted transport/config/provider data near the boundary into trusted internal representations. Static typing is not runtime validation.

### 3. Preserve domain invariants
Keep money, authorization-dependent decisions, lifecycle and state-transition rules in explicit application/domain ownership rather than incidental controller callbacks.

### 4. Make side effects explicit
List database/cache/provider/email/storage/job effects, order them deliberately and define partial-failure behavior.

### 5. Design error semantics
Separate expected domain/validation/conflict/not-found failures from programmer/dependency/infrastructure faults. Preserve cause internally; do not leak stacks, SQL, topology, secrets or tokens publicly.

### 6. Handle concurrency and repeat execution
Assume operations can overlap, time out and retry. Use durable constraints/transactions/idempotency/deduplication or runtime-safe coordination; process memory is not distributed coordination.

### 7. Observe decisions and boundaries
Use structured logs, stable operation/error identifiers, metrics and trace context without unnecessary PII/secrets.

### 8. Validate configuration and resources
Fail early on missing required configuration. Bound body/file sizes, concurrency, queues, batches, fan-out, memory-heavy transforms and external-call timeouts.

### 9. Apply verified runtime adapter
Use the repository's installed runtime/framework semantics for cancellation, DI/lifetimes, transactions, async/concurrency, graceful shutdown and pooling. Do not transpose Node/Python patterns into Go/JVM/.NET/Rails.

### 10. Verify behavior
Use domain/unit tests for invariants, service tests for orchestration/failure, integration tests for runtime/database/provider contracts, and targeted concurrency/retry tests where duplication or races matter.

## Decision rules
- Handlers coordinate transport; business rules should not depend on HTTP objects unless transport-specific.
- Parse/validate before business logic.
- Retry only safe/idempotent/reconcilable effects.
- Cache requires ownership, invalidation and freshness rules.
- Prefer explicit dependency boundaries over global mutable singletons.
- Every material external call needs a timeout.
- Use installed runtime/framework versions before version-sensitive patterns.

## Reference routing
Load `references/node-runtime-service-patterns.md` for Node.js runtime/service concerns.
Load `references/python-backend-runtime.md` for Python/FastAPI/Django concerns.
Load `references/validation-errors-observability.md` for trust boundaries, errors, logging and configuration.
Load `references/concurrency-jobs-cache.md` for repeat execution, concurrency, local jobs and cache decisions.
Load `references/backend-testing-production.md` for backend verification and production readiness.
Load `references/multi-runtime-adapters.md` for verified Go, Spring/JVM, ASP.NET Core or Rails runtime behavior.
Route persistence to `database-data`, identity to `identity-access`, distributed async to `realtime-async`, contracts to `api-engineering` and threat review to `security`.

## Quality gates
- Installed runtime/framework assumptions match repository evidence.
- Runtime validation and trust boundaries are explicit.
- Domain invariants have a clear testable owner.
- Side effects/failure order and concurrency/repeat behavior are understood.
- Public errors are stable and non-sensitive.
- Observability is useful and privacy-conscious.
- Timeouts/resource use are bounded where material.
- Tests cover success, expected failure and important retry/race behavior.

## Failure handling
If runtime behavior is unexplained, return to `debugging` before stacking fixes. If correctness depends on database, identity, queue or security guarantees, route the boundary rather than inventing local workarounds. If provider/runtime behavior differs from memory, verify installed versions/current docs.

## Output contract
Return verified runtime/framework context, execution/service boundary, validation/invariants, side effects/failure semantics, concurrency/idempotency/cache decisions, observability/config/resource rules, implementation/testing evidence and unresolved cross-domain risks.
