# Streaming, Cost and Observability

Streaming is a UX/runtime decision, not only a transport toggle. Define what the user sees before first token, during partial generation, while tools execute, when retrieval is pending, and when a stream fails or is cancelled. Preserve enough state to recover without duplicating actions.

Measure time-to-first-token, total latency, tool/retrieval time, output length, retries and completion/failure reason. Separate provider latency from application/network/tool latency so optimization targets the actual bottleneck.

Record model/provider/version, prompt/template version, token/input-output accounting where available, estimated or billed cost, cache usage, retrieval counts, tool calls and failure categories. Do not log raw sensitive prompts/results by default; apply privacy classification, redaction and retention rules.

Set per-feature cost budgets and abuse controls. Bound maximum steps, tool calls, retrieval volume, context growth and output size. Use cheaper models/caches/batching only when eval quality remains acceptable.

Handle disconnect/cancellation intentionally. Stop expensive upstream work when possible and ensure mutating tools are idempotent if execution may outlive the client connection.

Fallback behavior should distinguish overload/rate limits, provider outage, model capability error, invalid structured output and application bugs. A fallback provider/model is only valid if it satisfies required modalities/tools/schemas.

Operational dashboards should connect product success, quality/eval signals, latency, cost and errors. Sudden changes in refusal rate, tool approval rate, token usage or retrieval behavior can indicate drift, attack or provider behavior change.