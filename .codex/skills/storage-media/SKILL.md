---
name: storage-media
description: Owns file and media architecture across multipart/direct uploads, object storage, signed URLs, access policies, file validation, malware scanning, image/video processing, CDN delivery, lifecycle, metadata, quotas, and deletion; it does not own general database modeling or visual asset art direction.
---

# Purpose

Store and deliver user/product files safely and efficiently while preventing unauthorized access, unsafe uploads, broken lifecycle, runaway cost, and media-processing bottlenecks.

## Use when

- file upload/download, object storage, buckets, signed URLs or CDN delivery is required;
- images/video/documents need validation, transformations, thumbnails or processing;
- storage authorization, object ownership, retention/deletion, quotas or malware scanning must be designed;
- large uploads or direct-to-storage flows need implementation.

## Do not use when

- database schema is the primary concern (`database-data`);
- visual image-generation/art-direction is primary (`asset-production`);
- generic background-job mechanics are primary (`realtime-async`);
- general security audit is primary (`security`).

## Inputs

Verify:

- provider/storage product and SDK version;
- object categories, maximum size/count and expected volume;
- public/private access requirements and tenant ownership;
- allowed file/media types and processing requirements;
- browser/direct upload versus server-proxy path;
- CDN/cache behavior and replacement/version semantics;
- malware/content validation requirements;
- retention, deletion, legal/audit and backup expectations;
- provider egress/storage/transform quotas/costs.

## Workflow

### 1. Classify objects

Separate public immutable assets, private user content, sensitive documents, temporary uploads and generated derivatives. Different classes require different buckets/prefixes/access/lifecycle rules.

### 2. Design object identity

Use server-generated opaque object keys with tenant/resource association. Do not use raw user filenames as authoritative paths. Store original display filename/metadata separately when needed.

### 3. Validate before trust

Enforce size/count/type policy server-side or in trusted post-upload processing. File extension and client MIME are hints, not proof. Validate signatures/content for supported formats and reject dangerous/unexpected payloads.

### 4. Choose upload path

Proxy small/sensitive uploads through trusted servers when useful. For large files, prefer short-lived scoped signed upload URLs or provider multipart/resumable uploads to avoid server memory/bandwidth bottlenecks.

### 5. Separate upload from activation

For untrusted content, upload into a quarantine/pending state; validate/scan/process; then mark/publish as active. Do not expose a file publicly before required validation completes.

### 6. Enforce access

Private objects require server authorization or narrowly scoped expiring signed URLs. Bucket visibility alone is not a tenant authorization model. Validate object ownership before issuing upload/download/delete access.

### 7. Process media safely

Run image/video/document processing outside request lifetime when expensive. Bound dimensions/duration/resources, remove unnecessary metadata where privacy matters, generate known derivatives and prevent decompression/resource-exhaustion attacks.

### 8. Deliver efficiently

Use CDN/cache-control according to mutability. Prefer content-addressed/versioned keys for immutable derivatives. Avoid replacing cached objects in place when stale copies would be harmful.

### 9. Define lifecycle

Handle abandoned multipart uploads, orphan objects, replacement, user/account deletion, derivative cleanup, retention, legal holds and temporary-object expiry. Database deletion and object deletion may require asynchronous reconciliation.

### 10. Verify abuse/cost limits

Apply quotas/rate limits where upload abuse can create cost. Monitor storage growth, egress, transform volume, failed scans, orphan count and processing backlog.

## Decision rules

- User filenames are metadata, not trusted storage paths.
- Client MIME/extension alone never proves content type.
- Signed URLs must be short-lived and scoped to a specific action/object where possible.
- Public buckets are appropriate only for intentionally public data.
- Direct upload does not mean direct authorization; trusted code still decides what may be uploaded and where.
- Large/expensive processing belongs in async workers.
- Immutable/versioned media keys simplify CDN correctness.
- Deleting a database row does not guarantee object/derivative deletion; reconcile lifecycle explicitly.
- Do not proxy large media through application servers without a reason.

## Reference routing

Load `references/uploads-object-storage.md` for upload flows, validation, multipart/resumable behavior, object keys, quotas and lifecycle.

Load `references/signed-url-access.md` for private/public storage, signed upload/download URLs, tenant authorization and CDN caching.

Load `references/media-processing.md` for image/video/document validation, metadata, derivatives, processing safety and async pipelines.

Use `realtime-async` for worker/queue reliability, `database-data` for metadata/ownership schema, and `security` for malware/content abuse threat review.

## Quality gates

- Object classes and public/private boundaries are explicit.
- Object keys cannot be chosen to escape/collide with another tenant/resource.
- Size/type/content validation occurs at trusted boundaries.
- Private access is authorized before signed URL issuance.
- Expensive processing is resource-bounded and async where needed.
- CDN caching matches mutability/versioning.
- Retention/deletion/orphan cleanup is defined.
- Upload abuse/cost limits and monitoring exist for material risk.

## Failure handling

If provider upload/access semantics are unclear, inspect current official provider docs before relying on ACL defaults. If scanning/processing fails, keep the object quarantined rather than publishing it. If object deletion is partially unavailable, persist cleanup intent and retry/reconcile rather than silently orphaning sensitive data.

## Output contract

Return:

- storage/object classification;
- upload/validation/processing flow;
- access/signed URL policy;
- CDN/versioning strategy;
- lifecycle/quota/cost controls;
- tests/observability;
- async/database/security handoffs.
