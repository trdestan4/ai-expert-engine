---
name: api-engineering
description: Owns public and internal API contract design across REST, GraphQL, OpenAPI, resources, operations, errors, pagination, filtering, versioning, idempotency, rate limits, compatibility, documentation, and contract testing; it does not own backend business-logic internals, identity policy, database schema design, or transport-independent browser behavior.
---

# Purpose

Design APIs that are predictable for consumers, explicit about contracts and failure, evolvable without accidental breakage, secure at boundaries, and documented/testable from the same source of truth as implementation.

## Use when

- REST resource/operation design, request/response schemas, status codes, errors, pagination, filtering, sorting, search, or versioning is required;
- GraphQL schema/query/mutation/subscription contract design is required;
- OpenAPI descriptions, generated clients/docs, contract testing, or compatibility checks are involved;
- duplicate requests, rate limits, retries, conditional requests, or long-running operation semantics affect a public contract;
- an API needs review for consistency and evolvability.

## Do not use when

- server-side business logic and framework internals are the main concern (`backend-engineering`);
- cookie/CORS/cache semantics are the root platform issue (`web-platform`);
- authentication/authorization policy is the main decision (future `identity-access` / `security`);
- database modeling/migrations/RLS are the primary concern (future `database-data`);
- distributed messaging/realtime topology is the primary concern (future `realtime-async`).

## Inputs

Establish:

- consumer(s) and compatibility expectations;
- existing contract/style and deployed versions;
- resource/domain boundaries and invariants;
- expected request volume, pagination/search needs, and retry behavior;
- auth/permission context without redesigning it here;
- tooling/spec support in the repository;
- whether OpenAPI/GraphQL schema is source-of-truth, generated, or derived from code;
- operational constraints such as latency, payload size, rate limits, or asynchronous completion.

## Workflow

### 1. Start from consumer tasks and domain semantics

Model resources and operations around stable domain concepts, not database tables or controller filenames. Decide whether the interaction is retrieval, creation, command/state transition, bulk operation, search, or long-running work.

### 2. Choose the contract style deliberately

Use REST when resource/HTTP semantics and broad interoperability fit. Use GraphQL when consumer-driven selection over a typed graph materially improves the product and the operational complexity is justified. Do not choose GraphQL merely to avoid endpoint design.

### 3. Define request and response schemas

Specify required/optional/null behavior, scalar formats, identifiers, enums, nested structures, validation constraints, and representation ownership. Avoid ambiguous fields whose meaning changes by context.

### 4. Use HTTP semantics correctly for REST

Choose methods/status codes/cache headers/conditional semantics based on meaning. Distinguish validation, authentication, authorization, not-found, conflict, rate-limit, dependency, and server failures. Do not return `200` for every outcome.

### 5. Define stable error contracts

Prefer a documented machine-readable error model. For HTTP APIs, RFC 9457 Problem Details is the current standards-track successor to RFC 7807 when it fits the API. Human detail must not be the only machine-parsable signal.

### 6. Design collection behavior

For potentially large collections define:

- pagination model and stable ordering;
- filters/sorts/search grammar;
- maximum/default page sizes;
- cursor/token opacity and invalidation expectations;
- metadata only when consumers need it.

Offset pagination is acceptable for bounded/simple cases; cursor/keyset patterns are usually safer for large or changing datasets.

### 7. Design repeat/duplicate semantics

For operations that consumers may retry, define whether they are naturally idempotent, require an idempotency key, use a client-provided unique command identifier, or must reject ambiguous duplicates. Scope and retention of idempotency records must be explicit.

### 8. Define rate-limit and overload behavior

Rate limits should protect a real resource/abuse boundary. Document response semantics and retry guidance where useful; do not silently degrade correctness. Separate consumer quota, abuse prevention, and backend capacity controls conceptually.

### 9. Plan evolution and compatibility

Prefer additive changes where feasible. Identify breaking changes in schema, semantics, defaults, validation, enum expansion handling, auth requirements, and error behavior. Version only when compatibility cannot be preserved reasonably; do not version every internal implementation change.

### 10. Maintain machine-readable contracts

Use the repository-supported OpenAPI version/toolchain rather than blindly upgrading. As of the current specification set, OpenAPI 3.2.0 is the latest published OAS, but an existing ecosystem may legitimately target 3.1.x/3.0.x. For GraphQL, respect the server/client tooling and the latest stable spec features actually supported.

### 11. Verify contracts

Test schema validation, representative success/failure responses, backward compatibility, pagination boundaries, duplicate/retry behavior, authorization-sensitive shapes, and generated client/documentation consistency.

## Decision rules

- A public API is a product contract, not a serialization of the persistence layer.
- Compatibility includes semantics and validation behavior, not only field names.
- Human-readable error text must not be the only programmatic discriminator.
- Never expose internal exception, SQL, stack, secret, or infrastructure details in public errors.
- Do not make pagination optional for an unbounded collection.
- Retry guidance must account for idempotency; “retry on 5xx” is not universally safe.
- GraphQL resolvers still require authorization, batching/data-loading discipline, cost/depth controls where applicable, and observable failures.
- Generated OpenAPI/GraphQL artifacts must be checked for drift from runtime behavior.

## Reference routing

Load only the relevant deep module:

- `references/rest-contracts-openapi.md` for REST resource semantics and OpenAPI;
- `references/pagination-filtering-versioning.md` for collections and compatibility;
- `references/idempotency-rate-limits-errors.md` for retries, Problem Details, quotas, and overload;
- `references/graphql-contracts.md` for GraphQL schema/execution contract concerns;
- `references/api-testing-evolution.md` for contract tests, compatibility, deprecation, and release discipline.

Use `backend-engineering` for service implementation beneath the contract and `web-platform` for lower-level HTTP/browser semantics.

## Quality gates

- Contract reflects consumer/domain semantics rather than storage shape.
- Request/response validation and null/optional semantics are explicit.
- REST method/status/error semantics are coherent, or GraphQL schema semantics are coherent.
- Unbounded collections have pagination/resource controls.
- Retry/duplicate behavior is defined for side-effecting operations.
- Compatibility and deprecation rules are explicit for public consumers.
- Machine-readable specification/docs match implementation.
- Sensitive/internal details are excluded from public errors.
- Contract tests cover success, failure, boundaries, and evolution risks.

## Failure handling

If an existing API is inconsistent, preserve compatibility first, document the inconsistency, then design a migration/deprecation path rather than silently changing semantics. If tooling does not yet support the latest OpenAPI/GraphQL feature, target the supported version and record the limitation. If authorization or data consistency cannot be guaranteed by the contract layer alone, route the decision to the owning identity/database/security skill.

## Output contract

Return:

- API style and consumer assumptions;
- resource/operation/schema decisions;
- REST or GraphQL contract details;
- errors/pagination/filtering/versioning rules as relevant;
- idempotency/rate-limit semantics where relevant;
- specification/documentation source-of-truth;
- contract/compatibility test plan;
- unresolved cross-domain risks.