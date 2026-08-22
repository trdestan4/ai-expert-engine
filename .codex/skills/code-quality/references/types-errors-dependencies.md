# Types, Errors, Static Analysis and Dependencies

## Types and runtime trust

Use types to make invalid internal states harder to represent, but remember external input, JSON, environment variables, database/provider payloads and persisted legacy data require runtime validation. Avoid broad `any`, unchecked casts or non-null assertions used only to silence tooling.

Model discriminated states for async/workflows rather than independent booleans that allow impossible combinations. Keep domain identifiers distinct when accidental mixing is costly.

## Error discipline

Preserve cause/context and classify errors at boundaries: invalid input, unauthorized/forbidden, conflict/invariant, not found, transient dependency, internal bug. Do not blanket catch-and-return-null. Translate errors once at the right boundary and avoid leaking stack traces/secrets to users.

Retries require an error class/operation safe to retry; “catch all and retry” can duplicate payments/mutations.

## Static analysis

Enable language/compiler strictness appropriate to the repo and fix root causes rather than suppression. Lint rules should target defects/consistency with low false-positive cost. Security/static tools need triage ownership; disabling a noisy rule globally may hide real findings.

## Dependency hygiene

Add dependencies only when value exceeds maintenance/security/bundle/runtime complexity. Prefer existing repository capability when adequate. Review version compatibility, transitive graph, license/policy, install scripts and ecosystem health. Pin/lock according to repo conventions and remove unused dependencies.

## Generated code

Separate generated from hand-edited code, define source generator/version and regenerate deterministically. Do not hand-patch generated output unless the workflow explicitly supports it.
