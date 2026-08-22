# REST Contracts and OpenAPI

Use this reference for HTTP resource/operation design and machine-readable OpenAPI descriptions.

## Resource semantics

Model stable domain concepts and workflows, not tables. Use nouns/resources for representations and explicit command/action endpoints only when a state transition cannot be expressed clearly as ordinary resource manipulation. Method semantics, response codes, cacheability, conditional requests, and representation ownership must be consistent.

## Request/response design

Define required, optional, nullable, omitted, and default behavior explicitly. Avoid overloaded fields whose type/meaning changes by operation. Use stable identifiers and timestamps/formats with documented semantics.

## OpenAPI

The authoritative OpenAPI site currently publishes OAS 3.2.0 as the latest release. Do not upgrade an existing API merely because a newer spec exists; first verify the repository's validators, code generators, gateways, docs, and SDK tooling support the target version. An accurate 3.1/3.0 description is better than an unsupported 3.2 document.

Treat the description as a contract artifact. If code-first generation is used, inspect generated output for missing security schemes, nullability, unions, examples, error variants, and parameter constraints. If design-first is used, implementation and tests must detect drift.

## Compatibility

Adding a response field is usually additive but can still break rigid consumers; changing meaning, validation, enum assumptions, required fields, auth behavior, status codes, or pagination can be breaking. Document deprecation and migration rather than silently redefining an existing contract.