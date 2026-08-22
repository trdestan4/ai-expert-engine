---
name: software-architecture
description: Owns application-level structural decisions across module boundaries, dependency direction, layering, feature/domain decomposition, contracts, maintainability, scalability, and migration trade-offs; implementation details remain with frontend, backend, data, and production specialists.
---

# Purpose

Create the smallest architecture that satisfies current requirements, keeps ownership and dependency direction clear, remains testable, and can evolve without speculative abstraction or accidental coupling.

## Use when

- a project or feature needs module/layer boundaries before implementation;
- responsibilities are duplicated or tightly coupled;
- a modular-monolith, service, feature, or domain split is being decided;
- refactoring or migration changes public contracts or dependency direction;
- multiple structures have meaningful long-term trade-offs.

## Do not use when

- a local change has one obvious owner;
- the task is detailed frontend, React/Next, backend, database, or deployment implementation;
- requirements or root cause are not established;
- a pattern is being added only because it is fashionable.

## Inputs

Use product/use-case boundaries, current repository structure, runtime constraints, persistence boundaries, change frequency, team ownership where relevant, measured scale/performance needs, compatibility requirements, and demonstrated technical-debt pain.

## Workflow

### 1. Define architectural drivers

Record only forces that change structure: business capabilities, persistence boundaries, runtime/deployment boundaries, independent change/release needs, scale constraints, team ownership, and legacy/migration constraints.

### 2. Map responsibilities and invariants

Identify ownership of business rules, use-case orchestration, transport/UI, persistence/integrations, and stable shared contracts. Write important invariants before choosing directories.

### 3. Define cohesive boundaries

Group code that changes for the same reason and communicate through explicit contracts. Prefer feature/domain/module boundaries when they improve ownership. Prevent `shared` from becoming an unowned dumping ground.

### 4. Set dependency direction

Keep stable rules/contracts from depending unnecessarily on volatile framework or integration details. Introduce abstractions at real volatility, substitution, testing, or ownership boundaries rather than around every function.

### 5. Choose architecture proportionally

Compare only realistic options such as layered application, feature-sliced frontend, modular monolith, ports/adapters around volatile integrations, event-driven boundaries, or independent services. Use the least distributed and least abstract option that satisfies real drivers.

### 6. Define contracts

Specify module APIs, data/schema contracts, errors/outcomes, validation ownership, and compatibility rules. Avoid leaking internal framework or persistence objects through stable public boundaries without reason.

### 7. Design evolution

For existing systems prefer staged migration: characterize behavior, introduce a boundary/adapter, move one vertical slice, verify, repeat, then remove the obsolete path after consumers migrate.

### 8. Analyze operational consequences

Only when a boundary crosses a process/network/queue/storage line, account for latency, partial failure, retries, consistency, and observability. Do not import distributed-system complexity into in-process modules.

### 9. Record material decisions

For significant choices capture context, selected option, rejected material alternatives, consequences, and revisit trigger.

### 10. Test through change scenarios

Ask whether common changes—new variant, replaced integration, persistence change, UI/API change, test isolation, module migration—can occur without broad unrelated edits.

## Decision rules

- Architecture is an ownership/dependency system, not a folder aesthetic.
- Prefer process-local modular boundaries until independent deployment is justified.
- Introduce abstraction at volatility/ownership boundaries, not everywhere.
- Shared code needs a stable owner and genuine reuse reason.
- Stable business rules should avoid direct dependency on volatile framework details when separation pays for itself.
- Scale-driven structure requires workload evidence.
- Compatibility and migration constraints can outweigh an idealized final architecture.
- Good architecture makes undesirable dependencies obvious or difficult to introduce.

## Reference routing

Load `references/architecture-decision-system.md` for drivers, option comparison, concise ADRs, and revisit criteria.

Load `references/module-boundaries.md` for cohesion, coupling, dependency direction, contracts, shared code, and feature/domain decomposition.

Load `references/evolutionary-architecture.md` for staged migration, modular-monolith/service decisions, compatibility, and change-scenario testing.

Use `task-planning` to sequence an accepted architecture. Route detailed implementation to the owning specialist.

## Quality gates

- Drivers are explicit and evidence-based.
- Ownership/invariants are clear.
- Boundaries have high cohesion and intentional coupling.
- Dependency direction avoids unnecessary framework/integration leakage.
- Structure is no more complex/distributed than requirements justify.
- Contracts and compatibility are explicit.
- Risky structural change has a staged migration/recovery path.
- Common changes do not require unrelated broad edits.
- Major trade-offs and revisit triggers are documented.

## Failure handling

If requirements or repository ownership are unclear, return to `product-strategy` or `repository-intelligence`. If a structural proposal only solves one local implementation issue, shrink the scope and route to the implementation specialist. If decomposition adds operational complexity without a real independent-change need, prefer an in-process module boundary.

## Output contract

Return architectural drivers, responsibility/module map, dependency direction/contracts, selected structure and rejected material alternatives, migration strategy, trade-offs/revisit triggers, implementation handoff boundaries, and verification scenarios.
