# Interaction Patterns

Patterns are starting points. Choose by task, risk, frequency, data density and platform behavior; do not reproduce a design-system component because it exists.

## Forms

Use persistent labels, appropriate input types/autocomplete, useful defaults, clear required/optional rules, inline validation near the field and summary/focus behavior for complex errors. Preserve valid input after failure. Multi-step flows need progress only when it helps orientation and should allow safe back navigation.

For sensitive/destructive actions, use proportional confirmation: typed confirmation or reauthentication only when risk warrants it; avoid confirmation fatigue.

## Navigation

Prioritize recognition and stable orientation. Separate primary navigation from contextual tabs/subnavigation. Preserve high-value actions on mobile without crowding. Deep-linkable state belongs in URL when users need share/reload/back-forward semantics.

## Search, filter and sort

Make active filter state visible/reversible, reflect important state in URL, preserve context across results and define zero-result recovery. Faceting requires meaningful dimensions/count semantics. Avoid hidden complex filters for small catalogs and client-side filtering over incomplete datasets.

## Tables and data

Align by value type, keep units/context visible, support meaningful sorting/filtering, distinguish clickable row vs selectable row, provide bulk-action feedback and protect destructive operations. On narrow screens choose priority columns, horizontal scroll with context, detail views or alternate layout based on task—not automatic cards.

## Dialogs, drawers and popovers

Use modal/dialog for focused interruptive decisions, not routine navigation. Manage focus, background inertness, escape/close semantics and restoration. Avoid modal stacks. Drawers can preserve context for secondary detail but should not become a hidden full application.

## Menus/comboboxes

Prefer native controls when adequate. Custom combobox/menu/listbox must implement keyboard, focus, active-descendant/selection and screen-reader semantics correctly; coordinate with accessibility guidance.

## Optimistic UI

Use only when failure is uncommon and reversal/reconciliation is clear. Never show irreversible money/security success before authoritative confirmation. Distinguish pending from completed when provider/async state can lag.

## Feedback and status

Every action needs proportional feedback. Use local inline feedback for local changes; toasts for transient non-critical confirmation; persistent banners for ongoing/system status. Avoid toast-only errors that disappear before recovery.

## Empty/loading/error

Empty states should distinguish first use, no results, no permission and failed load. Loading indicators should not cause layout jumps or imply progress they cannot measure. Errors explain what happened at user level, preserve work and offer a next action when possible.

## Keyboard/touch/motion

All core functions need keyboard access, visible focus and adequate touch target. Drag/reorder needs alternatives when required. Motion should reinforce spatial/state changes and provide reduced-motion equivalents.
