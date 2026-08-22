# Usage / Quotas / Metering

For every quota define what is counted, unit, scope (user/tenant), time window, reset rule, soft/hard limit, race semantics and user-visible explanation. Counters need atomicity or reservation when concurrent actions could exceed limits.

Usage-based billing requires durable, deduplicated usage events with stable IDs, timestamps and attribution. Aggregation should be reproducible enough to explain an invoice. Late events, retries, corrections and provider reporting need explicit handling.

Do not use analytics events as the only billing ledger. For costly resources, preflight estimates may improve UX but authoritative enforcement remains server-side. Track both allowed and rejected usage when useful for expansion signals.