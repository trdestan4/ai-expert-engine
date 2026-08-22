# Phase 06 Routing — Business / Growth

Use the smallest business skill set that owns the decision.

## Primary ownership

- crawl/indexation, structured data, search architecture, international/local/product SEO → `seo`
- messaging, copy, value proposition, microcopy, ethical CRO → `content-conversion`
- catalog, variants, inventory, pricing, cart, checkout, orders, refunds, commerce discovery → `ecommerce`
- organizations/workspaces, memberships, plans, entitlements, seats, usage, SaaS lifecycle → `saas-platform`

## Typical routes

**Corporate marketing site:** `product-strategy` → creative/design skills → `content-conversion`; add `seo` for indexable/search scope.

**SEO-only technical audit:** `seo`; add `performance` only when measured runtime issues are part of the cause.

**Ecommerce product/checkout build:** `ecommerce` + relevant frontend/backend/data; add `integrations` for payments/webhooks, `seo` for search/product markup, `security` for payment/account risk.

**SaaS team billing feature:** `saas-platform` + `identity-access` + `integrations`; add `database-data` for schema/RLS and `security` when tenant/entitlement boundaries change.

**Landing page conversion rewrite:** `content-conversion`; add `ux-ui-design` only for layout/interaction and `seo` only for search intent/indexation.

## Overlap prevention

`seo` owns discoverability, not generic copy. `content-conversion` owns communication/decision friction, not crawler mechanics. `ecommerce` owns commerce domain state, while provider payments belong to `integrations`. `saas-platform` owns tenant/plan/entitlement product logic, while authentication belongs to `identity-access` and persistence enforcement belongs to `database-data`.

## Mandatory gate escalation

- Checkout/payment/order changes → `security` + `testing-qa`; `integrations` when provider side effects exist.
- Cross-tenant SaaS membership/entitlement changes → `security` + `testing-qa`; `database-data` where RLS/schema changes.
- Large SEO migrations → `testing-qa`/release verification and `performance` when rendering/runtime changes.
- Conversion experiments involving consent/personalization → `privacy-compliance`.

## Token rule

Do not load all four business skills by default. Marketing page copy may need only `content-conversion`; a catalog inventory bug may need only `ecommerce` plus debugging/data. Load specialist references only for the relevant vertical/problem.