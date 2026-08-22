# Model Selection and Provider Routing

Select models from verified current capability rather than brand familiarity or remembered model IDs. Start from the product contract: modality, reasoning depth, structured output/tool support, context needs, latency target, privacy/geography, rate limits, reliability and cost. Verify installed SDK/provider versions and current model catalogs before implementation.

Prefer the smallest/least expensive model that reliably clears the task's evaluation threshold. Larger/newer is justified only when measurable quality or capability requires it. Separate model quality from provider reliability: a strong model with unstable capacity can still be the wrong production default.

Define a provider adapter boundary when multiple providers are genuinely required. Normalize only what the product actually needs; do not pretend capabilities are identical. Tool calling, reasoning controls, multimodal input, streaming events, token accounting and structured output often differ.

Fallbacks must preserve the contract. A fallback that cannot support required schema/tool/modality behavior is not a fallback. Define retryable vs non-retryable failures, timeout budgets, rate-limit handling and when to degrade to a deterministic/manual path.

Record provider/model/version in telemetry and eval results. Treat migrations as behavior changes: rerun regression sets, compare latency/cost, schema/tool correctness and product outcomes before switching defaults.