# Privacy Data Map and Minimization

Privacy engineering begins with knowing what data exists, why, where it flows and who can access it. This is engineering guidance, not legal advice.

## Inventory

For each material data category record: source, subject, purpose, sensitivity/classification, fields/identifiers, collection trigger, storage systems/regions, processors/subprocessors, access roles, sharing/export, retention, deletion propagation, backup/log/cache/vector/derived copies and security controls.

Map data through browser/mobile → API → database/storage → queues/jobs → analytics/logs → third parties. Hidden copies often live in error logs, data warehouses, support tools, search indexes, embeddings/vector stores, CDN caches and backups.

## Minimization

Collect only fields needed for a defined purpose or clear near-term obligation. “Maybe useful later” is not a purpose. Prefer coarse/ephemeral data when it answers the same question. Avoid exposing sensitive identifiers in URLs/query strings, analytics event names, logs or support screenshots.

Separate authentication identifiers, profile data, billing records, analytics and marketing tracking; they commonly have different purpose/retention/access semantics.

## Purpose and access

Document authorized use, not merely who can query the table. Restrict internal/admin access by role/job and audit sensitive access when risk warrants it. Secondary use (training, marketing, product analytics) may require separate evaluation/consent/legal basis—verify jurisdiction-specific requirements rather than assuming.

## Derived data and AI

Embeddings, inferred attributes, scores and generated summaries can remain personal/sensitive even if raw text is not displayed. Tie derived artifacts to source-entity lifecycle, tenant isolation, retention and deletion/re-embedding strategy.

## Quality gate

A new personal-data field should have owner, purpose, source, access boundary, retention/deletion behavior and downstream processors before production. If those are unknown, escalate rather than silently storing forever.
