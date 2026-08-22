# Backend / API Engineering Policy

- Verify installed runtime/framework/spec tooling before version-sensitive advice.
- Keep transport/API contracts separate from domain/service internals.
- Runtime validation is mandatory for untrusted input; static typing is not runtime validation.
- Make side effects, timeouts, retries, idempotency, and concurrency assumptions explicit.
- Public errors must be stable, machine-readable when appropriate, and must not leak secrets/internal details.
- Do not expose persistence models directly as public contracts by default.
- Unbounded collections require pagination/resource controls.
- Cache and retry behavior require correctness/freshness semantics, not just performance intent.
- Durable work must not depend on request-lifetime fire-and-forget execution.
- Tests must cover important failure paths and compatibility boundaries, not only success cases.
- Route database, identity, distributed async, and security architecture to their owning specialists rather than duplicating them here.