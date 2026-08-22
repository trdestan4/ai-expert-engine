# Frontend Quality Baseline

Run this before calling a substantial frontend implementation complete.

## Correctness

- Typecheck/lint/build relevant to the repository pass.
- Main interaction and data flows match acceptance criteria.
- Loading, empty, success, validation, recoverable error, and permission states are handled where applicable.
- Direct navigation/reload/back-forward behavior is correct for URL-driven state.

## Semantic/accessibility baseline

- Native controls are used for native behaviors.
- Keyboard access and visible focus work.
- Inputs have programmatic labels and useful errors.
- Images/media have appropriate alternative treatment.
- Dialog/menu/popover focus does not strand users.
- Reduced-motion preference is respected for nonessential motion.

## Responsive/content resilience

- No page-level horizontal overflow at narrow widths.
- Long/translated content does not destroy layout.
- Touch targets/spacing remain usable.
- Sticky/fixed elements do not cover essential content.
- Dense/empty/extreme data states remain understandable.

## Data/state

- One authoritative owner exists for each important state value.
- Independent requests are not serialized accidentally.
- Duplicate submissions/race conditions are handled where material.
- Client validation is not treated as server trust.

## Performance baseline

- Client boundaries and third-party JS are not broader than needed.
- Heavy offscreen media/features are not eagerly loaded without reason.
- Images reserve layout space.
- No obvious N+1 client requests or render loops are introduced.

## Security hygiene

- No server secret/API credential is shipped into public client code.
- Raw untrusted HTML is not rendered without an approved sanitization path.
- UI visibility is not used as authorization.
- Sensitive session/user data is not unnecessarily persisted/logged client-side.

## Testing

Choose tests that prove changed behavior. Critical conversion/auth/data-loss flows deserve broader integration/E2E evidence; small pure behavior can use focused tests.

If a deeper accessibility, security, or performance specialist review is required by risk, this baseline does not replace it.
