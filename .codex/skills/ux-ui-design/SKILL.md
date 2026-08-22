---
name: ux-ui-design
description: Designs usable, responsive, accessible interface structure and interaction systems for web products across information architecture, flows, layouts, components, states, forms, navigation, content hierarchy, mobile behavior, and design-system foundations; it applies creative direction without sacrificing usability.
---

# Purpose

Turn product goals and creative direction into interfaces that are clear, efficient, responsive, scalable, and visually coherent across real content and interaction states.

## Use when

- a new page, flow, dashboard, ecommerce experience, or site structure needs UX/UI design;
- information architecture, navigation, hierarchy, layout, responsive behavior, or component patterns are unclear;
- a visual concept must be translated into usable screens;
- existing UI is inconsistent, confusing, dense, or visually weak;
- component/state/system foundations are needed before frontend implementation.

## Do not use when

- product outcome/audience is unresolved (`product-strategy` first);
- the task is purely brand identity (`brand-design`);
- only color, typography, imagery, or motion needs specialist work;
- implementation code is the primary deliverable (future frontend skills own it).

## Inputs

Use:

- product goals/user jobs;
- creative/brand direction;
- content inventory or representative content;
- required features and states;
- target devices/input contexts;
- accessibility requirements;
- technical constraints that affect interaction;
- known conversion/trust requirements.

## Workflow

### 1. Define user task hierarchy

Identify the primary task(s), supporting tasks, and low-priority actions. Interface prominence must follow task importance rather than stakeholder enthusiasm.

### 2. Design information architecture

Organize content/features by user mental model and journey. Define:

- global navigation;
- local/sub-navigation;
- page/route hierarchy;
- grouping and labels;
- search/filter needs;
- cross-linking/context recovery.

Avoid navigation labels that sound clever but hide meaning.

### 3. Design the user flow

For each high-value task, map entry → decision → action → success/recovery. Minimize unnecessary choices and repeated data entry. Include empty, loading, error, validation, permission, and success states where relevant.

### 4. Establish hierarchy before decoration

Define:

- content order;
- visual priority;
- primary/secondary actions;
- grouping;
- density;
- reading path;
- disclosure strategy.

The interface should remain understandable in grayscale/wireframe form.

### 5. Build layout system

Choose grid/container behavior based on content, not a fixed template. Define:

- max-width strategy;
- gutters/margins;
- column behavior;
- section rhythm;
- card/list/table usage;
- editorial vs application density;
- alignment rules;
- intentional full-bleed moments.

Avoid putting every piece of content inside a card.

### 6. Define component behavior

For relevant components specify:

- default;
- hover/focus/active;
- selected;
- disabled;
- loading;
- error;
- empty;
- success;
- destructive/confirmation behavior.

Components must encode hierarchy and semantics, not merely visual variants.

### 7. Design forms and conversion interactions

Use clear labels, appropriate input types, progressive disclosure, inline validation, useful errors, sensible defaults, and explicit completion feedback. Do not hide critical form context inside placeholders.

### 8. Design responsive behavior

Do not treat mobile as desktop stacked vertically. Decide what:

- reflows;
- reorders;
- collapses;
- becomes a different component;
- becomes sticky;
- moves to progressive disclosure;
- requires alternate imagery/layout.

Protect touch targets, text measure, checkout/forms, and navigation.

### 9. Apply creative direction

Use creative assets, typography, color, surfaces, and motion to reinforce hierarchy. Distinctiveness should be strongest in composition, branded content treatment, selected signature components, and transitions—not by making standard controls unfamiliar.

### 10. Prepare implementation handoff

Define component boundaries, tokens, responsive states, content constraints, key interactions, accessibility requirements, and edge cases necessary for frontend implementation.

## Decision rules

- User task clarity outranks decorative novelty.
- Familiar controls can live inside distinctive compositions.
- Cards are grouping tools, not default containers.
- Mobile requires re-composition, not only scaling.
- Use progressive disclosure when complexity is conditional, not to hide frequently needed information.
- Primary actions should remain visually stable across a flow.
- Empty/loading/error states are product states, not afterthoughts.
- Dense data interfaces need stronger hierarchy and scanning support, not simply more whitespace.
- Ecommerce/product pages should prioritize decision evidence, comparison, availability, price/value, and purchase confidence.

## Reference routing

Load `references/ux-ui-system.md` for IA, flow, hierarchy, responsive layout, components, states, and handoff.

Load `references/interaction-patterns.md` for forms, navigation, tables, search/filtering, overlays, feedback, and state behavior.

Use `creative-director` for unresolved visual thesis and `anti-generic-design` for template-like composition.

## Quality gates

- Primary user tasks are obvious.
- IA/labels match user intent.
- Main flows include failure/recovery states.
- Hierarchy works before decorative styling.
- Layout is content-driven and does not overuse cards.
- Responsive behavior is explicitly re-composed.
- Component states are complete.
- Accessibility and implementation constraints are visible in handoff.
- Creative expression does not obscure interaction conventions.

## Failure handling

If content is unavailable, use representative content ranges and state assumptions rather than designing around lorem ipsum proportions. If business goals conflict with usability, preserve the required outcome while reducing coercion/friction. If a distinctive concept makes controls unclear, keep the composition/brand language and restore familiar interaction affordances.

## Output contract

Return:

- user task/flow hierarchy;
- information architecture;
- page/layout strategy;
- component/state rules;
- responsive behavior;
- forms/navigation/interaction guidance;
- creative-direction application;
- accessibility/edge cases;
- frontend handoff requirements.
