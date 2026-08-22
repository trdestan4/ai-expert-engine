# Cart, Checkout and Orders

## Cart

Define guest/auth merge semantics, item identity (SKU/options), quantity bounds, price revalidation and expiration. Cart is intent, not authoritative order/payment state. Reprice/revalidate inventory/promotions at checkout according to business policy and show material changes clearly.

## Checkout orchestration

A robust sequence establishes authoritative cart → customer/contact/address → shipping/tax/promotions → payment intent/authorization → durable order/payment state. Exact order depends on provider/business, but browser redirects and client success flags never prove payment success.

Use idempotency keys for retried create/payment/order operations and reconcile provider state after ambiguous timeout. Prevent duplicate order side effects from webhook/redelivery/retry.

## Order state machine

Model states such as pending payment, paid/authorized, processing, partially fulfilled, fulfilled, cancelled, partially/fully refunded, disputed/chargeback as business requires. Avoid a single `paid` boolean.

Record state transitions/audit evidence and define allowed transitions. Fulfillment/shipping can be partial and independent from financial state.

## Returns/RMA/refunds

Model return eligibility/window, item quantities/condition/reason, shipping/restocking policy, refund method, partial refunds, store credit/gift card and tax/shipping adjustments. Provider refund success and internal state need reconciliation.

## Failure recovery

Handle payment succeeds but order write fails, order succeeds but email fails, webhook arrives before redirect, webhook duplicate/out-of-order, inventory changes mid-checkout and provider outage. Durable reconciliation jobs should repair ambiguous states.

## Security/fraud

Do not store sensitive card data unless intentionally within compliance scope; use provider tokenization/hosted elements when practical. Protect coupon/gift-card/store-credit balances and admin refund actions with authorization, audit and velocity controls.
