---
name: identity-access
description: Owns authentication and authorization architecture across sessions, cookies, JWTs, OAuth/OIDC, passkeys, MFA, account recovery, RBAC/ABAC, roles, permissions, tenant boundaries, and auth testing; it does not own database schema design or general security auditing.
---

# Purpose

Design identity and access flows that are secure, recoverable, least-privilege, understandable to users, and explicit about session/token lifecycle and authorization boundaries.

## Use when

- login, signup, logout, session persistence, refresh, MFA, passkeys, passwordless, OAuth/OIDC, social login, or account recovery is involved;
- roles, permissions, RBAC/ABAC, organization/workspace membership, invitations, or tenant access must be modeled;
- client/server auth boundaries, cookies/JWTs, or server-side authorization checks need implementation/review;
- an auth flow is being migrated or hardened.

## Do not use when

- RLS/schema/indexing are the main problem (`database-data`);
- general exploit/threat review is primary (future `security`);
- API resource/response contract is primary (`api-engineering`);
- browser cookie mechanics are the root issue (`web-platform` may lead, then identity-access).

## Inputs

Verify:

- user/account/organization model and trust boundaries;
- installed auth provider/library and versions;
- web/mobile/server clients and redirect origins;
- session/token storage model and expiration/rotation behavior;
- privilege model and sensitive actions;
- recovery, verification, invitation, and offboarding requirements;
- tenant isolation requirements;
- threat level and audit/compliance constraints.

## Workflow

### 1. Separate identity, authentication, session, and authorization

Define who the subject is, how identity is proven, how authenticated state persists, and what each subject may do. Never collapse these into one boolean such as `isAdmin`.

### 2. Choose the smallest safe authentication mechanism

Prefer mature provider/library primitives. For browser apps, favor secure server-managed sessions or well-designed token flows over custom token handling. Never invent cryptography.

### 3. Design session lifecycle

Specify creation, rotation, idle/absolute expiry, revocation, logout, device/session listing where needed, re-authentication for sensitive actions, and behavior after password/role/security changes.

### 4. Protect browser state

Use secure cookie attributes and server boundaries appropriate to the framework. Do not place long-lived privileged secrets in browser storage simply for convenience.

### 5. Design federation correctly

For OAuth/OIDC, verify provider metadata/tooling support, redirect URI rules, PKCE/nonce/state requirements, token audience/issuer validation, and account-linking rules. Follow current OAuth security BCP rather than legacy implicit/password flows.

### 6. Add stronger authenticators when risk justifies them

Use passkeys/WebAuthn, MFA, step-up authentication, or recovery codes where appropriate. Recovery must not be weaker than the protected account.

### 7. Model authorization explicitly

Define permissions from resource/action/subject relationships. Use RBAC for stable role bundles, ABAC/policy checks where contextual attributes are necessary, and tenant/resource ownership checks at trusted server/database boundaries.

### 8. Enforce on every trusted path

UI visibility is not authorization. Server actions, API routes, background jobs, admin tools, direct database paths, and storage access must enforce equivalent policy.

### 9. Handle lifecycle edge cases

Cover invitations, duplicate identities, email changes, disabled users, role downgrade, organization removal, deleted tenants, stolen sessions, refresh failures, and concurrent device sessions.

### 10. Test authorization negatively

Test allowed and denied paths, horizontal/vertical privilege escalation, stale sessions, revoked membership, cross-tenant access, recovery flows, redirect abuse, and replay-sensitive flows.

## Decision rules

- Prefer server-enforced authorization over client-enforced checks.
- Prefer opaque/session cookies for browser-only apps when they simplify revocation and reduce token exposure.
- Use JWTs only when distributed verification or ecosystem constraints justify them; signed does not mean revocable or encrypted.
- OAuth is authorization; OIDC adds identity. Do not infer identity from arbitrary access-token contents without provider contract.
- Use PKCE for authorization-code flows where supported; avoid deprecated implicit/resource-owner-password patterns.
- Passkeys are strong authentication, not a replacement for authorization or recovery design.
- Role names are not enough; permissions and resource scope must be explicit.
- Tenant membership must never imply unrestricted tenant-resource access without defined policy.

## Reference routing

Load `references/session-authentication.md` for sessions, cookies, JWT lifecycle, logout/revocation, and browser/server boundaries.

Load `references/oauth-oidc-passkeys.md` for OAuth/OIDC, PKCE, federation, WebAuthn/passkeys, and MFA.

Load `references/authorization-models.md` for RBAC, ABAC, permissions, tenant/resource policy, invitations, and lifecycle.

Load `references/recovery-and-sensitive-actions.md` for verification, password reset, account recovery, re-authentication, email change, and offboarding.

Use `database-data` when authorization moves into RLS/policies. Use future `security` for threat modeling, secret exposure, abuse, and broad exploit review.

## Quality gates

- Identity/auth/session/authorization concepts are separated.
- Session/token lifecycle includes expiry, rotation/revocation, and logout semantics.
- Sensitive flows have re-authentication/recovery protections where justified.
- Authorization is server-side and resource-scoped.
- Cross-tenant and privilege-escalation paths are denied by tests.
- OAuth/OIDC/passkey behavior is library/spec-version aware.
- No custom cryptography or browser-exposed privileged secrets are introduced.

## Failure handling

If provider behavior is unclear, inspect the installed provider/library and official current documentation before changing protocol details. If authorization rules are ambiguous, stop broad access and derive a permission matrix from actual user actions/resources. If recovery cannot be made trustworthy, fail closed for high-impact actions rather than weakening authentication.

## Output contract

Return:

- identity/session/authorization model;
- chosen auth mechanism and rationale;
- lifecycle and recovery behavior;
- permission/tenant enforcement plan;
- sensitive edge cases;
- required tests;
- handoff points to database/security/platform specialists.