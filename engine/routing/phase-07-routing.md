# Phase 07 Routing — Production

Use the smallest production skill set that owns the decision.

## Primary ownership

- `devops-deployment`: build/release pipelines, environments, secrets/config, deployment targets, promotion, rollout and rollback.
- `observability-sre`: logs/metrics/traces, OpenTelemetry, SLI/SLO, alerts, health, incidents, capacity and resilience.
- `git-delivery`: branch/commit/PR/review/protected-ref/release-versioning workflow.
- `documentation`: README/onboarding, architecture/ADR/API docs, runbooks and release/operations documentation.

## Routing examples

- “Vercel preview passed, promote same artifact to production.” → `devops-deployment`.
- “Production error rate spiked after deploy; define alerts and runbook.” → `observability-sre` + `debugging`; add `devops-deployment` only when rollback/promotion mechanics are needed.
- “Add branch protections and PR release workflow.” → `git-delivery`; add `devops-deployment` only for CI/deploy mechanics.
- “Update README, ADR and operator runbook after architecture change.” → `documentation`.
- “Add GitHub Action that deploys to prod.” → `devops-deployment` + `git-delivery`; add `security` for secret/OIDC/untrusted-input risk.

## Escalation

- R0/R1: only the directly responsible production skill.
- R2: add `testing-qa` when deployment/release behavior changes materially.
- R3: production credentials, infrastructure, migrations, public availability, supply chain or incident controls require relevant `security`, `testing-qa`, `observability-sre` and/or `database-data` review.
- R4: major production release/architecture change requires final `audit-review` and `release-readiness` once those skills exist.

## Release gate rule

A production change is not complete merely because CI/deployment reports success. Verify deployed artifact identity, health/critical smoke path, migration/job state and required telemetry. Critical security findings, unverified destructive migrations or absence of a credible rollback/roll-forward path block release.

## Token rule

Do not load all four production skills by default. Select the owner first, then add specialists only for cross-domain risk.