---
name: multi-review
description: Orchestrates independent specialist reviews for material cross-domain changes, selecting justified isolated reviewer lenses, normalizing and persisting evidence-backed findings, and consolidating risk without implementing fixes or replacing release-readiness.
---

# Purpose
Run independent review passes so correctness, design, security, performance, QA and release risks are evaluated from separate contexts rather than one self-review.

## Use when
- C2–C4 or R2–R4 work crosses quality domains;
- a significant feature/refactor/migration needs independent review;
- the caller requests comprehensive/pre-merge multi-disciplinary review.

## Do not use when
- one narrow specialist review is sufficient;
- systemic audit (`audit-review`) or final release decision (`release-readiness`) is primary;
- implementation/diagnosis is still incomplete.

## Inputs
Establish exact candidate/change surface, intended behavior, risk, acceptance criteria, actual diff/artifact, tests/checks, architecture/contracts, deployment implications and unresolved assumptions.

## Workflow
### 1. Define target and lenses
State exact candidate/scope and select only justified reviewers using `references/reviewer-selection.md`.

### 2. Require reviewer independence
On Cursor, mandatory lenses execute through matching `.cursor/agents/` isolated subagents. If isolation is unavailable, label the pass non-independent; it cannot satisfy R3/R4 independence by itself.

### 3. Preserve independent evidence
Give each reviewer the same verified candidate evidence plus its own lens, without another reviewer's verdict or desired conclusion.

### 4. Normalize findings
Every finding identifies candidate, reviewer, affected surface, severity and confidence, evidence, impact, acceptance condition, owner and blocker. Use `references/finding-severity-confidence.md`.

### 5. Persist mandatory findings
When `scripts/review_store.py` is available, persist mandatory reviewer findings using the reviewer-finding runtime schema. The stored candidate must match the reviewed artifact/commit. Accepted risk is not silence: it must have an explicit disposition and expiry.

### 6. Reconcile without voting
Deduplicate by root cause without erasing distinct interpretations. Conflicts resolve through stronger evidence, not majority vote.

### 7. Route remediation and re-review
Reviewers do not silently implement fixes. Send confirmed defects to owning skills and rerun only affected lenses after remediation.

### 8. Consolidate
Return blockers first, then non-blocking findings, accepted risk candidates, reviewer coverage, isolation evidence, persistence/evidence-store status, gaps and re-review requirements.

## Decision rules
- Separate reviewer context is required for true independence.
- Reviewer count scales with risk/surface; never load all by default.
- Critical/high findings need concrete evidence or a reproducible verification path.
- One blocker from a mandatory reviewer prevents a clean review.
- Severity and confidence are separate.
- Review cannot replace missing tests/runtime evidence.
- Accepted risk requires owner/rationale/expiry or follow-up.
- A non-isolated pass cannot be represented as independent evidence.

## Reference routing
Load `references/reviewer-selection.md` for reviewer selection and mandatory lenses. Load `references/finding-severity-confidence.md` for severity/confidence/blocker normalization. On Cursor invoke matching `.cursor/agents/`; `engine/reviewers/` remains the canonical reviewer contract/profile source.

## Quality gates
- Review candidate/scope is explicit.
- Mandatory R3/R4 reviewers are not skipped.
- Isolation evidence exists or result is marked non-independent.
- Findings are evidence-backed with acceptance conditions.
- Persisted mandatory findings validate and match the candidate when the store is available.
- Duplicate findings retain distinct risks.
- Blocking findings flow explicitly to `release-readiness` until resolved/accepted through policy.

## Failure handling
If the artifact cannot be inspected, mark review limited. If isolated execution is unavailable, do not simulate independence. If persistence fails schema/candidate validation, treat the evidence store as invalid rather than claiming durable review. If a blocker cannot be resolved, pass it unchanged to `release-readiness`.

## Output contract
Return scope/candidate, selected reviewers, isolation mode/evidence, findings with severity/confidence/evidence/owner, blocker list, accepted risks, persistence/evidence-store status, coverage gaps, remediation and re-review state.
