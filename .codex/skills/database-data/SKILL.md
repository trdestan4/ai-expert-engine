---
name: database-data
description: Owns relational and application data architecture across PostgreSQL, Supabase, schema/data modeling, SQL, ORM boundaries, indexing, query plans, transactions, locking, pooling, migrations, backup/recovery, RLS, Redis/cache data, multi-tenancy, audit/retention, and vector data; it does not own identity policy or general API design.
---

# Purpose

Design and evolve data systems that preserve integrity, tenant isolation, query performance, operability, and safe change over time rather than treating the database as passive storage.

## Use when

- schema/data modeling, PostgreSQL/Supabase, SQL/ORM, migrations, indexes, transactions, locking, pooling, backup/restore, RLS, Redis, or vector storage is involved;
- query performance or data integrity requires database-level reasoning;
- multi-tenant ownership, soft delete, audit history, retention, or data lifecycle needs design;
- a database change must be rolled out safely in production.

## Do not use when

- login/session/role semantics are primary (`identity-access`);
- API request/response design is primary (`api-engineering`);
- queue/event delivery semantics are primary (`realtime-async`);
- general security audit is primary (future `security`).

## Inputs

Inspect:

- actual database/version/provider and extensions;
- schema, constraints, indexes, migrations, ORM/client and generated types;
- query patterns/cardinality/volume/growth;
- tenant/access model and exposed schemas/APIs;
- transaction boundaries and concurrency risks;
- connection topology/pooling/runtime limits;
- backup/PITR/restore capability and recovery objectives;
- retention/audit/compliance requirements.

## Workflow

### 1. Model invariants before tables

Identify entities, ownership, lifecycle, uniqueness, required relationships, cardinality, deletion semantics, and consistency guarantees. Put durable invariants in database constraints where practical.

### 2. Choose data types deliberately

Use types that match semantics, range and query behavior. Avoid generic text/JSON for strongly relational facts simply to avoid schema design. Use JSON/JSONB when document-shaped variability is real and indexed/query patterns are understood.

### 3. Define keys and relationships

Choose stable primary keys, foreign keys, unique constraints, cascade/restrict behavior, tenant scoping, and junction tables intentionally. Do not rely only on application checks for referential integrity.

### 4. Design queries with indexes together

Derive indexes from actual filters, joins, sort order, selectivity and query plans. Avoid speculative index accumulation. Measure write/storage cost and use `EXPLAIN`/`EXPLAIN ANALYZE` appropriately.

### 5. Define transaction semantics

Group operations by invariant, not convenience. Understand isolation, row/table locks, deadlocks, retryable failures, uniqueness races and lost-update risks. Use database-native atomic operations/constraints when possible.

### 6. Control connections and pooling

Match connection strategy to deployment/runtime. Serverless or bursty workloads usually need intentional pooling. Do not let every process create unbounded direct connections.

### 7. Design migrations for live systems

Separate additive/backfill/switch/remove phases when compatibility or table size demands it. Plan locks, defaults, index creation, dual-read/write windows, rollback/roll-forward, and old-code compatibility.

### 8. Enforce data access boundaries

Use database roles/grants and RLS where the architecture benefits from row-level enforcement. In Supabase exposed schemas, RLS/least-privilege grants are mandatory design concerns; service-role/secret keys never belong in untrusted clients.

### 9. Define lifecycle and recovery

Specify backups, PITR where required, restore testing, RPO/RTO, data retention, deletion/anonymization, audit history, and ownership of recovery procedures. A backup that has never been restored is an assumption.

### 10. Verify performance and integrity

Test representative data scale, key queries, constraints, migration behavior, concurrency, cross-tenant access, RLS policy behavior, and restore/rollback procedures for high-risk changes.

## Decision rules

- Prefer database constraints for durable invariants that must hold across all writers.
- Normalize transactional facts by default; denormalize only for measured read/workflow benefits with update semantics defined.
- Add indexes for demonstrated access paths, not every column.
- A transaction should protect a business invariant, not wrap arbitrary code.
- Offset pagination becomes costly/unstable at scale; use keyset/cursor patterns where ordering semantics permit.
- RLS is defense-in-depth and can be primary access control for exposed Supabase data, but policy design must be tested for both correctness and performance.
- Redis is not a source of truth unless durability/consistency requirements explicitly make it one.
- Soft delete is a product/data-retention decision, not an automatic default.
- Vector storage belongs with the authoritative entity lifecycle and privacy/retention model.

## Reference routing

Load `references/postgresql-schema-modeling.md` for relational modeling, types, constraints, keys, tenancy, JSON and audit/retention.

Load `references/sql-index-query.md` for SQL design, indexes, query plans, pagination and optimization.

Load `references/transactions-locking-pooling.md` for transactions, isolation, locking, concurrency and connections.

Load `references/migrations-backup-recovery.md` for production migrations, backfills, backups, PITR, restore and RPO/RTO.

Load `references/supabase-rls.md` for Supabase exposed schemas, grants, RLS policies, service roles and RLS performance.

Load `references/redis-vector-data.md` for Redis/cache structures, ephemeral state, vectors/embeddings and lifecycle.

Use `identity-access` for user/session/permission semantics and future `security` for broad threat review.

## Quality gates

- Durable invariants are encoded explicitly.
- Keys, FKs, uniqueness and deletion behavior are intentional.
- Important queries have index/query-plan rationale.
- Transactions/concurrency failure modes are defined.
- Migration rollout is compatible with live old/new code where required.
- Exposed data has least-privilege grants/RLS or an explicit trusted-server-only boundary.
- Backup/recovery behavior is known for production-critical data.
- Tenant/data lifecycle and retention are testable.

## Failure handling

If query performance is uncertain, collect a representative plan/data distribution before guessing indexes. If a migration cannot be safely rolled back, define a verified roll-forward strategy. If RLS policy behavior is ambiguous, deny by default and test under actual roles/JWT claims. If provider/version capabilities differ from memory, inspect the installed/current provider documentation before using version-specific features.

## Output contract

Return:

- data model/invariants;
- schema/index/transaction decisions;
- migration and compatibility plan;
- access/RLS boundaries;
- performance/concurrency risks;
- backup/lifecycle requirements;
- verification/tests and specialist handoffs.