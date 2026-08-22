# Reviewer Selection and Expert Context

Select reviewers from the changed boundary, plausible failure modes and release risk—not from a fixed checklist.

## Independence rule

On Cursor, canonical independent executors live under `.cursor/agents/`: `code-reviewer`, `design-reviewer`, `security-reviewer`, `performance-reviewer`, `qa-reviewer`, `release-reviewer`. Each mandatory pass must run in its own subagent context. `engine/reviewers/*.md` defines the lens; reading that file in the implementation context is not independent review.

If isolated execution is unavailable, record `review_mode: non-independent`. Such a pass can assist remediation but cannot satisfy mandatory R3/R4 independence by itself.

## Expert-context rule

Isolation alone is insufficient for master review. Each reviewer loads:
1. reviewer contract and reviewer profile;
2. its owning expert `SKILL.md`;
3. only deep references relevant to the changed boundary;
4. supporting owner skill only when needed to interpret an invariant.

Default domain mapping:
- code-reviewer → `code-quality`; add `software-architecture` or implementation owner for changed contracts/invariants.
- design-reviewer → `ux-ui-design` + `anti-generic-design`; add color/type/art/motion specialist for that surface.
- security-reviewer → `security`; add `identity-access`, `database-data`, `storage-media`, `integrations` or `ai-engineering` when those trust boundaries change.
- performance-reviewer → `performance`; add frontend/runtime/data/async owner to interpret measured bottleneck.
- qa-reviewer → `testing-qa`; add owning domain for acceptance/invariant semantics.
- release-reviewer → `release-readiness`; add `devops-deployment`, `observability-sre`, `database-data` or other production owner as required.

Do not load all references. The reviewer should be deep on the changed boundary, not broad for its own sake.

## Default selection

- **code-reviewer:** non-trivial implementation/refactor, error/type/contract/state/concurrency or dependency change.
- **design-reviewer:** material user-facing visual/interaction/product-surface change.
- **security-reviewer:** auth/authz, tenant/data boundaries, secrets, untrusted input/files/URLs, payments/webhooks, privileged AI/tools, production controls, meaningful supply-chain change.
- **performance-reviewer:** hot path, web-vitals/bundle/media, database/load/cache/concurrency, queue/worker capacity or provider-latency-sensitive change.
- **qa-reviewer:** behavior-changing feature, bug fix, migration, async/retry flow, compatibility or material regression risk.
- **release-reviewer:** production deployment, migration/config/secrets/provider mode, difficult rollback or material operational change.

## Mandatory escalation matrix

- R3/R4 auth/authz/tenant/secrets/security boundary → security + QA; release when production-bound.
- payment/credit/balance/entitlement enforcement → security + QA; release for production; code/data/integration lens as needed.
- destructive or incompatible data migration → QA + release + database/data specialist.
- untrusted file/parser/SSRF/AI-tool boundary → security + QA; performance if resource abuse/capacity matters.
- material visual/interaction redesign → design + QA; accessibility specialist evidence for semantic/keyboard changes.
- material performance-sensitive change → performance + QA.
- broad production rollout → release mandatory plus only relevant other lenses.

## Reviewer evidence input

Give reviewers the same exact candidate/diff, requirements, relevant tests/runtime evidence and environment assumptions. Do not include another reviewer verdict, desired conclusion or severity suggestion before their pass. If a reviewer needs missing evidence, return a coverage gap or targeted verification request rather than guessing.

## Re-review

After remediation, rerun reviewers whose finding/evidence boundary changed. A new candidate commit can invalidate prior evidence even if the fix is small. Do not rerun unrelated lenses mechanically.

## Exclusions

Do not activate reviewers with no changed boundary. A tiny formatting/copy change does not need six reviewers. Conversely, do not skip security/QA merely because a high-risk authorization diff is two lines.
