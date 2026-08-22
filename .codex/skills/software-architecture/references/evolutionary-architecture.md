# Evolutionary Architecture and Migration

## Prefer evolution over rewrite

When a working system exists, preserve behavior and migrate in observable slices unless a full replacement is required by a hard constraint.

Typical sequence:

1. characterize existing behavior with tests/traffic/contracts;
2. identify the target boundary;
3. add an adapter/facade if consumers need stability;
4. migrate one vertical use case;
5. verify behavior, performance, and operational signals;
6. migrate remaining consumers;
7. remove the old path only after dependency search proves it is unused.

## Modular monolith vs services

A module should become independently deployed only when the benefit justifies network/operational cost. Strong drivers include:

- genuinely independent release cadence;
- independent scaling characteristics with measured pressure;
- distinct ownership/availability boundary;
- technology/runtime requirement impossible or harmful in-process;
- isolation required by operational constraints.

Weak drivers include “microservices are scalable”, codebase size alone, or a desire for cleaner folders.

## Compatibility

For public/internal contracts with existing consumers:

- prefer additive changes before removals;
- version only when compatibility cannot be preserved cleanly;
- migrate readers before destructive schema/field removal;
- define deprecation window/observability when consumers are not all controlled together.

## Data migration

Structural code migration and persisted-data migration are separate risks. For persistent data use staged expand/migrate/contract patterns when practical:

- expand schema/accept both forms;
- backfill/migrate with resumable verification;
- switch reads/writes;
- observe;
- contract/remove old representation.

Detailed database migration ownership belongs to the data phase.

## Distributed boundaries

Cross-process calls require explicit handling of latency, timeouts, retries, duplicate delivery, idempotency, partial failure, schema compatibility, and observability. These costs disappear for in-process calls; count them before extracting a service.

## Architecture fitness

Use enforceable checks where useful:

- forbidden import/dependency rules;
- package/module boundary linting;
- contract tests;
- circular dependency detection;
- ownership/codeowners;
- performance/reliability budgets.

A rule that matters but is never checked will eventually drift.

## Revisit triggers

Record observable triggers such as request volume, team split, deployment frequency, failure isolation need, dependency replacement, or build-time threshold. Revisit architecture when the trigger occurs, not on a calendar because “we may need scale.”
