# Structured Output and Tool Calling

Use structured output when model output becomes application state, API input, database data or a tool/action request. Define the narrowest useful schema, validate it at runtime and then apply semantic/domain validation. Schema-valid JSON can still contain an impossible date, unauthorized resource id or invalid business transition.

Do not use generated natural language as an authorization layer. Tool schemas describe shape, not permission. Every tool executes behind normal application authentication, authorization, tenant/resource checks, rate limits and input validation.

Keep tools small and capability-oriented. Prefer `create_invoice_draft` over a generic `execute_arbitrary_operation`. Scope credentials server-side. Never expose privileged API keys or unrestricted database clients to model-controlled code.

Model tool calls should be idempotent or carry idempotency keys when retries can cause duplicate side effects. Separate read-only discovery tools from mutating tools. High-impact operations require deterministic policy checks and, where user intent could be ambiguous, explicit approval before execution.

Handle malformed/invalid model outputs as expected runtime failures: retry only when evidence supports retry, cap attempts, preserve the original user intent and expose a safe fallback. Log tool name, validated arguments fingerprint, authorization outcome, duration and result class without leaking secrets or sensitive payloads.

When providers offer native schema/tool features, verify the installed SDK/API contract before coding. Do not emulate obsolete parameter names or remembered response shapes.