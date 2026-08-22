# Usage, Quotas and Metering

## Definitions

Separate usage event, aggregation window, quota/limit, entitlement, billing meter and analytics. A dashboard counter is not necessarily billing-authoritative.

Choose the value metric and unit precisely: request, token, seat-day, GB-month, active contact, build minute. Define rounding, timezone/window, resets, late events and corrections.

## Idempotent metering

Usage events need stable identity/dedup when retries are possible. Durable source data should permit reconciliation/replay. Avoid incrementing a mutable counter as the only evidence for billable usage when financial accuracy matters.

## Quota enforcement

Enforce server-side at the operation boundary. Consider concurrency so two simultaneous requests cannot both pass the last unit if the limit is strict. Some limits are soft/alerting; others hard. Define grace/burst behavior and customer-visible messaging.

## Aggregation

For high volume, aggregate asynchronously but preserve source/reconciliation. Watch cardinality and hot tenant partitions. Backfills/corrections need versioned meter logic so historical invoices are not silently recalculated with new semantics.

## Customer experience

Expose current usage, unit, window, reset/billing timing and near-limit warnings where helpful. Avoid surprise overages. Enterprise contracts may use different quotas/meters; configuration needs audit/versioning.

## Tests

Cover duplicate events, out-of-order/late events, concurrent limit crossing, plan change mid-window, timezone/reset, refunds/credits and provider reconciliation.
