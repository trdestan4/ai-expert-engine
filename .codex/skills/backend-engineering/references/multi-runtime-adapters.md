# Backend Runtime Adapters — Go, JVM, .NET and Rails

The core backend contract stays the same: explicit trust boundaries, domain invariants, bounded side effects, concurrency safety, observability and testability. Verify repository versions before framework-specific advice.

## Go
Prefer explicit context propagation for cancellation/deadlines, bounded goroutines, clear ownership of channels, and wrapped errors that preserve cause. Reuse HTTP/database clients and tune pools deliberately. Avoid process-global mutable state for request coordination.

## Java / Spring Boot
Keep web/controller, application service and persistence boundaries explicit. Understand transaction proxy boundaries, propagation and lazy-loading behavior before relying on annotations. Configure thread/connection pools and timeouts rather than accepting accidental defaults. Map domain failures to stable API errors without leaking internals.

## .NET / ASP.NET Core
Respect scoped/transient/singleton lifetimes, cancellation tokens and async end-to-end behavior. Avoid sync-over-async and accidental singleton capture of scoped dependencies. Validate options/configuration at startup and use structured logging/activity context.

## Ruby / Rails
Keep callbacks from becoming hidden orchestration. Make transaction and background-job boundaries explicit; assume jobs can repeat. Avoid N+1 queries and unbounded ActiveRecord loading. Strong parameters improve input handling but do not replace domain validation/authorization.

## Cross-runtime checks
For every runtime verify: graceful shutdown, request/job deadlines, connection reuse/pooling, bounded concurrency, structured errors/logs, health/readiness semantics, idempotency for retried effects, deterministic tests and production configuration validation.
