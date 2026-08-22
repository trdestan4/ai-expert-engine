---
name: ecommerce
description: Owns commerce-domain behavior across catalog, products, variants, pricing, inventory, search/filtering, cart, checkout, orders, shipping, tax, discounts, returns/refunds, customer accounts, merchandising, ecommerce analytics, and commerce lifecycle integrity; it coordinates but does not replace payment, database, SEO, security, or UI specialists.
---

# Purpose

Design ecommerce systems that preserve price/inventory/order correctness while producing a low-friction buying experience, operationally manageable catalog and trustworthy post-purchase lifecycle.

## Use when

- product/catalog/variant/inventory/pricing/cart/checkout/order/return/refund logic is involved;
- merchandising, filters/search, discounts/coupons, shipping/tax or customer commerce state needs design;
- an ecommerce product page or checkout needs end-to-end review;
- commerce analytics/events or operational state transitions are required.

## Do not use when

- payment-provider mechanics alone are primary (`integrations`);
- generic API/database/security implementation is primary;
- search crawl/structured-data specifics alone are primary (`seo`);
- SaaS subscriptions/entitlements are the main product (`saas-platform`).

## Inputs

Identify catalog model, variant/options, SKU/inventory source, price/tax/currency rules, promotions, fulfillment/shipping, cart persistence, customer model, payment integration, order statuses, cancellation/refund policy, returns, admin/ops needs, traffic/catalog scale and analytics requirements.

## Workflow

### 1. Model the sellable unit
Separate product presentation from variant/SKU/inventory identity. Define options, bundles, digital/service items and availability semantics.

### 2. Establish price truth
Define authoritative base/sale prices, currency, taxes, discounts, coupons and rounding. Recalculate authoritative totals server-side at checkout/order creation.

### 3. Design inventory semantics
Choose reservation/decrement timing, oversell policy, multi-location behavior and reconciliation. Treat inventory races as correctness problems.

### 4. Build cart and checkout state
Handle anonymous/authenticated carts, merges, invalidated prices/items, shipping methods, address validation, tax, payment handoff and recoverable failure states.

### 5. Model order lifecycle
Use explicit states and idempotent transitions for authorization/payment, fulfillment, cancellation, refund, return and partial operations. Preserve auditability.

### 6. Design discovery
Create category/collection, search/filter/sort and merchandising behavior that works for real catalog scale, URLs and SEO constraints.

### 7. Instrument commerce
Track view/search/filter/product/cart/checkout/purchase/refund events with consistent identifiers and avoid double-counting retry/reload flows.

## Decision rules

- Client-displayed totals are never the source of truth.
- Product, variant, SKU and inventory unit are distinct unless the domain proves otherwise.
- Payment success alone does not define fulfillment/order completion.
- Webhook/provider events require verification, idempotency and reconciliation through `integrations`.
- Inventory and order transitions must tolerate concurrency/retries.
- Checkout should ask only for information required for fulfillment, risk or regulation.
- Filters/facets must balance user usefulness, URL state and crawl/indexation control.

## Reference routing

Load `references/catalog-pricing-inventory.md` for products, variants, SKUs, pricing, discounts and stock.

Load `references/cart-checkout-orders.md` for cart lifecycle, checkout, order states, refunds/returns and failure recovery.

Load `references/discovery-merchandising-analytics.md` for search/filter/category, merchandising, analytics and operational signals.

Load `references/ecommerce-operations-seo.md` for admin/ops, fulfillment boundaries and ecommerce SEO coordination.

## Quality gates

- Sellable-unit and inventory identities are explicit.
- Server-authoritative price/tax/discount validation exists.
- Inventory concurrency/oversell policy is defined.
- Checkout has recoverable states and no duplicate-charge/order path.
- Order/payment/fulfillment/refund states are not conflated.
- Returns/refunds and partial operations are modeled.
- Commerce events are idempotent/deduplicated where necessary.
- Search/filter/category architecture coordinates with SEO and accessibility.

## Failure handling

If tax/shipping/legal rules vary by jurisdiction, do not invent them; model extension points and verify current provider/legal requirements. If payment state and internal state diverge, favor reconciliation rather than guessing. If inventory truth is external, define sync ownership and stale-data behavior.

## Output contract

Return commerce domain model, price/inventory rules, cart/checkout/order state model, discovery/merchandising plan, operational/admin needs, analytics events, failure/reconciliation plan, and specialist handoffs.