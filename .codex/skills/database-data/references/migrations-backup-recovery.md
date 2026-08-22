# Migrations, Backup and Recovery

## Migration strategy

Classify changes as metadata-only/fast, lock-sensitive, data-backfill, destructive, or compatibility-breaking. For live systems prefer expand → backfill → switch reads/writes → verify → contract/remove.

Avoid coupling deployment success to a long blocking backfill. Make backfills resumable, bounded and observable. For large indexes/constraints use database/provider-supported online/concurrent approaches where appropriate and verify version restrictions.

When changing nullability/types, first make old/new application versions compatible, migrate data, validate, then enforce stricter constraints. Destructive changes require evidence that old code/jobs are no longer using the data.

## ORM migrations

Generated migrations are starting points, not proof of safety. Review SQL, locks, defaults, table rewrites, index strategy and rollback/roll-forward behavior. Never edit applied migration history casually; create corrective migrations according to project conventions.

## Backup model

Know what the provider actually backs up: database, object storage, secrets/config, and external systems can have separate recovery paths. Define RPO (acceptable data loss) and RTO (acceptable restoration time) for production-critical data.

PITR improves recovery options but does not replace tested restoration. Verify credentials, encryption/key dependencies and operational runbooks.

## Restore testing

Periodically restore into an isolated environment, run integrity checks, verify critical application queries, and measure restoration time. A green backup dashboard without restore evidence is not a recovery guarantee.

## Rollback versus roll-forward

Schema rollbacks can be riskier than forward fixes once new writes occur. For destructive or data-transforming migrations, design a roll-forward correction path and compatibility window rather than assuming reversal is safe.