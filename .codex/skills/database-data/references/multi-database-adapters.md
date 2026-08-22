# Multi-Database Adapters

Select storage from invariants, access patterns, consistency, scale and operational constraints. Do not transpose PostgreSQL behavior onto another engine.

## MySQL / MariaDB

Verify engine/version, InnoDB behavior, default transaction isolation, SQL modes, charset/collation and online-DDL capabilities. Use `utf8mb4`/collation deliberately for language/search uniqueness requirements. Composite indexes follow left-prefix access patterns and selectivity; inspect `EXPLAIN`/runtime evidence.

Understand gap/next-key locking and how isolation affects concurrent range updates. Test migration locking/algorithm on representative size; `ALTER` syntax being reversible does not mean live-safe. Generated columns/functional indexes/version support vary.

## MongoDB

Model document boundaries around atomic update needs and read patterns, not object nesting aesthetics. Use schema validation where useful and bounded document/array growth. Choose indexes from actual filters/sorts; watch compound index order and high-cardinality/multikey cost.

Single-document operations are atomic; multi-document transactions add cost/constraints and should protect real invariants. Duplication/denormalization needs reconciliation ownership. Sharding requires shard-key distribution, query routing and migration/hotspot awareness.

## DynamoDB / key-value wide-column

Start from explicit access patterns. Partition keys must distribute traffic; avoid hot tenants/keys. Use conditional writes/transactions for concurrency and idempotency, secondary indexes for known alternate access, TTL where lifecycle fits and explicit consistency choice.

Avoid scans on critical large tables. Understand item-size, batch limits, pagination and retry/throttling. Capacity mode/autoscaling and hot partitions are application-visible. Global-table/multi-region consistency/conflict semantics require explicit design.

## Redis/cache structures

Redis is not automatically a durable source of truth. Define cache-aside/write-through/stream/lock/session purpose, TTL/eviction and stale/failure behavior. Distributed locks require fencing/ownership/timeouts if they protect critical effects; often DB atomic constraints are safer.

## Vector/search stores

Tie embeddings/index documents to source entity, tenant/privacy, version/model, refresh and deletion. Retrieval indexes are derived state unless intentionally authoritative. Reindex/re-embedding needs rollout/reconciliation.

## Cross-engine invariants

Absence of joins/constraints does not remove invariants—it moves enforcement/reconciliation responsibility. Define uniqueness, referential behavior, concurrency, backup/restore, retention/deletion and observability before adopting a store for convenience.

## Cross-engine migration

Treat as C3/C4: semantic mapping, bulk copy, CDC/dual read/write if needed, validation/reconciliation, cutover, lag/error visibility, rollback/roll-forward and data-loss detection. Test edge types/collations/timezones/IDs and old/new app coexistence.
