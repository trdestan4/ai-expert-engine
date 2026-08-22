# AI Expert Engine — Global Agent Rules

This repository defines a token-efficient, production-grade expert system for Cursor and Codex.

## Operating hierarchy

1. `master-agent` owns routing and orchestration.
2. `repository-intelligence` establishes evidence about an existing codebase.
3. `task-planning` converts non-trivial work into an executable, testable plan.
4. `debugging` owns evidence-driven diagnosis when behavior is wrong or uncertain.
5. Domain skills added in later phases own implementation expertise.
6. Review/release skills added later own independent quality approval.

## Non-negotiable rules

- Inspect before changing: never infer repository architecture when it can be verified cheaply.
- Load minimally: activate only the smallest set of skills and references needed for the current task.
- Preserve local conventions unless the task explicitly requires a migration or architectural change.
- Prefer evidence over assumptions; label material uncertainty and resolve it before high-risk changes.
- Separate diagnosis from implementation. Do not patch symptoms before identifying the likely cause.
- Keep changes scoped. Do not perform opportunistic rewrites unrelated to the accepted task.
- Treat authentication, authorization, payments, secrets, data access, migrations, production configuration, and destructive operations as elevated risk.
- High-risk changes require explicit verification and the relevant specialist/reviewer once those phases exist.
- Never claim completion without evidence appropriate to the task: tests, type checks, build checks, runtime verification, or documented manual verification.
- Do not silence failing tests, weaken security controls, or remove validation merely to make a check pass.
- Prefer deterministic scripts/checks for mechanical work; use model reasoning for judgment, trade-offs, and synthesis.
- Keep persistent instructions small. Deep expertise belongs in skill-local `references/`, reusable automation in `scripts/`, and examples/checklists outside the always-loaded path.
- If two skills overlap, route by ownership: orchestration → master, repository facts → repository intelligence, plan/decisions → task planning, failure diagnosis → debugging, implementation → domain specialist.

## Completion standard

A task is complete only when the requested outcome is implemented or answered, material risks are addressed, relevant checks pass, and unresolved limitations are stated plainly.
