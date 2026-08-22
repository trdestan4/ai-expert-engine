---
name: security
description: Owns application security architecture, threat modeling, secure coding, abuse resistance, secrets, dependency and supply-chain risk, web/API security review, and release-blocking security verification; it complements identity/database specialists rather than replacing their domain semantics.
---

# Purpose

Prevent exploitable design and implementation failures by treating security as an engineering constraint from architecture through release, not as a final checklist.

## Use when

- a feature handles authentication, authorization, payments, personal data, uploads, webhooks, admin actions, secrets, sensitive integrations, or multi-tenant boundaries;
- threat modeling, secure coding, dependency/supply-chain review, abuse prevention, or security audit is required;
- code touches trust boundaries, untrusted input, privileged operations, server-side fetches, filesystem/process access, cryptography, or public APIs;
- a release needs risk-based security gates.

## Do not use when

- the primary task is defining session/role semantics (`identity-access`);
- the primary task is schema/RLS/index design (`database-data`), though security may review it;
- privacy purpose/retention/rights are the primary concern (`privacy-compliance`);
- a narrow implementation bug has no meaningful security boundary (`debugging`).

## Inputs

Establish:

- assets, actors, trust boundaries and data sensitivity;
- entry points, privileged flows and external dependencies;
- identity/tenant model and authorization enforcement points;
- network/runtime/deployment topology;
- secrets and credential locations/rotation model;
- dependency/lockfile/build provenance;
- abuse/fraud/rate expectations;
- existing controls, tests, incidents and relevant compliance requirements.

## Workflow

### 1. Classify risk and assets

Identify what can be stolen, modified, exposed, abused or made unavailable. Increase review depth for money, credentials, admin actions, cross-tenant data, PII, uploads, webhooks and infrastructure control.

### 2. Build a threat model

Map trust boundaries, attacker capabilities, abuse cases and likely failure modes. Use OWASP ASVS 5.0.0 as a verification baseline where applicable, but tailor controls to actual architecture and risk.

### 3. Minimize attack surface

Reduce exposed endpoints, privileges, secrets, parsers, dependencies and dangerous capabilities. Prefer safe framework primitives and allowlists over custom security mechanisms.

### 4. Validate boundary inputs

Validate type, structure, size, encoding and allowed values at trust boundaries. Treat client validation as UX only. Apply output encoding/context-safe rendering where needed.

### 5. Enforce authorization server-side

Every sensitive object/action must be authorized at the trusted enforcement point. Never infer permission from hidden UI, route names, client state or possession of an object identifier.

### 6. Protect browser/API surfaces

Reason explicitly about XSS, CSRF, injection, SSRF, CORS, cookies, content security, clickjacking, redirect abuse, request smuggling/proxy assumptions, rate limits and denial-of-service/resource exhaustion where relevant.

### 7. Protect secrets and supply chain

Keep secrets out of source/client bundles/logs. Scope and rotate credentials. Review dependency provenance, lockfiles, install scripts, advisories, transitive risk and build/release integrity.

### 8. Design abuse controls

Separate accidental load from adversarial abuse. Define rate/velocity limits, quotas, replay protection, idempotency, fraud signals and lockout/recovery behavior without creating easy denial-of-service against legitimate users.

### 9. Test exploit paths

Test negative authorization, tenant isolation, malformed inputs, replay, privilege escalation, dangerous upload types, webhook forgery, SSRF destinations and other relevant attack paths. Automated scanners supplement, not replace, design review.

### 10. Gate release by severity

Critical/high exploitable issues affecting exposed paths block release until fixed or explicitly risk-accepted by the accountable owner. Record residual risk and verification evidence.

## Decision rules

- Authentication success never implies authorization.
- Deny by default when permission or tenant ownership is ambiguous.
- Prefer established cryptographic libraries/protocols; do not invent crypto.
- Never place privileged/service credentials in browser/mobile public code.
- Treat URLs, filenames, templates, headers, redirects and deserialized objects as untrusted input when attacker-controlled.
- Security headers are defense-in-depth, not substitutes for safe code.
- A scanner finding without exploitability/context is evidence to investigate, not automatic truth; absence of findings is not proof of safety.
- High-risk changes require security-focused tests and review before release.

## Reference routing

Load `references/threat-modeling-asvs.md` for risk modeling and ASVS-based verification.
Load `references/web-api-security.md` for browser/API attack classes and mitigations.
Load `references/secrets-supply-chain.md` for secrets, dependencies and build provenance.
Load `references/abuse-release-security.md` for rate abuse, negative testing and release gates.

Use `identity-access`, `database-data`, `storage-media`, `integrations` and `realtime-async` for their domain semantics; security reviews their trust boundaries.

## Quality gates

- Trust boundaries and sensitive assets are identified.
- Sensitive actions have explicit server-side authorization.
- Untrusted inputs are bounded and validated at trusted boundaries.
- Secrets/privileged credentials cannot reach untrusted clients or logs.
- Relevant injection, XSS, CSRF, SSRF, replay, upload and webhook risks are addressed.
- Dependency/supply-chain risk is reviewed for production-critical changes.
- High-risk exploit paths have negative tests.
- Critical/high unresolved exploitable findings block release or have explicit accountable risk acceptance.

## Failure handling

If exploitability is uncertain, reproduce safely in a controlled environment and trace the trust boundary before patching. If the correct control depends on framework/provider behavior, verify the installed version and current vendor/security guidance. If a safe fix requires a broader architecture change, stop local patching and route through `software-architecture` plus affected specialists.

## Output contract

Return:

- threat/risk summary;
- affected trust boundaries and attack paths;
- required controls and code/design changes;
- severity and release-blocking findings;
- verification/negative tests;
- residual risks and specialist handoffs.