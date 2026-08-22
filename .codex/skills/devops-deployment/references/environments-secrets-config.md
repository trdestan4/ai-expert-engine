# Environments, Secrets and Configuration

## Environment separation

Define local/test/preview/staging/production purpose and data/provider isolation. Staging similarity is useful but staging approval never authorizes production; release evidence is target-environment bound.

Avoid production data copied casually into lower environments. If sanitized snapshots are used, document process and access. Separate payment/email/auth/provider sandbox vs production identifiers and callbacks.

## Configuration

Validate required config and types at startup/build boundary rather than failing on first request. Distinguish build-time vs runtime/public variables; client-prefixed variables must never contain privileged secrets. Record config changes that can materially alter behavior even without code change.

## Secrets

Prefer managed secret stores/workload identity. Scope by environment/service, rotate high-privilege credentials and avoid plaintext state/logs/artifacts. A leaked secret requires rotation/revocation, not only code deletion.

## Drift

Treat manual console changes as drift. IaC/config source of truth should reconcile intentional exceptions. For emergency changes, record owner/reason and back-port to source.

## Promotion

Promote immutable artifact plus environment-specific config. Verify callback URLs/domains, migrations, queue names, storage buckets and feature flags before traffic shift. Production smoke tests must avoid destructive/user-visible side effects unless designed.
