# Release Gates

Choose gates from the release surface.

## Baseline
- candidate commit/artifact/environment identified;
- required build/type/lint/tests passed for that candidate;
- known findings dispositioned;
- deploy/config/secrets validated;
- recovery path and post-deploy verification defined.

## Conditional gates
- auth/authz/tenant/secrets/payments/uploads/AI tools: security review + targeted negative tests.
- schema/data migrations: migration compatibility, backup/recovery/roll-forward evidence and data-owner review.
- API/public contract: compatibility/contract tests and rollout/deprecation evidence.
- user-facing interaction: QA + accessibility; design review for material visual/product changes.
- performance-sensitive/hot path: measured performance evidence and regression budget.
- async/webhooks/payments: idempotency/retry/out-of-order/failure-path evidence.
- privacy-sensitive data: privacy/security review with current jurisdiction-specific claims verified separately when needed.
- broad/high-risk production rollout: observability, alerts, owner/watch window and abort criteria.

## Evidence freshness
Evidence must correspond to the candidate. Rebuilds, changed lockfiles/config/migrations or post-review commits can invalidate affected evidence.