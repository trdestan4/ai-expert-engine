# Node.js Runtime and Service Patterns

Use this reference only when the backend actually runs on Node.js or a Node-based server framework.

## Version and runtime evidence

Read the installed Node/runtime/framework versions before applying framework-specific APIs. Distinguish long-lived servers from serverless/edge execution because process lifetime, connection reuse, filesystem assumptions, timers, background work, and global caches behave differently.

## Service structure

Keep transport handlers thin enough that business rules can be tested without HTTP objects. Prefer explicit service/domain functions with typed inputs and outputs over passing framework request objects deep into the application.

Use dependency injection through constructors/functions/module composition when it improves testability and lifecycle control; avoid service-locator style global mutation.

## Async behavior

Every external call needs an intentional timeout and cancellation story where supported. Avoid sequential awaits for independent I/O. Do not launch fire-and-forget promises for work that must survive request completion or process termination; durable background work belongs to a queue/worker system.

## Resource lifetime

Reuse database/HTTP clients according to provider/runtime guidance, but never assume process globals are durable state. Bound request bodies, file buffers, batch sizes, and concurrency. Stream large payloads when it materially reduces memory pressure.

## Failure and observability

Preserve causal errors internally. Map expected domain errors separately from dependency/programmer faults. Structured logs should carry operation/request correlation without including credentials, tokens, full authorization headers, or unnecessary PII.