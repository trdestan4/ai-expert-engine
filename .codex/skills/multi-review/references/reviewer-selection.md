# Reviewer Selection

Select reviewers by changed boundary and risk, not by habit.

## Runtime rule
On Cursor, canonical independent reviewer executors are project subagents under `.cursor/agents/`:
- `code-reviewer`
- `design-reviewer`
- `security-reviewer`
- `performance-reviewer`
- `qa-reviewer`
- `release-reviewer`

Each selected reviewer must run in its own subagent context for the pass to count as independent. `engine/reviewers/*.md` defines the review contract and lens; it is not itself an isolated execution mechanism.

If a runtime lacks isolated subagents, record `review_mode: non-independent` and do not use that pass to satisfy mandatory R3/R4 independent-review evidence.

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
Do not activate reviewers with no changed boundary to inspect. A reviewer may request a domain specialist when evidence needed exceeds its lens.
