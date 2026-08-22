# Queues, Retries and Dead Letters

## Delivery model

Record actual broker semantics: ack/nack, visibility/lease timeout, redelivery, retention, ordering, partitioning, max attempts and payload limits. Design consumers for duplicate delivery unless stronger guarantees are both documented and relevant to business effects.

## Retry classification

Retry network timeouts, temporary provider failures, rate limits and other transient dependencies. Do not retry malformed input, invariant violations, forbidden operations or permanently missing resources without a state change that could make them valid.

Use bounded exponential backoff with jitter. Respect provider `Retry-After`/rate-limit semantics. Cap total attempts/age according to business usefulness.

## Dead letters

Dead-lettered work needs structured failure reason, original correlation/job identity, attempt metadata and a replay/manual-resolution path. Alert on DLQ growth or old messages.

## Worker behavior

Set bounded concurrency based on downstream/database capacity. Use graceful shutdown: stop pulling, allow current jobs to finish within a deadline, extend leases where needed, then safely redeliver unfinished work.

Do not ack before required durable state is committed. Use timeouts/cancellation on dependencies so workers do not hang indefinitely.

## Payloads

Prefer identifiers/version references over huge mutable object snapshots unless snapshot semantics are intentional. Avoid secrets/PII in broker payloads beyond what the consumer requires.

## Tests

Simulate worker crash before/after commit, duplicate redelivery, rate limit, timeout, poison payload, DLQ replay, partial downstream outage, lease expiry and concurrent consumers.