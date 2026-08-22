# Test Strategy and Boundaries

Start from risks and invariants, then choose the cheapest boundary that can prove them. Unit tests suit deterministic local logic; integration tests suit service/database/framework boundaries; contract tests protect independently evolving interfaces; E2E tests protect a small set of critical journeys.

Avoid a mock-heavy “unit only” suite when the real risk is ORM behavior, serialization, auth middleware or framework integration. Conversely, avoid pushing every edge case through slow E2E flows when the behavior can be proven reliably lower in the stack.

For each important behavior define success, invalid input, permission denial, absent/stale data, duplicate requests and relevant concurrency/failure cases. Bug fixes should add a regression test at the boundary that should have caught the defect.

Test names and fixtures should describe domain behavior rather than implementation details. Keep test data isolated per case/tenant and avoid order dependence or hidden global state.