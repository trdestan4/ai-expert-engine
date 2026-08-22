# Catalog, Pricing and Inventory

## Product model

Separate product, variant/SKU, option, media, category/collection, attribute, price and inventory concepts according to real merchandising/fulfillment needs. Avoid forcing every catalog into one flat `products` table or over-modeling simple stores.

Variant identity must remain stable across cart/order history even if display copy/media changes. Snapshot order-critical product/price/tax data at purchase where accounting/customer history requires it.

## Pricing

Server-side authoritative pricing. Model currency in exact decimal/minor units; do not trust browser-submitted amount/discount/tax/shipping. Distinguish list/base price, sale/promotion, customer/tier price, coupon, bundle, tax and shipping adjustments so reconciliation is explainable.

For multi-currency, decide price books vs FX conversion, rounding, display/charge currency and refund behavior. Never silently re-convert historical orders using today's FX.

## Promotions

Define eligibility, stacking/priority, usage limits, start/end timezone, minimum spend, customer/product scope and refunds. Make promotion evaluation deterministic and test overlapping rules. “Apply biggest discount” may not match business policy.

## Inventory

Choose source of truth and reservation semantics. Stock displayed to users may differ from physical/on-hand, available-to-promise and reserved. Concurrency must prevent oversell where required using atomic updates/transactions/reservations.

Preorder/backorder require explicit promise/fulfillment behavior, not negative stock hacks. Multi-location inventory needs allocation/reconciliation and failure handling.

## Search/filters

Attributes intended for filtering/sorting should be structured and normalized enough to support consistent values. Avoid unbounded arbitrary metadata as a substitute for a catalog model.

## Data lifecycle

Product deletion/unpublish must preserve historical orders and URLs/SEO strategy. Media/object cleanup, feeds/search indexes and cache invalidation follow catalog lifecycle deliberately.
