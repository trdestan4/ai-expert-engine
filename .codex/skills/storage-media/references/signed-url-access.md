# Signed URLs and Storage Access

## Public versus private

Public storage should contain only content intentionally accessible to anyone who knows/discovers the URL. User/account/tenant documents should default private and require an authorization decision before access capability is issued.

## Signed download URLs

Authorize the current subject against the database/resource first, then sign a specific object/action for a short lifetime. Avoid allowing clients to submit arbitrary object keys that are signed without ownership validation.

The signed URL itself is a bearer capability; anyone possessing it can generally use it until expiry. Keep TTL proportional to use case and avoid logging URLs containing sensitive query signatures.

## Signed upload URLs

Bind upload capability to server-chosen object key and expected user/tenant/resource. Constrain size/content properties using provider-supported policies and verify the final object before making it active.

## Storage policy / RLS

When a provider such as Supabase Storage uses database/RLS policies, treat storage object ownership/path claims as authorization data. Never rely on filename prefix alone without trusted policy checks.

## CDN and caching

Private signed content must not accidentally become publicly cacheable. Set cache headers/provider behavior according to sensitivity. For public immutable assets, long cache lifetimes plus versioned/content-hashed keys are desirable.

When replacing objects, use new keys/versions rather than expecting every CDN cache to notice in-place mutation immediately.

## Tests

Cover expired URL, URL reuse, unauthorized signing request, cross-tenant object key, public/private cache headers, revoked/deleted underlying resource and stale CDN behavior.