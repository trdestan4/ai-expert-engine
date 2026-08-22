# Phase 09 Routing — Final Control

## Ownership
- `multi-review`: independent review of a material change using selected reviewer lenses; consolidates findings but does not approve release.
- `audit-review`: broad repository/system health and systemic-risk audit using representative evidence; does not debug one bug or approve one release.
- `release-readiness`: final production go/hold/no-go decision for a specific candidate using current evidence and unresolved-risk disposition.

## Reviewer profiles
Reviewer profiles under `engine/reviewers/` are loaded only through `multi-review` or when `release-readiness` needs a missing mandatory review. They are not discoverable implementation skills.

Available lenses:
- code-reviewer
- design-reviewer
- security-reviewer
- performance-reviewer
- qa-reviewer
- release-reviewer

## Common routes
- significant feature/refactor before completion → owning skills → checks → `multi-review` with selected lenses.
- broad repository health request → `repository-intelligence` → `audit-review` → targeted specialists for confirmed findings.
- production release → implementation/checks → risk-specific reviews or `multi-review` → `release-readiness`.
- R3/R4 auth/data/payment/tenant change → security + QA review mandatory; production release also requires release reviewer/readiness.
- material visual redesign → design + QA review; accessibility specialist when semantics/interaction change.
- measured hot-path change → performance + QA review.
- destructive migration → database/data owner + QA + release review; `release-readiness` requires recovery evidence.

## Anti-patterns
- do not load all reviewers for routine work;
- do not let the implementation owner mark its own R3/R4 review complete without independent evidence;
- do not convert an audit score into release approval;
- do not downgrade blockers because a deadline exists;
- do not treat CI green, reviewer majority, or tool output as sufficient proof by itself.

## Completion
A final-control task closes only when selected review/audit evidence is recorded, findings have disposition, coverage gaps are explicit, and release tasks end in one valid release state.