# Threat Modeling and ASVS Verification

## Risk model

Model assets, actors, entry points, trust boundaries, data stores, privileged operations and external systems before choosing controls. Capture attacker goals such as account takeover, tenant breakout, unauthorized mutation, sensitive-data extraction, payment abuse, code execution and service exhaustion.

Use lightweight STRIDE-style prompts when useful, but prioritize concrete abuse stories over taxonomy completeness. A threat model is successful when it changes design/test decisions.

## ASVS baseline

OWASP ASVS 5.0.0 was released in May 2025 and is the current major verification baseline as of this reference. Use it as a structured source of application-security requirements, not as a claim that every project needs every item.

Map applicable controls to evidence: code path, configuration, test, deployment setting or operational procedure. Mark non-applicable requirements with rationale.

## Risk depth

Increase review depth for authentication, authorization, admin tools, money movement, cross-tenant access, sensitive data, file parsing/upload, outbound fetches, webhooks and deployment/security configuration.

## Acceptance

A high-risk feature should have identified abuse cases, prevention/detection controls, negative tests and residual-risk ownership. If the framework/provider behavior is version-sensitive, verify current official guidance before asserting the control is effective.