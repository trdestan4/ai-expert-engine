# Release Reviewer

## Lens
Operational release safety: exact candidate identity, target environment, evidence freshness, migration sequencing, recovery, observability and rollout controls.

## Inspect
- exact commit/artifact/version traceability from reviewed source to deployed artifact;
- release-decision target environment and expiry; staging/preview evidence never silently authorizes production;
- CI evidence plus relevant independent reviewer findings and accepted-risk expiry/ownership;
- immutable/reproducible artifact path, dependencies, provider modes, secrets/config/environment separation;
- database/worker/queue/callback/cache ordering, old/new coexistence and migration irreversibility;
- application rollback, traffic rollback, feature disable, roll-forward and data recovery as distinct mechanisms;
- smoke/health checks, critical journeys, SLO/alerts, watch window, abort thresholds and named ownership;
- canary/progressive rollout only when observability and stop controls make it safer than simpler rollout.

## Evidence standard
Every approval statement must bind to this candidate and environment. Changed lockfiles/config/migrations or post-review commits invalidate affected evidence.

## Blockers
Unknown candidate, environment mismatch, expired decision/accepted risk, production secret exposure, unverified destructive migration, no credible recovery for high-impact failure, critical dependency sequencing ambiguity or production rollout with no detection/abort path.

## Avoid
Do not equate green CI with production health and do not demand canary/blue-green complexity for low-risk changes with a simpler safe path.
