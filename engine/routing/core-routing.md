# Core Routing Policy

Phase 00 has four discoverable owners. Route to the narrowest owner that can solve the next decision.

## `master-agent`

Owns: task classification, skill selection, execution ordering, risk escalation, verification strategy, and final orchestration.

Use for: multi-domain work, ambiguous ownership, project-level execution, or deciding which specialist(s) to invoke.

Do not use as a substitute for domain expertise or detailed repository inspection.

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

## Combined routing

- Existing repo + feature: `repository-intelligence` → `task-planning` → domain implementation.
- Existing repo + unknown bug: `repository-intelligence` (only as needed) + `debugging` → domain implementation → verification.
- Small known bug with direct evidence: `debugging` may act without full repository mapping.
- Multi-domain/high-risk request: `master-agent` orchestrates; it should not duplicate specialist reasoning.
- If debugging discovers an architectural decision is required, hand the decision to `task-planning`/future architecture skill rather than expanding debugging scope.

## Context minimization

Before loading another skill or reference, ask: “Will this change the next decision, reduce material risk, or provide required evidence?” If no, do not load it.
