# Deployment Strategies, Coexistence and Recovery

Choose the simplest strategy that safely fits blast radius, compatibility and rollback needs.

## Rolling / recreate

Rolling is common when old/new versions can coexist against shared dependencies/schema. Verify backwards/forwards compatibility, readiness and session behavior. Recreate may be acceptable for low-availability internal tools but must acknowledge downtime.

## Blue-green

Useful when rapid traffic switch/rollback matters and duplicate environment cost/config parity are manageable. Shared database/state still limits rollback if new version writes incompatible data.

## Canary / progressive delivery

Expose small traffic/tenant cohort only when metrics/alerts and abort controls can detect harm. Define success/abort before rollout and avoid canarying irreversible schema/data changes without separate safety.

## Feature flags

Flags decouple deploy from release and provide kill switches but create combinatorial states. Define owner, default, targeting, expiry/removal and server-side authorization independence. Do not use a client flag as a security boundary.

## Schema/data coexistence

Use expand → dual-compatible app/backfill → switch → contract for risky migrations. Application rollback and data rollback are different; once new incompatible writes occur, old binaries may no longer be safe.

## Recovery hierarchy

Consider: feature disable, traffic rollback, app rollback, config rollback, dependency/provider failover, roll-forward fix, restore/PITR and reconciliation. Define data-loss window/RPO/RTO where material.

## Release evidence

Candidate, target environment, migration order, worker/queue compatibility, cache invalidation, smoke checks, alerts and named abort owner must be explicit for material production rollout.
