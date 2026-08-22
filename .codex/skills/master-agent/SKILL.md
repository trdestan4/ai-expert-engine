---
name: master-agent
description: Orchestrates complex or multi-domain engineering work by classifying the task, selecting the minimum required specialists, sequencing execution, escalating risk, and enforcing verification; it does not replace domain implementation expertise.
---

# Purpose

Coordinate the AI Expert Engine so work is solved by the right specialist, with the smallest useful context, correct execution order, explicit risk handling, and evidence-based completion.

## Use when

- the request spans multiple domains or layers;
- ownership is ambiguous;
- a project-level feature, refactor, migration, audit, or release needs coordination;
- risk determines which specialists/reviewers must participate;
- multiple valid approaches require an execution-level decision.

## Do not use when

- a single narrow specialist clearly owns a simple task;
- the task is only repository discovery (`repository-intelligence` owns that);
- the task is only diagnosis of broken behavior (`debugging` owns diagnosis);
- the task is only decomposing an already-scoped change (`task-planning` owns detailed planning).

## Inputs

Establish only what is necessary:

- user outcome and explicit constraints;
- whether work is greenfield or existing-repository work;
- known stack/repository facts or a need to discover them;
- material risk boundaries;
- acceptance criteria if supplied.

Do not block on optional preferences when a safe, reversible default exists.

## Workflow

### 1. Classify intent, complexity, and risk separately

Identify primary intent: explain, design, implement, debug, refactor, migrate, review, optimize, secure, deploy, or release.

Classify **complexity**:

- **C0** — tiny/local deterministic task with one clear owner;
- **C1** — normal single-domain task;
- **C2** — multi-file or cross-layer task with meaningful dependencies;
- **C3** — broad multi-domain change, migration, or substantial refactor;
- **C4** — system-level architecture, release, or program of coordinated changes.

Classify **risk independently** using `references/risk-and-escalation.md`:

- **R0** cosmetic/informational;
- **R1** normal implementation;
- **R2** contract-sensitive/cross-layer;
- **R3** high-risk trust/data/production boundary;
- **R4** critical/release-systemic.

Never infer risk from code size. A C0 permission edit may still be R3; a C3 cosmetic reorganization may have lower security risk.

### 2. Establish evidence needs

For existing repositories, invoke `repository-intelligence` only to resolve facts that affect the next decisions. Do not request a full codebase map by default.

For broken/uncertain behavior, delegate diagnosis to `debugging` before planning a fix.

### 3. Select the minimum skill set

Choose one primary owner and only the supporting specialists necessary to cross real boundaries.

A specialist is justified only when it:

- owns a required implementation domain;
- resolves material uncertainty;
- supplies a mandatory risk review;
- verifies an acceptance criterion the primary owner cannot independently establish.

Avoid “just in case” skill loading.

### 4. Decide whether detailed planning is warranted

Invoke `task-planning` for C2–C4 work, R3–R4 risk, migrations, or tasks with dependency/order constraints. Skip formal planning for low-risk deterministic edits.

### 5. Build execution order

Sequence by dependency and risk. Typical order:

1. repository facts / diagnosis;
2. requirements and architecture decisions;
3. data/API contracts before dependent UI where applicable;
4. implementation;
5. tests and verification;
6. risk-specific review;
7. release readiness for production release work.

Prefer reversible steps before irreversible ones.

### 6. Execute without ownership drift

Keep each specialist inside its contract. If a specialist discovers a decision outside its domain, route that decision rather than allowing the skill to expand indefinitely.

### 7. Verify

Select evidence proportional to the changed boundary and risk:

- syntax/type/lint checks;
- targeted tests;
- integration/E2E checks;
- build/runtime verification;
- schema/migration validation;
- security/performance/accessibility/SEO review when applicable.

A passing build alone is not proof of behavioral correctness.

### 8. Close the task

Report the outcome, meaningful checks, unresolved limitations, and any follow-up that is genuinely required. Do not claim success when a mandatory check could not be performed.

## Decision rules

- If one specialist can own the full task safely, do not orchestrate multiple skills.
- If the repository is unfamiliar and implementation depends on its conventions, inspect before planning.
- If behavior is wrong and cause is uncertain, diagnose before modifying.
- If a change crosses a trust/data boundary, elevate risk even if code size is small.
- If specialists disagree, prefer verified repository evidence, explicit requirements, safer/reversible choices, and documented trade-offs in that order.
- If verification disproves the implementation assumption, return to diagnosis/planning; do not weaken the check.
- Complexity controls orchestration depth; risk controls mandatory safeguards/review. Never substitute one for the other.

## Reference routing

Load `references/risk-and-escalation.md` when risk classification is ambiguous or determines mandatory review.

Use the shared policies in:

- `../../../engine/routing/core-routing.md`
- `../../../engine/policies/token-budget.md`

Do not load domain references here; route to the domain owner.

## Quality gates

- Primary owner is unambiguous.
- Complexity and risk are classified independently when material.
- Every activated skill has a concrete reason.
- Execution order respects dependencies and irreversible risk.
- Acceptance criteria are testable.
- Mandatory risk review is not skipped.
- Completion is supported by evidence, not confidence language.
- Context load remains proportional to task complexity.

## Failure handling

If routing is uncertain, gather the smallest missing evidence rather than loading all candidate skills. If a specialist fails or verification contradicts the plan, preserve evidence, reassess the failed assumption, and reroute only the affected decision. Escalate to a broader review only after narrower recovery fails or risk requires it.

## Output contract

Return a compact orchestration result containing:

- intent and, when useful, independent complexity/risk classification;
- selected owner(s) and execution order for non-trivial work;
- material risk gates;
- verification evidence;
- final status and unresolved limitations.
