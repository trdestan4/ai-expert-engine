# Finding Severity, Confidence and Disposition

Severity, confidence and release-blocking status are separate decisions.

## Severity

- **Critical:** credible catastrophic outcome such as broad unauthorized access, privileged secret compromise, RCE/major data exfiltration, uncontrolled money movement, unrecoverable corruption or production-wide availability loss. Block by default.
- **High:** serious security/correctness/data/operational/user impact with meaningful likelihood or blast radius. Usually blocks high-risk release until remediated or explicitly accepted under policy.
- **Medium:** material defect/risk with bounded impact, workaround or limited exposure. May block depending on critical journey, accumulation and release context.
- **Low:** limited quality/maintainability/polish issue with small operational/user impact.
- **Info:** observation/opportunity with no demonstrated defect.

Severity should account for impact, affected users/tenants/data/money, exploitability/likelihood, persistence, detectability and recovery difficulty. Do not inflate severity because a vulnerability category sounds scary or reduce it because the fix is inconvenient.

## Confidence

- **Verified:** reproduced, proven by code/config/runtime evidence or deterministic invariant/contract violation.
- **Strong:** multiple consistent signals and clear causal path with a small verification gap.
- **Tentative:** plausible concern requiring a discriminating check before treating it as fact.

A tentative concern can justify investigation/HOLD when potential impact is critical and evidence is unavailable, but it should not be represented as a verified vulnerability.

## Blocker decision

Blocker status reflects release safety, not only severity. Typical blockers:
- verified critical/high issue on changed critical path;
- high-risk negative test/evidence absent where policy requires it;
- environment/candidate/recovery ambiguity for production;
- incompatible migration with no safe coexistence/recovery;
- expired accepted blocker risk.

A medium issue may block if it breaks the only critical user journey. A high issue may occasionally be accepted with strong containment, accountable authority and future expiry. Acceptance never rewrites severity.

## Finding contract

Every actionable finding records:
- stable ID and reviewer;
- exact candidate and affected surface;
- title;
- severity + confidence;
- concrete evidence or reproduction path;
- user/system/security impact;
- acceptance condition that can be verified;
- owning specialist/team;
- blocker flag;
- status: open/resolved/accepted;
- resolution/risk expiry when applicable.

## Deduplication

Merge findings only when they share the same root cause and acceptance condition. Preserve separate consequences when one root cause creates independently important security/data/availability risks. Reviewer disagreement is resolved by evidence or additional verification, not voting.

## Disposition

- **Resolved:** acceptance condition verified on the current candidate.
- **Accepted:** unresolved risk deliberately allowed with authority, rationale, containment/monitoring and future expiry.
- **Open:** unresolved; if blocker, release gate remains blocked.

Do not mark a finding resolved because code changed. Re-test the acceptance condition.
