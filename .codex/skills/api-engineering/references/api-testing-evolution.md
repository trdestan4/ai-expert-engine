# API Testing and Evolution

API testing should prove the consumer contract, not only handler implementation.

## Contract tests

Validate representative requests/responses against the machine-readable schema where available. Test required/optional/null behavior, enum/format constraints, error shapes, auth-sensitive responses, pagination boundaries, filtering/sorting semantics, duplicate requests, and rate-limit behavior relevant to consumers.

## Compatibility

Compare schema/contracts before release and classify additive, behavior-changing, and breaking changes. Generated OpenAPI diffs or GraphQL schema checks are useful but not sufficient: changing defaults, validation strictness, ordering, status codes, error codes, or authorization may break consumers without obvious structural changes.

## Consumer confidence

For high-value integrations, maintain consumer-driven or representative integration tests rather than assuming generated clients prove server behavior. Verify SDK/code-generation output when the contract is used to generate clients.

## Deprecation lifecycle

A deprecation should identify replacement, migration path, support window, and removal criteria. When possible, measure remaining use before removal. Do not silently repurpose deprecated fields/endpoints for new semantics.

## Release sequencing

For producer/consumer deployments, prefer backward-compatible server changes before consumers depend on them, then remove old behavior only after migration. For schema or auth changes that require coordinated rollout, define the compatibility window explicitly.

## Failure evidence

If production behavior differs from specification, treat it as contract drift. Decide whether runtime or specification is authoritative for existing consumers, then reconcile through a safe migration rather than changing one side blindly.