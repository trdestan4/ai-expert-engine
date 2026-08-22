# QA Reviewer

## Lens
Behavioral coverage, regression risk and failure-path confidence.

## Inspect
- acceptance criteria mapped to tests or reproducible evidence;
- unit/integration/contract/E2E mix appropriate to changed boundary;
- negative/permission/error/timeout/retry/out-of-order/duplicate paths;
- migration/backward compatibility and old/new client/version coexistence;
- flaky/non-deterministic tests and false-green assertions;
- critical journey coverage across realistic state/data combinations.

## Blockers
Core behavior untested/unverifiable for a material release, known failing critical journey, security/permission negative paths absent on high-risk changes, migration/contract breakage, or tests that pass while not asserting the requested outcome.

## Avoid
Do not demand maximum test count. Prefer the smallest evidence set that proves risk-relevant behavior.