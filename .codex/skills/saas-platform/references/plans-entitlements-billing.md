# Plans / Entitlements / Billing

Separate marketing plan names from machine-enforced entitlements. Plans map to capabilities, limits, seats or support levels; runtime checks should consume server-authoritative entitlements rather than scattered string comparisons.

Subscription lifecycle needs states for trial, active, scheduled change, past-due/grace, canceled and terminated as relevant to the business. Provider webhooks can be delayed, duplicated or out of order; verify, dedupe and reconcile through `integrations`.

Define upgrade/downgrade timing, proration responsibility, seat overage behavior and what happens to data/features no longer entitled. Billing success is not authorization by itself; entitlement changes should follow a controlled internal state transition.