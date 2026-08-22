# Authorization Models

## Permission-first design

Model permissions as actions on scoped resources, then bundle them into roles when useful. Examples: `invoice.read`, `invoice.refund`, `member.invite`, each constrained to organization/project/resource scope.

RBAC works well when permissions cluster into stable job roles. ABAC/policy checks help when access depends on attributes such as ownership, tenant, region, resource state, risk, or time. Avoid turning every conditional into a global role.

## Tenant boundaries

A tenant/workspace membership row is an authorization input, not blanket access. Every resource access path must prove the subject belongs to the correct tenant and has permission for the operation. Cross-tenant identifiers supplied by clients are untrusted.

## Enforcement

Keep authorization near trusted operations. UI gating improves UX but never replaces server/database checks. Background jobs, exports, admin endpoints, storage paths, and webhook-triggered actions require the same policy semantics.

## Lifecycle

Define invitation expiry, acceptance identity, membership removal, role downgrade, ownership transfer, disabled accounts, last-owner protection, and tenant deletion. Decide whether permission changes invalidate sessions immediately or are resolved dynamically.

## Policy structure

Centralize reusable policy decisions rather than scattering ad-hoc `if role == ...` checks. Keep resource loading and policy evaluation explicit enough to test. Deny by default when a new action/resource is not mapped.

## Tests

Build a permission matrix covering anonymous, member, privileged member, owner/admin, disabled/removed member, cross-tenant subject, object owner/non-owner, and state-dependent operations. Test both positive and negative cases.