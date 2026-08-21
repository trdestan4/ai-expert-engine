---
name: debugging
description: Diagnoses incorrect, failing, intermittent, degraded, or unexplained software behavior through evidence, hypothesis testing, and root-cause isolation before a fix is planned or implemented; it does not own routine feature implementation.
---

# Purpose

Find the most likely root cause with the least destructive experimentation, preserve useful evidence, and hand off a proven diagnosis plus verification strategy.

## Use when

- runtime behavior is wrong or inconsistent;
- tests/build/type checks fail unexpectedly;
- a regression appeared after a change;
- performance degrades and the bottleneck is not established;
- authentication, API, database, network, deployment, dependency, or environment behavior is unexplained;
- previous fixes treated symptoms but the problem persists.

## Do not use when

- no failure/incorrect behavior exists and the task is ordinary implementation;
- the cause is already proven and only implementation remains;
- the task is broad repository architecture discovery (`repository-intelligence` owns that);
- the task is a design/architecture choice unrelated to a failure (`task-planning`/future architecture skill owns it).

## Inputs

Gather the smallest useful evidence set:

- expected vs actual behavior;
- reproduction steps or failing check;
- error/stack/log lines nearest to failure;
- recent relevant changes when known;
- runtime/environment and relevant versions;
- target files/symbols/configuration;
- whether failure is deterministic or intermittent.

## Workflow

### 1. Define the failure precisely

Write a falsifiable statement: under condition X, expected Y, observed Z. Separate user-visible symptom from underlying mechanism.

### 2. Reproduce or establish evidence

Prefer the cheapest deterministic reproduction. If direct reproduction is unavailable, identify the strongest observable evidence and its limitations. Do not claim a bug is fixed if it was never reproduced or otherwise verified.

### 3. Localize the failing boundary

Trace the shortest relevant flow and identify where expected state first diverges from actual state. Boundaries may include:

- browser → frontend;
- component → state/data client;
- frontend → API;
- API → auth/authorization;
- service → database/cache/queue;
- build → runtime/deployment environment.

### 4. Generate ranked hypotheses

Create a small set of plausible causes ranked by evidence and explanatory power. A good hypothesis explains all known symptoms and predicts a differentiating observation.

Avoid shotgun lists.

### 5. Test the cheapest differentiator

For the highest-value hypothesis, choose the smallest reversible experiment or inspection that can prove/disprove it. Prefer logging/inspection/targeted test/config comparison over broad edits.

### 6. Update beliefs

After each result:

- confirmed → isolate exact mechanism;
- disproven → remove hypothesis;
- ambiguous → improve the experiment rather than editing randomly.

Preserve decisive evidence; discard irrelevant noise.

### 7. Identify root cause and contributing factors

Distinguish:

- **root cause** — change/failure mechanism necessary to explain the defect;
- **trigger** — event that exposed it;
- **contributing factor** — made failure easier/harder to detect or recover from;
- **symptom** — observable effect.

### 8. Define the smallest correct fix boundary

Do not implement unrelated cleanup. State what must change, what must remain unchanged, and which regression check proves the failure stays fixed.

### 9. Verify after fix

The implementation owner must prove:

1. original reproduction now passes;
2. nearby expected behavior still passes;
3. relevant broader checks pass;
4. no security/data contract was weakened to hide the failure.

## Decision rules

- Evidence outranks intuition and framework folklore.
- The first error may be downstream; find the earliest meaningful divergence.
- Correlation with a recent change is a lead, not proof.
- If a temporary bypass makes the symptom disappear, that does not prove the bypassed component is the root cause.
- Do not change multiple independent variables in one diagnostic experiment unless unavoidable.
- For intermittent failures, investigate timing, concurrency, caching, retries, environment, and shared state before declaring “cannot reproduce.”
- For performance problems, measure before optimizing and identify the constrained resource/path first.
- A failed fix is new evidence; reassess the hypothesis instead of stacking more patches.

## Reference routing

Load `references/root-cause-method.md` for ambiguous/multi-hypothesis failures.

Load `references/failure-recovery.md` when a previous attempted fix failed, evidence is incomplete, or production behavior cannot be reproduced locally.

Use `repository-intelligence` only for targeted repository facts needed by diagnosis.

## Quality gates

- Expected/actual behavior is explicit.
- Diagnosis is backed by reproducible or clearly qualified evidence.
- Root cause is distinguished from symptom/trigger.
- Hypotheses were discriminated, not merely listed.
- Proposed fix boundary addresses the causal mechanism.
- Regression verification covers the original failure.
- No check/security control is weakened to obtain a pass.

## Failure handling

If reproduction is impossible, switch to evidence triangulation: logs, traces, state snapshots, version/config diffs, and production-vs-local differences. If access/evidence is insufficient for a causal claim, return the strongest bounded hypothesis and the next discriminating check instead of pretending certainty. If the failure crosses a specialist domain, keep diagnosis ownership but request domain evidence/review.

## Output contract

Return:

- precise failure statement;
- decisive evidence;
- root cause or bounded hypothesis with confidence;
- causal explanation;
- smallest fix boundary;
- regression/verification plan;
- unresolved evidence gaps if any.
