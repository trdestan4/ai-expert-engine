---
name: code-quality
description: Owns maintainability and implementation-quality review across clarity, cohesion, coupling, type safety, error handling, dependency hygiene, duplication, dead code, refactoring, technical debt, change safety, and review standards; it improves code without replacing architecture or domain specialists.
---

# Purpose

Keep production code understandable, changeable and reviewable as the system grows, favoring explicit behavior and low accidental complexity over cleverness or stylistic churn.

## Use when

- code needs senior review/refactoring for maintainability;
- duplication, coupling, dead code, weak types, unclear ownership, dependency sprawl or technical debt is growing;
- a large change needs implementation-quality gates;
- a bug-prone area needs simplification before further features.

## Do not use when

- application architecture itself is the primary decision (`software-architecture`);
- runtime performance is primary (`performance`);
- exploit/security review is primary (`security`);
- a framework-specific correctness issue is primary (use the owning framework skill first).

## Inputs

Inspect:

- changed files and surrounding ownership boundaries;
- repository conventions/tooling;
- public interfaces and call sites;
- types, error contracts and side effects;
- duplication/dead code/dependency graph;
- tests and regression history;
- complexity hotspots and maintenance pain;
- intended future change direction.

## Workflow

### 1. Review behavior before style

Understand what the code must do and which invariants it protects. Do not refactor code you do not understand simply to match a preferred pattern.

### 2. Check ownership and cohesion

Functions/modules/components should have a clear reason to change. Split responsibilities when independent concepts are entangled; avoid fragmentation into meaningless tiny wrappers.

### 3. Reduce coupling

Keep dependency direction explicit, avoid deep knowledge of internals across modules, and use stable interfaces at boundaries. Prefer local reasoning over hidden global state.

### 4. Strengthen types and contracts

Model meaningful states explicitly. Avoid broad `any`/unchecked casts/stringly-typed states when the type system can prevent invalid behavior. Runtime validation remains required for untrusted data.

### 5. Make failures explicit

Do not swallow errors or return ambiguous sentinel values. Preserve useful context while keeping public errors safe. Define ownership of retries/fallbacks rather than scattering them.

### 6. Remove accidental complexity

Delete dead code, unused abstractions, duplicated transformations and speculative generalization. Prefer the simplest structure that preserves real variation and future change needs.

### 7. Refactor safely

Use characterization/regression tests for risky behavior, make changes in reviewable increments and avoid mixing broad refactors with unrelated feature behavior when possible.

### 8. Control dependencies

Add libraries only when their maintenance/security/runtime cost is justified. Prefer existing platform/repo primitives when adequate. Remove abandoned/duplicate dependencies intentionally.

### 9. Record debt with consequence

Technical debt should name the constraint, impact, trigger/owner and expected remediation—not become a vague TODO graveyard.

## Decision rules

- Clear code beats clever code.
- DRY means remove duplicated knowledge, not every repeated line.
- Abstraction is justified by stable shared behavior, not imagined reuse.
- Prefer composition and explicit data flow over hidden inheritance/global state unless the domain strongly supports otherwise.
- A function/module size alone is not a quality metric; responsibility and cognitive load matter.
- Type assertions that bypass uncertainty require evidence.
- Refactors need behavior-preservation evidence proportional to risk.
- Consistency with good repository conventions usually beats introducing a new personal style.

## Reference routing

Load `references/maintainability-refactoring.md` for cohesion, coupling, abstractions and safe refactoring.
Load `references/types-errors-dependencies.md` for type safety, error contracts and dependency hygiene.
Load `references/review-debt.md` for senior review severity, technical debt and change-quality gates.

Use `software-architecture` for system/module architecture, `testing-qa` for test strategy, and `security`/`performance` for specialist review.

## Quality gates

- Changed code has clear ownership and readable control/data flow.
- Types/contracts prevent important invalid states where practical.
- Errors are neither silently swallowed nor leaked unsafely.
- New abstractions/dependencies have explicit justification.
- Dead/duplicate/speculative code is not added unnecessarily.
- Risky refactors preserve behavior with tests/evidence.
- Review findings distinguish blockers from preferences.
- Technical debt that remains has explicit consequence/owner/trigger where important.

## Failure handling

If a refactor's behavior is not understood, add characterization tests or narrow the change before proceeding. If cleanup requires a cross-module architecture change, route to `software-architecture`. If quality advice conflicts with measured performance/security requirements, the specialist constraint wins and code-quality adapts around it.

## Output contract

Return:

- blocker/high/medium quality findings;
- maintainability/type/error/dependency issues;
- recommended refactors with scope;
- behavior-preservation tests;
- technical-debt items and residual risks.