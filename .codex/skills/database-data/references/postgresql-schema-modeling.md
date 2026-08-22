# PostgreSQL Schema and Data Modeling

Use the repository's actual PostgreSQL version. As of August 2026 PostgreSQL 18 is the current stable major and 19 is beta; never apply 19-only behavior to production projects unless the repo explicitly targets it.

## Modeling

Start with business invariants, ownership and lifecycle. Prefer explicit relational structure for facts with stable relationships. Use primary keys, foreign keys, unique constraints, checks and NOT NULL to make invalid states difficult to store.

Choose delete behavior deliberately: RESTRICT/NO ACTION for protected dependencies, CASCADE only for true owned lifecycles, SET NULL where independent child history remains meaningful. Avoid broad cascades that make destructive operations opaque.

## Multi-tenancy

Include tenant/workspace identity in ownership paths. Where composite uniqueness is tenant-scoped, encode it as such. Prevent accidental cross-tenant joins through clear keys and policy/query conventions.

## Types

Use timestamptz for instants that cross zones; preserve local-zone concepts separately when the business cares about wall-clock schedules. Use numeric/decimal for money-like exact arithmetic where appropriate. Enums can enforce compact stable domains but migrations/evolution should be considered; lookup tables/check constraints may suit evolving domains.

JSONB is useful for sparse/variable documents and external payload snapshots, but not a substitute for searchable relational structure. Index only JSON paths actually queried.

## Audit and lifecycle

Distinguish operational timestamps from immutable audit/event history. Soft delete adds filtering, uniqueness and retention complexity; adopt it only when restoration/history/legal needs justify it.

Data retention/anonymization must cover derived/search/vector copies as well as source rows.