# State, Data, and Forms

## State ownership matrix

Choose ownership before library:

| State kind | Default owner |
| --- | --- |
| transient UI (open/hover/draft toggle) | local component |
| shareable/navigation/filter/page state | URL/search params |
| authoritative remote entities | server-state/cache layer |
| form draft/touched/errors | form state |
| cross-feature durable client-only state | shared store only when justified |
| derived value | derive from authoritative state |

Avoid copying the same value into URL + component + global store + query cache.

## Remote data

Define the contract before hooks/components:

- identity/key of the resource;
- freshness/staleness expectation;
- initial/loading/empty/error/partial state;
- refetch trigger;
- mutation effect;
- optimistic or pessimistic behavior;
- cancellation/race behavior;
- invalidation/update strategy.

Server-state libraries are useful when browser-side caching/revalidation is genuinely needed; they are not mandatory wrappers around every request.

## Effects

Effects are for synchronizing with systems outside React/component calculation: subscriptions, browser APIs, imperative widgets, timers, network behavior not owned elsewhere. Do not use effects to compute derived values, mirror props into state, or implement event logic that belongs in the event handler.

## Mutations

For a mutation define:

1. validate client input for fast feedback;
2. send through the authoritative server boundary;
3. show pending state without duplicate submission;
4. map field/form/business errors intentionally;
5. update/invalidate local server state;
6. recover/rollback optimistic UI if used;
7. preserve enough user input to correct recoverable errors.

Never treat disabled buttons or client checks as authorization.

## Forms

Use meaningful labels, descriptions, autocomplete/input modes/types, keyboard-compatible controls, and field grouping. Distinguish:

- syntax/format validation;
- domain/business validation;
- authorization/availability checks;
- server/infrastructure errors.

Do not show all failures as “Something went wrong.”

Validate on a cadence appropriate to the field; aggressive validation on every keystroke can create noise. Always validate authoritatively on the server boundary.

## Error model

Map errors to the smallest useful recovery scope:

- field error → near field;
- form/business error → form summary/context;
- recoverable data load → local retry;
- route/page failure → boundary/fallback;
- unexpected programming error → observability + safe user fallback.

Do not expose internal stack traces or raw server error objects in UI.

## Verification

Test slow responses, duplicate action attempts, empty results, stale data, out-of-order requests when possible, server validation failure, offline/network failure, back/forward URL behavior, and successful recovery without losing user work.
