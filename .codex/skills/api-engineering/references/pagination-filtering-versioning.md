# Pagination, Filtering, and Versioning

Collection APIs need deterministic behavior under growth and concurrent change.

## Pagination

Define a stable ordering before choosing pagination. Offset/page-number pagination is simple and acceptable for bounded/admin/reporting datasets where concurrent inserts are not a major correctness issue. Cursor/keyset pagination is usually better for large or frequently changing datasets because it avoids deep offsets and reduces duplicate/skip behavior.

Cursors should be opaque to clients unless the contract intentionally exposes their structure. Define maximum/default page sizes and invalid/expired cursor behavior. Do not fetch entire collections and paginate in application memory.

## Filtering and sorting

Expose only meaningful, supported filters/sorts. Validate operators and field names rather than dynamically translating arbitrary client input into queries. Define how multiple filters combine and whether search is exact, prefix, full-text, semantic, or provider-specific.

## Versioning

Prefer additive evolution and explicit deprecation before a new API version. Version when incompatible semantics cannot reasonably coexist. A versioning scheme may be path/header/media-type/schema based; consistency and migration tooling matter more than fashion.

Compatibility includes validation, defaults, nullability, enum behavior, ordering, pagination semantics, errors, and authorization—not only JSON field presence.

## Deprecation

Document replacement, migration steps, support window, telemetry/consumer usage when available, and removal criteria. Do not leave dead versions indefinitely without ownership.