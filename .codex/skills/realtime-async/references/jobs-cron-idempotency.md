# Jobs, Cron and Idempotency

## Job identity

Give important jobs stable business identities separate from broker message IDs. Use unique constraints/state records/deduplication keys to make repeated enqueue or delivery safe.

Idempotency means repeated execution yields an acceptable single business effect; merely detecting the same request in memory is not durable idempotency.

## Scheduled work

Define timezone, daylight-saving behavior, overlap policy, missed-run/catch-up behavior and maximum runtime. Prefer UTC schedules for system maintenance unless wall-clock business time is required.

For singleton jobs, use provider-native singleton/lease primitives or a durable database lock/state record. Include lease expiry and ownership so crashed workers do not block forever.

## State machine

For multi-step jobs, persist states such as pending/running/succeeded/failed/cancelled and attempt timestamps. State transitions should be atomic/validated so two workers cannot both perform an exclusive step.

## External side effects

Use provider idempotency keys where available, but also protect your own business state. Persist the external operation identity/result so retry after a timeout can reconcile whether the provider actually completed the request.

## Cancellation

Cancellation is cooperative unless the execution platform guarantees termination. Define safe checkpoints and whether already-completed side effects need compensation.

## Tests

Cover duplicate schedule firing, overlapping run, worker crash, timeout after external side effect, retry after partial progress, lease expiry, cancellation and manual replay.