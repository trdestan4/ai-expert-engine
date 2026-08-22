# Session Authentication

## Session model

Define the session identifier, server-side/session-store data, cookie attributes, idle timeout, absolute timeout, rotation triggers, revocation, logout, and device/session visibility before implementation.

For browser applications, prefer `HttpOnly`, `Secure`, appropriately scoped cookies and an intentional `SameSite` policy. Session identifiers must be unpredictable and must not encode privileged state that the server blindly trusts.

Rotate session identifiers after authentication and meaningful privilege changes. Password reset, account disable, role downgrade, suspected compromise, and explicit global logout should invalidate relevant sessions.

## JWT model

JWT is a serialization/signature format, not a complete session strategy. Validate issuer, audience, expiry/not-before, algorithm/key selection, and expected claims. Keep access tokens short-lived when replay risk matters. Define refresh-token rotation/reuse detection if refresh tokens exist.

Do not put secrets or unnecessary PII in tokens. Signature does not encrypt claims. Avoid putting long-lived privileged tokens in `localStorage` solely because it is convenient.

## Server boundaries

Authentication proves a subject; every privileged server entry point must still perform authorization. Framework middleware can improve routing/UX, but final authorization should occur near the protected operation/resource.

## CSRF and browser behavior

Cookie-authenticated state-changing requests require CSRF-aware design unless the framework/protocol provides an equivalent robust control. Origin/SameSite checks can be part of defense-in-depth but should match the application's actual cross-site needs.

## Tests

Cover login fixation, logout/revocation, expiry, refresh race/reuse, stolen/stale session behavior, privilege changes, multiple devices, browser restart behavior, and failure when the backing session store is unavailable.