# Quality Engineering Policy

- Quality gates are risk-based; do not load every reviewer for every task.
- Correctness, security, accessibility and privacy constraints outrank stylistic optimization.
- R3/R4 changes involving auth/authz, money, tenant isolation, privileged actions, uploads, webhooks, secrets or sensitive data require security-focused review.
- New personal-data collection, purpose, processor, sharing or retention requires privacy review.
- Critical user interactions and authentication/form flows require accessibility verification.
- Behavior-changing production code requires test evidence proportional to risk.
- Performance claims require before/after evidence; optimize measured bottlenecks.
- Current Core Web Vitals targets: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 at p75; verify when standards change.
- WCAG 2.2 is the preferred current accessibility baseline unless product/jurisdiction requires otherwise.
- OWASP ASVS 5.0.0 is a current application-security verification baseline; tailor controls to actual risk.
- Automated scanners, coverage percentages, Lighthouse scores and accessibility scores are evidence, not proof of quality.
- Critical/high exploitable security findings and inaccessible core journeys can block release.
- Refactors must preserve behavior with evidence proportional to risk.
- Jurisdiction-specific legal/compliance claims require current authoritative verification; technical review is not legal certification.
- Residual risks and explicit risk acceptance must have an accountable owner.