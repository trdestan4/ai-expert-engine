# Abuse, Security Testing and Release Triage

## Abuse cases

Think beyond confidentiality/injection. Model spam, scraping, credential stuffing, account enumeration, invitation abuse, free-trial farming, quota exhaustion, refund/coupon abuse, payment retries, expensive AI/tool calls, file-storage abuse and admin/operator misuse.

Controls may include progressive friction, rate/velocity limits, quotas, idempotency, risk scoring, step-up auth, anomaly detection, moderation or operational review. Choose controls from abuse economics and false-positive cost; CAPTCHA everywhere is not a strategy.

## Security testing portfolio

Use code review and targeted negative tests for changed boundaries. Add SAST/SCA/secret scanning where it has signal. DAST/fuzzing is valuable for parsers/protocols/public HTTP surfaces but cannot prove authorization correctness without contextual scenarios. Property-based tests can explore encodings/state transitions; security unit tests can protect known invariants.

For authz, build a subject × action × resource/tenant matrix including direct-object access and background/admin paths. For SSRF/file/parser paths, include redirects, alternate encodings, nested/compressed inputs and resource limits.

## Severity

Assess exploitability/reachability, required privilege/user interaction, confidentiality/integrity/availability impact, tenant/customer scope, persistence, detectability and recovery. Confidence is separate: verified, strong or tentative.

Blockers generally include cross-tenant access, privileged secret exposure, remote code execution/critical injection, unauthorized money movement/tool action, destructive authz bypass or high-impact data exfiltration. Medium findings can still block when release scope or policy makes the residual risk unacceptable.

## Release evidence

R3/R4 security review should identify exact candidate, changed trust boundaries, tests, configuration/provider assumptions and unresolved findings. Candidate changes invalidate affected evidence. Accepted blocker risk needs accountable rationale and future expiry; expiry reactivates the blocker.

Security headers/scanners/green CI are supporting evidence. A release pass requires the changed abuse paths and trust boundaries to be adequately verified.
