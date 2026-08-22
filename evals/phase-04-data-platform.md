# Phase 04 Evals — Data / Platform

## Routing positives

1. **"Supabase login oluyor ama refresh sonrası session yok."**
   - Expect: `debugging` + `identity-access`; `web-platform` when cookie/browser mechanics are implicated.
   - Do not auto-load database RLS unless data authorization is part of evidence.

2. **"Organization admin başka tenant'ın kayıtlarını görebiliyor."**
   - Expect: `identity-access` + `database-data`; future `security` review because cross-tenant access is high risk.

3. **"PostgreSQL sorgusu 8 milyon satırda çok yavaş."**
   - Expect: `database-data` only initially.
   - Verify plan/cardinality before suggesting indexes.

4. **"Production tablosuna NOT NULL kolon ekleyip 50M satırı backfill edeceğiz."**
   - Expect: `database-data` + `task-planning`.
   - Require expand/backfill/compatibility/lock analysis.

5. **"OrderPaid event bazen iki kere işleniyor."**
   - Expect: `realtime-async`; add `database-data` if durable dedupe/constraint is needed.

6. **"Stripe webhook duplicate geliyor ve iki refund oluşuyor."**
   - Expect: `integrations` + `realtime-async` + `database-data` as required by implementation.

7. **"Private müşteri dokümanlarını upload edip 5 dakikalık link vereceğiz."**
   - Expect: `storage-media`; add `identity-access` for resource policy.

8. **"Email provider 429 veriyor ve bildirimler kayboluyor."**
   - Expect: `integrations`; add `realtime-async` if durable queue/retry pipeline is involved.

## Routing negatives

1. **Hero component mobile'da bozuluyor.**
   - Do not activate Phase 04; route `frontend-engineering`.

2. **REST error response naming consistency.**
   - Route `api-engineering`, not integrations/database.

3. **Next.js hydration mismatch.**
   - Route `debugging` + `react-nextjs`.

4. **Brand palette generic görünüyor.**
   - Route creative skills, not data/platform.

## Edge cases

- OAuth provider returns same verified email for an existing local account: account linking must have explicit trusted rules; do not silently merge identities.
- Role downgrade while old session is active: authorization must reflect revocation strategy and not rely on stale client role state.
- Supabase service-role key appears in a `NEXT_PUBLIC_*` variable: block as critical boundary violation; do not continue normal implementation.
- RLS `SELECT` works but UPDATE can move row to another tenant: test `WITH CHECK`/new-row ownership semantics.
- Migration is reversible syntactically but new app has already written incompatible data: prefer roll-forward analysis.
- Queue provider redelivers after worker committed state but before ack: consumer must not duplicate business effect.
- Webhook event arrives older than current provider state: ignore/reconcile according to version/state semantics rather than blindly overwrite.
- Payment request times out after provider success: reconcile by operation/provider ID before retrying create.
- Signed URL endpoint accepts arbitrary object key: block until resource/tenant ownership is checked before signing.
- Image extension is `.jpg` but decoder sees non-image/huge payload: quarantine/reject despite client MIME.

## Quality assertions

A passing Phase 04 implementation should demonstrate, when relevant:

- explicit identity/session/authorization separation;
- server/resource-scoped authorization and cross-tenant negative tests;
- current provider/library/version verification for auth/database/storage behavior;
- database constraints for durable invariants;
- measured query/index reasoning and transaction/concurrency semantics;
- migration/backfill/restore/recovery plan for risky data changes;
- Supabase RLS/least-privilege handling with no client-side secret/service-role key;
- idempotency before automatic retries for durable jobs/events;
- DLQ/replay/recovery and queue-age observability for important async work;
- verified/deduplicated webhooks with timeout/rate/reconciliation strategy;
- payment state-machine and ambiguous-outcome handling;
- trusted authorization before signed object capabilities;
- file/content validation beyond extension/MIME and safe media processing;
- retention/deletion propagation across database, storage and derived/vector data;
- smallest necessary Phase 04 skill/reference set rather than loading the full phase.