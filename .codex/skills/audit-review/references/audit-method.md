# Audit Method

Audit by risk concentration, not directory order.

1. Define explicit audit questions and production criticality.
2. Map trust/data/money/PII/external-input/destructive/release boundaries.
3. Select representative critical journeys and architecture seams.
4. Inspect source, config, tests, CI, deployment/observability evidence and docs where each question requires them.
5. Trace invariants end to end: where created, validated, authorized, persisted, retried, observed and recovered.
6. Distinguish one-off defects from repeated patterns or policy/architecture breaches.
7. Corroborate severe/systemic claims with multiple pieces of evidence where practical.
8. Prioritize root-cause remediation by impact, blast radius, dependency order and reversibility.

Audit dimensions may include architecture, auth/authz, data integrity/isolation, API contracts, async/idempotency, security/privacy, frontend/UX/accessibility, performance, tests, dependencies/supply chain, deployment/recovery, observability, documentation and business-domain correctness.

Never treat scanner count or lint volume as the audit score.