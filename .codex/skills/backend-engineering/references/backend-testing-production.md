# Backend Testing and Production Readiness

Backend verification should prove behavior at the boundary where failures actually occur.

## Test pyramid by responsibility

Use pure/domain tests for invariants and state transitions, service tests for orchestration and side-effect policy, integration tests for framework/database/cache/external adapters, and a small set of end-to-end tests for critical business flows. Do not replace all meaningful tests with mocked controller tests.

## Failure-path coverage

For important operations test invalid input, conflicts, missing dependencies, timeouts, duplicate/retry attempts, partial failure, and authorization-sensitive behavior where applicable. A success-only suite is not production evidence.

## Determinism

Control time, randomness, IDs, and external dependencies deliberately. Tests should not depend on execution order or shared mutable global state.

## Production checks

Verify startup/config validation, health/readiness behavior, dependency timeouts, connection/resource limits, graceful shutdown where relevant, structured logging, and error redaction. Confirm migrations/config required by the change are deployed in the correct order.

## Performance evidence

Use targeted measurement for known hot paths rather than speculative micro-optimization. Watch N+1 dependency/database calls, unbounded loops, large serialization, fan-out, and memory buffering.

## Release evidence

A backend change is ready when expected behavior, failure behavior, compatibility assumptions, and operational visibility are demonstrated. If production-only behavior cannot be reproduced, state the evidence gap and the telemetry needed to validate safely after release.