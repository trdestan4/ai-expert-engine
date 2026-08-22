# Phase 05 Routing — Quality Engineering

Use the smallest specialist set that can verify the actual risk.

## Primary ownership

- Threats, secure coding, abuse, secrets, dependency/supply-chain and release security → `security`
- Personal-data purpose, minimization, consent/rights, retention and privacy evidence → `privacy-compliance`
- CWV, client/server latency, assets, cache, load and performance budgets → `performance`
- Risk-based unit/integration/contract/E2E/visual/reliability test strategy → `testing-qa`
- WCAG, semantics, keyboard/focus, screen readers, forms/auth accessibility and a11y testing → `accessibility`
- Maintainability, types/errors, dependencies, refactoring and technical debt → `code-quality`

## Typical routes

**New checkout/payment feature:** owning product/backend/integration skills → `security` + `testing-qa`; add `performance` if the flow materially changes latency/client work and `privacy-compliance` if personal/payment-adjacent data handling changes.

**New login/recovery UI:** `identity-access` + frontend owner → `security` + `accessibility` + `testing-qa`.

**Slow landing page:** `performance`; add `frontend-engineering`/`react-nextjs` for implementation and `accessibility` if optimizations change semantics/motion.

**Cross-tenant authorization bug:** `debugging` → owning identity/data skill → `security` + `testing-qa` regression coverage.

**Large refactor with no behavior change:** `code-quality` + `testing-qa`; add `software-architecture` only if boundaries/dependency direction change.

**Analytics/consent change:** `privacy-compliance`; add `security` only for sensitive trust-boundary issues and `performance` if third-party runtime cost matters.

## Mandatory gate escalation

Security review is mandatory for R3/R4 changes touching auth/authz, money, tenant isolation, secrets, uploads, webhooks, privileged/admin actions or sensitive-data exposure.

Testing evidence is mandatory for behavior-changing production code; depth scales with risk.

Accessibility review is mandatory for new/changed critical user interactions, authentication and form flows.

Performance review is mandatory when a change materially increases bundles, blocking requests, expensive queries/jobs or critical-path work.

Privacy review is mandatory when new personal-data collection, purpose, processor, retention or sharing is introduced.

## Token rule

Do not load all quality skills by default. Route from the change's real risk. Normal low-risk code may need only `code-quality` or `testing-qa`; high-risk product changes may activate several gates.