# Cloud, Infrastructure as Code and Kubernetes

Use provider/version evidence before applying remembered defaults. Cloud primitives sit under the same invariants: least privilege, reproducibility, bounded blast radius, observable rollout, cost awareness and recovery.

## AWS / GCP / Azure

Prefer workload identity/OIDC/managed identity over long-lived static credentials. Separate production accounts/projects/subscriptions and privileges deliberately. Define public/network exposure, VPC/VNet/subnets, ingress/egress, encryption/key ownership, region/residency, quotas and budget/cost controls.

Managed services reduce undifferentiated operations but still need backup/restore, HA/failover, maintenance/version, capacity/limits and security configuration. Verify provider-specific defaults/current docs before claiming encryption, retention or failover guarantees.

## Terraform / OpenTofu

Pin tool/provider constraints appropriately and commit lockfiles per repo policy. Protect remote state and locking; state can contain secrets. Separate reusable modules from environment composition and avoid giant modules with hidden side effects.

Review plan from exact commit/environment. Understand create-before-destroy, replacement, moved/imported resources, lifecycle ignores and provider drift. Destructive replacements require explicit data/service recovery. Plan success is not apply/runtime health.

## Kubernetes

Define requests/limits from measured workload, probes, disruption/PDB behavior, rollout strategy, service/network exposure, secrets/config, autoscaling and security context. Readiness gates traffic; liveness should detect irrecoverable process failure, not restart healthy pods because a dependency is slow.

Avoid privileged containers, host PID/network/mounts and broad service-account RBAC unless justified. Use namespace/account/role/network policies as appropriate to cluster threat model. Image digest/provenance/scanning policy may be required for high-risk environments.

Jobs/migrations need one-owner/exactly-once-business-effect semantics even if Kubernetes restarts/retries pods. Graceful termination and preStop/terminationGracePeriod must align with request/worker drain.

Autoscaling requires metric behavior and downstream capacity awareness; scaling app pods cannot fix a saturated database/provider and may amplify load.

## Production evidence

Material IaC/cluster change requires plan/diff, identity/permission review, environment confirmation, rollout/recovery, observability and post-apply verification. Application/data specialists still own schema/queue/storage correctness.
