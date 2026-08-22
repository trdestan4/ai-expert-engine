# Semantic HTML, CSS, and TypeScript

## Semantic HTML

Build structure from meaning and native behavior before visual wrappers.

- Use one coherent document heading hierarchy rather than sizing headings by appearance.
- Use `button` for actions and `a` for navigation.
- Use `label` relationships and native input types for forms.
- Use lists/tables only when content semantics match them.
- Use landmark elements where they improve navigation and structure.
- Preserve native keyboard/focus/form behavior unless a product requirement truly needs a custom interaction.

Avoid div/button emulation, duplicated interactive nesting, invalid table/list markup, and clickable elements without keyboard/focus semantics.

## CSS architecture

Choose the repository's established styling system unless it prevents the requirement. Organize CSS around tokens, layout primitives, component states, and intentional exceptions.

### Token layers

Prefer separating raw scales from semantic decisions:

- raw: color/size/type values;
- semantic: `text-primary`, `surface-raised`, `space-section`, `action-primary`;
- component: only when a component has a stable local contract.

Do not tokenize every arbitrary number. Tokens should encode reusable decisions.

### Layout

Prefer normal flow, Grid, Flexbox, container/media queries, intrinsic sizing, `min/max/clamp`, and logical properties before absolute positioning or JS measurement.

Treat `z-index` as a layer system rather than escalating integers.

Use fluid constraints where content can vary; avoid fixed heights for text-rich components.

### Cascade/specificity

Keep selectors locally understandable. Avoid `!important` as routine conflict resolution. Prefer explicit variants and predictable layer/order conventions over specificity battles.

## TypeScript

Types should make invalid states difficult to represent.

Prefer:

- explicit public props/interfaces;
- discriminated unions for mutually exclusive UI states;
- narrow event/data types;
- schema-derived types at validated boundaries when available;
- exhaustive switches for finite state machines;
- `unknown` + validation/narrowing over unsafe `any`.

Do not duplicate backend/database entity shapes as UI contracts when the UI needs a smaller or differently shaped model.

## Component contracts

A reusable component contract should define:

- semantic role;
- required/optional content;
- behavioral states;
- controlled/uncontrolled ownership if relevant;
- responsive/content constraints;
- accessibility expectations;
- extension points.

Avoid prop matrices that allow nonsensical combinations. Split variants/components when behavior diverges materially.
