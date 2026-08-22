# Redis, Cache Data and Vector Storage

## Redis / ephemeral data

Use Redis for workloads matching its strengths: cache, rate-limit counters, ephemeral coordination, queue/pub-sub primitives, short-lived sessions, deduplication or fast derived views. Define TTL/eviction and failure behavior explicitly.

Do not treat cached data as authoritative unless persistence/replication and recovery requirements intentionally make Redis part of the source-of-truth architecture. Cache misses and Redis outages should have a defined degraded path.

Key design should encode namespace/tenant/version and avoid unbounded cardinality. Avoid wildcard key scans in request paths. Atomic counters/Lua/transactions may be needed for race-sensitive operations, but distributed locks require careful expiry/ownership semantics.

## Cache invalidation

State the freshness contract first: cache-aside, write-through, write-behind or event invalidation. Include invalidation after mutation, namespace/version bumps, negative caching, stampede prevention and maximum stale age.

## Vector/embedding data

Keep embeddings linked to the authoritative entity/version that produced them. Define model/provider/version, chunking/source metadata, deletion propagation, tenant isolation and re-embedding strategy.

Vector similarity is not authorization: filter candidate data by tenant/resource permissions using a trusted boundary. Do not leak cross-tenant documents because a vector index is queried globally.

## Privacy/lifecycle

Embeddings can encode sensitive source information. Apply retention/deletion and access controls to vector copies as well as source rows. Avoid embedding secrets or unnecessary personal data.

## Tests

Cover cache outage/miss/stale behavior, invalidation races, tenant key isolation, TTL expiry, stampedes, duplicate recomputation, vector deletion/re-embedding and cross-tenant retrieval attempts.