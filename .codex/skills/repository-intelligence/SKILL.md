---
name: repository-intelligence
description: Builds a verified, minimal repository profile covering stack, structure, conventions, entry points, dependencies, configuration, architecture, and change surface when implementation decisions depend on existing-codebase facts; it does not plan or implement the change.
---

# Purpose

Turn an unfamiliar or partially known repository into reliable implementation context without flooding the model with the whole codebase.

## Use when

- work targets an existing repository whose relevant structure is not established;
- stack/framework/version or local conventions affect implementation;
- a change may cross modules, packages, routes, services, schemas, configs, or deployment boundaries;
- impact analysis is required before refactoring/migration;
- another skill needs verified repository facts.

## Do not use when

- the task is greenfield and no repository exists;
- all relevant files/contracts are already known and current;
- the user only wants generic technical guidance;
- the task is diagnosing behavior rather than discovering structure (`debugging` owns diagnosis, though it may request targeted repository evidence).

## Inputs

- repository root or available file tree;
- user request / decision that needs repository evidence;
- any known target files, symbols, errors, or stack hints.

## Workflow

### 1. Define the evidence question

Do not “analyze the whole repo.” State what must be learned to make the next decision, such as:

- Where is auth actually enforced?
- Which package owns API routes?
- What database client and migration system are in use?
- Which component conventions should a new page follow?

### 2. Inspect high-signal surfaces first

Prefer, in order when relevant:

1. root manifests/workspace files;
2. framework/build/config files;
3. package/dependency manifests and lockfile signals;
4. top-level source directories and entry points;
5. files/symbols directly connected to the requested change;
6. tests and examples that encode behavior;
7. CI/deployment/environment configuration when the change touches production behavior.

Avoid recursively reading every source file.

### 3. Detect the stack from evidence

Record exact evidence for:

- languages and versions when discoverable;
- frameworks/runtime;
- package manager/workspace model;
- styling/UI system;
- backend/API layer;
- database/ORM/storage;
- auth provider/session model;
- testing/build/deployment tooling.

Distinguish “verified” from “inferred.” Do not convert inference into fact.

### 4. Map only the relevant architecture

Identify:

- entry points and request/data flow;
- ownership boundaries;
- shared layers/utilities;
- public/internal contracts;
- state/data persistence points;
- relevant tests;
- configuration and environment dependencies.

Use symbol/path references rather than copying source into the profile.

### 5. Learn local conventions

Sample representative nearby code to determine:

- naming and file organization;
- component/service patterns;
- validation/error conventions;
- type/schema conventions;
- test style;
- import/module boundaries.

Prefer local established conventions over generic preferences unless they create a material defect.

### 6. Determine change surface

Classify affected areas as:

- **direct** — must change;
- **dependent** — likely needs verification/update;
- **risk boundary** — auth/data/API/config/production surface requiring specialist review;
- **unrelated** — explicitly keep out of scope.

### 7. Emit a compact repository profile

Use the schema in `../../../engine/schemas/repository-profile.schema.json` when a structured artifact is useful. Keep only facts that can affect the current task.

## Decision rules

- If a fact can be checked cheaply, verify it instead of guessing.
- If multiple implementations coexist, inspect the code nearest to the target and identify whether a migration is in progress.
- Lockfiles and installed manifests outrank remembered framework defaults.
- Tests can be stronger behavioral evidence than comments; current executable code outranks stale documentation.
- Do not assume a `.env.example` value exists in production or that a dependency is actually used merely because it is installed.
- Stop discovery when additional inspection is unlikely to change routing, plan, or risk.

## Reference routing

Load `references/repository-profile.md` for the profile fields and evidence-strength model.

For token discipline, also follow `../../../engine/policies/token-budget.md`.

## Quality gates

- Stack claims have repository evidence.
- Relevant entry points and ownership boundaries are identified.
- Local conventions are based on representative files, not preference.
- Direct/dependent/risk surfaces are separated.
- Unknowns that could change implementation are explicit.
- Profile is scoped to the requested work rather than a repository encyclopedia.

## Failure handling

If expected files are missing, do not invent structure. Broaden inspection one level and report unresolved facts. If evidence conflicts, record both sources, prefer the runtime/current configuration where possible, and flag the conflict for planning/debugging. If access is incomplete, state what could not be verified and avoid conclusions that depend on it.

## Output contract

Return a compact repository profile with:

- verified stack;
- relevant architecture/data flow;
- conventions;
- target/change surface;
- risk boundaries;
- unresolved material questions;
- exact file/symbol evidence where available.
