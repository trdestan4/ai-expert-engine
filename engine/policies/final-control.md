# Final Control Policy

Final control exists to challenge completion claims, not decorate them.

## Independence
- implementation owner may summarize evidence but must not be the only reviewer for mandatory R3/R4 gates;
- reviewer conclusions are independent and reconciled by evidence, not vote;
- review findings are not silently fixed and erased from the record.

## Evidence
- claims reference the actual candidate/diff/artifact/config/runtime evidence;
- stale evidence is invalidated when relevant candidate inputs change;
- missing mandatory evidence yields HOLD/limited confidence, not assumed pass;
- automated checks are necessary but do not replace manual/behavioral evidence where the risk requires it.

## Severity and blocking
- severity and confidence are separate;
- critical/high verified findings block clean approval unless explicitly and validly dispositioned;
- security/data/payment/tenant isolation and unrecoverable destructive-change failures block release by default;
- schedule pressure cannot lower severity.

## Risk acceptance
Accepted risk must be explicit, attributable, scoped, monitored and followed up. Acceptance never rewrites the underlying finding severity.

## Scope discipline
- multi-review reviews a change;
- audit-review assesses broader systemic health;
- release-readiness decides a specific release;
- reviewers are lenses, not auto-loaded skills;
- final control routes remediation back to domain owners.

## Release states
Only `GO`, `GO WITH CONDITIONS`, `HOLD`, or `NO-GO` are valid final release decisions.

## Quality target
The engine prefers a truthful HOLD with named missing evidence over a confident but unverified GO.