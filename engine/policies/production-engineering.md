# Production Engineering Policy

1. Production releases must be traceable to source commit, workflow/build and deployed artifact/deployment identity.
2. Build/release inputs should be reproducible; lockfiles and pinned runtimes/tooling are preferred where practical.
3. Secrets never enter source, logs or client-exposed configuration. Prefer least privilege and short-lived/OIDC credentials where supported.
4. Preview/staging/production service identities and destructive integrations are explicitly separated.
5. High-risk deployment changes define rollback before release; irreversible data changes require a proven roll-forward/recovery strategy.
6. Third-party GitHub Actions should use full-length commit SHA pins when immutable supply-chain control is required. Artifact attestations may be used to strengthen provenance.
7. Production telemetry uses structured logs, metrics and traces with service/environment/version correlation. Current OpenTelemetry semantic conventions should be preferred when compatible; verify library/version stability before migrations.
8. Alerts must be actionable. SLOs/SLIs must map to measurable user-visible reliability rather than vanity infrastructure metrics.
9. A successful deploy is not release evidence by itself: post-deploy health/smoke/migration/job checks are required proportionally to risk.
10. Documentation changes are required when setup, architecture, operational procedures, public contracts or release/migration behavior changes.
11. Production incidents prioritize containment and evidence; postmortems focus on system conditions and durable corrections.
12. R3/R4 production risk can block release until security/testing/observability/database/final-control gates pass.