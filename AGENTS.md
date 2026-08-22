# AI Expert Engine — Global Agent Rules

This repository defines a token-efficient, production-grade expert system for Cursor and Codex.

## Operating hierarchy
1. `master-agent` owns routing and orchestration.
2. `repository-intelligence` establishes verified repository facts.
3. `task-planning` decomposes non-trivial work.
4. `debugging` owns evidence-driven diagnosis.
5. Domain skills own implementation expertise.
6. `multi-review` owns independent multi-lens review; `audit-review` owns systemic audits.
7. `release-readiness` owns the final GO / GO WITH CONDITIONS / HOLD / NO-GO decision.

## Non-negotiable rules
- Inspect before changing; repository evidence outranks assumptions.
- Load the smallest useful skill/reference/reviewer set.
- Preserve local conventions unless the task requires migration.
- Separate diagnosis from implementation and keep changes scoped.
- Authentication, authorization, payments, secrets, tenant/data access, migrations, production configuration, privileged AI/tool actions and destructive operations are elevated risk.
- Complexity C0–C4 and risk R0–R4 are independent. Small changes can be R3/R4.
- R3/R4 requires relevant independent review; the implementation owner cannot self-approve it.
- Green CI is never sufficient production-release evidence.
- Never weaken tests/security/validation or downgrade findings to make a gate pass.
- Prefer deterministic scripts for mechanical checks; use model reasoning for judgment.

## Runtime evidence discipline
For C2+ work and especially R3/R4, use the local runtime contracts/tools when available rather than leaving important routing/review/release state only in prose.

- Routing envelopes belong in `.ai-expert-engine/state/` and must validate against `engine/schemas/runtime-routing.schema.json` when persisted.
- C3/C4, multi-stage, migration and long-running work should maintain a schema-valid checkpoint with `scripts/session_checkpoint.py`; side discussions must not silently replace goal, risk, acceptance criteria or hard constraints.
- Record routing/review/release telemetry with `scripts/engine_telemetry.py` when shell access and task scope justify it. Token fields are recorded only when the runtime exposes real counts; never fabricate estimates as measured usage.
- Mandatory reviewer findings should be normalized to `engine/schemas/reviewer-finding.schema.json` and persisted with `scripts/review_store.py` when available. Accepted risk needs rationale/owner in the finding context and an expiry.
- Release decisions used for automation must be built from current evidence with `scripts/build_release_decision.py` and enforced by `scripts/release_gate.py` or the reusable AI Expert Release Gate workflow. A prose GO is advisory, not technical enforcement.
- Persisted JSON does not count as evidence merely because it exists; it must be schema-valid, candidate-specific and current.

## Knowledge freshness
Version-sensitive claims must follow repository versions first. `engine/knowledge/sources.json` records freshness windows for external standards/providers. When a critical source is stale or a current behavior materially affects the decision, verify the current official source before relying on memory.

## Completion standard
A task is complete only when the requested outcome is implemented or answered, material risks are addressed, relevant checks pass, mandatory independent review is complete, runtime evidence is current where required, and unresolved limitations are stated plainly. Production work requiring a final gate must report both the release decision and whether it is technically enforced or advisory.
