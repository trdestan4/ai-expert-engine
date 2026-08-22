# Phase 07 Evals — Production

## Routing positives

1. “GitHub Action ile testten sonra Vercel production deploy ve rollback planı kur.” → `devops-deployment` + `git-delivery`; add `security` for credentials/workflow hardening.
2. “Prod API’de hata oranı yükseliyor; SLO, alert ve runbook oluştur.” → `observability-sre`.
3. “Branch protection, CODEOWNERS, release tag/changelog standardı kur.” → `git-delivery`.
4. “Yeni mimariden sonra README, ADR ve incident runbook güncelle.” → `documentation`.
5. “DB migration ile canary deploy yapacağız.” → `devops-deployment` + `database-data` + `testing-qa` + `observability-sre`.

## Routing negatives

1. “React component render çok yavaş.” → not production by default; `react-nextjs` + `performance`.
2. “PostgreSQL index ekle.” → `database-data`; deployment only if rollout/migration production sequencing is requested.
3. “Landing page copy değiştir.” → `content-conversion`, not documentation.
4. “JWT authorization bugı.” → `debugging` + `identity-access`/`security`, not git-delivery.

## Edge cases

- Preview deployment accidentally points to production payment/database credentials → `devops-deployment` + mandatory `security`; release blocked until isolation is proven.
- CI green but production alias points to an older deployment → inspect artifact/deployment identity; do not claim release success.
- Destructive migration already ran and application rollback would reintroduce incompatible code → require safe roll-forward/recovery, not blind rollback.
- Alert fires on every single 500 but has no owner/action → redesign alert; do not preserve noisy paging for appearances.
- Runbook says only “check logs” → documentation quality failure until concrete queries/first actions exist.
- GitHub workflow uses mutable third-party action tags for sensitive production deployment → flag supply-chain risk and prefer verified full SHA pinning.

## Quality assertions

- Every R3/R4 deployment change has rollback or explicit safe roll-forward/recovery strategy.
- Production secret/client exposure is a release blocker.
- CI success alone never proves production health.
- Deployment/regression telemetry can correlate release/version with errors/latency.
- SLO/alerts have measurable definitions and ownership.
- Critical runbooks contain concrete checks, mitigation and verification.
- Release/tag/artifact provenance is traceable.
- Setup/architecture/operations changes cannot leave known stale canonical documentation.