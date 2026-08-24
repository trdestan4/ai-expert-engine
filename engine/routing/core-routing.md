# Core Routing Policy

Phase 00 has four discoverable owners. Route to the narrowest owner that can solve the next decision, then hand implementation/review to later-phase owners only when their boundary is actually reached.

## `master-agent`
Owns task classification, skill selection, execution ordering, risk escalation, verification strategy, and final orchestration. Use for multi-domain work, ambiguous ownership, project-level execution, or coordinating material review/release gates. Do not use as a substitute for domain expertise, repository inspection, independent review, or release approval.

## `repository-intelligence`
Owns verified facts about repository structure, stack, conventions, dependencies, entry points, configs, architecture, and change surface. Use for unfamiliar/existing repositories or when implementation depends on facts not yet established.

## `task-planning`
Owns decomposition of non-trivial accepted work into dependencies, decisions, acceptance criteria, verification steps, and rollback-aware execution order. Use when sequencing reduces risk; skip for tiny deterministic edits.

## `debugging`
Owns diagnosis of incorrect, failing, inconsistent, degraded, or unexplained behavior. Diagnose before modification when the cause is not proven.

## Final-control owners
- `multi-review`: independent selected reviewer lenses for a material change.
- `audit-review`: broad repository/system health and systemic-risk audit.
- `release-readiness`: final production GO / GO WITH CONDITIONS / HOLD / NO-GO decision for a specific candidate.

## Combined routing
- Existing repo + feature: `repository-intelligence` → `task-planning` → domain implementation → proportional verification/review.
- Existing repo + unknown bug: repository evidence as needed + `debugging` → proven domain owner → verification.
- Small known bug with direct evidence: `debugging` may act without full repository mapping.
- Multi-domain/high-risk request: `master-agent` orchestrates; it should not duplicate specialist reasoning.
- If debugging discovers an architectural decision, route to `software-architecture` and/or `task-planning`.
- Material cross-domain change requiring independent review: implementation → `multi-review` with selected reviewer profiles.
- Broad system health request: `repository-intelligence` → `audit-review` → targeted owners for confirmed findings.
- Production release: implementation/checks → required independent reviews → `release-readiness`.
- R3/R4 auth/data/payment/tenant/destructive production work: mandatory relevant independent review before a clean release decision.
- Reference-driven creative implementation: `design-reconstruction` only when reference analysis is needed → existing Phase 01 intent owners → minimum Phase 10 implementation owner(s) → `visual-qa` when fidelity is acceptance-critical.
- Complex scroll/3D creative page: keep intent in `creative-director`/`motion-direction`; use `creative-frontend`, `animation-engineering`, `threejs-webgl`, `realtime-shaders`, and `three-d-asset-pipeline` only for boundaries actually present; coordinate `performance`/`accessibility` and visual evidence proportionally.

## Context minimization
Before loading another skill, reviewer, or reference, ask: “Will this change the next decision, reduce material risk, or provide required evidence?” If no, do not load it. “Premium/cinematic/Awwwards/3D” is not permission to activate the entire creative stack.
