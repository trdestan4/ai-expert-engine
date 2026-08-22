# Cart / Checkout / Orders

A cart is provisional state: items can become unavailable, prices can change and promotions can expire. Revalidate before order/payment commitment and explain recoverable changes to the user. Define anonymous cart identity, authenticated merge behavior and expiration.

Checkout should have a clear server-side state machine for address/shipping/tax/payment/order creation. Duplicate submissions, browser reloads and provider retries must not create duplicate charges/orders. Use idempotency and verified provider events through the integrations layer.

Orders need explicit payment, fulfillment, cancellation, return and refund states, including partial quantities/amounts. Preserve immutable historical commercial facts where needed instead of rereading today's product price/name. Failed provider callbacks require reconciliation.