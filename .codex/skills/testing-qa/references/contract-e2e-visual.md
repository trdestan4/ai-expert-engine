# Contract, E2E, Browser and Visual Testing

## Contract testing

Protect public/internal APIs, events and provider adapters against accidental breaking changes. Validate schema plus semantics that matter: required/optional behavior, error model, pagination/order, idempotency, version/coexistence and backward-compatible additions. Consumer-driven contracts are useful when independently deployed consumers evolve at different speeds.

## E2E strategy

Keep E2E focused on high-value journeys and risky integration points: auth/recovery, checkout/payment, critical creation/edit flow, tenant boundaries, destructive actions, migration/coexistence. E2E should run against a production-like build/runtime when framework behavior differs from dev.

Avoid E2E suites that duplicate every unit edge case. Prefer stable test IDs/accessible roles over brittle DOM/CSS selectors.

## Browser/device matrix

Choose from actual user/support requirements: engine families, mobile/desktop, touch/keyboard, viewport/zoom, reduced motion, locale/RTL and lower-end performance. Do not test every browser version mechanically; cover materially different behavior and supported policy.

## Visual regression

Use visual snapshots for layout/component/state regressions that DOM assertions miss. Include deterministic fonts/data/animations and meaningful viewports. Review diffs rather than auto-updating baselines. Visual snapshots cannot prove usability, semantics or accessibility.

## Accessibility in tests

Automated axe-like checks catch a subset. Add keyboard/focus tests for interactive components and targeted screen-reader/manual verification for complex widgets/critical flows. Use semantic roles/names as test selectors when it improves both accessibility and resilience.

## Test environment

Control provider sandbox modes, feature flags, seeds, time and callbacks. Clean up or isolate tenant/data state. A test that passes because it hits a different environment/provider mode than production is false confidence.
