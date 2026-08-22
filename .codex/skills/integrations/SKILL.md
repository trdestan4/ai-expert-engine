---
name: integrations
description: Owns third-party service integration architecture across external APIs/SDKs, webhooks, payments/billing, email/SMS/notifications, OAuth-connected services, provider rate limits, retries, reconciliation, sandbox/production separation, and integration testing; it does not own generic API design, identity architecture, or queue mechanics.
---

# Purpose

Integrate external services without letting provider behavior, retries, outages, duplicate webhooks, secret handling, or SDK churn corrupt internal business state.

## Use when

- a third-party REST/GraphQL/SDK integration is added or changed;
- webhook ingestion/delivery is required;
- payments, subscriptions, billing, email, SMS, push, maps, analytics, CRM, search or other provider systems are involved;
- external rate limits, retries, provider outages or reconciliation affect application correctness.

## Do not use when

- the application is designing its own API contract (`api-engineering`);
- OAuth login/identity semantics are primary (`identity-access`);
- generic queue/retry topology is primary (`realtime-async`);
- file/object storage is primary (`storage-media`).

## Inputs

Verify:

- provider and installed SDK/API version;
- sandbox/test versus production environment;
- authentication/secrets and allowed scopes;
- provider idempotency, retry, webhook-signature and rate-limit contracts;
- data ownership/source-of-truth and reconciliation needs;
- PII/payment/sensitive-data handling boundaries;
- expected availability/latency and fallback behavior;
- webhook endpoint/replay requirements;
- provider-specific quotas/costs.

## Workflow

### 1. Define ownership and source of truth

Decide which internal state is authoritative and which provider state must be reconciled. Avoid scattering raw provider objects through domain code.

### 2. Isolate provider adapter

Wrap provider SDK/API behind a narrow integration boundary with internal input/output types. Keep business decisions outside the adapter so provider replacement/version migration is possible.

### 3. Verify request semantics

Use explicit timeouts, correlation IDs, safe retries and provider idempotency keys where supported. Respect rate-limit headers and avoid retry storms.

### 4. Treat webhooks as untrusted asynchronous input

Verify signatures/timestamps according to provider docs before parsing trusted fields. Persist/deduplicate event identity, respond quickly, process durable work asynchronously where needed, and tolerate retries/out-of-order delivery.

### 5. Protect secrets/scopes

Use server-side secret storage, least privilege and environment separation. Never ship secret API keys to the browser unless the provider explicitly defines them as publishable/client-safe.

### 6. Handle payments/billing as state machines

Do not infer payment success solely from browser redirects. Persist provider object IDs, process authoritative provider events/API responses, reconcile ambiguous timeouts, and model refund/cancel/failure/past-due states explicitly.

### 7. Make messaging observable

For email/SMS/push, distinguish queued/sent/delivered/bounced/failed when the provider supports it. Protect notification templates from injection/leaking sensitive data and honor user/preferences/compliance boundaries.

### 8. Design degradation

Classify provider failures into fail-open/fail-closed/deferred behavior according to product risk. Core business writes should not become inconsistent because analytics or noncritical messaging is down.

### 9. Reconcile

For business-critical providers, build periodic/on-demand reconciliation against provider state. Webhooks alone are not a perfect ledger.

### 10. Test provider boundaries

Use sandboxes/mocks/contract fixtures for normal tests and targeted integration tests for signature verification, idempotency, timeout-after-success, rate limits, duplicate/out-of-order webhooks, partial outages and version changes.

## Decision rules

- Provider SDK objects should not become domain models by default.
- Every external call needs an explicit timeout.
- Retry only operations safe to retry or protected by idempotency/reconciliation.
- Webhook acknowledgement is not business completion.
- Browser redirect/query params are not proof of payment.
- Verify webhook signatures using the raw payload exactly as the provider requires.
- Sandbox and production identifiers/secrets must not mix.
- Store only provider data the application actually needs and is allowed to retain.
- For critical money/state integrations, reconciliation is a requirement, not an optional debugging tool.

## Reference routing

Load `references/webhooks-and-provider-reliability.md` for signatures, dedupe, retries, timeouts, rate limits and reconciliation.

Load `references/payments-billing.md` for checkout/payment intents, subscriptions, invoices, refunds, webhooks and financial state machines.

Load `references/email-notifications.md` for transactional email/SMS/push delivery, preferences, template safety and provider events.

Load `references/third-party-api-adapters.md` for SDK/API boundaries, scopes, environment separation, versioning and resilience.

Use `realtime-async` for generic queue/worker mechanics and `identity-access` for federated login/account linking.

## Quality gates

- Provider boundary is isolated from domain logic.
- Timeouts, retryability and idempotency are explicit.
- Webhooks are verified, deduplicated and replay-safe.
- Secrets/scopes/environment separation are correct.
- Critical external state has reconciliation strategy.
- Payment/notification states are not oversimplified.
- Provider outage behavior preserves internal consistency.
- Contract/integration tests cover duplicate and ambiguous outcomes.

## Failure handling

If provider documentation and SDK behavior conflict, inspect the installed SDK/source/current official docs before guessing. If an external outcome is ambiguous after timeout, reconcile by provider operation/object identity rather than issuing a blind duplicate. If a provider is unavailable, preserve durable internal intent and defer/retry only where business semantics allow.

## Output contract

Return:

- provider adapter/source-of-truth design;
- request/webhook reliability rules;
- secret/scope/environment model;
- payment/notification lifecycle where relevant;
- degradation/reconciliation strategy;
- tests/observability;
- handoff to async/security/storage specialists.