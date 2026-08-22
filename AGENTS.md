# AI Expert Engine — Global Agent Rules

This repository defines a token-efficient, production-grade expert system for Cursor and Codex.

## Operating hierarchy

1. `master-agent` owns routing and orchestration.
2. `repository-intelligence` establishes evidence about an existing codebase.
3. `task-planning` converts non-trivial work into an executable, testable plan.
4. `debugging` owns evidence-driven diagnosis when behavior is wrong or uncertain.
5. Domain skills own implementation expertise inside their boundaries.
6. `multi-review` owns independent multi-lens review for material changes; `audit-review` owns broad systemic audits.
7. `release-readiness` is the final production release gate and returns GO, GO WITH CONDITIONS, HOLD, or NO-GO.

## Non-negotiable rules

- Inspect before changing: never infer repository architecture when it can be verified cheaply.
- Load minimally: activate only the smallest set of skills, references, and reviewers needed for the current task.
- Preserve local conventions unless the task explicitly requires a migration or architectural change.
- Prefer evidence over assumptions; label material uncertainty and resolve it before high-risk changes.
- Separate diagnosis from implementation. Do not patch symptoms before identifying the likely cause.
- Keep changes scoped. Do not perform opportunistic rewrites unrelated to the accepted task.
- Treat authentication, authorization, payments, secrets, tenant/data access, migrations, production configuration, privileged AI/tool actions, and destructive operations as elevated risk.
- R3/R4 changes require explicit verification and the relevant independent specialist/reviewer; the implementation owner alone cannot self-approve mandatory review.
- Production release work uses `release-readiness` when risk or impact warrants a final gate; green CI alone is never sufficient proof of release health.
- Never claim completion without evidence appropriate to the task: tests, type checks, builds, runtime verification, review evidence, or documented manual verification.
- Do not silence failing tests, weaken security controls, remove validation, or downgrade findings merely to make a check/release pass.
- Prefer deterministic scripts/checks for mechanical work; use model reasoning for judgment, trade-offs, review, and synthesis.
- Keep persistent instructions small. Deep expertise belongs in skill-local `references/`, reusable automation in `scripts/`, reviewer lenses in `engine/reviewers/`, and examples/evals outside the always-loaded path.
- If two skills overlap, route by ownership: orchestration → master, repository facts → repository intelligence, plan/decisions → task planning, failure diagnosis → debugging, implementation → domain specialist, independent change review → multi-review, systemic audit → audit-review, production decision → release-readiness.

## Completion standard

A task is complete only when the requested outcome is implemented or answered, material risks are addressed, relevant checks pass, mandatory independent review is complete when required, and unresolved limitations are stated plainly.
