# Logs, Metrics, Traces and OpenTelemetry

Observability should answer operational questions from production behavior, not maximize telemetry volume.

## Logs

Use structured events with timestamp, service/version/environment, severity, stable event name and correlation/trace IDs. Include business/resource identifiers only when necessary and privacy-safe. Avoid secrets/tokens/payment/sensitive payloads. Log exceptions with cause/context once at the right boundary rather than duplicating every layer.

Control high-cardinality fields and retention/cost. Sampling logs can hide rare security/finance events; choose per event class.

## Metrics

Prefer bounded-cardinality metrics for rates/errors/latency/saturation and business-critical state. Histograms preserve percentile distribution better than average-only gauges. Label explosions by user/request/order ID can destroy monitoring cost/performance.

## Traces

Trace critical distributed paths and preserve parent/child context across HTTP/queues/jobs. Spans should identify dependency/operation, status, latency and relevant safe attributes. Sampling strategy must retain enough errors/tails/critical transactions to diagnose; head sampling alone may miss rare slow paths.

## OpenTelemetry

Use current semantic conventions/version appropriate to installed SDKs. Standardize service/resource attributes and instrumentation ownership. Avoid instrumenting everything twice through auto + manual libraries.

## Correlation

Link release version, feature flag/tenant cohort and provider dependency to telemetry when useful for incident/regression analysis. Metrics detect; traces/logs explain; business state/reconciliation may prove durable outcome.
