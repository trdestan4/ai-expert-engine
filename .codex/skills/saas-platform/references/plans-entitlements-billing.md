# Plans, Entitlements and Billing

Separate marketing plan names, provider price IDs, billing state and product entitlements. The browser/UI is never authoritative for access.

## Entitlements

Model capabilities/limits server-side from subscription/account policy. Prefer stable entitlement keys over scattering `plan === pro` checks. Support grace/trial/past-due/cancel-at-period-end and manual/enterprise overrides explicitly.

Entitlement changes can be migrations: old/new plans may overlap, grandfathering may exist and users can downgrade below current usage. Define which resources become read-only, blocked or retained.

## Billing lifecycle

Provider subscription/payment state is a state machine. Handle checkout completed, invoice paid/failed, trial end, subscription update/cancel, refund/dispute and webhook replay/out-of-order according to provider semantics. Reconcile periodically rather than trusting one webhook forever.

## Upgrades/downgrades

Define proration, effective time, credit, quota changes and feature removal. Do not revoke critical data immediately on downgrade without policy/recovery. UI copy must match actual server state.

## Pricing architecture

Separate value metric (seat/usage/storage/etc), packaging and provider billing implementation. Enterprise negotiated terms may require contract overrides. Never trust client-submitted amount/price ID if the user is not authorized to select it.

## Security/operations

Admin comp/override/refund actions need authorization/audit. Sandbox/production provider IDs/secrets never mix. Money uses exact units and provider reconciliation after ambiguous timeouts.
