# Web and API Security

## Injection and output safety

Validate untrusted values at boundaries and use parameterized/database/framework primitives instead of string-built commands/queries. Encode output for its actual HTML/attribute/URL/JS context. Avoid unsafe HTML rendering unless content is trusted/sanitized with a reviewed policy.

## Browser controls

Reason about XSS, CSRF, cookies, SameSite, CORS, CSP, clickjacking and open redirects based on the application's auth model. CORS is not authentication. CSRF risk depends on credential attachment and request semantics, not whether an endpoint is called “API”.

## API authorization

Authorize each resource/action server-side. Test object-level and function-level authorization, tenant boundaries, mass assignment/over-posting and excessive data exposure. Bind identifiers to authorized ownership rather than trusting client-supplied tenant/user IDs.

## SSRF and outbound requests

Treat user-controlled destinations as dangerous. Prefer allowlisted destinations/provider IDs, restrict protocols/ports/IP ranges where applicable, block cloud/internal metadata targets and control redirects/DNS resolution behavior.

## Resource abuse

Bound payload size, pagination, file size, query complexity, concurrency and expensive operations. Apply rate/velocity limits with identity/resource dimensions appropriate to abuse cases.

## Verification

Security tests should attempt malformed encodings, alternate IDs/tenants, replay, forged origins/tokens, unsafe destinations, oversized inputs and privilege escalation—not just ordinary validation failures.