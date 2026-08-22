# Consent, Preferences, Rights, Retention and Deletion

Engineering guidance only; verify current legal requirements for the actual jurisdiction/product.

## Consent and preferences

Separate necessary processing from analytics/marketing/personalization. Where valid consent is required, do not infer it from silence/prechecked boxes. Record consent/policy version, timestamp/source and preference changes when needed. Withdrawal should be as usable as granting and propagate to downstream tracking/processing.

A cookie banner is not a privacy program. Ensure tags/SDKs actually honor the modeled state; avoid loading non-essential trackers before the applicable choice.

## Data subject/user rights workflows

Design export/access/correction/delete workflows with identity verification proportional to risk. Define scope across primary DB, object storage, analytics, support systems and derived/vector/search copies. Avoid exporting other tenants/users through weak object scoping.

Deletion can be immediate in live systems while backups expire through controlled retention if that matches policy/law; document exceptions rather than claiming impossible instant erasure from immutable backups.

## Retention

Every sensitive category needs a retention trigger and duration/condition, not “forever.” Examples: account closure + grace, invoice/legal retention, security log window, temporary upload TTL. Implement scheduled purge/partition lifecycle where manual deletion would drift.

Logs, queues, caches, object derivatives, search indexes and vector stores need retention semantics too. A database row deletion is not complete if accessible copies remain elsewhere.

## Soft delete

Soft delete is useful for recovery/audit only with explicit purge, access and uniqueness behavior. It is not equivalent to deletion. Avoid indefinite hidden personal data behind `deleted_at`.

## Evidence

Test lifecycle: create data → propagate → change consent/preferences → export/delete → verify downstream removal/restriction. For high-risk data, operational dashboards/reconciliation can detect orphan copies.
