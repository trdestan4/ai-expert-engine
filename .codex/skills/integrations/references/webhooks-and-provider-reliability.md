# Webhooks and Provider Reliability

## Inbound webhooks

Verify signature, timestamp/replay window and provider-specific signing algorithm using the raw request body when required. Reject invalid signatures before trusting payload fields.

Persist provider event ID or a stable deduplication key before performing non-idempotent effects. Providers commonly retry; duplicate delivery is normal, not exceptional.

Return the provider-required success status quickly after durable acceptance. Long business workflows belong in a queue/worker when possible.

## Ordering and versions

Webhook arrival order may differ from event occurrence order. Reconcile state using provider object version/timestamp/status transitions or fetch current provider state when stale/out-of-order delivery matters.

## Outbound provider requests

Apply explicit connect/read/total timeouts as the client supports. Classify operations as safe to retry, provider-idempotent, application-idempotent or unsafe. Respect `Retry-After` and quota headers.

Use bounded exponential backoff with jitter. Circuit breaking/bulkheads may help repeated dependency failure but should not mask business state.

## Reconciliation

For money, entitlements or other critical external state, run periodic or on-demand reconciliation. Store provider IDs needed to compare internal/provider state and repair drift.

## Observability

Record provider operation, safe request identity, latency, status/error class, retry count and correlation IDs. Do not log full tokens, signatures, payment details or sensitive payloads.

## Tests

Cover bad signature, stale timestamp, duplicate ID, out-of-order event, timeout after provider success, 429, 5xx burst, provider outage, replay, and reconciliation repair.