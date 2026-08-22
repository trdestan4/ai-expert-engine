# SLI, SLO, Error Budgets and Alerting

## SLIs

Measure user-visible service outcomes: availability/success, latency, freshness, durability or a defensible correctness proxy. Define numerator, denominator, event population and exclusions precisely. Infrastructure CPU, pod count or queue depth can explain symptoms but are not user SLIs by themselves.

Segment only when the segment changes action or contract: endpoint class, tenant tier, region, dependency or critical journey. Avoid dimensions whose cardinality makes telemetry unaffordable or statistically meaningless.

## SLOs

Set targets from product/customer/reliability needs and achievable architecture, not round-number ambition. Use rolling windows appropriate to operations and distinguish contractual SLA from internal SLO. A critical checkout or authentication journey can deserve a different objective from low-value background work.

## Error budgets

Error budget turns an SLO into release and operational policy. Track both remaining budget and consumption rate. Define in advance what happens when budget is healthy, rapidly burning or exhausted: continue normal change, require extra rollout safeguards, prioritize reliability work, or temporarily constrain risky releases. Do not invent an automatic feature freeze after one transient breach unless policy actually requires it.

## Burn-rate alerts

Prefer multi-window, multi-burn alerts that detect both fast catastrophic consumption and slower sustained degradation while controlling noise. Tune windows to the SLO period and realistic on-call response. Validate alert math against recorded incidents or synthetic time series; a copied threshold is not automatically appropriate for another service.

## Alert quality

Page only when timely human action is required. Include symptom, user impact, environment/service, current candidate or rollout cohort, supporting dashboard/runbook, likely dependency and ownership. Ticket lower-urgency capacity, cost or configuration drift. Every recurring false page should trigger alert redesign rather than permanent human habituation.

## Telemetry economics

Reliability telemetry itself has cost. Bound metric-label cardinality, log volume and trace sampling while preserving enough exemplars/correlation to investigate tail failures. Sample intelligently rather than dropping exactly the rare slow/error traces needed during incidents.

## Release correlation

Dashboards and alerts should expose candidate/version/flag/rollout cohort where possible so post-deploy regressions are attributable. Define measurable abort thresholds and the person or automation authorized to halt rollout before production exposure begins.
