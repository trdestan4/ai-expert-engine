# Architecture Decisions and Module Boundaries

## Drivers before patterns

A structural decision is justified by a driver: ownership, rate of change, invariant, persistence boundary, deployment boundary, measured scale, compatibility, or operational constraint. A named pattern alone is not a driver.

## Cohesion and coupling

Aim for high internal cohesion: code inside a module changes for related reasons. Coupling across modules should be intentional and visible through a small contract.

Bad signs:

- one feature change edits many unrelated folders;
- shared utilities contain domain decisions from many owners;
- UI reaches directly into persistence/integration details;
- modules depend on each other's internals;
- circular dependencies encode unclear ownership.

## Boundary types

Use the boundary that matches the problem:

- component boundary: UI behavior/reuse;
- feature/module boundary: use-case ownership;
- domain boundary: distinct rules/language/invariants;
- adapter boundary: volatile external system/framework;
- process/service boundary: independent deployment/scale/failure/ownership.

Do not jump directly from “separate responsibility” to “separate service.”

## Dependency direction

Stable business/use-case contracts should not be forced to import volatile infrastructure details when decoupling has clear value. But avoid interface ceremony where no substitution, volatility, ownership, or testing benefit exists.

## Shared code

Move code to shared only when:

- semantics are genuinely identical;
- API can remain stable for all consumers;
- ownership is clear;
- duplication cost exceeds coupling cost.

Two similar functions are not automatically the same abstraction.

## Contracts

A module contract should express the smallest public surface needed. Prefer domain/use-case values over framework request/response objects when the boundary should survive framework changes.

Define errors/outcomes and compatibility expectations, not just function names.

## ADR format

Use for material decisions only:

- Context / drivers
- Decision
- Material alternatives considered
- Consequences/trade-offs
- Revisit trigger

Avoid long essays and retrospective justification.

## Change scenario test

Before accepting a boundary, simulate two or three realistic future changes. A good boundary contains the changes likely to happen together and isolates changes likely to happen independently.
