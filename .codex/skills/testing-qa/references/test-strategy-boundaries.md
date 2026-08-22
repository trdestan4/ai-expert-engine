# Test Strategy and Boundaries

Start from risks, invariants and acceptance criteria, then choose the cheapest boundary that can prove them.

## Test levels

- **Unit:** deterministic local logic/state machines/parsers where framework behavior is irrelevant.
- **Component/UI:** interaction/state/accessibility behavior with realistic boundaries.
- **Integration:** database/ORM/framework/provider adapter/queue/storage boundaries.
- **Contract:** independently evolving API/event/provider interfaces and compatibility.
- **E2E:** a small set of critical journeys across production-like composition.

Avoid mock-heavy unit suites when the risk is middleware, ORM serialization, auth/RLS or framework routing. Avoid pushing every edge case through slow E2E when a lower boundary proves it better.

## Behavior matrix

For important behavior cover success, invalid input, permission denial, absent/stale data, duplicate/replay, timeout/retry, partial failure and relevant concurrency/order cases. High-risk authz requires subject × action × resource/tenant negative tests.

Bug fixes should reproduce the defect, fail before the fix and pass after at the boundary that should have caught it when practical.

## Property/model-based testing

Use property-based tests for parsers/serializers, financial/math invariants, normalization and large input spaces. Use state-machine/model-based tests for workflows such as orders, subscriptions, retries or entitlement transitions when enumerating every sequence manually is fragile.

## Mutation testing

Mutation testing can reveal assertions that execute code without proving behavior. Use selectively on critical deterministic logic; do not chase mutation score globally when integration boundaries carry the real risk.

## Fuzzing

Fuzz untrusted parsers, codecs, URL/path normalization, file formats and protocol handling when input space and risk justify it. Bound resources and keep crash/minimized corpus artifacts for regression.

## Determinism

Control clocks, randomness, IDs, network and tenant/test data. Avoid order dependence and shared mutable fixtures. Seed randomized tests and report the seed/counterexample.

## Coverage

Line/branch coverage is diagnostic. 100% line coverage with no unauthorized-path test can still be unsafe. Map critical acceptance/risk to explicit evidence instead of optimizing a percentage.
