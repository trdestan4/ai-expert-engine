# Phase 05 Evals — Quality Engineering

## Routing positives

1. “Admin endpoint can read another tenant's invoice by changing the ID.” → `security` + owning identity/data skill + `testing-qa`.
2. “Add GA/Meta tracking and consent preferences.” → `privacy-compliance`; add `performance` if third-party scripts materially affect runtime.
3. “Homepage INP is 430ms and bundle grew 180KB.” → `performance` + relevant frontend/framework skill.
4. “Design test strategy for checkout.” → `testing-qa`; add `security` for money/auth risks.
5. “Modal cannot be used by keyboard and focus disappears.” → `accessibility` + frontend owner.
6. “Refactor duplicated service code without changing behavior.” → `code-quality` + `testing-qa`.

## Routing negatives

1. Pure PostgreSQL index design should route to `database-data`; `performance` joins only if measured latency is the goal.
2. Session lifetime semantics belong to `identity-access`; `security` reviews threats but does not own product/session policy.
3. UI color/typography direction belongs to creative/design skills; `accessibility` only owns accessibility constraints.
4. A simple CSS spacing edit does not automatically activate all six quality skills.
5. KVKK/GDPR legal interpretation must not be invented by `privacy-compliance`; current authoritative verification is required.

## Edge cases

- A client-side performance optimization removes labels/semantics: performance improvement must be rejected until accessibility regression is fixed.
- A cache optimization exposes personalized data publicly: security/correctness blocks the optimization.
- A test suite has 95% coverage but no tenant-denial tests: coverage percentage does not satisfy security confidence.
- A scanner reports a vulnerable package that is unreachable in production: investigate exploitability/reachability rather than blindly declaring critical risk.
- A user asks for WCAG compliance from an automated score only: reject proof-by-score and require manual critical-journey verification.
- A deletion endpoint removes primary rows but leaves analytics/vector copies: privacy lifecycle is incomplete.

## Quality assertions

- `security` mentions trust boundaries, server-side authorization, secrets, supply chain, negative tests and release blocking.
- `privacy-compliance` distinguishes engineering controls from legal certification and requires current verification for jurisdiction-specific claims.
- `performance` uses measured baselines and contains current LCP/INP/CLS p75 targets.
- `testing-qa` selects test boundaries by risk, includes negative paths and treats flakiness as a defect.
- `accessibility` references WCAG 2.2, native semantics, keyboard/focus and automated+manual testing.
- `code-quality` distinguishes blockers from preferences and requires behavior-preserving refactor evidence.
- Routing activates only quality gates justified by the change's actual risk.
- Critical security/accessibility blockers can prevent release.