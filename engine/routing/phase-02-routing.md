# Phase 02 Routing — Web Engineering / Frontend

Use the smallest owner set that can complete the task safely.

## Primary ownership

- Framework-independent HTTP/browser/runtime/cookie/CORS/storage/cache semantics → `web-platform`
- Semantic HTML, CSS, TypeScript, components, state/data/forms, responsive implementation → `frontend-engineering`
- React hooks/components and Next.js App Router/RSC/Actions/Handlers/cache/rendering/hydration → `react-nextjs`
- Application module boundaries, dependency direction, architecture trade-offs/migration → `software-architecture`

## Typical routes

**Implement approved marketing page in Next.js:** `frontend-engineering` → `react-nextjs`; load Phase 01 skills only if an unresolved design decision appears.

**Build a reusable React component system:** `frontend-engineering` + `react-nextjs`; `ux-ui-design` only when component behavior/design contract is unresolved.

**Cookie disappears after reload:** `debugging` → `web-platform`; add `react-nextjs` only when framework request/runtime handling is part of the proven cause.

**Hydration mismatch:** `debugging` → `react-nextjs`; add `web-platform` only for browser/runtime evidence outside framework behavior.

**Choose app module structure before a major feature:** `software-architecture` → `task-planning`; add frontend specialists only for implementation.

**CSS/layout/responsive bug:** `frontend-engineering` only unless approved UX intent is ambiguous.

**“Make this page faster”:** use baseline Phase 02 rules for obvious structural issues, but formal performance audit/optimization routes to the later performance phase.

## Overlap prevention

- `web-platform` explains standards/browser mechanisms; it does not own application component architecture.
- `frontend-engineering` owns framework-neutral implementation and quality; it does not invent React/Next runtime semantics.
- `react-nextjs` owns framework-specific behavior but must preserve the frontend/component contracts established by `frontend-engineering`.
- `software-architecture` decides structural boundaries; it does not become the detailed implementation owner.
- Phase 01 owns experience/design intent; Phase 02 implements it and returns unresolved design conflicts rather than silently changing the direction.

## Token rule

Do not load all four skills for ordinary frontend work. Typical tasks use one primary skill plus at most one adjacent specialist. `software-architecture` is for material structural decisions, not every new folder/component.
