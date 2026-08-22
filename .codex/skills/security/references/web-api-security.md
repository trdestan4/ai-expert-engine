# Web and API Security

## Injection and output contexts

Validate untrusted data at trust boundaries and use safe structured APIs. SQL parameterization prevents SQL injection but does not protect shell commands, templates, LDAP, XPath, NoSQL operators or unsafe dynamic code. Identify the actual sink.

For XSS, output context matters: HTML text, attribute, URL, CSS and JavaScript contexts need appropriate primitives. Avoid unsafe HTML rendering; when rich HTML is required, sanitize with a reviewed allowlist and verify URL/protocol/style behavior. CSP/Trusted Types can add defense in depth but do not excuse unsafe source handling.

## Authorization

Authorize every resource/action server-side using current authenticated subject plus resource/tenant context. Test object-level, function-level and field-level access, mass assignment/over-posting and excessive exposure. Never trust client-supplied user/tenant IDs as ownership proof. UI hiding is not authorization.

## Browser threats

Reason about cookies, SameSite, CSRF, CORS, CSP, clickjacking, open redirects and postMessage based on actual credential attachment and origin/site model. CORS governs browser read access, not server authorization. SameSite reduces some CSRF paths but is not a universal model; state-changing endpoints still need deliberate protections appropriate to auth architecture.

Review service workers, local storage and client caches for sensitive data persistence. Treat DOM sinks, URL fragments/query strings and third-party scripts as browser trust surfaces.

## SSRF

Prefer provider IDs or explicit destination allowlists over arbitrary URLs. If URLs are accepted: constrain schemes/ports, parse canonically, resolve DNS/IP and reject loopback/link-local/private/special ranges where required, re-check redirects, consider DNS rebinding and parser differentials, and block cloud metadata/internal control planes. Egress network controls complement application validation.

## Request/proxy differentials

For apps behind CDN/proxy/load balancer, review host/scheme/client-IP/header trust. Ambiguous content-length/transfer-encoding and cache-key differences can create request smuggling or cache poisoning in some stacks; only report when the deployed chain and versions make a path credible. Normalize/strip untrusted forwarded headers at the trusted proxy boundary.

## Deserialization/prototype pollution

Avoid deserializing untrusted native object graphs. For JavaScript, treat deep merge/path setters and `__proto__`/constructor/prototype keys carefully; use schemas and safe libraries. For JVM/.NET/Python/Ruby ecosystems, avoid unsafe generic deserialization formats/gadgets and verify framework defaults.

## Resource abuse

Bound body/file size, decompression ratio, nested structures, pagination, regex/query complexity, GraphQL depth/cost, concurrency and expensive transforms. Rate limits should use attacker-relevant dimensions (account, IP/device, resource, tenant, payment method) and protect both capacity and abuse cases.

## Verification

Attempt alternate IDs/tenants/roles, malformed encodings, duplicate parameters/headers when relevant, replay, forged origins/tokens, unsafe destinations/redirects, oversized/nested inputs, cache variation and privilege escalation. Security tests must target the actual deployed trust chain, not only controller validation.
