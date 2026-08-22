# Code Review, Quality Gates and Technical Debt

## Review order

1. requested behavior/invariants;
2. security/privacy/data integrity;
3. compatibility/migration/concurrency/failure handling;
4. tests/evidence;
5. maintainability/dependencies;
6. style/readability.

Do not bury a correctness blocker under twenty naming comments.

## Finding quality

A useful finding names the affected surface, evidence/counterexample, impact and acceptance condition. Separate severity from confidence. “Could be cleaner” is not a blocker.

## Technical debt classification

Record debt by consequence and trigger:
- known correctness/security risk;
- maintainability/change friction;
- operational burden;
- performance/cost constraint;
- obsolete compatibility/dependency.

Include owner, evidence, reason for deferral and condition/date to revisit. Avoid a giant undifferentiated debt backlog.

## Quality gates

Automate deterministic checks: format, type, lint, tests, schema validation, dependency/security scans where useful. Human/model review owns context/judgment. A green gate is evidence only for what it actually checks.

## Debt vs premature cleanup

Do not refactor unrelated code during a focused bug fix unless it materially blocks safe implementation. Conversely, do not preserve a dangerous boundary because “out of scope”; escalate and minimally contain it.

## Exceptions

Suppressions/waivers require narrow scope and reason. High-impact accepted risk should have accountable owner and expiry/follow-up. Remove obsolete suppressions as part of maintenance.
