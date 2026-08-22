---
name: release-readiness
description: Makes the final evidence-based GO, GO WITH CONDITIONS, HOLD or NO-GO decision for an exact candidate and target environment by checking current quality/reviewer evidence, persistent and accepted-risk expiry, migration/recovery, observability and technical gate enforcement.
---

# Purpose
Decide whether a specific candidate may enter a specific production environment using current candidate/environment-bound evidence rather than optimism, schedule pressure or green CI alone.

## Use when
- production release, launch, migration cutover or high-impact rollout is imminent;
- R3/R4 work requires a final gate;
- reviewer findings and accepted risks must be reconciled into a release decision.

## Do not use when
- implementation/diagnosis remains primary;
- systemic repository audit is requested (`audit-review`);
- mandatory independent review has not occurred (`multi-review`);
- only CI/CD mechanics are requested (`devops-deployment`).

## Inputs
Require exact candidate commit/artifact/version, **target environment**, risk/change surfaces, current test/build/runtime evidence, persisted reviewer findings, security/privacy/accessibility/performance evidence when relevant, migrations/jobs/config/secrets/provider state, observability, rollback/roll-forward/data recovery, accepted risks with future expiry and desired rollout scope.

## Workflow
### 1. Identify candidate and environment
Name exact commit/artifact plus target environment, traffic/tenant scope, flags, migrations, jobs and provider modes. Vague “latest main” or “same as staging” is insufficient for high risk.

### 2. Determine mandatory gates
Use `references/release-gates.md` from the actual changed boundaries/risk rather than running every gate indiscriminately.

### 3. Verify evidence binding and freshness
Evidence must correspond to this candidate and relevant target-environment configuration. Changed code, lockfile, migration, secret/config, flag or provider mode can invalidate affected evidence.

### 4. Reconcile findings and accepted risk
Use `references/risk-acceptance-rollback.md`. Open effective blockers produce HOLD/NO-GO. Accepted risk retains severity, authority/rationale/mitigation and a **future expiry**; once expired it becomes an effective blocker again.

### 5. Validate deployment and recovery
Check environment/secrets, migrations, workers, queues/callbacks, cache/schema ordering, old/new coexistence and exact feature-disable/rollback/roll-forward/data-recovery paths. Application rollback does not restore destroyed data.

### 6. Validate observation and abort
Ensure critical journeys, logs/metrics/traces/alerts, candidate/cohort correlation, watcher ownership and measurable abort/rollback triggers exist for material rollout.

### 7. Build enforceable decision artifact
When local tools are available, use `scripts/build_release_decision.py` with exact candidate, target environment, current evidence paths and appropriate expiry/TTL. The artifact must validate against release-decision schema and bind evidence by deterministic hash.

### 8. Issue decision and classify enforcement
Decision is exactly GO, GO WITH CONDITIONS, HOLD or NO-GO. Technical enforcement requires deployment to invoke `scripts/release_gate.py` (or reusable AI Expert Release Gate) with the **actual target environment**. A staging GO never authorizes production. Expired/mismatched candidate/environment/evidence fails enforcement. Otherwise report decision as advisory.

## Decision rules
- Green CI is necessary evidence only for what it checks; never sufficient release proof.
- Released artifact traces to reviewed/tested source.
- R3/R4 requires relevant independent expert review.
- Critical security, cross-tenant, unauthorized money/action, destructive data or unrecoverable migration defects block by default.
- Missing/stale/environment-mismatched mandatory evidence produces HOLD.
- Accepted blocker risk needs accountable authority, rationale, containment, monitoring and future expiry.
- Data recovery and application rollback are different.
- Progressive rollout helps only with real observability and stop controls.
- Schedule pressure never changes severity or gate state.
- Candidate/environment/evidence/expiry mismatch must fail technical enforcement.

## Reference routing
Load `references/release-gates.md` for gate/evidence selection. Load `references/risk-acceptance-rollback.md` for acceptance, recovery and abort criteria. Use `multi-review` when mandatory independent evidence is missing; owning production/data/security skills supply missing domain evidence.

## Quality gates
- Exact candidate and target environment are explicit.
- Mandatory gates derive from risk/change surface.
- Evidence is current and bound to candidate/environment.
- Effective blockers include expired accepted risks.
- Migration/data recovery and application recovery are distinguished.
- Observation/abort criteria and owner exist for material rollout.
- Release artifact has future expiry.
- Decision is exactly one allowed state.
- Enforcement status is honestly reported as enforced or advisory.

## Failure handling
If candidate/environment/evidence is missing or stale, issue HOLD. If an effective blocker cannot be safely remediated/accepted, issue NO-GO. Candidate/config/environment changes invalidate affected evidence. If release-gate integration is absent or does not bind the actual target environment, do not claim technical prevention: report advisory.

## Output contract
Return candidate, target environment/scope, risk/change surface, mandatory gates/evidence status, unresolved/effective blockers, accepted risks/expiry, deployment/migration/recovery, observability/abort criteria, release artifact expiry, final GO/GO WITH CONDITIONS/HOLD/NO-GO and enforcement status.
