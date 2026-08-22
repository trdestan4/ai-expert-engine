---
name: release-readiness
description: Makes the final evidence-based go/hold/no-go decision for production releases by checking mandatory quality gates, unresolved blockers, migration/recovery safety, observability, approvals and accepted risk; it does not implement fixes or substitute for domain review.
---

# Purpose

Decide whether a specific release is safe enough to proceed, hold for evidence/remediation, or stop, using explicit release evidence rather than optimism, schedule pressure or a green build alone.

## Use when

- production release, launch, migration cutover or high-impact rollout is imminent;
- R3/R4 changes require a final gate;
- multiple reviewer findings must be reconciled into a release decision;
- the caller asks whether a change is ready for production.

## Do not use when

- implementation or diagnosis is still the primary task;
- a broad repository health audit is requested (`audit-review`);
- independent specialist review has not occurred where risk requires it (`multi-review`);
- the task is only CI/CD mechanics (`devops-deployment`).

## Inputs

Require the release/change identity, intended environment, risk classification, changed surfaces, test/build evidence, reviewer findings, security/privacy/accessibility/performance evidence where applicable, deployment artifact identity, migration/worker/job dependencies, configuration/secrets status, observability/alerting, rollback or safe roll-forward plan, known incidents/limitations and explicit risk acceptances.

## Workflow

### 1. Identify release boundary
Name commit/artifact/version, environment, traffic scope, feature flags, migrations, jobs and external dependencies. A vague “latest main” is insufficient for high-risk release approval.

### 2. Determine mandatory gates
Use `references/release-gates.md`. Gates depend on actual changed boundaries and risk; do not run every possible review for every release.

### 3. Verify evidence freshness
Confirm tests/reviews/artifacts correspond to the candidate being released. Evidence from an older commit/build cannot approve a different artifact without justification.

### 4. Reconcile blockers and accepted risk
Use `references/risk-acceptance-rollback.md`. Critical/high unresolved issues default to HOLD/NO-GO unless a documented authority accepts a risk that is genuinely accept-able and recovery is credible.

### 5. Validate deployment and data safety
Check environment/secrets, migration compatibility, background workers, callbacks, cache/schema ordering, external-provider modes and whether old/new versions can coexist during rollout.

### 6. Validate recovery
Know the exact rollback, feature-disable, traffic-revert, data-recovery or roll-forward path. Destructive data changes without proven recovery can block release even when application rollback exists.

### 7. Validate observation window
Ensure critical journeys, health signals, logs/metrics/traces and actionable alerts can detect material failure during rollout. Define who watches and what triggers abort/rollback.

### 8. Issue decision
Return one of:
- **GO** — mandatory gates satisfied; residual risk explicit;
- **GO WITH CONDITIONS** — non-blocking conditions/monitoring/limited exposure are explicit and owned;
- **HOLD** — missing evidence or remediable blocker prevents approval;
- **NO-GO** — known unacceptable risk makes release unsafe.

## Decision rules

- Green CI is necessary evidence, not sufficient release evidence.
- The released artifact must be traceable to the reviewed/tested source.
- R3/R4 trust/data/payment/production boundaries require independent relevant review.
- Critical security, cross-tenant, payment-duplication, destructive-data or unrecoverable migration defects block release by default.
- Missing required evidence produces HOLD, not an assumed pass.
- Accepted risk must identify owner/authority, rationale, exposure, mitigation and follow-up/expiry where relevant.
- Rollback plans must match the actual failure mode; application rollback does not restore destroyed data.
- Progressive rollout reduces blast radius only when observability and stop controls are real.
- Schedule pressure never changes technical severity.

## Reference routing

Load `references/release-gates.md` for gate selection and evidence matrix.
Load `references/risk-acceptance-rollback.md` for blocker handling, risk acceptance, rollback/roll-forward and abort criteria.
Use selected reviewer profiles through `multi-review` when required evidence is missing.

## Quality gates

- Candidate commit/artifact/environment are explicit.
- Mandatory gates are derived from risk/change surface.
- Evidence is current for the release candidate.
- All blockers have disposition; none are silently omitted.
- Migration/data recovery and deployment recovery are distinguished.
- Production observation/abort criteria exist for material releases.
- Risk acceptance is explicit and attributable when used.
- Decision is exactly GO, GO WITH CONDITIONS, HOLD or NO-GO with reasons.

## Failure handling

If artifact identity or required evidence is missing, issue HOLD and name the evidence needed. If a blocker cannot be safely mitigated or accepted, issue NO-GO. If the release candidate changes after review, invalidate affected evidence and re-run only the gates touched by the change.

## Output contract

Return release identity, risk/change surface, mandatory gates and evidence status, unresolved findings, accepted risks, deployment/migration/recovery plan, observability/abort criteria, final GO/GO WITH CONDITIONS/HOLD/NO-GO decision and exact conditions for changing that decision.