---
name: devops-deployment
description: Owns build and deployment delivery across CI/CD, environments, configuration, secrets, artifacts, containers, serverless/Vercel, major cloud platforms, infrastructure as code, Kubernetes, promotion strategies and rollback; it does not own application observability, Git review policy or domain logic.
---

# Purpose
Turn verified application and infrastructure changes into reproducible, secure, reversible production releases with explicit environment boundaries and evidence that the deployed artifact/configuration is the reviewed candidate.

## Use when
- CI/CD, preview/staging/production, build artifacts or deployment automation are involved;
- Docker, serverless, Vercel, AWS/GCP/Azure, Terraform/OpenTofu or Kubernetes needs deployment design/review;
- secrets/configuration, environment promotion, canary/blue-green, rollback or migration sequencing affects release safety;
- build provenance, artifact integrity or infrastructure change controls are required.

## Do not use when
- logs/metrics/traces/SLOs and incidents are primary (`observability-sre`);
- branching/PR/release-note workflow is primary (`git-delivery`);
- application security review is primary (`security`);
- database migration semantics alone are primary (`database-data`).

## Inputs
Inspect repository/runtime versions, build commands, lockfiles, CI provider, deployment/cloud target, IaC/Kubernetes manifests when present, environment model, secrets/identity, artifact flow, migration dependencies, rollback capabilities, traffic strategy, approvals/compliance constraints and production topology.

## Workflow
### 1. Establish reproducible inputs
Pin runtime/toolchain/provider constraints where practical, use lockfiles and deterministic build/plan commands, separate source/generated artifacts and fail early on missing required configuration.

### 2. Separate environments
Define development, preview, staging and production semantics. Environment names do not imply identical data, domains, permissions, provider modes or network exposure.

### 3. Build/plan once and promote deliberately
Prefer immutable artifacts and reviewed IaC plans where supported. Do not rebuild or re-plan a materially different candidate after approval without invalidating evidence.

### 4. Protect identities and secrets
Keep secrets out of source/logs/client bundles. Prefer short-lived workload identity/OIDC over long-lived keys where supported and scope permissions to the smallest environment/action.

### 5. Order dependencies
Coordinate schema migrations, workers, queues, caches, callbacks, infrastructure and app versions so overlap windows are understood.

### 6. Choose rollout by risk
Use simple replacement for compatible low-risk changes; progressive/canary/blue-green for high-impact changes only when traffic controls, metrics and stop mechanisms are real.

### 7. Define recovery before release
Know whether recovery is artifact promotion, feature disable, infrastructure rollback, roll-forward, state restore or data recovery. Application rollback does not undo destroyed data or incompatible infrastructure state.

### 8. Verify deployed state
Check artifact/commit/config identity, health/smoke paths, migration/job state, critical integrations and infrastructure convergence. CI/apply success alone is not production-health proof.

### 9. Apply provider/IaC/orchestrator specifics
Use verified cloud/provider/Kubernetes versions and repository conventions for IAM, state, network exposure, probes, resources, rollouts and drift. Do not generalize Vercel/serverless semantics to clusters or vice versa.

## Decision rules
- Production credentials never belong in source or browser-exposed variables.
- Deployable artifacts and IaC plans must be traceable to source/environment.
- Full commit SHA pinning is the strongest GitHub Actions reference model for third-party actions.
- Preview must not silently target destructive production services.
- Overlapping app versions require backward/forward-compatible schema/dependency changes.
- Rollback/recovery is part of release design.
- Infrastructure success is not application correctness.
- Provider/version-specific behavior requires current evidence.

## Reference routing
Load `references/ci-cd-pipelines.md` for pipeline stages, gates and reproducible builds.
Load `references/environments-secrets-config.md` for environment separation, secret handling, OIDC and configuration.
Load `references/deployment-strategies-rollbacks.md` for canary/blue-green, promotion, sequencing and rollback.
Load `references/docker-serverless-vercel.md` for container, serverless and Vercel concerns.
Load `references/supply-chain-artifacts.md` for action pinning, provenance, attestations and build integrity.
Load `references/cloud-iac-kubernetes.md` for AWS/GCP/Azure, Terraform/OpenTofu and Kubernetes deployment concerns.

## Quality gates
- Build/plan inputs and artifact identity are reproducible and traceable.
- Environment/configuration/IAM boundaries are explicit.
- Secrets are scoped and absent from source/client exposure.
- Required tests/security checks precede production promotion.
- Database/worker/infrastructure dependency ordering is defined.
- Rollback or safe roll-forward/recovery exists.
- Post-release smoke/health verification is defined.
- High-risk releases escalate `security`, `testing-qa`, `observability-sre` and `release-readiness` appropriately.

## Failure handling
If deployed state is uncertain, inspect the actual artifact/infrastructure rather than infer from branch state. If destructive data/IaC change prevents safe rollback, block until recovery/roll-forward is proven. If provider behavior differs from memory, verify current provider/tool documentation before production change.

## Output contract
Return environment/release model, pipeline and IaC gates, artifact/config/secrets/identity strategy, deployment target and rollout, migration/infrastructure ordering, rollback/roll-forward/recovery plan, post-deploy verification and specialist handoffs.
