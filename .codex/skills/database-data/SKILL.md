---
name: database-data
description: Owns relational and application data architecture across PostgreSQL, Supabase and other verified data stores, including schema modeling, SQL/ORM boundaries, indexes/query plans, transactions, migrations, recovery, RLS, Redis/cache, multi-tenancy, audit/retention, vectors and cross-engine data lifecycle.
---

# Purpose
Design and evolve data systems that preserve integrity, tenant isolation, query performance, operability and safe change rather than treating storage as passive persistence.

## Use when
- schema/modeling, SQL/ORM, migrations, indexes, transactions, locking, pooling, backup/restore, RLS, Redis, vectors or another database engine is involved;
- query performance or durable invariants need storage-level reasoning;
- multi-tenant ownership, audit/retention, soft delete or data lifecycle needs design;
- a database or cross-engine migration must roll out safely.

## Do not use when
- login/session/permission semantics are primary (`identity-access`);
- public API request/response design is primary (`api-engineering`);
- queue/event delivery is primary (`realtime-async`);
- general threat audit is primary (`security`).

## Inputs
Inspect actual engine/provider/version, schema/constraints/indexes/migrations, ORM/client, query patterns/cardinality/growth, tenant/access model, transaction/concurrency risks, connection topology, backup/PITR/restore capability, retention/privacy requirements and deployment constraints.

## Workflow
### 1. Model invariants first
Identify entities, ownership, lifecycle, uniqueness, relationships, deletion and consistency guarantees. Encode durable invariants in storage constraints/conditional writes where the engine supports them.

### 2. Choose data model and types deliberately
Use relational structure for relational facts, document/key-value models only when access/invariant needs justify them, and JSON for genuine variable document shape rather than avoiding modeling.

### 3. Define keys and relationships
Make identifiers, references, uniqueness, tenant scope and deletion behavior explicit. If the engine lacks foreign keys/joins, name the application/reconciliation owner for those guarantees.

### 4. Design access paths with indexes
Derive indexes/secondary access structures from real filters, joins/keys, ordering, selectivity and plans. Avoid index-everything or scan-by-default thinking.

### 5. Define transaction/concurrency semantics
Group operations by invariant. Understand isolation/atomicity, locks or conditional writes, retryable failures, uniqueness races and lost updates.

### 6. Control connections/capacity
Match pools/capacity/partition strategy to runtime. Serverless burst behavior, hot partitions and unbounded connections are design concerns.

### 7. Migrate live systems safely
Use expand/backfill/switch/contract or engine-appropriate equivalents, measure locks/rebuilds, maintain old/new compatibility, verify reconciliation and distinguish rollback from roll-forward/data restore.

### 8. Enforce access boundaries
Use grants/RLS/roles or equivalent trusted-server boundaries. Supabase exposed schemas require deliberate RLS/least privilege; privileged keys never belong in untrusted clients.

### 9. Define lifecycle and recovery
Specify backup/PITR or provider equivalent, restore testing, RPO/RTO, retention/deletion/anonymization, audit history and derived/vector/cache propagation.

### 10. Verify representative behavior
Test scale-sensitive queries/access patterns, constraints, migration behavior, concurrency, cross-tenant access and restore/cutover behavior. Never assume one engine's semantics apply to another.

## Decision rules
- Durable invariants belong as close to authoritative storage as practical.
- Indexes/access structures follow demonstrated query patterns.
- Transactions protect business invariants, not arbitrary code blocks.
- RLS can be a primary exposed-data boundary but requires correctness and performance tests.
- Redis/cache is not source of truth unless intentionally designed so.
- Soft delete is a lifecycle decision, not a default.
- Cross-engine migrations are C3/C4 until reconciliation/cutover/recovery evidence proves otherwise.
- Repository/provider version outranks remembered defaults.

## Reference routing
Load `references/postgresql-schema-modeling.md` for PostgreSQL relational modeling, keys, JSON and retention.
Load `references/sql-index-query.md` for SQL, indexes, plans and pagination.
Load `references/transactions-locking-pooling.md` for transactions, locking, concurrency and connections.
Load `references/migrations-backup-recovery.md` for live migrations, backups, PITR and restore.
Load `references/supabase-rls.md` for Supabase grants/RLS/service-role behavior.
Load `references/redis-vector-data.md` for Redis/cache and vector lifecycle.
Load `references/multi-database-adapters.md` for verified MySQL/MariaDB, MongoDB, DynamoDB or other non-PostgreSQL patterns.
Use `identity-access` for permission semantics and `security` for broad threat review.

## Quality gates
- Durable invariants and ownership are explicit.
- Keys/uniqueness/relationships/deletion behavior are intentional for the selected engine.
- Important access paths have plan/index rationale.
- Transaction/concurrency failure modes are defined.
- Live migration supports compatibility and reconciliation where needed.
- Exposed data has least privilege/RLS or an explicit trusted-server boundary.
- Backup/recovery behavior is known and tested for critical data.
- Tenant/retention/deletion behavior is testable across derived copies.

## Failure handling
If performance is uncertain, collect representative plans/distribution before guessing. If rollback is unsafe, define verified roll-forward/recovery. If access policy is ambiguous, deny by default. If engine capabilities differ from memory, inspect the actual provider/version documentation.

## Output contract
Return data model/invariants, engine-specific schema/access decisions, index/transaction reasoning, migration/reconciliation plan, access boundaries, performance/concurrency risks, recovery/lifecycle requirements and verification evidence.
