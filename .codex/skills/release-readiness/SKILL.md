---
name: release-readiness
description: Makes the final evidence-based production GO, GO WITH CONDITIONS, HOLD or NO-GO decision by checking candidate identity, persistent findings, quality gates, migration/recovery, observability and accepted risk; automation is enforceable only when the release gate is wired.
---

# Purpose
Decide whether a specific production candidate may proceed using current candidate-bound evidence rather than optimism, schedule pressure or green CI alone.

## Use when
- production release, launch, migration cutover or high-impact rollout is imminent;
- R3/R4 work requires a final gate;
- reviewer findings must be reconciled into a release decision.

## Do not use when
- implementation/diagnosis remains primary;
- systemic repository audit is requested (`audit-review`);
- mandatory independent review has not occurred (`multi-review`);
- only CI/CD mechanics are requested (`devops-deployment`).

## Inputs
Require candidate commit/artifact/version, environment, risk/change surfaces, current test/build evidence, persisted reviewer findings where available, security/privacy/accessibility/performance evidence when relevant, migration/jobs/config/secrets state, observability, rollback/roll-forward/data recovery and explicit accepted risks.

## Workflow
### 1. Identify candidate
Name exact commit/artifact/environment/traffic scope/flags/migrations/jobs/dependencies. Vague “latest main” is insufficient for high risk.

### 2. Determine gates
Use `references/release-gates.md` based on actual boundaries/risk.

### 3. Verify evidence freshness
Evidence must correspond to this candidate. Older tests/reviews cannot approve a changed artifact without justification.

### 4. Reconcile persistent blockers and accepted risk
Use `references/risk-acceptance-rollback.md`. Open critical/high blockers default to HOLD/NO-GO. Accepted risk does not rewrite severity and must retain accountable disposition/expiry.

### 5. Validate deployment and data recovery
Check environment/secrets, migrations, workers, callbacks, cache/schema ordering, provider modes, coexistence and exact rollback/roll-forward/data recovery. Application rollback does not restore destroyed data.

### 6. Validate observation and abort
Ensure critical journeys, logs/metrics/traces/alerts, watcher ownership and abort/rollback triggers exist for material rollout.

### 7. Build candidate-bound decision artifact
When local runtime tools are available, use `scripts/build_release_decision.py` with the actual evidence paths. The output records evidence paths plus their deterministic hash and must validate against the release-decision schema.

### 8. Issue and classify enforcement
Decision is exactly GO, GO WITH CONDITIONS, HOLD or NO-GO. If production workflow invokes `scripts/release_gate.py` or the reusable AI Expert Release Gate, report **enforced**; otherwise explicitly report **advisory**. A HOLD/NO-GO can never be translated into deploy permission by automation.

## Decision rules
- Green CI is necessary evidence, never sufficient release evidence.
- Released artifact must trace to reviewed/tested source.
- R3/R4 requires relevant independent review.
- Critical security, cross-tenant, payment duplication, destructive data or unrecoverable migration defects block by default.
- Missing required evidence produces HOLD.
- Accepted risk identifies owner/authority, rationale, exposure, mitigation and expiry/follow-up.
- Data recovery and application rollback are different.
- Progressive rollout helps only with real observability and stop controls.
- Schedule pressure never changes severity.
- A copied/stale release artifact whose candidate/evidence hash no longer matches must fail technical enforcement.

## Reference routing
Load `references/release-gates.md` for evidence/gate selection. Load `references/risk-acceptance-rollback.md` for blocker handling, accepted risk, rollback/roll-forward and abort criteria. Use `multi-review` for missing mandatory reviewer evidence.

## Quality gates
- Candidate commit/artifact/environment are explicit.
- Mandatory gates derive from risk/surface.
- Evidence freshness and candidate binding are verified.
- Persistent blockers have explicit disposition.
- Migration/data recovery and application recovery are distinguished.
- Observation/abort criteria exist for material release.
- Decision is exactly one allowed state.
- Enforcement status is reported honestly as enforced or advisory.

## Failure handling
If artifact identity/evidence is missing, issue HOLD. If a blocker cannot be safely remediated/accepted, issue NO-GO. Candidate changes invalidate affected evidence. If release-gate integration is absent, do not claim technical prevention: report the decision as advisory until deployment workflow is wired.

## Output contract
Return candidate/environment, risk/surface, mandatory gates/evidence status, unresolved/persisted findings, accepted risks, deployment/migration/recovery, observability/abort criteria, final GO/GO WITH CONDITIONS/HOLD/NO-GO and enforcement status.
