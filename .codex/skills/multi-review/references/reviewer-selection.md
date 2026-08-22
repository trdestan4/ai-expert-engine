# Reviewer Selection

Select reviewers by changed boundary and risk, not by habit.

## Default lenses
- code-reviewer: non-trivial implementation/refactor, type/error/dependency correctness.
- design-reviewer: user-facing visual/UX/product-surface changes.
- security-reviewer: auth/authz, secrets, input trust, tenant/data boundaries, payments, AI tools, uploads or production controls.
- performance-reviewer: hot paths, bundle/rendering, DB/query/load/cache/concurrency or media-heavy changes.
- qa-reviewer: behavior-changing features, migrations, async/retry flows, compatibility and regression risk.
- release-reviewer: deployment/migration/config/rollback/operability and production launch risk.

## Mandatory escalation
- R3/R4 security/data/payment/tenant boundary: security-reviewer + qa-reviewer; release-reviewer when production-bound.
- destructive migration or difficult rollback: qa-reviewer + release-reviewer + relevant data specialist.
- material user-facing redesign: design-reviewer + qa-reviewer; accessibility specialist if interaction/semantic behavior changes.
- material performance-sensitive change: performance-reviewer + qa-reviewer.
- broad multi-domain release: choose only relevant lenses, but release-reviewer is mandatory.

## Exclusions
Do not activate reviewers with no changed boundary to inspect. A reviewer may request a domain specialist when the evidence needed exceeds its lens.