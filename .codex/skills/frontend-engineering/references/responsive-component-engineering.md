# Responsive and Frontend Quality

## Responsive engineering

Treat breakpoints as points where the composition stops working, not as a fixed device taxonomy. Start with content constraints and choose reflow rules that remain valid across widths.

Explicitly test:

- 320px-class narrow widths;
- wide desktop containers;
- long headings/names/prices;
- translated text expansion;
- 200% text zoom where applicable;
- empty/one-item/many-item states;
- touch and keyboard input;
- reduced motion;
- landscape/short viewport when sticky UI exists.

Use local horizontal scrolling for genuinely tabular/timeline content only when reflow would destroy meaning. Avoid page-level horizontal overflow.

## Component engineering

A component should have one understandable responsibility and a small valid API. Prefer composition and slots/children over boolean prop explosions.

Split components when:

- state lifecycles are independent;
- one part can render on a different server/client boundary;
- reuse is meaningful and stable;
- tests or ownership become clearer.

Do not split purely to satisfy line-count folklore.

## Content resilience

Design for real content, not screenshot-perfect placeholders. Define truncation/wrapping only where product meaning permits it. Preserve important identifiers, prices, availability, errors, and primary actions.

Images need aspect-ratio/crop rules and intrinsic dimensions where possible. Loading placeholders should not cause large layout shifts.

## Baseline accessibility

At implementation time verify:

- semantic controls/landmarks;
- keyboard path and visible focus;
- labels/names/descriptions;
- meaningful image alternatives;
- dialog/menu focus ownership when used;
- status/error announcement where needed;
- reduced-motion respect;
- touch targets and contrast consistent with the approved design.

A later accessibility specialist can perform full WCAG review; do not defer obvious defects.

## Baseline performance

Avoid structural costs before measurement:

- unnecessary client JavaScript;
- sequential independent requests;
- giant client state/provider boundaries;
- importing whole libraries for tiny utilities;
- eagerly loading offscreen heavy media/components;
- layout thrashing/JS-driven layout where CSS suffices.

Measure before deeper optimization.

## Baseline security hygiene

- Never embed server secrets into client bundles.
- Treat all browser input/state as untrusted at server boundaries.
- Avoid rendering unsanitized HTML.
- Do not rely on hidden/disabled UI as access control.
- Avoid logging sensitive tokens/user data in browser telemetry.

Deeper policy belongs to the security phase.

## Test selection

Prefer the smallest test that proves the changed contract:

- pure logic → unit;
- component interaction → component/integration;
- route/data integration → integration;
- critical user journey → E2E.

Avoid snapshot-only coverage for behavior-rich components.
