# UX/UI System Reference

Design from user jobs and information relationships before styling. The system must survive real content, permissions, failure and responsive constraints.

## Sequence

1. primary user jobs and decision context;
2. information architecture/navigation model;
3. critical task flows and recovery;
4. content/action hierarchy;
5. layout/grid/density;
6. components and complete states;
7. responsive re-composition;
8. creative styling/brand expression;
9. implementation handoff and verification.

## Information architecture

Group by user mental model and task frequency, not internal org chart. Keep labels recognizable. For large products, distinguish global/product/workspace/context navigation and preserve orientation. Search is not a substitute for broken IA.

## Flow design

For each critical journey map entry, prerequisite, happy path, validation, permission denial, interruption, empty/stale states, destructive consequences, confirmation/recovery and completion. Minimize repeated entry and irreversible surprises.

## Layout and density

Choose grids from content relationships. Use cards only when content benefits from independent grouping/surface behavior. Dense operational UI may need tables, split views, sticky context and progressive detail; marketing/editorial UI may use stronger spatial rhythm. Avoid universal rounded-card shells.

## Responsive recomposition

For each major region decide: preserve, reflow, reorder, collapse, transform component, progressive disclosure, sticky, alternate imagery or remove non-essential enhancement. Mobile is not desktop stacked vertically. Test narrow widths, short viewport height, safe areas, touch targets, keyboards and long localized text.

## State completeness

Relevant components/flows consider default, hover, focus, active, selected, disabled, loading/skeleton, empty, error, offline/retry, success, destructive confirmation, permission/availability and partial-data states. Skeletons must reflect realistic shape and not mask long waits.

## Forms

Persistent labels, useful defaults, input purpose/types/autocomplete, server-authoritative validation, field-level + summary errors when needed, preserved user input and proportional confirmation. Separate validation errors from system failures.

## Data-heavy UI

Optimize scanning and comparison: alignment, density, column priority, sorting/filtering state, pagination/virtualization based on data size, bulk selection, sticky context and responsive alternatives. Do not convert every table row into a giant card on mobile without testing the actual task.

## Design system boundary

Components encode repeated behavior/state, not every one-off composition. Prefer semantic tokens and composition over boolean-prop explosion. Allow signature marketing/product compositions without forcing them into generic components.

## Handoff

Specify component boundaries, tokens, content limits, states, interactions, accessibility expectations, responsive rules, analytics semantics where relevant and edge cases. Handoff should explain behavior/invariants, not just measurements.
