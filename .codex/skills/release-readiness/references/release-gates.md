# Release Gates and Evidence Matrix

Select gates from changed boundaries and risk. The final decision is bound to an exact candidate **and target environment**; staging/preview evidence is supporting evidence, never production authorization by itself.

## Baseline gates

For every material production release establish:
- exact commit/artifact/version and immutable trace from reviewed source;
- explicit target environment and traffic/tenant scope;
- build/type/lint/test evidence required by repository policy for this candidate;
- open reviewer findings and accepted-risk status;
- environment config/secrets/provider modes/callbacks;
- deployment/migration ordering;
- recovery path and post-deploy verification.

## Conditional gate matrix

### Identity/security/tenant/secrets
Require relevant independent security review, negative authorization/tenant tests and verified production configuration. Privileged client secret or cross-tenant bypass blocks by default.

### Payments/billing/credits/entitlements
Require authoritative amount/entitlement boundary, idempotency/reconciliation evidence, duplicate/out-of-order failure tests and security/QA review. Browser redirect/client state is never payment proof.

### Schema/data migration
Require compatibility/coexistence analysis, representative migration/backfill evidence, backup/restore or roll-forward path, data integrity/reconciliation and owner review. Application rollback is not data recovery.

### Public API/event contract
Require compatibility/contract tests, version/deprecation/coexistence evidence and consumer rollout plan when independently deployed clients exist.

### User-facing interaction
Require QA; accessibility for semantic/keyboard/AT-relevant changes; design review for material visual/product direction changes. Verify long content/locales/responsive states when relevant.

### Performance/capacity
Require before/after or representative measured evidence and explicit budget/SLO for critical hot paths. Average-only latency is insufficient when tail risk matters.

### Async/queue/webhook
Require duplicate/retry/out-of-order/idempotency, poison/DLQ/reconciliation and worker shutdown/deployment coexistence evidence.

### Privacy-sensitive data
Require data-map/lifecycle/access review and current jurisdiction-specific claims verified separately when material.

### AI/tool execution
Require tool/action authorization, prompt/retrieval trust-boundary controls, secret isolation, cost/abuse limits and adversarial evals appropriate to risk.

### Broad infrastructure/production rollout
Require IaC/permission diff, observability/alerts, rollback/roll-forward, named watch owner and measurable abort criteria.

## Evidence freshness

Evidence must correspond to the candidate, environment and relevant configuration. Rebuilds, changed lockfiles, flags, provider IDs, environment variables, migrations or post-review commits can invalidate affected evidence.

Release decisions must expire. Shorter TTL is appropriate for R3/R4 and production because config, dependency/provider state and accepted risk can change. Expired decisions require regeneration from current evidence.

## Gate outcomes

- **GO:** all mandatory evidence present, no effective blockers, risks acceptable under policy.
- **GO WITH CONDITIONS:** no effective blockers, but explicit operational conditions remain; technical enforcement requires condition acknowledgement where configured.
- **HOLD:** evidence/config/environment/review is incomplete or stale but a safe path to resolve exists.
- **NO-GO:** known blocker cannot be safely remediated/accepted for this release or recovery is unacceptable.

Schedule pressure does not alter gate requirements.
