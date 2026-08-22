# Risk & Escalation Model

Use risk to decide review depth, not to inflate every task.

## R0 — Cosmetic / informational

Examples: copy, spacing, non-functional styling, documentation typo.

Default: one owner, targeted verification.

## R1 — Normal implementation

Examples: isolated component, ordinary page, internal helper, low-impact API behavior with established patterns.

Default: primary specialist + relevant tests.

## R2 — Cross-layer / contract-sensitive

Examples: full-stack feature, public API shape, shared state model, significant dependency change, non-destructive schema evolution.

Default: plan + affected specialists + integration verification.

## R3 — High risk

Any change involving authentication, authorization, secrets, payments/billing, PII, RLS, destructive/persistent data changes, file trust boundaries, production infrastructure, or security controls.

Default: specialist implementation + mandatory targeted security/data review + rollback/verification strategy.

## R4 — Critical / release-systemic

Examples: major architecture migration, broad production rollout, critical security remediation, disaster recovery, release readiness across multiple domains.

Default: explicit plan, independent reviews, rollback path, release gate, documented unresolved risk.

## Escalation rules

Escalate one level when:

- blast radius is unclear;
- recovery is difficult or irreversible;
- tests cannot cover the changed boundary adequately;
- the system handles sensitive data or money;
- multiple services/tenants are affected;
- production behavior differs materially from local behavior.

Do not de-escalate because a diff is small. Risk follows the boundary being changed, not line count.
