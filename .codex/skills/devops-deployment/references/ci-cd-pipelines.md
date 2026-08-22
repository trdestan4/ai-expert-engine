# CI/CD Pipelines

## Pipeline goals

CI should produce reproducible evidence for the candidate; CD should promote the reviewed artifact safely. Separate build/test/review/artifact creation from environment promotion where practical.

## Candidate and artifact identity

Build once/promote same immutable artifact when possible. Record commit, dependency lock state, build configuration and artifact digest/version. Rebuilding separately for production can create an unreviewed artifact.

## Trust and permissions

Use least-privilege workflow tokens and environment-scoped secrets. Do not expose write secrets to untrusted fork code. Pin third-party actions/tools according to governance and verify downloaded binaries/checksums when risk warrants it.

## Gates

Run deterministic format/type/lint/test/schema/security/dependency checks appropriate to repo. High-risk release additionally needs independent review and candidate/environment-bound release gate; green CI alone does not authorize production.

## Concurrency

Prevent overlapping deploys/migrations when unsafe using environment concurrency/locks. Cancel stale preview work where appropriate but do not cancel a production migration halfway unless recovery is designed.

## Caching

Cache dependencies/build artifacts with keys that preserve correctness. Never cache secrets. Treat cache poisoning/untrusted branch restoration as a supply-chain consideration.

## Failure handling

CI failures should be reproducible and logs/artifacts retained enough to diagnose. Avoid rerun-until-green for flaky tests. Deployment failure requires known rollback/roll-forward and state reconciliation rather than “rerun deploy” by habit.
