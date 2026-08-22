---
name: multi-review
description: Orchestrates independent specialist reviews for material cross-domain changes, selects only justified reviewer lenses, reconciles findings by evidence and severity, and returns a consolidated defect/risk view; it does not implement fixes or replace release-readiness.
---

# Purpose

Run independent review passes over material work so correctness, design quality, security, performance, QA and release risks are evaluated from separate lenses instead of being collapsed into one self-review.

## Use when

- a C2–C4 or R2–R4 change crosses multiple quality domains;
- a significant feature/refactor/migration needs independent review before completion;
- implementation quality may look acceptable from one domain but fail another;
- the caller asks for a comprehensive review, pre-merge review or multi-disciplinary critique.

## Do not use when

- a single narrow specialist review is sufficient;
- broad repository/system auditing is primary (`audit-review`);
- the decision is specifically whether a release may proceed (`release-readiness`);
- implementation or diagnosis is still incomplete and review evidence would be premature.

## Inputs

Establish the changed surface, user-visible behavior, risk level, acceptance criteria, implementation evidence, tests/checks already run, relevant architecture/contracts, deployment implications and unresolved assumptions. Review the actual diff/artifact when available rather than only a summary.

## Workflow

### 1. Define the review target
State the exact change, boundaries, intended behavior and known risks. Separate review scope from unrelated repository debt.

### 2. Select reviewer lenses
Use `references/reviewer-selection.md`. Activate only reviewers whose lens can materially change the decision. Typical profiles live under `engine/reviewers/`.

### 3. Preserve reviewer independence
Give each reviewer the same verified change evidence plus its own lens. Do not pre-seed reviewers with a desired conclusion or another reviewer's verdict.

### 4. Require evidence-backed findings
Every finding must identify affected behavior/path, severity, evidence, why it matters and a concrete acceptance condition. Speculation without a verification path is not a blocker.

### 5. Deduplicate without erasing disagreement
Merge duplicate findings by root cause. Keep materially different interpretations separate until evidence resolves them.

### 6. Reconcile severity and confidence
Use `references/finding-severity-confidence.md`. Severity reflects impact/exploitability/blast radius; confidence reflects evidence strength. Do not inflate severity to compensate for weak evidence.

### 7. Route fixes to owners
Reviewers do not silently implement unrelated fixes. Route each confirmed defect to the domain owner and re-run only affected review lenses after remediation.

### 8. Produce a consolidated result
Return blocking findings first, then non-blocking findings, accepted risks, reviewer coverage, evidence gaps and re-review requirements.

## Decision rules

- Independent review means independent reasoning, not merely different headings in one pass.
- Reviewer count scales with risk and changed boundaries; never load all reviewers by default.
- A critical/high finding needs concrete evidence or a clearly reproducible verification path.
- One blocker from a mandatory reviewer is enough to prevent a clean review result.
- Conflicting reviewer conclusions are resolved by stronger evidence, not majority vote.
- Review cannot replace missing tests, runtime evidence or domain verification.
- Existing unrelated debt is reported separately unless the change materially worsens it.
- Accepted risk must name owner/rationale/expiry or follow-up; silence is not acceptance.

## Reference routing

Load `references/reviewer-selection.md` to choose reviewer profiles and mandatory lenses.
Load `references/finding-severity-confidence.md` to normalize findings, severity, confidence and blocker semantics.
Use reviewer profiles under `../../../engine/reviewers/` only for selected lenses.

## Quality gates

- Review target and changed boundary are explicit.
- Reviewer selection is justified by actual risk/surface.
- Mandatory reviewers for R3/R4 boundaries are not skipped.
- Findings contain evidence and acceptance conditions.
- Severity and confidence are separated.
- Duplicate findings are consolidated without losing distinct risks.
- Blocking findings are unresolved only when explicitly carried as risk to `release-readiness`.
- Re-review scope after fixes is proportional and explicit.

## Failure handling

If the artifact/diff cannot be inspected, label the review as limited and do not claim a clean result. If reviewers conflict, gather the smallest discriminating evidence or route to the owning specialist. If a blocker cannot be resolved before release consideration, pass it explicitly to `release-readiness` rather than downgrading it for convenience.

## Output contract

Return review scope, selected reviewers, per-finding severity/confidence/evidence/owner, blocker list, accepted-risk candidates, coverage gaps, required remediation and re-review status.