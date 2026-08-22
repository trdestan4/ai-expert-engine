# Phase 08 Routing — AI / Asset Production

Route narrowly. Do not load both skills unless the task actually spans AI runtime behavior and visual-asset production.

## `ai-engineering`

Use for LLM/model/provider selection, prompt/schema design, structured output, tools, agents, MCP, RAG/embeddings/reranking, AI streaming, evals, guardrails, prompt-injection resistance, AI latency/cost and AI observability.

Common companions:
- `backend-engineering` / `api-engineering` for service/API implementation;
- `identity-access` / `security` when tools or retrieved data cross permission boundaries;
- `database-data` for vector/storage/data modeling;
- `testing-qa` for broader release coverage;
- `observability-sre` for production telemetry/incident behavior;
- `ux-ui-design` / `frontend-engineering` for AI interaction UX.

Do not route ordinary deterministic API/search/business logic here merely because the product markets itself as AI.

## `asset-production`

Use for generation/editing of images, SVG/icons, illustration, 3D/video/motion assets, responsive derivatives, compression/export, provenance and web-ready handoff.

Common companions:
- `creative-director`, `visual-art-direction`, `brand-design` for visual direction;
- `motion-direction` for interaction/motion language;
- `accessibility` for meaningful images/media/captions;
- `performance` / `frontend-engineering` for runtime delivery;
- `storage-media` for upload/object-storage pipelines.

Do not route layout/component design here just because it contains images.

## Combined route examples

- “Build a RAG assistant over private tenant documents” → `ai-engineering` + `database-data` + `identity-access` + `security`; add `backend-engineering` as implementation warrants.
- “Add an agent that can refund orders” → `ai-engineering` + `ecommerce` + `integrations` + `security` + `testing-qa`; high-impact action policy is mandatory.
- “Create a coherent hero/product image system and responsive exports” → `asset-production` + creative specialists; add `performance`/`frontend-engineering` for implementation.
- “Generate an image inside the product using an AI model API” → `ai-engineering` owns model/API runtime; `asset-production` owns visual/asset contract when quality/art-direction/export matters.

## Mandatory gate escalation

Escalate to `security` and `privacy-compliance` for sensitive prompts, private corpora, cross-tenant retrieval, external-content tool execution, privileged actions or retained model data.

Escalate to `testing-qa` for material AI behavior/model/retrieval/tool changes and to `release-readiness` for R3/R4 AI releases, autonomous high-impact actions or production asset pipelines that can break critical UX.

## Token rule

Load the main skill first and only the reference that matches the actual subproblem. Normal AI work should not automatically load every RAG, MCP, agent and asset reference. Normal asset work should not load AI runtime references unless the application itself integrates generation models.