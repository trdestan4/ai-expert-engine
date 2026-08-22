# AI / Asset Production Policy

1. Current repository SDK versions and authoritative provider/protocol docs outrank remembered APIs, model IDs or platform behavior.
2. AI features must define deterministic boundaries, runtime validation, least-privilege tools and measurable evaluation criteria before production claims.
3. Untrusted user/web/document/email/RAG/tool content is data, not authority; prompt-injection defense uses layered controls rather than one prompt/filter.
4. High-impact AI actions require independent application authorization, semantic validation, idempotency and approval when user intent/risk warrants it.
5. RAG requires permission-aware retrieval, source provenance, freshness/no-answer behavior and regression evaluation.
6. AI model/provider/prompt/retrieval changes are behavior changes; material changes require comparable eval evidence plus latency/cost impact.
7. MCP behavior must match the supported SDK/spec revision. The current 2026-07-28 specification uses a stateless core; do not transplant older session assumptions into migrated stacks or force new semantics onto incompatible clients.
8. AI telemetry must expose model/provider/version, latency, failure/tool/retrieval classes and cost/token signals while respecting privacy/data-retention constraints.
9. Asset production follows creative/art direction; generation prompts are not a substitute for brand/product reasoning.
10. Generated or edited assets must preserve explicit locks/constraints, avoid baking essential UI copy into raster output, and carry responsive/accessibility handoff where applicable.
11. SVG/untrusted visual markup must be treated as code-like input and sanitized before privileged browser use.
12. Asset format/compression decisions are based on actual surface/browser/toolchain/performance evidence, not format trends.
13. Asset masters, variants, provenance/licenses and source/edit lineage must remain traceable; unknown rights are reported, never invented.
14. AI and asset specialists coordinate with existing security, privacy, performance, accessibility, storage, product and creative owners rather than absorbing their responsibilities.