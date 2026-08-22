---
name: observability-sre
description: Owns production observability and reliability engineering across structured logs, metrics, traces, OpenTelemetry, dashboards, health signals, SLIs/SLOs, alerting, incident response, capacity, resilience and production diagnostics; it does not own deployment automation or application-domain business logic.
---

# Purpose

Make production behavior measurable enough to detect customer-impacting failure, diagnose root cause quickly, manage reliability intentionally, and improve systems from evidence instead of intuition.

## Use when

- logging, metrics, tracing, OpenTelemetry, dashboards or error tracking are involved;
- health checks, SLIs/SLOs, alerts, on-call response or incident runbooks need design;
- production latency, errors, saturation, queue lag, dependency health or capacity require monitoring;
- a system needs reliability/resilience review before or after release.

## Do not use when

- CI/CD or deployment promotion is primary (`devops-deployment`);
- test strategy is primary (`testing-qa`);
- performance optimization without production telemetry is primary (`performance`);
- code-level root cause investigation alone is primary (`debugging`).

## Inputs

Identify critical user journeys, service boundaries, dependencies, deployment/runtime topology, existing telemetry vendors, request/job correlation identifiers, privacy constraints, traffic patterns, known failure modes, recovery expectations and operational ownership.

## Workflow

### 1. Start from user-visible reliability
List critical journeys and failure states before choosing dashboards. Derive signals from availability, latency, correctness and freshness rather than instrumenting everything equally.

### 2. Establish structured telemetry
Use structured logs, meaningful metrics and traces with consistent service/environment/version/request identifiers. Prefer OpenTelemetry semantic conventions where compatible with current instrumentation.

### 3. Correlate signals
Logs, traces, metrics, deployments and domain events should be linkable through stable identifiers. Avoid telemetry that cannot distinguish environment, tenant-safe context, release or operation.

### 4. Define SLIs and SLOs
Use measurable service indicators tied to user outcomes. Select realistic objectives and error budgets; do not invent SLOs from industry folklore without product/reliability context.

### 5. Alert on actionable symptoms
Prefer customer-impacting or burn-rate/saturation signals over noisy raw events. Every alert needs owner, severity, immediate diagnostic path and expected action.

### 6. Prepare incident response
Define triage, containment, rollback/mitigation, communication, escalation and evidence preservation. Runbooks should point to concrete dashboards/queries/actions rather than generic advice.

### 7. Learn after incidents
Create blameless technical follow-up focused on contributing conditions, detection gaps, recovery friction and system changes. Track corrective actions to completion.

## Decision rules

- Telemetry must avoid secrets and unnecessary personal data.
- High-cardinality labels/tags require deliberate cost and backend consideration.
- Logs are not a substitute for metrics; metrics are not a substitute for traces.
- Alerts without a plausible operator action are usually dashboard signals, not paging signals.
- Health checks must reflect meaningful dependency/readiness state without creating cascading load.
- SLOs should describe user-relevant reliability, not infrastructure vanity metrics.
- Telemetry naming should follow current OpenTelemetry semantic conventions where feasible and repository/provider compatibility permits.

## Reference routing

Load `references/logs-metrics-traces-otel.md` for structured telemetry, correlation and OpenTelemetry conventions.
Load `references/sli-slo-alerting.md` for SLIs, SLOs, error budgets, burn rates and alert design.
Load `references/incident-response-runbooks.md` for incident command, mitigation, communication and postmortems.
Load `references/health-capacity-resilience.md` for health checks, saturation, capacity, dependency resilience and graceful degradation.

## Quality gates

- Critical journeys map to observable signals.
- Logs/metrics/traces include environment/service/version correlation.
- Sensitive data is minimized/redacted.
- Alerts are actionable and severity-owned.
- SLOs have measurable definitions and data sources.
- Deployments can be correlated with regressions.
- Incident runbooks identify concrete first checks and mitigation paths.
- Capacity/resilience assumptions are explicit for critical systems.

## Failure handling

If telemetry is absent, instrument the smallest useful critical path before speculating. If metrics disagree with logs/traces, validate sampling, aggregation, time windows and dimensions. If an alert is repeatedly non-actionable, redesign or demote it rather than training operators to ignore it.

## Output contract

Return critical journeys/signals, telemetry model, correlation fields, SLI/SLO definitions, dashboards/alerts, health/capacity strategy, incident/runbook requirements and unresolved observability risks.