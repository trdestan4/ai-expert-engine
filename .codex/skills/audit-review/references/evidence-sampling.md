# Audit Evidence Sampling

Sampling is necessary in large repositories, but conclusions must reflect what was actually inspected.

## Risk-weighted sample

Prioritize:
- authentication/authorization/tenant/admin boundaries;
- money, destructive writes and migrations;
- untrusted files/URLs/parsers and AI/tools;
- externally exposed APIs/webhooks;
- critical user journeys;
- production deploy/config/secrets;
- high-change/high-incident modules;
- shared libraries/components whose defect propagates widely.

Then inspect representative ordinary modules to see whether the high-risk pattern is exceptional or systemic.

## Sample diversity

Include different services/packages, owners/ages, framework layers and state types where relevant. In design audits include hero plus forms/tables/states/mobile; in API audits include read/write/error/auth; in data audits include schema/migration/query/access; in CI audits include PR and production paths.

## Expand/stop rules

Expand when:
- a severe defect suggests siblings likely share the pattern;
- docs/policy conflict with code;
- samples across modules disagree;
- repository profiling is truncated or architecture is unclear.

Stop when:
- all critical boundaries are covered;
- additional samples repeat the same evidence and do not change prevalence/severity;
- remaining scope is explicitly lower risk;
- access/time/tool limits are reached and recorded.

## Confidence language

Do not say “the repository is secure” from five files. Say, for example, “verified tenant authorization on 4/4 sampled high-risk write paths; background export path was not accessible, so overall tenant isolation remains partially verified.”

## Negative evidence

Absence of a finding is meaningful only when the sample would likely expose it. A grep that finds no secret strings does not prove secrets are safe; no failing accessibility scanner does not prove keyboard usability.

## Reproducibility

Record paths/commits/commands/tests/screenshots or queries enough for another reviewer to reproduce material conclusions without rerunning the entire audit from memory.
