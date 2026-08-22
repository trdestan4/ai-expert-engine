---
name: multi-review
description: Orchestrates independent specialist reviews for material cross-domain changes, selecting justified isolated reviewer lenses, loading each reviewer's expert-domain skill context, normalizing and persisting evidence-backed findings, and consolidating risk without implementing fixes or replacing release-readiness.
---

# Purpose
Run independent master-level review passes so correctness, design, security, performance, QA and release risks are evaluated from separate expert contexts rather than one self-review or a shallow checklist.

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

### 3. Load reviewer expertise, not only reviewer prompts
Each isolated reviewer must read its canonical reviewer contract/profile plus its owning expert `SKILL.md` and only the deep references relevant to the changed boundary. Supporting domain skills may be loaded when the evidence crosses those boundaries. A one-screen reviewer lens without domain skill context is advisory, not master-level R3/R4 evidence.

### 4. Preserve independent evidence
Give each reviewer the same verified candidate evidence plus its own lens. Do not provide another reviewer's verdict, a desired conclusion or severity hint before the pass.

### 5. Normalize findings
Every finding identifies candidate, reviewer, affected surface, severity and confidence, evidence, impact, acceptance condition, owner and blocker. Use `references/finding-severity-confidence.md`.

### 6. Persist mandatory findings
When `scripts/review_store.py` is available, persist mandatory reviewer findings using the reviewer-finding runtime schema. The stored candidate must match the reviewed artifact/commit. Accepted blocker risk requires explicit disposition and a future expiry; expired acceptance becomes an effective blocker again.

### 7. Reconcile without voting
Deduplicate by root cause without erasing distinct interpretations. Conflicts resolve through stronger evidence or additional targeted verification, never majority vote.

### 8. Route remediation and re-review
Reviewers do not silently implement fixes. Send confirmed defects to owning skills and rerun only affected lenses after remediation. Candidate changes invalidate affected review evidence.

### 9. Consolidate
Return blockers first, then non-blocking findings, accepted risk candidates, reviewer coverage, domain-context evidence, isolation evidence, persistence/evidence-store status, gaps and re-review requirements.

## Decision rules
- Separate reviewer context is required for true independence.
- Domain skill/reference loading is required for master-level mandatory review.
- Reviewer count scales with risk/surface; never load all by default.
- Critical/high findings need concrete evidence or a reproducible verification path.
- One blocker from a mandatory reviewer prevents a clean review.
- Severity and confidence are separate.
- Review cannot replace missing tests/runtime evidence.
- Accepted risk requires owner/rationale/future expiry.
- A non-isolated or domain-unloaded pass cannot be represented as full R3/R4 independent expert evidence.

## Reference routing
Load `references/reviewer-selection.md` for reviewer selection, mandatory lenses and domain-skill mapping. Load `references/finding-severity-confidence.md` for severity/confidence/blocker normalization. On Cursor invoke matching `.cursor/agents/`; `engine/reviewers/` remains the canonical reviewer contract/profile source.

## Quality gates
- Review candidate/scope is explicit.
- Mandatory R3/R4 reviewers are not skipped.
- Isolation evidence exists or result is marked non-independent.
- Reviewer domain skill/references were loaded proportionally.
- Findings are evidence-backed with acceptance conditions.
- Persisted mandatory findings validate and match the candidate when the store is available.
- Duplicate findings retain distinct risks.
- Blocking findings flow explicitly to `release-readiness` until resolved or accepted under policy.

## Failure handling
If the artifact cannot be inspected, mark review limited. If isolated execution is unavailable, do not simulate independence. If expert-domain context cannot be loaded, mark the pass shallow/advisory for high-risk evidence. If persistence fails schema/candidate validation, treat the evidence store as invalid rather than claiming durable review. If a blocker cannot be resolved, pass it unchanged to `release-readiness`.

## Output contract
Return scope/candidate, selected reviewers, isolation mode/evidence, domain skill/reference context loaded per reviewer, findings with severity/confidence/evidence/owner, blocker list, accepted risks, persistence/evidence-store status, coverage gaps, remediation and re-review state.
