# Consent, Rights, Retention and Jurisdiction Verification

Consent/preference state should identify what was agreed to, when, under which notice/version and how it can be withdrawn. Do not bundle unrelated optional purposes into one irreversible flag.

Design access/export/correction/deletion flows as privileged operations: verify the requester, preserve tenant boundaries, avoid exporting secrets/internal fields and record operational evidence without logging unnecessary personal content.

Retention is category/purpose-specific. Define active retention plus handling for logs, analytics, archives, search/vector replicas, provider copies and backups. If immutable backups cannot be edited immediately, document expiry and restore-time deletion/reconciliation behavior.

KVKK, GDPR and other regimes change through legislation, regulator guidance and court decisions. The skill may implement common privacy engineering controls, but jurisdiction-specific legal claims, transfer mechanisms, thresholds, notice wording and statutory timelines must be verified against current authoritative sources or qualified counsel.

Never label a system legally “compliant” merely because technical controls or an internal checklist passed.