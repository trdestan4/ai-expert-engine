---
name: task-planning
description: Converts accepted non-trivial engineering work into a dependency-aware, risk-aware, testable execution plan with explicit decisions and acceptance criteria; it does not perform repository discovery, root-cause diagnosis, or domain implementation.
---

# Purpose

Create the smallest plan that materially improves execution quality, sequencing, reversibility, and verification.

## Use when

- a feature spans multiple files/layers or has ordered dependencies;
- a refactor, migration, architecture change, or broad fix needs staging;
- acceptance criteria are incomplete or need conversion into testable outcomes;
- irreversible/high-risk steps need rollback planning;
- multiple implementation paths require an explicit trade-off decision.

## Do not use when

- the task is a tiny deterministic edit with one obvious implementation;
- repository facts are missing (`repository-intelligence` first);
- the root cause of a bug is not established (`debugging` first);
- detailed domain implementation knowledge is required (route to the relevant specialist).

## Inputs

- desired outcome and constraints;
- verified repository facts when applicable;
- known diagnosis for bug-fix planning;
- risk classification;
- relevant existing contracts/interfaces;
- explicit user acceptance criteria, if any.

## Workflow

### 1. Define the outcome

Rewrite the task internally as an observable result, not an activity. Preserve user constraints and explicitly identify out-of-scope work.

### 2. Resolve material unknowns

Separate:

- **blocking unknowns** — can change architecture, safety, data model, or public behavior;
- **non-blocking choices** — safe/reversible defaults can be selected;
- **irrelevant uncertainty** — does not affect the plan.

Do not turn optional preferences into blockers.

### 3. Identify contracts and invariants

List boundaries that must remain true, such as:

- public API compatibility;
- persisted-data invariants;
- auth/permission guarantees;
- UI behavior/accessibility requirements;
- performance/security constraints;
- repository conventions that should be preserved.

### 4. Decompose by dependency

Create steps that are independently understandable and verifiable. Order prerequisites before consumers. Prefer vertical slices when they produce earlier behavioral evidence; prefer foundation-first sequencing when contracts must stabilize before dependent work.

### 5. Choose an approach

When more than one material approach exists, compare only decision-relevant dimensions:

- correctness and fit with local architecture;
- implementation complexity;
- maintenance cost;
- reversibility/migration cost;
- security/data risk;
- performance/scalability where material.

Use `references/decision-framework.md` for significant trade-offs. Do not produce ceremonial comparison tables for obvious choices.

### 6. Add verification to each meaningful step

Every step that changes behavior should state how it will be proven. Prefer targeted tests/checks closest to the changed boundary, followed by broader integration checks where needed.

### 7. Add rollback/recovery for risky work

For data/config/deployment/contract changes, define the safe rollback or forward-fix path before execution.

### 8. Define completion criteria

The plan is complete only if another qualified agent could execute it without inventing material requirements or sequencing.

## Decision rules

- Plan depth should scale with uncertainty, blast radius, and irreversibility—not line count.
- Prefer existing patterns over introducing new abstractions unless the current design blocks the requirement.
- Avoid speculative “future-proofing” that is not justified by current requirements.
- Split steps at ownership/risk boundaries, not arbitrarily by file count.
- Do not mix diagnosis steps into an implementation plan unless diagnosis is itself the requested task.
- When a decision is reversible and low risk, choose a sensible default instead of over-planning.
- When a decision affects persistent data/security/public contracts, make the trade-off explicit and require the relevant review.

## Reference routing

Load `references/decision-framework.md` only when there is a meaningful architectural/implementation trade-off.

Follow `../../../engine/policies/token-budget.md` for plan depth.

## Quality gates

- Outcome is observable and scoped.
- Blocking unknowns are resolved or explicitly surfaced.
- Dependencies are ordered correctly.
- High-risk/irreversible steps have recovery strategy.
- Every behavior-changing phase has verification.
- Acceptance criteria cover the user outcome, not just implementation mechanics.
- Plan contains no unnecessary domain tutorials or unrelated cleanup.

## Failure handling

If planning reveals missing repository evidence, return that evidence request to `repository-intelligence`. If the cause of a reported defect is not proven, return to `debugging`. If a domain-specific decision cannot be made safely, identify the specialist required instead of guessing. If requirements conflict, surface the conflict and prefer explicit user constraints over inferred preferences.

## Output contract

For non-trivial work return:

- goal and scope;
- key constraints/invariants;
- material decision(s) and rationale when needed;
- ordered implementation steps;
- verification per stage;
- rollback/recovery for elevated-risk work;
- final acceptance criteria.
