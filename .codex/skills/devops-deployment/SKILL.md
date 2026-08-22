---
name: devops-deployment
description: Owns build and deployment delivery across CI/CD, environments, configuration, secrets, artifacts, Docker, Vercel/serverless targets, previews, staging/production promotion, deployment strategies, infrastructure change coordination, and rollback; it does not own application observability, Git review policy, or domain logic.
---

# Purpose

Turn verified application changes into reproducible, secure, reversible production releases with explicit environment boundaries and evidence that the deployed artifact is the one that passed validation.

## Use when

- CI/CD pipelines, preview/staging/production environments, build artifacts or deployment automation are involved;
- Docker, serverless, Vercel or similar deployment targets need design/review;
- secrets/configuration, environment promotion, canary/blue-green, rollback or migration sequencing affects release safety;
- build provenance, artifact integrity or deployment supply-chain controls are required.

## Do not use when

- logs/metrics/traces/SLOs and incidents are primary (`observability-sre`);
- branching/PR/commit/release-note workflow is primary (`git-delivery`);
- application security review is primary (`security`);
- database migration semantics alone are primary (`database-data`).

## Inputs

Inspect repository/runtime versions, build commands, package lockfiles, CI provider, deployment target, environment model, secrets/configuration, artifact flow, migration dependencies, rollback capabilities, traffic strategy, required approvals, compliance constraints and current production topology.

## Workflow

### 1. Establish reproducible build inputs
Pin runtime/toolchain where practical, use lockfiles, define deterministic build commands, separate source from generated artifacts, and fail fast on missing required configuration.

### 2. Separate environments deliberately
Define development, preview, staging and production semantics. Never assume environment names imply identical data, secrets, domains, permissions or external-provider modes.

### 3. Build once, promote intentionally
Prefer immutable artifacts and promotion of the verified artifact when the platform supports it. Avoid rebuilding different source/configuration between approval and production without explicit evidence.

### 4. Protect secrets and credentials
Keep secrets out of source/logs/client bundles. Prefer short-lived/OIDC credentials where supported; scope deployment tokens and environment access to minimum required privilege.

### 5. Order release dependencies
Coordinate schema migrations, background workers, queues, caches and external callbacks so old/new application versions can coexist when rollout is non-atomic.

### 6. Choose deployment strategy by risk
Use rolling/simple replacement for low-risk compatible changes; canary/blue-green/progressive exposure for high-impact changes where traffic controls and observability justify the complexity.

### 7. Define rollback before release
Know whether rollback means alias/promote previous artifact, application revert, feature flag, database roll-forward, or restore. Never promise database rollback when destructive data change makes it unsafe.

### 8. Verify deployed state
Check deployment identity/commit, health, smoke paths, migrations, required jobs and critical integrations. A successful CI job is not proof that production behavior is healthy.

## Decision rules

- Production credentials never belong in source or browser-exposed environment variables.
- A deployable artifact should be traceable to commit, workflow and environment.
- Prefer immutable promotion over rebuilding after approval when possible.
- Third-party CI actions should be pinned immutably when supply-chain risk matters; full commit SHA is the strongest GitHub Actions pinning model.
- Preview environments must not silently point to destructive production services.
- Migrations and application rollout must be backward/forward compatible when versions can overlap.
- Rollback capability is part of release design, not an incident-time improvisation.
- Platform-specific behavior must be verified against the repository/provider version before use.

## Reference routing

Load `references/ci-cd-pipelines.md` for pipeline stages, gates, caching and reproducible builds.
Load `references/environments-secrets-config.md` for environment separation, secret handling, OIDC and configuration validation.
Load `references/deployment-strategies-rollbacks.md` for canary/blue-green, promotion, migration sequencing and rollback.
Load `references/docker-serverless-vercel.md` for container, serverless and Vercel deployment concerns.
Load `references/supply-chain-artifacts.md` for action pinning, artifact provenance, attestations and build integrity.

## Quality gates

- Build inputs and artifact identity are reproducible and traceable.
- Preview/staging/production configuration boundaries are explicit.
- Secrets are scoped and absent from source/client exposure.
- Required tests/security checks run before production promotion.
- Database/worker/external dependency sequencing is defined.
- Rollback or safe roll-forward strategy exists for release-critical changes.
- Deployment has post-release smoke/health verification.
- High-risk releases escalate `security`, `testing-qa`, `observability-sre` and `release-readiness` as appropriate.

## Failure handling

If deployment state is uncertain, inspect the actual deployment/artifact rather than infer from branch state. If a destructive migration prevents safe rollback, block release until a roll-forward/recovery path is proven. If provider capabilities differ from memory, verify current provider documentation/tooling before changing production behavior.

## Output contract

Return environment/release model, pipeline stages and gates, artifact/config/secrets strategy, deployment target/strategy, migration ordering, rollback/roll-forward plan, post-deploy verification and specialist handoffs.