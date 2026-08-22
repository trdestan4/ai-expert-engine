# Cloud, Infrastructure as Code and Kubernetes

Use provider/version evidence before applying remembered defaults. Cloud primitives are implementation choices underneath the same release invariants: least privilege, reproducibility, bounded blast radius, observable rollout and recovery.

## AWS / GCP / Azure
Prefer workload identity/OIDC or short-lived credentials over long-lived static keys where supported. Separate accounts/projects/subscriptions and production permissions deliberately. Define network/public exposure, encryption/key ownership, region/residency, quotas and cost controls explicitly.

## Terraform / OpenTofu
Pin provider/tool constraints appropriately, review plans before apply, protect remote state and locking, keep secrets out of state where possible, and separate reusable modules from environment composition. A plan from one commit/environment is not evidence for another. Destructive replacements require recovery/blast-radius review.

## Kubernetes
Define requests/limits, probes, disruption behavior, rollout strategy, service/network exposure, secrets/config and autoscaling from workload behavior. Readiness gates traffic; liveness should not turn dependency slowness into restart storms. Jobs and migrations need one-owner execution semantics. Avoid privileged pods/host mounts unless justified and reviewed.

## Managed databases/queues/storage
Provisioning infrastructure does not define application correctness. Database migration safety remains `database-data`; queue delivery semantics remain `realtime-async`; object authorization remains `storage-media`.

## Production gates
For material IaC changes require plan/diff evidence, identity/permission review, rollback or forward-recovery path, observability and environment-specific verification. Never treat `terraform apply`, Helm success or provider deployment completion as application-health proof.
