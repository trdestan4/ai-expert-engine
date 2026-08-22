# Payments and Billing

## State model

Model payment and subscription lifecycle explicitly: created/pending/requires-action/authorized/succeeded/failed/cancelled/refunded/disputed as applicable to the provider. Do not compress all provider states into a boolean `paid`.

## Checkout and confirmation

Create server-side provider objects from trusted prices/quantities/entitlements. Never trust client-supplied amount/currency/product authorization without server validation. Browser return URLs improve UX but are not authoritative payment confirmation.

## Idempotency

Use provider idempotency keys for create/charge/refund operations where supported and keep an internal operation ID/unique constraint. On network timeout, query/reconcile the known provider operation before creating another payment.

## Webhooks

Verify signatures and deduplicate event IDs. Use webhooks/provider API to converge internal order/subscription state. Handle retries/out-of-order events and store provider customer/payment/subscription/invoice IDs needed for reconciliation.

## Subscriptions

Separate plan/catalog, provider price IDs, billing period, trial, current period, cancel-at-period-end, status and internal entitlements. Entitlements should have deterministic rules for past-due, grace period, cancellation and provider outage.

## Money

Use integer minor units or exact decimal types according to currency/provider rules. Never use binary floating-point for authoritative monetary arithmetic. Record currency explicitly.

## Refunds/disputes

Treat refund/chargeback/dispute as separate state transitions with audit trail and entitlement/order implications. Avoid deleting the original payment record.

## Tests

Cover duplicate checkout submit, required 3DS/action, timeout after success, webhook before redirect, duplicate/out-of-order webhook, partial/full refund, subscription upgrade/downgrade/cancel, failed renewal, dispute and reconciliation.