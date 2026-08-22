# React Runtime and Component Patterns

Apply only after confirming the repository's React version and local conventions.

## Components and ownership

Keep render functions pure. Put side effects in explicit event/effect boundaries. Prefer composition over inheritance/configuration matrices.

Do not define component functions inside other component render functions when identity/state preservation matters. Hoist stable static structures when it improves readability/performance.

## State and derived values

Store the minimum authoritative state. Derive booleans, filtered lists, totals, labels, and other deterministic values during render unless the computation is genuinely expensive.

Prefer functional state updates when the next value depends on the previous value. Use refs for mutable transient values that should not trigger rendering.

## Effects

Use effects for synchronization with external systems. Before writing one ask whether the logic belongs in:

- render derivation;
- an event handler;
- the data layer;
- a framework server boundary.

Keep dependencies accurate rather than suppressing lint rules. Split effects with unrelated lifecycles.

## Render performance

Optimization priority:

1. remove unnecessary client work/data;
2. avoid async waterfalls;
3. reduce bundle/client boundary size;
4. isolate frequently changing state;
5. profile actual rerender/render bottlenecks;
6. memoize only when cost/identity warrants it.

Do not blanket `memo`, `useMemo`, and `useCallback` across simple code.

For non-urgent expensive updates, React concurrency primitives such as transitions/deferred values may keep input responsive when supported by the installed version.

## Async behavior

Start independent promises early and await late. Use Suspense around meaningful independent reveal units where the framework/runtime supports the data pattern.

Avoid component nesting that forces otherwise-independent requests to wait for parents unnecessarily.

## Context and shared state

Keep context values focused and stable. Do not put unrelated rapidly-changing state into one app-wide provider. Prefer colocated/local ownership first.

## Client/server boundary

In frameworks with Server Components, client components still follow these rules but should receive the minimum serialized data required. Keep browser interactivity in narrow client islands when practical.

## Verification

Test actual user interactions, state transitions, effect cleanup, error/loading behavior, and rerender hot paths when performance is material. Compiler/lint success is not enough to prove lifecycle correctness.
