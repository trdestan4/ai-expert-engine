# GraphQL Contracts

Use this reference when the API contract is GraphQL rather than REST.

## Specification and tooling

The latest stable GraphQL specification is the September 2025 edition; a newer working draft may exist. Use only features supported by the repository's GraphQL server, schema tooling, code generation, and clients. Draft features must not be assumed production-ready.

## Schema design

Model domain capabilities rather than mirroring database tables. Prefer clear object/input types, consistent nullability, purposeful mutations, and stable identifiers. Nullability is a compatibility and runtime contract: tightening or loosening it can affect clients and error propagation.

## Execution behavior

Resolvers must not hide N+1 query patterns. Batch/cache per request where appropriate, but do not let DataLoader-style caching become cross-request stale state accidentally. Keep resolver transport logic thin enough that domain/service rules remain reusable.

## Authorization

Authentication/authorization still applies at field/object/action boundaries. Do not rely on the client omitting sensitive fields. Route policy design to the identity/security layer while ensuring resolver execution enforces it.

## Cost and abuse

For public/high-volume APIs, control query depth/complexity, expensive fields, pagination, introspection exposure according to the threat/product model, and subscription fan-out. Persisted operations may help performance/allow-listing but are not a universal replacement for authorization.

## Evolution

Prefer additive fields/types and deprecation over removal. Monitor usage before removing deprecated fields where possible. Schema registry/check tooling should detect breaking changes before release.