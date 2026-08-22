# Types, Errors and Dependency Hygiene

Use the type system to encode meaningful domain states and prevent invalid combinations where practical. Avoid broad `any`, unchecked casts and generic string flags when a narrower union/schema can preserve intent. Static types do not validate untrusted runtime data.

Error handling should preserve useful internal context while exposing stable safe public errors. Avoid catch-and-ignore patterns, ambiguous `null/false` sentinels and logging the same failure at many layers. Decide which layer owns retry, fallback, translation and user messaging.

Prefer explicit return types/contracts at public module boundaries when they improve stability and reviewability. Keep side effects visible rather than hidden inside innocently named helpers.

Dependencies carry maintenance, security, bundle/runtime and upgrade cost. Before adding one, check whether the platform/framework/repository already provides the needed capability. Pin/lock according to repository policy and remove duplicate/abandoned libraries intentionally.

A type assertion, suppression or dependency exception should explain why the invariant is safe and what evidence/owner protects it.