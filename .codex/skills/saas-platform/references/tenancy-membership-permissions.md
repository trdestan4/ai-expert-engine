# SaaS Tenancy, Membership and Enterprise Identity

## Tenant model

Define tenant/workspace/org identity, user membership, roles/permissions, resource ownership and cross-tenant policy explicitly. A logged-in user may belong to several tenants; every server/data/storage/background path must resolve the active resource tenant independently of client UI state.

## Membership lifecycle

Model invite pending/accepted/expired/revoked, role change, suspension and offboarding. Invites need scoped token, expiry, target tenant/role and rules for existing accounts/domain conflicts. Removing a member must revoke effective access across sessions/tokens/jobs where policy requires it.

## Authorization

Role names are convenience; permissions/actions/resource scope are the actual policy. Test cross-tenant IDs, downgraded roles, owner/admin edge cases and direct API/storage access. RLS/data enforcement coordinates with `database-data`; identity/session with `identity-access`.

## Enterprise SSO

For SAML/OIDC enterprise SSO, define domain/org discovery, IdP configuration ownership, just-in-time provisioning policy, account linking, logout/session implications and break-glass/admin recovery. Do not trust email domain alone as tenant authorization.

## SCIM / provisioning

SCIM or directory sync changes membership lifecycle: create/update/deactivate, group→role mapping, idempotency, duplicate identity reconciliation and customer-admin expectations. Deprovision should remove effective access predictably and be observable/auditable.

## Tenant residency/enterprise controls

If enterprise customers require region/data residency, explicit tenant region assignment, provider configuration, migration and backup/log/analytics scope are part of platform design. Do not promise residency based only on primary DB location.

## Audit

High-value admin actions (role, SSO config, billing, export, destructive settings) need actor/resource/time/result and security-conscious metadata. Audit logs themselves require authorization/retention.
