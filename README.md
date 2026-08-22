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
- Next phases: Quality, Business, Production, AI/Assets, Final Control

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

## Quality automation

Every `scripts/validate_*.py` validator is executed automatically by GitHub Actions on pushes and pull requests.
