# Backend Runtime Adapters — Go, JVM/Spring, .NET and Rails

The core backend contract stays constant: explicit trust boundaries, domain invariants, bounded side effects/concurrency, timeouts/cancellation, observability, graceful lifecycle and tests. Verify repository/runtime/framework versions first.

## Go

Propagate `context.Context` for request/job cancellation/deadlines; do not store it in structs as durable state. Reuse HTTP/database clients and configure transport/pools intentionally. Bound goroutines and define channel ownership/closure; leaking goroutines under timeouts is a production defect.

Wrap errors with context while preserving cause (`errors.Is/As`). Avoid process-global mutable request state. For HTTP servers, configure timeouts/limits and graceful shutdown; distinguish liveness/readiness where deployed under orchestration.

## Java / Spring Boot

Keep controller/web, application service/domain and persistence boundaries explicit. Understand proxy-based transaction behavior: self-invocation, propagation, checked/unchecked rollback rules and async/thread boundaries can invalidate annotation assumptions. Avoid lazy-loading/N+1 leakage into serialization.

Configure request/executor/connection pools and timeouts. Propagate trace/security context deliberately across async work. Validate configuration at startup and map domain failures to stable external errors without leaking internals.

## .NET / ASP.NET Core

Respect DI lifetimes: singleton must not capture scoped services. Use `CancellationToken` end-to-end for request/dependency work. Avoid sync-over-async (`.Result/.Wait`) and accidental blocking thread-pool starvation.

Validate options/configuration on startup. Use typed/pooled `HttpClient` patterns and explicit timeouts/resilience. Understand EF Core tracking/query/transaction behavior; avoid unbounded materialization and N+1. Structured logs/Activity/OpenTelemetry context should carry request correlation without sensitive payloads.

## Ruby / Rails

Keep callbacks from becoming hidden orchestration; prefer explicit services/use cases for cross-aggregate side effects. ActiveRecord validations do not replace database constraints for durable invariants. Watch N+1/unbounded relation loading and transaction scope.

Background jobs can repeat; design idempotency and transaction/after-commit handoff. Strong parameters improve mass-assignment handling but do not replace authorization/domain validation. Review thread/process/server worker model and connection pool sizing for deployment environment.

## Cross-runtime production checks

- request/job deadlines and external-call timeouts;
- bounded concurrency and queues;
- connection/client reuse/pooling;
- validation at trust boundaries;
- graceful shutdown/draining;
- structured errors/logs/traces;
- health/readiness semantics;
- idempotency for retried effects;
- production configuration validation;
- representative integration/concurrency tests.

Do not transpose Node/Python idioms directly onto another runtime. Load runtime-specific official docs when behavior affects correctness.
