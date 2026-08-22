# Ecommerce Operations, Feeds, Marketplace and SEO

## Operations

Commerce crosses catalog, support, finance, fulfillment and marketing. Define ownership for order exceptions, failed payments, stuck fulfillment, refunds/disputes, inventory drift, feed failures and provider reconciliation. Admin tools need least privilege and audit for money/inventory actions.

## Marketplace / multi-vendor

If sellers/vendors exist, model merchant identity, catalog ownership, commissions/fees, payout state, refunds/disputes, seller permissions, moderation and tax/compliance handoff. Marketplace money movement is materially different from single-merchant checkout; use provider marketplace primitives when available rather than inventing ledger/payout flows casually.

## Gift cards/store credit

Treat balances as money-like value with exact units, authorization, idempotent ledger/transactions, expiration/legal policy verification and refund behavior. Do not model only as mutable balance without audit trail for high-value systems.

## Feeds/integrations

Product feeds to Google/Meta/marketplaces need stable IDs, availability/price consistency, currency, shipping/tax fields and monitoring. Provider catalog drift requires reconciliation and alerting.

## SEO

Product/category URLs need canonical strategy, structured data matching visible/authoritative product state, pagination/faceted crawl controls and lifecycle for discontinued/out-of-stock items. Do not mark misleading availability/price in structured data.

## International

Coordinate locale/domain/subdirectory/hreflang strategy, translated catalog, currency/price book, tax/shipping availability and legal copy. Currency switching is not localization by itself.
