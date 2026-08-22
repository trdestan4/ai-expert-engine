# SLI, SLO, Error Budgets and Alerting

## SLIs

Measure user-visible service outcomes: availability/success, latency, freshness, durability or correctness proxy. Define numerator/denominator precisely and exclude requests only with documented rationale. Infrastructure CPU alone is not a user SLI.

## SLOs

Set targets from product/customer/reliability needs and achievable architecture. Use rolling windows appropriate to operations. Distinguish contractual SLA from internal SLO.

## Error budgets

Error budget turns SLO into release/operational policy. Track consumption and use it to prioritize reliability vs change when agreed by product/engineering. Do not treat one transient breach as automatic feature freeze without policy.

## Burn-rate alerts

Prefer multi-window/multi-burn alerts that detect both fast catastrophic and slower sustained consumption while reducing noise. Exact thresholds/windows should reflect SLO/on-call response and can follow established SRE patterns; verify tooling/math.

## Alert quality

Alert only when action is needed. Include symptom, impact, environment/service, key dashboard/runbook and ownership. Page on user-impact/budget burn, not every component metric. Ticket lower-urgency capacity/drift issues.

## Release correlation

Dashboards/alerts should expose candidate/version/rollout cohort where possible so post-deploy regressions are quickly attributable. Define abort thresholds before progressive rollout.
