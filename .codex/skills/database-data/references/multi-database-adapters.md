# Multi-Database Adapters

Select storage from invariants, access patterns, consistency, scale and operational constraints. Do not transpose PostgreSQL behavior onto another engine.

## MySQL / MariaDB
Verify engine/version, transaction isolation, collation/charset, generated/default behavior and online-DDL capabilities. Design composite indexes around actual left-prefix access patterns. Test migration locking on representative size; syntax-level reversibility is not live safety.

## MongoDB
Model document boundaries around atomic update needs and read patterns, not merely object nesting. Use schema validation where appropriate, deliberate indexes, bounded arrays and explicit multi-document transaction requirements. Avoid unbounded documents and casual duplication without reconciliation ownership.

## DynamoDB / key-value wide-column systems
Start from access patterns and partition-key distribution. Protect against hot partitions, unbounded scans and item-size assumptions. Model conditional writes/idempotency for concurrency, secondary indexes for known query shapes, and eventual/strong consistency deliberately. Capacity and retry behavior are application-visible concerns.

## Generic NoSQL rules
Absence of joins/constraints does not remove invariants; it moves enforcement and reconciliation responsibility. Define source of truth, uniqueness strategy, concurrency model, retention/deletion propagation, backup/restore and observability before adopting a store for convenience.

## Migration across engines
Treat cross-engine migration as C3/C4 work: schema/semantic mapping, dual-read/write or replication strategy, reconciliation, cutover evidence, rollback/roll-forward and data-loss detection are mandatory.
