# Idempotency, Rate Limits, and Error Contracts

Use this reference for operations where retries, duplicate delivery, overload, or machine-readable failure behavior affect consumers.

## Idempotency

HTTP method semantics are not enough for every business operation. For retryable side-effecting operations such as payment/order/booking creation, define an idempotency key or equivalent deduplication contract when duplicate execution would cause harm. Specify scope (consumer/account/endpoint), request-fingerprint behavior, retention window, concurrent same-key handling, and whether the original result is replayed.

Do not store idempotency state only in process memory when multiple instances/restarts are possible.

## Error contracts

RFC 9457 is the current Problem Details standard for HTTP APIs and obsoletes RFC 7807. Use it when it fits the product rather than inventing a weak `{error: string}` shape. `type`, status/title semantics, stable extension fields, and field-level validation information should be documented. Do not require clients to parse human-readable `detail` text.

## Rate limits and overload

Separate product quota, abuse prevention, expensive-operation protection, and capacity shedding. Provide stable machine-readable signals and `Retry-After` where meaningful. Avoid a single global limit that punishes unrelated cheap and expensive operations equally.

## Retries

Only recommend retry for failures that are plausibly transient and only when duplicate execution is safe. Bound attempts and coordinate retry policy with server timeout/idempotency behavior to avoid retry storms.