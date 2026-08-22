# AI Expert Engine

A token-efficient master-class agent system for production web design and software engineering in Cursor and Codex.

## Architecture principle

The engine uses a small number of discoverable domain skills with deep expertise loaded lazily from references, scripts, policies, schemas, and evals. This keeps routing clean and context cost low while preserving expert depth.

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
- Next phase: Final Control

## Phase 00 — Core / AI Brain

Provides orchestration, repository intelligence, task planning, debugging, token policy, schemas, routing contracts, evals, and structural validation.

## Phase 01 — Creative / Product Intelligence

Provides product strategy, creative direction, brand design, anti-generic design review, color intelligence, typography intelligence, visual art direction, motion direction, and UX/UI design.

The design system explicitly rejects shortcut mappings such as `premium = navy + gold`, `luxury = black + gold`, or `AI/tech = purple gradient`. Visual decisions must be justified by product, audience, brand, content, usability, accessibility, performance, and category context.

## Phase 02 — Web Engineering / Frontend

Provides framework-independent web-platform reasoning, production frontend engineering, React/Next.js runtime expertise, and application-level software architecture.

Key rules include semantic/native browser behavior first, explicit state ownership, content-resilient responsive implementation, narrow server/client boundaries, repository-version-aware Next.js decisions, deliberate cache/freshness behavior, complete async/error/form states, and architecture proportional to real product/operational drivers.

## Phase 03 — Backend / API Engineering

Provides production backend service/runtime guidance plus REST/GraphQL contract engineering. Backend decisions cover runtime-aware service boundaries, validation, domain invariants, side effects, errors, observability, configuration, concurrency, retries, cache, and testing. API decisions cover REST/GraphQL semantics, OpenAPI, Problem Details, pagination/filtering/versioning, idempotency, rate limits, compatibility, deprecation, and contract tests.

Runtime/framework/spec advice is repository-version-aware: the engine never upgrades or applies new behavior merely because a newer standard exists.

## Phase 04 — Data / Platform

Provides identity/access architecture, PostgreSQL/Supabase data engineering, realtime and durable async workflows, third-party integrations, and secure object/media storage.

Identity decisions cover sessions, OAuth/OIDC, passkeys/MFA, recovery, RBAC/ABAC and tenant/resource permissions. Data decisions cover constraints, SQL/indexes/query plans, transactions/locking/pooling, production migrations, backups/recovery, Supabase RLS, Redis and vector lifecycle. Async decisions cover WebSockets/SSE, queues/workers, retries/DLQ, cron, idempotency, outbox and eventual consistency. Integration decisions cover webhooks, payments/billing, notifications, provider rate limits/timeouts and reconciliation. Storage decisions cover signed URLs, direct/multipart uploads, content validation, quarantine, media processing, CDN/versioning and object lifecycle.

Critical boundaries are deny-by-default for cross-tenant access, client-exposed privileged keys, duplicate side effects, unverified webhooks, unsafe live migrations and unauthorized object signing.

## Phase 05 — Quality Engineering

Provides security, privacy/compliance engineering, performance, testing/QA, accessibility and senior code-quality gates.

Security uses threat modeling and OWASP ASVS-aligned verification, secure coding, abuse controls, secrets/supply-chain review and release-blocking severity. Privacy maps personal-data lifecycle, minimization, consent/rights/retention and requires current authoritative verification for jurisdiction-specific legal claims. Performance uses measured evidence, current Core Web Vitals and client/server/load budgets. Testing selects unit/integration/contract/E2E/visual/security/load coverage by risk. Accessibility uses WCAG 2.2, semantic/native UI, keyboard/focus, accessible authentication and automated plus manual verification. Code quality governs maintainability, type/error/dependency hygiene, safe refactoring and technical debt.

Quality skills are not loaded automatically as a bundle: routing activates only the gates justified by the change's actual risk. Critical security and core-accessibility failures can block release.

## Phase 06 — Business / Growth

Provides search discoverability, conversion messaging, ecommerce domain logic and SaaS platform/business-model architecture.

SEO covers crawl/indexation, information architecture, structured data, ecommerce/local/international search, migrations and current AI/generative-search guidance without ranking guarantees. Content/conversion covers evidence-based value propositions, landing pages, UX writing, objections, trust and ethical CRO without dark patterns. Ecommerce covers product/variant/SKU, authoritative pricing, inventory, cart/checkout, order/refund lifecycles, merchandising and analytics. SaaS covers organizations/workspaces, memberships, plans, entitlements, seats, subscription lifecycle, usage metering, quotas, operator controls and tenant-aware metrics.

Business skills coordinate rather than replace engineering owners: payments/webhooks stay with integrations, authentication with identity-access, data isolation with database-data/security, and runtime performance with performance.

## Phase 07 — Production Engineering

Provides CI/CD and deployment engineering, production observability/SRE, source-control delivery governance, and durable engineering/operations documentation.

Deployment decisions cover reproducible builds, environment/config/secrets boundaries, immutable artifact promotion, Docker/serverless/Vercel targets, migration sequencing, progressive rollout and rollback/roll-forward. Observability covers structured logs, metrics, traces, OpenTelemetry conventions, SLIs/SLOs, actionable alerts, health/capacity, incidents and runbooks. Git delivery covers branch/commit/PR discipline, protected refs, CODEOWNERS, release/version/changelog traceability and GitHub Actions governance. Documentation covers README/onboarding, architecture/ADRs/API docs, operator runbooks, release/migration notes and stale-doc prevention.

Production success requires evidence after deployment: artifact identity, critical health/smoke verification, migration/job state and appropriate telemetry. Critical secrets exposure, destructive unverified migrations or missing recovery strategy can block release.

## Phase 08 — AI / Asset Production

Provides production AI-system engineering plus disciplined visual-asset production.

AI engineering covers current-version-aware model/provider selection, structured outputs, tool calling, bounded agents, MCP, RAG/embeddings/reranking, streaming, evaluation, prompt-injection defense, observability, latency and cost. Model/tool behavior is never trusted as an authorization layer: privileged actions remain independently validated, authorized and risk-gated. RAG treats retrieved documents as untrusted data and preserves permission, provenance, freshness and no-answer behavior. MCP behavior follows the project-supported protocol/SDK revision instead of remembered transport semantics.

Asset production turns approved creative/art direction into coherent images, edits, SVG/icons, illustrations, 3D/video/motion assets and responsive delivery variants. It preserves explicit source locks, sanitizes untrusted SVG, avoids baking essential UI copy into raster output, tracks masters/provenance/licensing, and verifies crop, quality, accessibility and performance at the actual product surface.

Both skills remain lazy and specialist-scoped: ordinary backend work does not load AI engineering, and ordinary UI layout does not load asset production unless the task truly needs those capabilities.

## Quality automation

Every `scripts/validate_*.py` validator is executed automatically by GitHub Actions on pushes and pull requests.
