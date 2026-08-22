# Third-Party API Adapters

## Boundary

Expose a narrow internal interface that represents what the application needs, not the provider's entire SDK. Map provider requests/responses/errors inside the adapter and keep provider-specific fields from leaking into unrelated domain code.

## Version and capability

Inspect installed SDK version and current provider API version before changing behavior. Pin/upgrade deliberately; read migration notes for changed defaults, pagination, retries, webhook schemas and deprecated fields.

## Authentication and scopes

Use least-privilege scopes/credentials. Separate publishable/client credentials from server secrets. Keep sandbox/test and production accounts, endpoints, IDs and secrets clearly separated.

## Reliability

Set timeouts on every network call. Respect rate limits. Decide retry behavior per operation. Include idempotency/reconciliation for state-changing calls rather than generic automatic retry middleware.

## Data mapping

Validate provider responses at the trust boundary if malformed/changed data could damage internal state. Normalize external IDs, timestamps and optional fields. Preserve unknown raw payload snapshots only when debugging/audit value justifies retention/privacy cost.

## Degradation

Classify dependency importance. Analytics/recommendation failures may fail open; payment/identity/signature verification usually fail closed or defer. Make fallback behavior visible to product/operations.

## Tests

Use contract fixtures for stable unit tests and small real-provider sandbox tests for critical auth/signature/version behavior. Test missing fields, new enum values, rate limits, timeout, invalid credentials, provider 5xx, pagination and environment mix-up.