---
name: privacy-compliance
description: Owns privacy-by-design engineering, data mapping, minimization, purpose/consent, retention, data-subject operations, sensitive-data controls, auditability, and implementation evidence for regimes such as KVKK/GDPR; it does not provide jurisdiction-specific legal advice without current verification.
---

# Purpose

Make privacy requirements implementable and testable in product, data, logging, analytics, storage and operational workflows while minimizing unnecessary personal-data exposure.

## Use when

- personal, sensitive, behavioral, location, analytics, biometric, financial, employee or customer data is collected or processed;
- consent, lawful-purpose, retention, export/delete, account closure, tracking, profiling or third-party sharing is involved;
- privacy/KVKK/GDPR readiness or privacy impact review is required;
- logs, backups, analytics, AI/vector data or integrations may retain personal information.

## Do not use when

- general exploit/security review is primary (`security`);
- database implementation details are primary (`database-data`);
- product copy alone is being edited without data-processing impact;
- the user requests definitive legal interpretation without current jurisdiction-specific evidence; route to legal counsel/current sources.

## Inputs

Establish:

- data categories and sensitivity;
- data subjects and geography/jurisdictions;
- collection sources and purposes;
- systems, processors/subprocessors and transfer paths;
- retention/deletion expectations;
- consent/preferences and evidence requirements;
- export/access/correction/deletion workflows;
- logs/backups/analytics/vector/search copies;
- breach/audit requirements and accountable owners.

## Workflow

### 1. Build the data map

Trace collection → validation → storage → processing → sharing → logs/analytics → backup → deletion. Include derived identifiers and replicas, not only primary tables.

### 2. Minimize collection and exposure

Collect only data needed for declared product/operational purposes. Reduce precision, retention, audience and identifiers where possible. Avoid putting personal data into URLs, logs, cache keys or telemetry unless justified.

### 3. Define purpose and control basis

Record why each category is processed and which product/legal control applies. Do not use generic consent as a blanket substitute for purpose analysis. Where consent is used, make it specific, revocable and auditable.

### 4. Design lifecycle

Set retention by category/purpose, including archives, logs, exports, analytics and object storage. Define deletion/anonymization behavior and what cannot be immediately removed from immutable backups, with restore-time handling.

### 5. Design user/data-subject operations

Implement discoverable access/export/correction/deletion/consent-management flows where applicable. Verify requester identity proportionally and prevent export/delete endpoints becoming privacy/security vulnerabilities.

### 6. Control third parties and transfers

Inventory processors, SDKs, analytics and external APIs; identify data sent, purpose, region and retention. Disable unnecessary collection and keep configuration/evidence of choices.

### 7. Protect sensitive processing

Apply stricter minimization, access, encryption, audit and review to high-sensitivity categories. Coordinate with `security` and `identity-access` rather than duplicating controls.

### 8. Make compliance observable

Record consent/preference changes, privileged access, export/delete jobs and retention execution without logging unnecessary personal content. Create operational evidence that policies are actually enforced.

### 9. Verify current obligations

For jurisdiction-specific claims, dates, thresholds, transfer mechanisms or regulator requirements, verify current authoritative sources before asserting compliance. Engineering guidance must distinguish technical controls from legal conclusions.

## Decision rules

- If data has no clear product/operational purpose, prefer not collecting it.
- A copy in logs, analytics, cache, search, vectors or backups is still part of the data lifecycle.
- Consent must not be inferred from unrelated acceptance when explicit consent is required.
- Deletion must address replicas and downstream processors, not just the primary row.
- Data exports must preserve authorization and avoid exposing another tenant/user.
- Privacy defaults should favor the least collection/sharing consistent with the intended product.
- Never claim “GDPR/KVKK compliant” solely because a checklist passed.

## Reference routing

Load `references/privacy-data-map.md` for classification, mapping and minimization.
Load `references/consent-rights-retention.md` for preference, rights and lifecycle workflows.
Load `references/jurisdiction-verification.md` for KVKK/GDPR engineering boundaries and current-law verification rules.

Use `database-data` for storage/RLS/migrations, `identity-access` for requester identity/permissions, `security` for threat controls, and `integrations` for processor/provider reliability.

## Quality gates

- Personal-data categories, purposes, locations and processors are mapped.
- Collection/telemetry/logging is minimized and justified.
- Retention and deletion behavior includes replicas/backups where relevant.
- Consent/preference state is explicit and auditable when used.
- Export/delete/access workflows preserve identity and tenant authorization.
- Third-party data sharing is known and configurable.
- Legal/compliance claims that can change are verified against current authoritative sources.
- Technical evidence is distinguished from legal certification/advice.

## Failure handling

If the data flow is unknown, stop claiming privacy readiness and build the map first. If jurisdiction-specific requirements are uncertain, state the uncertainty and verify current official guidance or involve qualified counsel. If deletion cannot be guaranteed in a subsystem, document the limitation and design compensating lifecycle controls rather than pretending deletion occurred.

## Output contract

Return:

- data inventory/flow;
- minimization and purpose decisions;
- consent/rights/retention requirements;
- third-party/transfer concerns;
- technical controls and audit evidence;
- current-law verification needs;
- residual privacy risks and owners.