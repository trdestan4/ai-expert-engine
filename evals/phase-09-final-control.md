# Phase 09 Evals — Final Control

## F01 — Routine low-risk CSS correction
Expected: no multi-review bundle; frontend owner verifies locally. Final-control skills stay unloaded.

## F02 — Material checkout refactor
Expected: multi-review selects code + QA; security if payment/auth boundary changed. Findings require evidence and acceptance conditions.

## F03 — Cross-tenant authorization change
Expected: R3; security + QA mandatory. Release-readiness cannot GO while tenant-isolation evidence is missing.

## F04 — Visual redesign
Expected: design + QA; accessibility specialist when semantics/interaction changed. Security/performance reviewers only if their boundaries changed.

## F05 — Broad repository audit
Expected: repository-intelligence then audit-review; risk-weighted sampling, critical journeys, systemic/local distinction, explicit coverage gaps.

## F06 — One bad file in audit
Expected: local finding unless repeated/shared-policy evidence supports systemic classification.

## F07 — Green CI but destructive migration has no recovery
Expected: release-readiness = NO-GO or HOLD; green CI cannot override data recovery risk.

## F08 — Release artifact rebuilt after approval
Expected: affected evidence is stale; HOLD until candidate identity and relevant gates are revalidated.

## F09 — Two reviewers disagree
Expected: no majority vote. Gather discriminating evidence or route to owner; preserve disagreement until resolved.

## F10 — Tentative security concern
Expected: severity/confidence separate. Tentative concern gets verification path; not promoted to verified blocker without evidence.

## F11 — Accepted medium operational risk
Expected: acceptance records owner, rationale, exposure, mitigation/monitoring and follow-up. Underlying finding severity is unchanged.

## F12 — Critical payment duplicate-charge path
Expected: blocker; release NO-GO until remediated and re-reviewed.

## F13 — Missing production telemetry for risky canary
Expected: HOLD; progressive rollout is not safe without detection/abort controls.

## F14 — Unrelated legacy debt during feature review
Expected: report separately; do not expand feature remediation scope unless the change worsens or depends on that debt.

## F15 — Final candidate changes after review
Expected: invalidate only affected evidence/reviews and rerun proportional gates, not every reviewer automatically.

## Global assertions
- reviewer selection is risk-based, not all-on-by-default;
- reviewers remain independent;
- findings use severity + confidence + evidence;
- release output uses only GO / GO WITH CONDITIONS / HOLD / NO-GO;
- critical/high blockers are never silently dropped;
- missing mandatory evidence cannot become an assumed pass.