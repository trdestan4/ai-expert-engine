---
name: git-delivery
description: Owns source-control delivery across Git/GitHub branching, commits, pull requests, reviews, protected-branch policy, release/versioning, changelogs and repository collaboration conventions; it does not own deployment infrastructure, runtime observability, or application architecture.
---

# Purpose

Make code changes reviewable, attributable, reversible and easy to integrate by defining disciplined version-control and release collaboration rather than treating Git as a storage mechanism.

## Use when

- branching, commit structure, PR workflow, review policy, CODEOWNERS or protected branches are involved;
- release tags, semantic versioning, changelogs or release notes need design;
- repository contribution/conventional-commit policy or merge strategy needs review;
- GitHub Actions security intersects source-control governance.

## Do not use when

- CI/CD deployment execution is primary (`devops-deployment`);
- production monitoring/incidents are primary (`observability-sre`);
- code maintainability review itself is primary (`code-quality`);
- product documentation is primary (`documentation`).

## Inputs

Inspect repository topology, default branch, team size, release cadence, required checks, branch protections, CODEOWNERS, commit history conventions, package/version strategy, deployment coupling and compliance/audit needs.

## Workflow

### 1. Define integration model
Choose trunk-based, short-lived feature branches or another model based on team/release constraints. Prefer small mergeable changes and avoid long-lived divergence without a real reason.

### 2. Structure commits for review
Keep commits coherent, explain intent, avoid mixing unrelated changes and preserve useful history. Conventional Commits may be used when automation benefits justify the convention.

### 3. Design pull-request gates
Require relevant tests, reviews, security/quality checks and change explanation proportional to risk. PR templates should capture risk/verification/rollback information without becoming bureaucracy.

### 4. Protect critical refs
Use protected branches/rulesets, scoped merge permissions and required checks for production-critical repositories. CODEOWNERS should map real ownership, not merely generate approvals.

### 5. Choose merge strategy deliberately
Squash for noisy feature-branch history, merge commits when preserving branch context matters, rebase for linear history where the team can support it. Do not change repository-wide strategy casually.

### 6. Manage releases explicitly
Define tags/versioning, release notes, migration/breaking-change communication and mapping from source commit to deployed artifact.

## Decision rules

- Never rewrite shared protected history casually.
- Do not commit secrets, generated credentials or environment-specific sensitive files.
- A PR should be small enough to review meaningfully when practical.
- Required checks must reflect real risk, not ceremonial green boxes.
- Third-party GitHub Actions should use immutable full commit SHA pins when supply-chain protection is important.
- Release tags and artifacts should map to an identifiable source commit.
- Breaking changes require explicit migration/deprecation communication.

## Reference routing

Load `references/branching-commits-prs.md` for branch models, commit hygiene, PR structure and review policy.
Load `references/release-versioning-changelog.md` for tags, semantic versioning, release notes and breaking changes.
Load `references/github-governance-actions-security.md` for protected branches, CODEOWNERS, rulesets, permissions and workflow supply-chain controls.

## Quality gates

- Default/integration branch policy is explicit.
- Commits/PRs isolate unrelated work.
- Required review/checks match change risk.
- Protected refs cannot be bypassed accidentally for critical workflows.
- Release/tag strategy is traceable to source.
- Breaking changes and migrations are documented.
- Workflow permissions/actions are reviewed for least privilege and immutable pinning where justified.

## Failure handling

If repository history/conventions are unclear, inspect recent merged work before imposing a new model. If a branch is diverged, preserve recoverability before rebasing/resetting. If a release cannot be traced to source/artifact, stop and reconstruct provenance before making further production claims.

## Output contract

Return branch/integration model, commit/PR conventions, review/protection gates, merge strategy, release/version/changelog model, workflow-governance risks and migration recommendations.