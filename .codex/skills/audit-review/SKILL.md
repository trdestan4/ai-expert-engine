---
name: audit-review
description: Performs evidence-based repository or system audits across architecture, security, quality, operability and product risks by sampling the real implementation, tracing high-risk paths, and separating systemic findings from local defects; it does not replace targeted debugging or release approval.
---

# Purpose

Assess the health of a repository/system beyond one change by finding systemic weaknesses, cross-cutting inconsistencies and hidden risk concentrations with reproducible evidence and prioritized remediation.

## Use when

- the user requests a broad audit, health check, production-readiness audit or technical due diligence;
- a repository has grown without a trusted quality baseline;
- repeated incidents/defects suggest systemic causes;
- architecture/security/performance/data/quality practices need cross-cutting assessment.

## Do not use when

- one known bug needs root-cause diagnosis (`debugging`);
- one change needs independent reviewers (`multi-review`);
- the final question is whether a specific release can proceed (`release-readiness`);
- a domain-specific audit can be answered safely by one specialist alone.

## Inputs

Identify audit objective, repository/system scope, production criticality, known incidents, stack/runtime versions, high-risk trust/data paths, representative user journeys, CI/CD and deployment evidence, tests, observability, documentation and constraints on depth/time. Existing-repository audits should use `repository-intelligence` for verified facts before broad conclusions.

## Workflow

### 1. Define audit questions
Translate “audit everything” into explicit risk questions: architecture integrity, auth/data isolation, correctness, test evidence, performance, accessibility, privacy, supply chain, deploy/recovery and operational visibility.

### 2. Build a risk map
Prioritize externally exposed surfaces, authorization/data boundaries, money/PII, destructive workflows, high-traffic paths, complex state transitions and release infrastructure.

### 3. Sample evidence deliberately
Use `references/audit-method.md` and `references/evidence-sampling.md`. Inspect representative code/config/tests/CI/runtime artifacts across each selected risk area; do not infer repository-wide quality from one file.

### 4. Trace critical journeys end to end
Follow selected flows across UI/API/auth/data/async/integration/deployment boundaries where applicable. Record where invariants are enforced and where evidence is missing.

### 5. Distinguish local from systemic findings
A local bug affects a bounded path. A systemic finding is repeated, policy-breaking or architectural and likely to create multiple future failures. Do not label isolated style preferences as systemic risk.

### 6. Validate findings
Seek corroborating evidence, tests, runtime behavior or repeated patterns. State unknowns separately from confirmed weaknesses.

### 7. Prioritize remediation
Rank by impact, exploitability/probability, blast radius, frequency, reversibility and dependency order. Fix risk concentration/root causes before cosmetic debt.

### 8. Define a target state
For material systemic findings, specify measurable acceptance criteria, owners/boundaries and a staged remediation path that preserves service continuity.

## Decision rules

- Audit breadth never excuses shallow evidence.
- Sample more deeply where risk is concentrated; do not spend equal effort on low-risk folders.
- Missing evidence is a finding only when the evidence is required for safe operation or verification.
- One weak file does not prove a systemic pattern; repeated pattern or architecture/policy breach does.
- Tool output is evidence, not verdict; interpret scanners/profilers/tests in repository context.
- Do not produce legal/compliance certainty from engineering evidence alone.
- Separate “must fix”, “should fix”, “observe”, and “unknown/needs evidence”.
- Audit findings should be actionable without demanding gratuitous rewrites.

## Reference routing

Load `references/audit-method.md` for audit dimensions, systemic-vs-local reasoning and remediation prioritization.
Load `references/evidence-sampling.md` for representative sampling, critical-journey tracing and confidence limits.
Use `multi-review` when a particular finding/change needs independent specialist validation.

## Quality gates

- Audit scope and risk questions are explicit.
- High-risk surfaces receive deeper evidence than low-risk surfaces.
- Findings cite concrete implementation/config/runtime evidence.
- Systemic claims have repeated or architectural evidence.
- Unknowns and inaccessible evidence are visible.
- Severity/prioritization reflects impact and blast radius, not aesthetics.
- Remediation preserves ownership and dependency order.
- Final result states confidence and coverage limitations.

## Failure handling

If repository/runtime evidence is unavailable, narrow the audit claim and list what remains unverified. If scope is too broad for credible sampling, prioritize risk areas rather than pretending full coverage. If a severe finding is discovered, route it to the owning specialist and `multi-review`/`release-readiness` as appropriate rather than burying it in a long report.

## Output contract

Return audit scope, evidence/coverage map, prioritized systemic and local findings, severity/confidence, critical-journey results, unknowns, remediation roadmap, verification criteria and residual risk.