# SQL, Indexes and Query Plans

## Query design

Select only needed columns, keep predicates sargable where possible, avoid accidental N+1 access patterns, and understand join cardinality before optimizing syntax. Measure representative production-shaped data rather than tiny fixtures.

## Index selection

Indexes should correspond to real filters, joins, ordering and uniqueness requirements. Consider column order, equality versus range predicates, partial indexes for selective subsets, covering/index-only opportunities, and expression indexes when the expression is stable and truly queried.

Every index adds write, vacuum and storage cost. Remove redundant indexes only after checking constraint/foreign-key and workload requirements.

## Plans

Use `EXPLAIN` to inspect estimated strategy and `EXPLAIN ANALYZE` when executing the query is safe. Compare estimated versus actual row counts to detect statistics/selectivity problems. Look for sequential scans that are actually problematic, expensive sorts, repeated nested-loop work, spill, and poor join order.

Do not treat a sequential scan as automatically bad; small or high-selectivity tables may make it optimal.

## Pagination

Offset/limit is simple and useful for shallow pages but degrades with deep offsets and can be unstable under writes. Keyset/cursor pagination requires a deterministic ordering key and clear next/previous semantics but scales better for large ordered collections.

## Optimization order

First confirm the query is semantically correct, then reduce unnecessary work/data, then fix schema/index/statistics problems, and only then consider caching. Caching a pathological query hides rather than removes cost.