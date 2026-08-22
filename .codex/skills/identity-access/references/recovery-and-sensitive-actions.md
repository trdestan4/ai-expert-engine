# Recovery and Sensitive Actions

## Verification flows

Email/phone verification tokens must be random, scoped to one purpose/account, short-lived, single-use where possible, and invalidated after successful use or superseding changes. Avoid placing sensitive state in readable query parameters when a server-side reference can be used.

## Password reset

Reset artifacts should not reveal whether an account exists. After reset, consider revoking existing sessions and security-sensitive refresh tokens. Notify the user of the credential change without exposing secrets.

## Email/identity change

High-impact identity changes should require recent authentication or equivalent step-up. Protect both old and new channels where appropriate. Do not immediately trust a new email merely because it was submitted by an authenticated session.

## Account recovery

Recovery should have explicit assurance tiers. Prefer previously enrolled strong authenticators/recovery codes over support-agent overrides. Manual recovery must have auditability, rate limits, and clear escalation procedures.

## Sensitive actions

Examples requiring recent authentication depending on risk: password/passkey changes, MFA disable, recovery-channel change, payout/bank change, API-key creation, destructive organization actions, export of sensitive data, or privilege escalation.

## Offboarding

Define disabled versus deleted state, session revocation, token/API-key revocation, ownership transfer, pending jobs, audit retention, and data deletion/anonymization requirements.

## Tests

Cover token replay, token expiry, multiple outstanding resets, account enumeration, stale sessions after reset, recovery-code reuse, email-change races, offboarded users, and step-up expiration.