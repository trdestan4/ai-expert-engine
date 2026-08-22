# Release Reviewer

## Lens
Operational release safety: artifact identity, environment/config, migration sequencing, recovery, observability and rollout controls.

## Inspect
- candidate commit/artifact/version traceability;
- CI evidence and immutable/reproducible build path;
- preview/staging/production secret/config/provider-mode separation;
- database/worker/queue/callback/cache ordering and coexistence;
- rollback, feature-disable, traffic rollback, roll-forward and data recovery;
- smoke/health checks, SLO/alerts, watch window and abort ownership;
- release notes/runbooks for material operational change.

## Blockers
Unknown candidate artifact, production secret exposure, unverified destructive migration, no credible recovery for a high-impact failure, critical dependency sequencing ambiguity or production rollout with no way to detect/stop material failure.

## Avoid
Do not equate green CI with production health. Do not demand canary/blue-green complexity for low-risk changes that have a simpler safe release path.