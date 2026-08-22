# AI Expert Engine v1.0

A token-efficient master-class agent system for production web design, software engineering, AI systems, asset production and release control in Cursor and Codex.

## Architecture principle

The engine uses a bounded set of discoverable domain skills with deep expertise loaded lazily from references, policies, schemas, evals, reviewer profiles and deterministic validators. Normal tasks load only the minimum owners needed; high-risk work escalates independent review and release gates.

## Build status

- Phase 00 — Core / AI Brain: complete
- Phase 01 — Creative / Product Intelligence: complete
- Phase 02 — Web Engineering / Frontend: complete
- Phase 03 — Backend / API Engineering: complete
- Phase 04 — Data / Platform: complete
- Phase 05 — Quality Engineering: complete
- Phase 06 — Business / Growth: complete
- Phase 07 — Production Engineering: complete
- Phase 08 — AI / Asset Production: complete
- Phase 09 — Final Control: complete

**Engine status: v1.0 complete — 43 discoverable skills + 6 independent reviewer profiles.**

## Phase 00 — Core / AI Brain

Provides orchestration, repository intelligence, task planning, debugging, token policy, schemas, routing contracts, evals and structural validation. Complexity (C0–C4) and risk (R0–R4) are classified independently so small trust-boundary edits can still receive high-risk safeguards.

## Phase 01 — Creative / Product Intelligence

Provides product strategy, creative direction, brand design, anti-generic design review, color intelligence, typography intelligence, visual art direction, motion direction and UX/UI design.

The design system explicitly rejects shortcut mappings such as `premium = navy + gold`, `luxury = black + gold`, or `AI/tech = purple gradient`. Visual decisions must be justified by product, audience, brand, content, usability, accessibility, performance and category context.

## Phase 02 — Web Engineering / Frontend

Provides framework-independent web-platform reasoning, production frontend engineering, React/Next.js runtime expertise and application-level software architecture.

Key rules include semantic/native browser behavior first, explicit state ownership, content-resilient responsive implementation, narrow server/client boundaries, repository-version-aware framework decisions, deliberate cache/freshness behavior and complete async/error/form states.

## Phase 03 — Backend / API Engineering

Provides production backend service/runtime guidance plus REST/GraphQL contract engineering. Backend decisions cover validation, domain invariants, side effects, errors, observability, configuration, concurrency, retries, cache and testing. API decisions cover REST/GraphQL semantics, OpenAPI, Problem Details, pagination/filtering/versioning, idempotency, rate limits, compatibility, deprecation and contract tests.

Runtime/framework/spec advice is repository-version-aware: the engine never upgrades or applies new behavior merely because a newer standard exists.

## Phase 04 — Data / Platform

Provides identity/access architecture, PostgreSQL/Supabase data engineering, realtime and durable async workflows, third-party integrations and secure object/media storage.

Critical boundaries are deny-by-default for cross-tenant access, client-exposed privileged keys, duplicate side effects, unverified webhooks, unsafe live migrations and unauthorized object signing.

## Phase 05 — Quality Engineering

Provides security, privacy/compliance engineering, performance, testing/QA, accessibility and senior code-quality gates.

Quality skills are not loaded automatically as a bundle: routing activates only the gates justified by the change's actual risk. Critical security and core-accessibility failures can block release.

## Phase 06 — Business / Growth

Provides search discoverability, conversion messaging, ecommerce domain logic and SaaS platform/business-model architecture.

SEO covers crawl/indexation, information architecture, structured data, ecommerce/local/international search and current AI/generative-search guidance without ranking guarantees. Content/conversion uses evidence-based messaging and rejects dark patterns. Ecommerce separates product/variant/SKU, authoritative pricing, inventory, checkout, order/payment/fulfillment/refund states. SaaS separates identity, tenant membership, entitlements and billing state.

## Phase 07 — Production Engineering

Provides CI/CD and deployment engineering, production observability/SRE, source-control delivery governance and durable engineering/operations documentation.

Production success requires evidence after deployment: artifact identity, critical health/smoke verification, migration/job state and appropriate telemetry. Critical secret exposure, destructive unverified migrations or missing recovery strategy can block release.

## Phase 08 — AI / Asset Production

Provides production AI-system engineering plus disciplined visual-asset production.

AI engineering covers current-version-aware model/provider selection, structured outputs, tool calling, bounded agents, MCP, RAG/embeddings/reranking, streaming, evaluation, prompt-injection defense, observability, latency and cost. Privileged actions remain independently authorized and validated; retrieved content never gains policy authority.

Asset production turns approved creative/art direction into coherent images, edits, SVG/icons, illustration, 3D/video/motion and responsive delivery variants while preserving source locks, accessibility, performance, provenance and licensing state.

## Phase 09 — Final Control

Provides independent multi-review, systemic audit and final release-readiness control.

`multi-review` selects only justified reviewer lenses and reconciles evidence-backed findings without majority voting. `audit-review` uses risk-weighted sampling and critical-journey tracing to separate local defects from systemic risk. `release-readiness` is the sole final production gate and returns only **GO**, **GO WITH CONDITIONS**, **HOLD**, or **NO-GO**.

Six reviewer profiles provide independent code, design, security, performance, QA and release lenses. Severity and confidence are separate; missing mandatory evidence produces HOLD rather than an assumed pass; accepted risk never rewrites the underlying severity.

## Engine integrity

`engine/manifest.json` defines the complete 10-phase system and expected discoverable skill count. `scripts/validate_engine.py` cross-checks every phase registry against physical skill folders, frontmatter, local references, schemas, validators, reviewer infrastructure, README completion and CI governance.

`evals/master-regression.md` contains cross-phase scenarios covering routing, design anti-patterns, frontend/backend/API/data/auth, ecommerce/SaaS, security/accessibility/performance, production, AI/RAG/MCP/assets and final release control.

## Quality automation

Every `scripts/validate_*.py` validator is executed automatically by GitHub Actions on pushes and pull requests. Third-party validation workflow actions are immutable-SHA pinned and checkout does not persist credentials.
