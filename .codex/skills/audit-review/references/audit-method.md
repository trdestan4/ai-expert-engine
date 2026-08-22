# Systemic Audit Method

A repository audit looks for systemic failure patterns and missing controls, not just line-by-line defects.

## 1. Define audit question and boundaries

State what “healthy” means for this audit: architecture, security, quality, release system, design system, performance, migration readiness or full engineering posture. Identify in-scope repositories/services/environments and evidence limits.

## 2. Build evidence map

Use repository intelligence to identify entry points, trust boundaries, data stores, deployment workflows, high-change modules, critical journeys, tests, configuration and ownership. Mark verified vs inferred vs unknown.

## 3. Risk-led sampling

Do not read files uniformly. Sample high-impact flows end-to-end (e.g. login→authorization→data, checkout→webhook→order, upload→processing→serve, deploy→migration→recovery) plus representative ordinary modules to detect convention drift.

## 4. Cross-check declared vs actual controls

Compare README/policies/architecture claims to code/config/workflows/tests. “RLS enabled”, “release gated”, “accessible”, “monorepo modular” or “all APIs validated” are hypotheses until representative evidence supports them.

## 5. Look for systemic patterns

Cluster findings by root cause: missing ownership, repeated authorization bypass pattern, inconsistent validation, duplicated domain policy, weak test boundary, environment drift, stale dependency/runtime convention, generic design/template reuse, observability blind spot.

Distinguish one isolated defect from a pattern likely to recur.

## 6. Verify severity and prevalence

For each pattern state evidence, sample size, affected surface, plausible prevalence and confidence. Expand sampling when a first finding suggests systemic exposure; stop when additional samples no longer change the conclusion or scope is exhausted.

## 7. Prioritize remediation

Order by risk reduction and leverage: fix dangerous trust/data/release controls first; then shared abstractions/policies/tooling that prevent recurrence; then local polish. Avoid proposing a full rewrite merely because architecture is imperfect.

## Audit output

Return scope/evidence limitations, systemic strengths, findings grouped by root cause, severity/confidence, prevalence evidence, immediate blockers, strategic remediation sequence and verification plan.
