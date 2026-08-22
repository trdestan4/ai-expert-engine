# Python Backend Runtime

Use this reference for Python backend services, including FastAPI, Django, Flask-style services, ASGI/WSGI deployments, workers, and Python-specific runtime concerns.

## Version and execution model

Verify Python and framework versions plus ASGI/WSGI/server configuration before using version-sensitive APIs. Know whether the application is synchronous, asynchronous, or mixed. Async syntax does not make blocking database/filesystem/SDK calls non-blocking.

## Service boundaries

Keep transport parsing/serialization at the edge and domain/service logic in ordinary Python modules where practical. Use framework dependency systems for request-scoped resources only when they clarify lifecycle and testability.

## Async and blocking I/O

Do not call blocking libraries on an async event loop without an appropriate thread/process strategy. Limit concurrent fan-out; cancellation and timeouts must propagate when possible. CPU-heavy work should not monopolize request workers.

## Django/FastAPI patterns

For Django, preserve transaction boundaries, ORM query visibility, middleware order, settings separation, and request lifecycle semantics. For FastAPI/Starlette, validate Pydantic/schema behavior against installed versions, understand dependency lifecycle, and distinguish request validation from domain validation.

## Production behavior

Do not use in-process memory as durable coordination across multiple workers. Bound uploads, response sizes, batch queries, and task concurrency. Startup checks should validate required configuration and dependency availability without leaking secrets.

## Testing

Test pure domain logic independently, then framework integration, persistence behavior, and representative async/concurrency cases. Use the same serialization/validation rules in tests as production rather than bypassing them with unchecked objects.