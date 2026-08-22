---
name: documentation
description: Owns durable engineering documentation across README/onboarding, architecture and ADRs, API/developer guidance, operations/runbooks, deployment/release notes and maintenance documentation; it does not replace executable tests, source comments for local intent, or product marketing content.
---

# Purpose

Keep the system understandable and operable by someone other than the original author, with documentation that reflects current architecture, setup, decisions, operational procedures and change history.

## Use when

- README, onboarding/setup, architecture docs or ADRs are required;
- API/developer usage, operational runbooks, deployment or release documentation needs creation/update;
- a change alters setup, configuration, architecture, operations or public behavior and docs must remain synchronized;
- ownership/maintenance knowledge is at risk of living only in chat or one engineer's memory.

## Do not use when

- marketing/landing-page copy is primary (`content-conversion`);
- code-level naming/refactoring is primary (`code-quality`);
- CI/CD execution itself is primary (`devops-deployment`);
- incident response execution is primary (`observability-sre`).

## Inputs

Inspect current README/docs, architecture, build/run/test commands, environment setup, API contracts, deployment flow, operational dependencies, ownership, support/debug paths, recent changes and intended audience.

## Workflow

### 1. Identify audience and task
Separate newcomer setup, contributor development, architecture reasoning, operator response and API consumer needs. Avoid one giant README trying to serve every purpose.

### 2. Document executable setup
Provide prerequisites, supported versions, install/bootstrap, required configuration names, run/test/build commands and common verification steps. Never place real secrets in examples.

### 3. Capture architecture and decisions
Document boundaries, major data/control flows, external dependencies and important tradeoffs. Use ADRs for consequential decisions that future maintainers may otherwise reverse accidentally.

### 4. Keep interfaces synchronized
Public/internal API docs, schemas and examples must reflect actual behavior/version. Prefer generated/source-linked documentation when it reduces drift without hiding important semantics.

### 5. Document operations
Runbooks should include symptoms, first checks, dashboards/log queries, safe mitigations, rollback/restore paths, escalation and post-action verification.

### 6. Document change and migration
Breaking changes, migrations, deprecated behavior, release notes and operator/user actions must be explicit when a release changes expectations.

### 7. Verify documentation
Test commands and links where practical. Remove stale instructions rather than appending contradictory new ones.

## Decision rules

- Documentation is part of the change when setup, behavior, architecture or operations change.
- Prefer concise task-oriented docs over exhaustive prose nobody can maintain.
- Examples use placeholders and non-secret values.
- ADRs record context, decision, alternatives/tradeoffs and consequences; they are not meeting transcripts.
- Runbooks contain concrete actions and verification, not vague advice.
- Generated docs must still preserve human-readable semantics and version ownership.
- Stale documentation is a defect because it creates false operational confidence.

## Reference routing

Load `references/readme-onboarding.md` for repository setup, contributor flow and developer experience.
Load `references/architecture-adrs-api.md` for architecture docs, ADRs, diagrams and API/developer documentation.
Load `references/runbooks-operations-release.md` for operational runbooks, deployment/release/migration documentation and maintenance ownership.

## Quality gates

- Setup commands and prerequisites are current/testable.
- Secret values are never documented as real credentials.
- Architecture boundaries and external dependencies are discoverable.
- Consequential decisions have durable rationale where needed.
- API/interface examples match current behavior.
- Operational procedures include verification and recovery.
- Breaking/migration actions are explicit.
- New docs replace or reconcile stale conflicting instructions.

## Failure handling

If documentation and code disagree, treat code/runtime as evidence but do not silently rewrite intent without checking architecture/history. If a command cannot be verified, label the uncertainty and inspect the repository/tooling before publishing it as canonical.

## Output contract

Return target audience, documents to create/update, exact setup/architecture/operations/release content, stale-doc removals, verification performed and remaining ownership gaps.