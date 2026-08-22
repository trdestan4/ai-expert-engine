---
name: saas-platform
description: Owns SaaS product architecture across organizations/workspaces, tenancy, members/invitations, roles, plans, subscriptions, entitlements, seats, usage metering, quotas, trials, onboarding, admin/support controls, lifecycle events, and SaaS product analytics; it coordinates identity, billing, database, security and product strategy specialists.
---

# Purpose

Design SaaS products whose tenancy, permissions, plans and entitlements remain correct as customers, teams, billing models and operational needs grow.

## Use when

- organizations/workspaces/teams/members/invitations are involved;
- plans, subscriptions, trials, seats, entitlements, quotas or usage-based billing need architecture;
- multi-tenant SaaS onboarding, admin/support tooling or lifecycle state must be designed;
- product features must vary safely by tenant/plan/role/usage.

## Do not use when

- authentication mechanics alone are primary (`identity-access`);
- payment-provider integration alone is primary (`integrations`);
- generic RLS/schema work alone is primary (`database-data`);
- general product prioritization is primary (`product-strategy`).

## Inputs

Identify account/tenant model, individual vs organization use, membership/invitation flow, role model, plan catalog, billing provider, subscription lifecycle, seat rules, entitlement model, metered features, quota/reset period, trials, upgrades/downgrades, cancellation, grace periods, support/admin capabilities and audit requirements.

## Workflow

### 1. Define tenant/account boundaries
Choose personal accounts, organizations/workspaces or hybrid model. Make resource ownership and tenant switching explicit.

### 2. Model membership and permissions
Separate identity from tenant membership. Define invitation acceptance, role changes, last-owner/admin protection, offboarding and cross-tenant isolation.

### 3. Separate billing from entitlement
Billing provider state is evidence, not the runtime authorization model. Map plans/subscriptions to internal entitlements/features with explicit effective dates and fallback behavior.

### 4. Model lifecycle transitions
Handle trial start/end, activation, upgrade, downgrade, cancellation, non-payment, grace, resume and account deletion. Make webhook retries idempotent and reconcile provider state.

### 5. Design usage and quotas
Define measurement event, aggregation, period, limits, soft/hard enforcement, race behavior and user-visible usage. Metering must be auditable for billed usage.

### 6. Build operator controls
Support needs impersonation alternatives, safe account lookup, subscription/entitlement inspection, controlled overrides, audit logs and reversible interventions.

### 7. Measure product health
Track activation, adoption, retention, expansion/churn and feature usage with tenant/user distinctions and privacy-aware instrumentation.

## Decision rules

- User identity is not the tenant.
- Tenant membership/role and paid entitlements are separate dimensions.
- Never trust a client-side plan flag for authorization.
- Provider webhooks require verification, idempotency and reconciliation.
- Entitlements should be explicit capabilities/limits, not scattered `plan === pro` conditionals.
- Downgrades need data/feature behavior before they occur.
- Usage billing requires deterministic metering and auditability.
- Support overrides need scope, expiry/reason and audit history.

## Reference routing

Load `references/tenancy-membership-permissions.md` for org/workspace ownership, memberships, invitations and roles.

Load `references/plans-entitlements-billing.md` for plans, subscriptions, feature entitlements, seats, trials and lifecycle mapping.

Load `references/usage-quotas-metering.md` for limits, counters, usage events and metered billing.

Load `references/onboarding-admin-analytics.md` for activation, tenant onboarding, operator tooling, audits and SaaS metrics.

## Quality gates

- Tenant/resource ownership is explicit and testable.
- Cross-tenant access defaults to deny.
- Membership/role changes protect critical ownership invariants.
- Entitlements are server-authoritative and decoupled from presentation.
- Subscription lifecycle handles retries/out-of-order events/reconciliation.
- Upgrade/downgrade/cancel/grace behavior is defined.
- Metered usage has deterministic event/period/limit semantics.
- Admin/support actions are permissioned and auditable.

## Failure handling

If billing provider state is ambiguous, reconcile rather than infer from one webhook. If a plan change would invalidate stored data, require an explicit downgrade policy. If tenancy model is unclear, do not implement scattered tenant IDs until ownership/invariants are defined.

## Output contract

Return tenant/account model, membership/permission rules, plans/entitlements, subscription lifecycle, usage/quota model, onboarding/admin requirements, analytics metrics, failure/reconciliation behavior and specialist handoffs.