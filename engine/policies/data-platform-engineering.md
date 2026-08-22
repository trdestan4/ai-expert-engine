# Data / Platform Engineering Policy

- Identity, authentication, session and authorization are separate concepts; UI gating never replaces trusted enforcement.
- Authorization must be resource/tenant scoped and deny cross-tenant access by default.
- Follow current OAuth security BCP and installed provider/library capabilities; do not hand-roll cryptography or token verification.
- Durable data invariants belong in database constraints/transactions where practical, not only application conditionals.
- Query/index decisions require real access patterns and plans; caching is not the first fix for pathological queries.
- Live migrations require compatibility, lock/backfill and roll-forward/rollback analysis.
- Supabase exposed schemas require least-privilege grants and RLS; service-role/secret keys are backend-only.
- Queue/event consumers must tolerate duplicates and retryable failure; important side effects require idempotency/deduplication.
- Dead-lettered/stuck work requires observable recovery ownership, not silent accumulation.
- Webhooks are untrusted input: verify signatures, deduplicate and reconcile critical provider state.
- Payments are state machines; browser redirects are not proof of payment and financial operations require reconciliation/idempotency.
- Every external network integration has explicit timeout and rate/retry behavior.
- Private storage access requires trusted authorization before signed capability issuance.
- File extension/client MIME is not sufficient validation; untrusted media must be resource-bounded and quarantined when scanning is required.
- Data/object/vector deletion and retention must propagate to derived copies and asynchronous cleanup.
- Provider/runtime/spec advice is repository-version-aware; never upgrade solely because a newer feature exists.
