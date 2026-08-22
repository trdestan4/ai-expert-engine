---
name: testing-qa
description: Owns risk-based test strategy, unit/integration/contract/E2E/visual/accessibility/security/performance testing, test data and environments, regression design, flaky-test control, release confidence, and QA evidence; it verifies behavior without duplicating domain implementation ownership.
---

# Purpose

Build enough trustworthy evidence to release and change software safely, using the smallest test portfolio that catches important failures at the right boundary.

## Use when

- a feature or bug fix needs a test strategy;
- unit, integration, contract, E2E, visual, cross-browser/mobile, regression or load/security test coverage is required;
- test suites are flaky, slow, low-value or miss production bugs;
- release confidence/acceptance evidence needs definition.

## Do not use when

- implementation logic itself is the primary task (use the owning engineering skill, then testing);
- security threat modeling is primary (`security`);
- performance diagnosis is primary (`performance`);
- accessibility criteria are primary (`accessibility`), though testing executes their checks.

## Inputs

Establish:

- user/business-critical flows and invariants;
- change scope/risk level and known regressions;
- architecture boundaries and external dependencies;
- supported browsers/devices/runtimes;
- existing test frameworks, fixtures and CI;
- production failure history;
- environment/data constraints;
- deterministic versus time/network/provider-dependent behavior.

## Workflow

### 1. Convert risk into assertions

List what must remain true, what may fail, and what failure would be costly. Prioritize auth/permissions, money, tenant isolation, data mutation, migrations, uploads, integrations and critical journeys.

### 2. Choose the lowest useful boundary

Use unit tests for isolated deterministic logic, integration tests for real component/service/data boundaries, contract tests for consumer/provider agreements, and E2E for critical cross-system journeys. Do not force every behavior through E2E.

### 3. Test negative and edge paths

Cover invalid input, permission denial, missing/duplicate/stale data, timeout/retry, concurrency, partial failure and rollback behavior where relevant. Success-only suites create false confidence.

### 4. Use realistic dependencies selectively

Mock unstable/external systems at narrow seams but keep representative integration tests against real database/framework/provider contracts where drift would matter.

### 5. Make test data intentional

Use explicit factories/fixtures with tenant, permission, lifecycle and boundary cases. Avoid hidden global state and order dependence.

### 6. Verify UI experience

For important UI, test keyboard/accessibility behavior, loading/error/empty states, responsive layouts and visual regressions when pixels/design contracts matter.

### 7. Control flakiness

Remove arbitrary sleeps, shared mutable state, random external dependencies and timing assumptions. Quarantine only with owner/expiry; never normalize chronic flakiness.

### 8. Build CI gates by risk

Fast deterministic tests run early. Expensive E2E/security/performance checks run when scope/risk warrants them. A failed critical test blocks release until fixed or explicitly risk-accepted.

### 9. Track escaped defects

When a production bug occurs, add the smallest durable regression test at the boundary that should have caught it and review why existing coverage missed it.

## Decision rules

- Test observable behavior/invariants, not implementation trivia.
- Prefer a few high-signal integration tests over massive mock-heavy suites when boundary behavior is the risk.
- E2E is for critical journeys, not every permutation.
- Contract tests protect independently evolving services/clients/providers.
- Flaky failures are defects in the test system.
- Coverage percentage is a diagnostic, not a quality target by itself.
- Every bug fix should consider a regression test.
- High-risk data/auth/payment changes require negative-path coverage.

## Reference routing

Load `references/test-strategy-boundaries.md` for risk-based test selection and test architecture.
Load `references/contract-e2e-visual.md` for contracts, E2E, browser/mobile and visual regression.
Load `references/reliability-security-performance-tests.md` for concurrency, failure injection, security/load and flaky-test control.

Use `accessibility`, `security` and `performance` to define specialist acceptance criteria; testing executes/verifies them.

## Quality gates

- Critical flows/invariants map to explicit tests.
- Negative/permission/failure paths are covered where risk warrants.
- Tests run at the appropriate boundary with minimal brittleness.
- External/provider drift has contract/integration coverage where needed.
- Test data is deterministic and tenant-safe.
- Flaky tests have root cause/ownership rather than permanent retries.
- CI gates align with risk and execution cost.
- Important production defects produce regression coverage.

## Failure handling

If a test cannot be made deterministic, isolate the nondeterministic dependency and redesign the boundary before adding retries. If environment constraints prevent a critical test, state the confidence gap and provide a manual/temporary verification path with an owner. Never report full release confidence when required evidence is missing.

## Output contract

Return:

- risk/test matrix;
- selected test levels and cases;
- fixtures/environment needs;
- CI gate plan;
- failures/flakiness and fixes;
- release-confidence evidence and known gaps.