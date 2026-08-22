# Email and Notifications

## Message categories

Separate security/transactional messages from product notifications and marketing. Different categories have different urgency, opt-out, deliverability and compliance expectations.

## Delivery model

Persist important notification intent before provider submission. Track provider message ID and status when delivery/bounce events matter. Queued/sent/delivered are different states; do not promise delivery based only on provider acceptance.

## Templates

Escape untrusted content, validate links, avoid leaking sensitive data in subject/previews, and keep templates versioned/testable. Security emails should identify the action and safe recovery path without including secrets unnecessarily.

## Preferences

Honor user channel/category preferences where product/legal requirements allow. Critical authentication/security notices may be mandatory; define that exception explicitly rather than bypassing all preferences.

## Rate and abuse controls

Prevent notification storms from retry loops or repeated events. Deduplicate/coalesce where appropriate. Verification/password-reset sends need abuse/rate controls without revealing account existence.

## Provider events

Handle bounce, complaint, unsubscribe and delivery events according to provider semantics. Suppress repeatedly invalid destinations rather than retrying indefinitely.

## Tests

Cover template escaping, locale fallback, duplicate event, provider outage, bounce/complaint, preference changes, security-email enumeration behavior, delayed queue and malformed recipient data.