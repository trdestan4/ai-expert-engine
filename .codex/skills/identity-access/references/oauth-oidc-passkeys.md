# OAuth, OIDC, Passkeys and MFA

## OAuth/OIDC

Treat OAuth as delegated authorization and OIDC as the identity layer built on top. Prefer Authorization Code flows with PKCE where supported. Follow current OAuth security best practice (RFC 9700) and avoid legacy implicit and resource-owner-password patterns for new designs.

Validate exact redirect URIs according to provider rules, bind transactions with state/nonce/PKCE as applicable, validate issuer/audience and signature keys, and protect authorization-code/token exchanges from replay and mix-up. Account linking must use verified provider identity, not matching an untrusted email string alone.

Use provider discovery/metadata and mature libraries. Never hand-roll token validation when a maintained implementation exists.

## Passkeys / WebAuthn

Passkeys/WebAuthn use public-key credentials scoped to the relying party. Verify RP ID/origin, challenges, credential identifiers, counters/backup state as supported by the library, and user-verification policy. Do not treat attestation as required unless the product has a real device-trust need.

As of 2026, WebAuthn Level 3 is on the W3C Recommendation track; use the installed browser/server library capabilities rather than assuming every Level 3 feature is universally available.

## MFA and step-up

Choose factors according to threat model. Prefer phishing-resistant methods for high-risk accounts where feasible. Step-up authentication is appropriate for actions such as payout changes, credential management, recovery changes, destructive admin actions, or viewing highly sensitive data.

## Recovery

Do not let recovery bypass the assurance level of normal authentication. Backup codes/tokens must be single-use, rate-limited, revocable, and stored safely. Recovery notifications should not disclose more account information than necessary.

## Tests

Test redirect tampering, state/nonce mismatch, PKCE failure, token issuer/audience mismatch, account-linking collisions, passkey registration/authentication errors, lost authenticators, MFA downgrade, and replayed recovery artifacts.