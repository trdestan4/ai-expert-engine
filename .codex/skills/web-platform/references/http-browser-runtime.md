# HTTP, Origins, Cookies, and Cache

Use this reference only when the task depends on framework-independent transport behavior.

## Request/response model

Reason from the concrete tuple: URL, method, request headers/body, response status, response headers/body, redirect chain, and intermediary/cache involvement. Separate transport success from application success.

### Methods

- GET/HEAD are retrieval-oriented; avoid side effects that make navigation/prefetch unsafe.
- PUT/DELETE are conventionally idempotent; POST is not assumed idempotent. Actual API semantics still belong to the API owner.
- Browser forms naturally support GET/POST; other methods generally require script/framework handling.

### Status/redirects

Treat 2xx, 3xx, 4xx, and 5xx as protocol outcomes, not UI states by themselves. Preserve method semantics across redirects according to the chosen status and framework behavior. Direct navigation and client navigation may observe redirects differently because the framework can mediate them.

## Origin vs site

Origin = scheme + host + port. Site is a broader browser concept based on registrable domain and scheme in modern cookie policy contexts. Diagnose these separately.

CORS is a browser-enforced read policy for cross-origin requests. It does not stop non-browser clients from sending requests and does not establish authentication/authorization.

For credentialed cross-origin requests, reason about both client credential mode and server response headers; wildcard-origin behavior is constrained with credentials.

## Cookies

Evaluate attributes independently:

- Domain/host scope
- Path
- Secure
- HttpOnly
- SameSite
- expiration/max-age

A cookie existing in storage does not prove it is sent on a given request. A cookie being sent does not prove the server accepts the session.

Avoid storing sensitive session credentials in script-readable storage merely for convenience; identity/security policy belongs to the auth/security owner.

## Caching

Identify the layer first. For HTTP caches reason about freshness and validation using response/request directives and validators (for example ETag/Last-Modified where applicable), plus `Vary` when representation depends on request headers.

Do not confuse:

- HTTP browser cache;
- CDN/shared cache;
- service-worker Cache Storage;
- framework data/render cache;
- client query cache.

A stale page can originate from any one of these.

## Diagnostic evidence

Capture the browser network request, response headers, redirect chain, initiator/navigation type, cookie request/response details, cache indicator, and exact origin. Prefer this evidence over changing CORS/cookie/cache flags at random.
