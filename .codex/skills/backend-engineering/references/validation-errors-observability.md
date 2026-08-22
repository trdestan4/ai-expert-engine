# Validation, Errors, Observability, and Configuration

This reference defines backend boundary discipline shared across frameworks.

## Validation layers

Distinguish transport/schema validation from domain invariants. Transport validation answers whether input is shaped and typed correctly; domain validation answers whether the requested transition is allowed. Avoid duplicating the same rule in multiple layers unless each layer protects a different boundary.

Normalize external data before business logic. Preserve machine-readable field locations/codes for expected validation failures.

## Error taxonomy

Classify errors into expected domain failures, validation failures, conflicts, not-found, dependency/transient failures, infrastructure failures, and programmer defects. Map them once at the transport/API edge. Do not catch broad exceptions merely to return success-shaped responses.

## Observability

Structured logs should record operation, stable identifiers, outcome, latency, dependency/error class, and trace correlation where available. Metrics answer trends; traces answer causal request paths; logs provide event detail. Do not use logs as a substitute for persisted domain state.

Redact tokens, credentials, secrets, authorization headers, payment data, and unnecessary PII. Avoid logging full request/response bodies by default.

## Configuration

Validate required configuration early. Separate configuration shape from secret values. Keep environment-specific values outside source control and avoid scattered `if production` branches. A missing security-critical configuration should fail closed rather than silently choosing a permissive fallback.