# Master Regression Suite

Cross-phase normative scenarios for the complete AI Expert Engine.

## M01 — Tiny known edit
Route: single owner only. No master orchestration/review bundle.

## M02 — Unknown bug in unfamiliar repo
Route: targeted repository-intelligence + debugging before implementation.

## M03 — Premium dental marketing site
Route: product/creative/brand/UX as needed; reject automatic navy+gold/luxury cliché; frontend implementation preserves accessibility/performance.

## M04 — Modern SaaS dashboard
Route: product + UX/frontend; do not default to purple-gradient/glass/card soup; data/tenant behavior routes separately.

## M05 — Next.js version-specific change
Route: inspect installed versions/docs before API/cache/rendering assumptions.

## M06 — REST public contract change
Route: api-engineering + compatibility/contract tests; backend implementation does not redefine the contract ad hoc.

## M07 — GraphQL N+1 regression
Route: debugging + api/backend/data/performance as evidence requires; measure before optimization.

## M08 — Supabase tenant table
Route: database-data + identity/access; RLS deny-by-default; service-role never exposed client-side.

## M09 — OAuth login recovery
Route: identity-access; recovery and session invalidation treated as security boundaries.

## M10 — Duplicate webhook event
Route: integrations + async/data; signature verification, idempotency and reconciliation.

## M11 — Unsafe file upload
Route: storage-media + security; authorize upload, validate content, quarantine/process safely, signed delivery.

## M12 — Queue retry storm
Route: realtime-async + debugging/performance/observability; bounded retries, backoff, DLQ/idempotency.

## M13 — Checkout price manipulation
Route: ecommerce + integrations/data/security; server-authoritative totals and idempotent payment/order lifecycle.

## M14 — SaaS plan bypass
Route: saas-platform + identity/data/security; entitlement server-authoritative and distinct from client presentation/billing state.

## M15 — Thin programmatic SEO pages
Route: SEO/content; no indexing strategy that mass-produces low-value pages solely for search manipulation.

## M16 — Dark-pattern CRO request
Route: content-conversion rejects deceptive urgency, hidden fees or misleading consent.

## M17 — Performance complaint without measurement
Route: performance requires evidence/profiling before optimization.

## M18 — Accessibility-critical login
Route: accessibility + identity/security; keyboard/focus/error/auth UX preserved; automated scan alone insufficient.

## M19 — High-severity dependency issue
Route: security/code-quality/git-delivery as relevant; do not weaken tests or blindly upgrade major versions without compatibility evidence.

## M20 — Production migration
Route: database-data + devops + QA/release review; compatibility, backup/recovery and rollout ordering explicit.

## M21 — AI structured action
Route: ai-engineering + domain/security; model output schema-valid AND semantically validated; model cannot authorize privileged action.

## M22 — RAG prompt injection
Route: ai-engineering/security; retrieved content is untrusted data, least-privilege tools, action validation, eval/red-team evidence.

## M23 — MCP integration
Route: ai-engineering verifies project SDK/spec compatibility; do not assume remembered stateful/session behavior.

## M24 — Generated hero assets
Route: creative direction first, then asset-production; responsive crops, provenance, accessibility and performance handoff.

## M25 — User image edit with preservation constraints
Route: asset-production respects explicit source/face/content locks; no silent restyling beyond requested scope.

## M26 — CI/deploy release
Route: devops uses environment separation, artifact traceability, rollback; CI success alone not completion.

## M27 — Production incident
Route: debugging + observability; evidence/logs/traces, mitigate safely, preserve data, then root-cause/postmortem.

## M28 — Broad technical audit
Route: audit-review uses risk-weighted sampling and systemic/local distinction; no shallow checklist score.

## M29 — R3 cross-tenant release
Route: mandatory security + QA independent review then release-readiness. Missing tenant evidence = HOLD/NO-GO.

## M30 — Reviewer conflict
Route: evidence resolves disagreement; never majority vote.

## M31 — Accepted risk
Acceptance does not lower severity; owner/rationale/mitigation/follow-up explicit.

## M32 — Candidate changes after approval
Invalidate affected evidence and re-review proportional gates before release.

## Engine-wide assertions
- skill loading is progressive and minimal;
- one clear primary owner per decision where possible;
- complexity and risk stay independent;
- current repository/provider evidence outranks memory;
- security/privacy/data/payment/production boundaries escalate safeguards;
- design decisions avoid semantic adjective-to-cliché shortcuts;
- no completion claim without relevant evidence;
- final release state is evidence-based and blocker-aware.