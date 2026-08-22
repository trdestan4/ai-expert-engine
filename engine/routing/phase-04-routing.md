# Phase 04 Routing — Data / Platform

Use the smallest owning skill set; do not load all five for ordinary changes.

## Primary ownership
- Login/session/OAuth/OIDC/passkeys/MFA/recovery/RBAC/ABAC/permissions/tenant membership → `identity-access`
- PostgreSQL/Supabase/schema/SQL/indexes/transactions/migrations/RLS/Redis/vector data → `database-data`
- WebSockets/SSE/queues/workers/cron/retries/DLQ/events/idempotency/outbox → `realtime-async`
- External APIs/SDKs/webhooks/payments/billing/email/SMS/provider reconciliation → `integrations`
- File/object storage/uploads/signed URLs/media processing/CDN/lifecycle → `storage-media`

## Typical routes
**Supabase login disappears after refresh:** `debugging` → `identity-access`; add `web-platform` for cookie/browser mechanics and `database-data` only if RLS/profile access is part of the failure.

**Design tenant roles + RLS:** `identity-access` defines permission model → `database-data` implements database enforcement.

**Slow PostgreSQL query:** `database-data`; add `performance` only for broader measured performance work.

**Large live schema migration:** `database-data` + `task-planning`; production cutover adds `testing-qa`, `devops-deployment` and `release-readiness` as risk requires.

**Send email after order:** `integrations` for provider/message semantics; `realtime-async` only if durable queued delivery is required.

**Stripe/provider duplicate webhook:** `integrations` owns signature/provider event semantics → `realtime-async` if durable worker/retry pipeline is involved → `database-data` if unique/idempotent state constraint is required.

**Realtime dashboard updates:** `realtime-async`; add `frontend-engineering` for UI state and `identity-access` only for channel/resource authorization design.

**Private image upload:** `storage-media`; add `identity-access` for ownership policy, `database-data` for metadata/RLS, `realtime-async` for heavy processing and `security` for hostile-file/trust-boundary review.

**Payment checkout:** `integrations` owns provider/payment lifecycle; `api-engineering` owns public application API contract; `database-data` owns order/payment persistence constraints; `security` and `testing-qa` review payment/trust behavior.

## Overlap prevention
`identity-access` defines who/what may act. `database-data` owns persisted invariants and data-level enforcement. `realtime-async` owns delivery/execution semantics. `integrations` owns external provider contracts. `storage-media` owns object/file lifecycle and access capability.

General exploit review belongs to `security`. Deployment/monitoring mechanics belong to `devops-deployment` and `observability-sre`. Final production approval belongs to `release-readiness`.

## Token rule
Load only references required by verified stack/use case. Supabase RLS should not load Redis/vector docs; REST webhook work should not load payments; ordinary DB migrations should not load auth/passkey references; simple uploads should not load all media-processing guidance.
