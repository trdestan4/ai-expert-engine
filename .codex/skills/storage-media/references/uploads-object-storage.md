# Uploads and Object Storage

## Object classes and keys

Use separate buckets/prefix policies for public assets, private user content, temporary uploads and quarantine if provider capabilities permit. Generate opaque keys server-side from trusted tenant/resource context; never concatenate unsanitized user paths.

Keep display filename, content metadata, owner/resource and object key separately. Normalize filename only for display/download headers, not authorization.

## Upload methods

Small files can be proxied through the application when server-side inspection is required. Large files should usually use provider-signed direct or multipart/resumable upload so application memory/bandwidth does not scale with object size.

Signed upload issuance must validate intended owner, size/type policy and quota before granting capability. Limit expiry, object key and permitted operation/content constraints as supported by provider.

## Validation

Enforce maximum bytes before/while receiving. Check actual format signatures/decoder behavior for supported types. Reject polyglot/unsupported archives/executables according to product policy. Protect archive/image/video processing from decompression bombs and huge dimensions/duration.

## Quarantine

For untrusted documents/media requiring scanning, upload to pending/quarantine, persist processing state, scan/validate, then move/mark active. Do not expose public URLs during pending state.

## Lifecycle

Clean abandoned multipart sessions, expired temp objects and orphan derivatives. For replacement, prefer versioned keys and update the database pointer; delete old objects asynchronously after safe transition.

## Tests

Cover oversized upload, forged MIME/extension, key tampering, cross-tenant destination, interrupted multipart, duplicate finalize, quota exceeded, orphan cleanup and provider timeout.