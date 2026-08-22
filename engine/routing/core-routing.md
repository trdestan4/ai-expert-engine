# Core Routing Policy

Phase 00 has four discoverable owners. Route to the narrowest owner that can solve the next decision, then hand implementation/review to later-phase owners only when their boundary is actually reached.

## `master-agent`

Owns: task classification, skill selection, execution ordering, risk escalation, verification strategy, and final orchestration.

Use for: multi-domain work, ambiguous ownership, project-level execution, deciding which specialist(s) to invoke, or coordinating material review/release gates.

Do not use as a substitute for domain expertise, detailed repository inspection, independent review, or release approval.

## `repository-intelligence`

Owns: verified facts about repository structure, stack, conventions, dependencies, entry points, configs, architecture, and change surface.

Use for: unfamiliar/existing repositories, architecture discovery, impact analysis, or when implementation depends on facts not yet established.

Do not use for generic greenfield questions with no repository context.

## `task-planning`

Owns: decomposing non-trivial accepted work into dependencies, decisions, acceptance criteria, verification steps, and rollback-aware execution order.

Use for: multi-step features, refactors, migrations, broad fixes, or work where ordering matters.

Do not use for tiny deterministic edits where a plan would add overhead without reducing risk.

## `debugging`

Owns: diagnosis of incorrect, failing, inconsistent, degraded, or unexplained behavior.

Use for: bugs, broken builds, failing tests, runtime errors, regressions, intermittent behavior, and performance anomalies that require diagnosis.

Do not use when the cause is already proven and the remaining work is straightforward implementation.

## Final-control owners

- `multi-review`: independent selected reviewer lenses for a material change.
- `audit-review`: broad repository/system health and systemic-risk audit.
- `release-readiness`: final production GO / GO WITH CONDITIONS / HOLD / NO-GO decision for a specific candidate.

These do not replace implementation owners or debugging.

## Combined routing

- Existing repo + feature: `repository-intelligence` → `task-planning` → domain implementation → proportional verification/review.
- Existing repo + unknown bug: `repository-intelligence` (only as needed) + `debugging` → domain implementation → verification.
- Small known bug with direct evidence: `debugging` may act without full repository mapping.
- Multi-domain/high-risk request: `master-agent` orchestrates; it should not duplicate specialist reasoning.
- If debugging discovers an architectural decision, route to `software-architecture` and/or `task-planning` instead of expanding debugging scope.
- Material cross-domain change requiring independent review: implementation → `multi-review` with selected reviewer profiles.
- Broad technical/system health request: `repository-intelligence` → `audit-review` → targeted owners for confirmed findings.
- Production release: implementation/checks → required independent reviews → `release-readiness`.
- R3/R4 auth/data/payment/tenant/destructive production work: mandatory relevant independent review before a clean release decision.

## Context minimization

Before loading another skill, reviewer, or reference, ask: “Will this change the next decision, reduce material risk, or provide required evidence?” If no, do not load it.
