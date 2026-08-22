# Jurisdiction Verification and Privacy Control Mapping

This skill must not present legal advice. Privacy laws, regulator guidance and territorial scope change; verify current authoritative sources for the specific organization, users, data and processing.

## Separate law from engineering

Label statements as:
- **verified legal/product requirement** — supplied by counsel/policy or checked against current authoritative source;
- **engineering control** — minimizes risk or enables compliance regardless of jurisdiction;
- **assumption/unknown** — requires legal/product decision.

Do not convert GDPR/CCPA-like concepts into one universal rule. Consent, legitimate/contractual bases, children's data, sensitive categories, retention, cross-border transfer, sale/share/targeted advertising and rights deadlines differ.

## Verification questions

Identify organization/controller/processor role, user/data-subject locations, processing locations, sensitive/child data, business thresholds/exemptions if relevant, processors/subprocessors, transfer/residency constraints and contractual/customer obligations.

For enterprise products, customer DPAs/security/privacy commitments can be stricter than baseline law and become product requirements.

## Processor and transfer controls

Maintain processor inventory with purpose, data categories, regions, subprocessors, security/privacy terms and deletion/export capabilities. Engineering should make provider region/config explicit and avoid hidden fallback regions when residency commitments exist.

## Evidence/control mapping

Map each verified requirement to implementation/config/process/test evidence and accountable owner. Examples: consent state → tag gating test; delete right → lifecycle job + reconciliation; residency → provider region config + deployment evidence.

## Change management

Store source URL/version/date and review window for material legal/provider claims. When law/provider docs change, trigger targeted review of affected controls rather than blindly rewriting all privacy text.
