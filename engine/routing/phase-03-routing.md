# Phase 03 Routing — Backend / API

Use the smallest owning skill set.

## Primary ownership
- Backend runtime/framework, services, domain orchestration, validation, errors, config, observability, local cache/concurrency, backend tests → `backend-engineering`
- REST/GraphQL contract, OpenAPI, request/response shapes, pagination/filtering/versioning, idempotency contract, rate-limit semantics, compatibility/contract tests → `api-engineering`

## Typical routes
**Implement a server-side business rule:** `backend-engineering`.

**Design a REST endpoint contract:** `api-engineering`; add `backend-engineering` only when implementation/service behavior is also requested.

**Build a full API-backed feature:** `api-engineering` → `backend-engineering`, then add `database-data`, `identity-access`, `realtime-async` and/or `security` only when those boundaries are actually touched.

**FastAPI/Django/Node runtime bug:** `debugging` → `backend-engineering`; add `api-engineering` only if public contract behavior is wrong or changing.

**Pagination/filtering redesign:** `api-engineering`; persistence optimization belongs to `database-data`.

**Duplicate payment/order request risk:** `api-engineering` owns client-visible idempotency contract; `backend-engineering` owns application-side execution behavior; `database-data`, `integrations` and `security` join when persistence/provider/trust guarantees are material.

**Cookie/CORS/browser issue:** `web-platform`, not backend/API by default.

## Specialist boundaries
- Schema, SQL, migrations, transactions, indexing, RLS, persistence guarantees → `database-data`
- Authentication, sessions, roles, permissions, OAuth/OIDC, MFA → `identity-access`
- Queues, workers, pub/sub, WebSockets, SSE, retries/DLQ/eventual consistency → `realtime-async`
- Threat modeling, injection/abuse controls, secrets, security review → `security`

These are active engine owners. Phase 03 must hand work to them instead of absorbing their responsibilities.

## Overlap prevention
`api-engineering` defines what consumers can rely on. `backend-engineering` defines how server-side application behavior fulfills that contract. Do not duplicate database schema, identity policy, distributed messaging, or security architecture inside either skill.

## Token rule
Load Node or Python references only when that runtime is verified. Load REST or GraphQL references only for the selected API style. Normal backend-only work should not load all API references, and contract-only work should not load framework runtime references.
