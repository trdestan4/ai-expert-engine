# Failure Recovery

Use when an attempted fix failed, the environment differs from local, or evidence is incomplete.

## After a failed fix

1. Revert or isolate the diagnostic change if it adds noise or risk.
2. Record what the failed attempt disproved; do not repeat it under a different form.
3. Re-run the original reproduction to ensure the symptom did not drift.
4. Re-rank hypotheses with the new evidence.
5. Choose one new discriminating experiment.

Do not stack speculative patches.

## Production-only failure

Compare dimensions systematically:

- runtime/framework/package versions;
- environment variables and feature flags;
- build output/configuration;
- network/CDN/proxy behavior;
- database schema/data volume/permissions;
- cache/queue state;
- concurrency/load/timing;
- browser/platform differences;
- deployment region/runtime constraints.

Prefer observable diffs over “works on my machine” reasoning.

## Incomplete observability

If the decisive state is not observable, add the smallest temporary/structured instrumentation needed to answer one hypothesis. Do not log secrets, tokens, passwords, sensitive payloads, or unnecessary PII.

## Safe stop

Stop speculative execution and return a bounded diagnosis when:

- required evidence is inaccessible;
- the next test could be destructive without authorization/rollback;
- multiple causes remain indistinguishable with available telemetry;
- continued changes would increase blast radius more than information gained.
