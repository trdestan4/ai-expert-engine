# Threat Modeling and ASVS Verification

Security review starts from the system, attacker and trust boundaries—not a vulnerability-name checklist.

## Build the model

Identify assets, actors, entry points, trust boundaries, privileged operations, data stores, external providers, background workers, browser/client boundaries and deployment/admin planes. For each important flow record what is trusted, what is merely authenticated, where authorization occurs and what durable side effect can happen.

Use abuse stories such as account takeover, tenant breakout, unauthorized mutation, secret extraction, payment manipulation, stored XSS, arbitrary outbound fetch, unsafe file processing, tool/agent abuse, destructive admin action and service exhaustion. STRIDE-style prompts can help coverage, but taxonomy completion is not the goal.

## Reachability and prerequisites

A finding should answer: attacker capability, reachable path, prerequisites, control bypass, impact, blast radius, detectability and recovery. Distinguish theoretical weakness from exploitable path. A scary primitive behind strong independent authorization may have lower practical risk than a simple IDOR across tenants.

## ASVS baseline

OWASP ASVS 5.0.0 is the current stable major verification baseline as of this reference. Use versioned requirement identifiers when recording durable evidence. Select only applicable requirements by risk/product surface; do not pretend every project requires every ASVS item.

Map each applicable control to evidence: code/config, automated negative test, infrastructure setting, provider behavior verified for installed/current version, or operational procedure. “Framework handles it” is not evidence without confirming the relevant default/configuration.

## Trust-boundary review depth

Escalate for authentication/recovery, authorization/admin, cross-tenant access, money movement, sensitive/regulated data, file/archive/media parsing, URL fetch/import/proxy features, webhooks, AI tools/actions, dependency/build changes, secret rotation and production security controls.

## Architecture threats

Review confused-deputy paths: a highly privileged service acting on client-supplied tenant/resource identifiers; backend-for-frontend bypassing policy; queue worker trusting producer metadata; signed URL service signing arbitrary keys; AI/tool executor trusting retrieved/model text as authority.

Review parser differentials where multiple components interpret the same URL/path/header/content: proxy vs app, allowlist parser vs HTTP client, CDN vs origin, sanitizer vs browser, archive metadata vs filesystem.

## Acceptance

For high-risk features require abuse cases, prevention controls, detection/telemetry where useful, negative tests and residual-risk ownership. If version-sensitive behavior is material, verify current official guidance rather than relying on this reference's snapshot.
