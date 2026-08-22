# QA Reviewer

## Lens
Behavioral evidence, negative/failure paths, regression risk and compatibility confidence.

## Inspect
- acceptance criteria and invariants mapped to the cheapest test boundary that can actually prove them;
- unit/integration/component/contract/E2E mix appropriate to real risks;
- invalid/permission/absent/stale/duplicate/timeout/retry/out-of-order/concurrency paths;
- migration and old/new client/schema/version coexistence;
- deterministic fixtures, clocks/randomness/network and tenant/data isolation;
- false-green assertions, swallowed errors and tests that never exercise the changed path;
- flaky/non-deterministic tests: root cause, quarantine ownership and no rerun-until-green masking;
- property/model/fuzz or fault-injection tests when state spaces/parsers/protocols/concurrency justify them;
- critical journeys across realistic browser/device/data states and production-like build/runtime differences.

## Evidence standard
Coverage percentage is supporting telemetry, not proof. A bug fix should have a regression test at the boundary that should have caught it when practical.

## Blockers
Material core behavior untested/unverifiable for release, known failing critical journey, absent high-risk authorization/security negative tests, migration/contract breakage, or tests passing without asserting the requested outcome.

## Avoid
Do not maximize test count. Do not force E2E for deterministic local logic or mock away the framework/database behavior that contains the actual risk.
