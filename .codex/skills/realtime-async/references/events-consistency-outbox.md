# Events, Consistency and Outbox

## Event meaning

Name events as facts that already happened (`OrderPaid`) rather than remote commands disguised as events where possible. Define producer ownership, schema/version, entity identity, occurred-at time, correlation/causation IDs and privacy classification.

## Dual-write problem

If a database state change and event publication must agree, avoid `commit DB; publish message` without recovery. Use transactional outbox, change-data-capture or provider-specific atomic integration so accepted state cannot silently lose its event.

Consumers should use inbox/deduplication or idempotent transitions because outbox publication can repeat.

## Ordering/versioning

Prefer per-entity sequence/version checks rather than global ordering. Out-of-order events should either be safely ignored/reconciled or buffered according to business requirements.

## Eventual consistency

Document what can be temporarily stale, the expected convergence window and how users/systems observe pending state. Do not present asynchronous acceptance as completed business success.

## Schema evolution

Add compatible fields first, tolerate unknown fields where appropriate, and version/break only when necessary. Keep old consumers in mind during rollout. Avoid events coupled directly to an internal ORM row shape.

## Compensation

For distributed workflows where atomic transactions are impossible, define compensating actions and terminal/manual states. Compensation is a business action, not a generic rollback.

## Tests

Test lost publisher recovery, duplicate publication, old/new schema consumers, out-of-order versions, delayed consumers, partial workflow failure, compensation and rebuild/replay from persisted history where supported.