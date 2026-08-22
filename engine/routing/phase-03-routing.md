# Phase 03 Routing — Backend / API

Use the smallest owning skill set.

## Primary ownership

- Backend runtime/framework, services, domain orchestration, validation, errors, config, observability, local cache/concurrency, backend tests → `backend-engineering`
- REST/GraphQL contract, OpenAPI, request/response shapes, pagination/filtering/versioning, idempotency contract, rate-limit semantics, compatibility/contract tests → `api-engineering`

## Typical routes

**Implement a server-side business rule:** `backend-engineering`.

**Design a REST endpoint contract:** `api-engineering`; add `backend-engineering` only when implementation/service behavior is also requested.

**Build a full API-backed feature:** `api-engineering` → `backend-engineering`, then future database/identity/security specialists only if their boundaries are touched.

**FastAPI/Django/Node runtime bug:** `debugging` → `backend-engineering`; add `api-engineering` only if public contract behavior is wrong or changing.

**Pagination/filtering redesign:** `api-engineering`; persistence optimization belongs to future `database-data`.

**Duplicate payment/order request risk:** `api-engineering` owns client-visible idempotency contract; `backend-engineering` owns application-side execution behavior; future database/security specialists review guarantees as needed.

**Cookie/CORS/browser issue:** `web-platform`, not backend/API by default.

## Overlap prevention

`api-engineering` defines what consumers can rely on. `backend-engineering` defines how server-side application behavior fulfills that contract. Do not duplicate database schema, identity policy, distributed messaging, or security architecture inside either skill.

## Token rule

Load Node or Python references only when that runtime is verified. Load REST or GraphQL references only for the selected API style. Normal backend-only work should not load all API references, and contract-only work should not load framework runtime references.