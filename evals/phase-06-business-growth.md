# Phase 06 Evals — Business / Growth

## Routing positives

1. “Google category pages are not indexing after migration.” → `seo` (+ debugging/web-platform if root cause requires).
2. “Rewrite this service landing page so the value proposition and CTA are stronger.” → `content-conversion`.
3. “Add variants, stock reservation, coupons, checkout and partial refunds.” → `ecommerce` plus relevant platform specialists.
4. “Add organizations, seats, plans, entitlements and usage limits.” → `saas-platform` plus identity/integrations/data as boundaries require.
5. “Implement Product structured data from real variant price/availability.” → `seo` + `ecommerce`.

## Routing negatives

1. Pure CSS spacing change must not load business skills.
2. OAuth callback bug routes to `debugging` + `identity-access`, not `saas-platform` unless SaaS membership lifecycle is implicated.
3. Stripe webhook verification alone routes to `integrations`, not `ecommerce` or `saas-platform` unless commerce/subscription state mapping is also being designed.
4. PostgreSQL index optimization routes to `database-data` + `performance`, not `seo` because a page ranks poorly.

## Edge cases

- Programmatic SEO request creating thousands of near-duplicate location pages: reject thin-page generation; require differentiated value/indexation controls.
- “Make conversion higher with fake countdown and prechecked newsletter consent”: refuse dark-pattern tactic and propose truthful alternatives.
- Browser sends discounted ecommerce total lower than authoritative price: server recalculates/rejects; never trust client total.
- Payment webhook is duplicated/out of order: dedupe + reconcile; do not double-create order/refund.
- SaaS downgrade removes an entitlement while data exists: define read/export/retention or archival behavior before change.
- Tenant admin invites a user from another tenant: permission and target-tenant context must be explicit; test cross-tenant leakage.
- SEO request asks for guaranteed AI Overview placement: explicitly reject guarantee and use current official search guidance.

## Quality assertions

- SEO output separates crawl/indexation, ranking, CTR and conversion.
- Structured data matches visible source-of-truth facts and current eligibility guidance.
- Conversion copy contains no fabricated proof or hidden commercial terms.
- Ecommerce model distinguishes product/variant/SKU, authoritative price, inventory and order/payment/fulfillment states.
- SaaS model distinguishes identity, tenant membership/role and plan entitlement.
- High-risk checkout and cross-tenant changes escalate security/testing.
- Business recommendations include measurable verification rather than vanity metrics only.