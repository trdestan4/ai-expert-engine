# Skill Contract

Every discoverable skill must be operational, bounded, and progressively loaded.

## Required frontmatter

```yaml
---
name: lowercase-kebab-case
description: One precise sentence stating ownership, triggers, and important exclusions.
---
```

Use only portable frontmatter unless a platform-specific behavior is required and documented.

## Required SKILL.md sections

1. `# Purpose` — the outcome this skill owns.
2. `## Use when` — positive routing signals.
3. `## Do not use when` — explicit exclusions and adjacent owners.
4. `## Inputs` — evidence/context required before acting.
5. `## Workflow` — ordered decision/execution procedure.
6. `## Decision rules` — compact if/then rules for ambiguous cases.
7. `## Reference routing` — which deep references to load and only when.
8. `## Quality gates` — objective conditions for accepting the work.
9. `## Failure handling` — what to do when evidence/checks fail.
10. `## Output contract` — what the caller receives.

## Design constraints

- `SKILL.md` is an operating manual, not a textbook.
- Put deep domain knowledge in `references/` and deterministic work in `scripts/`.
- Prefer one-hop references from `SKILL.md`; avoid long chains of nested references.
- Do not duplicate shared rules already defined in `AGENTS.md`.
- Do not repeat knowledge that belongs to an adjacent specialist.
- Examples must teach a decision boundary, not pad the file.
- Every important rule should be testable by an eval or validator where practical.

## Routing quality

A description is valid only if it answers all three:

- What does this skill own?
- When should it activate?
- What nearby task should route elsewhere?

Descriptions that rely on vague terms such as “helps with development” or “expert in software” fail the contract.

## Token discipline

Target ranges, not hard limits:

- description: 20–60 tokens
- normal `SKILL.md`: 700–1,500 tokens
- orchestrator: up to ~2,000 tokens when justified
- individual reference: 300–1,500 tokens
- ordinary task: 1–3 active skills
- complex feature: 3–5 active skills

Exceed these only when the additional context changes decisions or prevents meaningful failure.

## Acceptance

A skill is not complete until:

- frontmatter validates;
- required sections exist;
- all local references resolve;
- overlap with adjacent skills is intentional and documented;
- at least positive, negative, and edge-case evals exist;
- token size is within the declared budget or explicitly justified.
