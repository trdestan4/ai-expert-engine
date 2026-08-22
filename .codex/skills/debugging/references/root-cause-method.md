# Root-Cause Method

Use when the failure has multiple plausible causes or previous assumptions are weak.

## Build a causal chain

Trace:

`input/state → transformation/boundary → first divergence → downstream symptom`

The root cause should explain why the first divergence occurs, not merely where the final error is thrown.

## Rank hypotheses

For each candidate ask:

1. Does it explain every known symptom?
2. What observation would be likely if it were true?
3. What observation would make it unlikely?
4. What is the cheapest safe test that separates it from alternatives?

Prefer hypotheses with both explanatory coverage and discriminating tests.

## Useful evidence classes

- deterministic failing tests/reproductions;
- stack traces and earliest causal error;
- request/response or state transitions;
- configuration/version differences;
- git diff/change timing;
- database/cache/queue state;
- metrics/traces for latency/resource failures;
- browser/network behavior for frontend/session issues.

## Common traps

- fixing the line that throws without finding the invalid state source;
- blaming network/cache/race conditions without timing evidence;
- assuming an installed dependency is the active implementation;
- changing several variables and losing causal attribution;
- treating disappearance of symptoms as proof of correctness.

## Confidence language

Use `confirmed` only when evidence directly demonstrates the causal mechanism or the hypothesis makes a differentiating prediction that is observed. Otherwise use `high`, `medium`, or `low` confidence and name the missing proof.
