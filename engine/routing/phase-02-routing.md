# Phase 02 Routing — Web Engineering / Frontend

Use the smallest owner set that can complete the task safely. Phase 02 remains the default frontend implementation layer; Phase 10 activates for advanced creative runtime/visual boundaries only.

## Primary ownership
- Framework-independent HTTP/browser/runtime/cookie/CORS/storage/cache semantics → `web-platform`
- Semantic HTML, CSS, TypeScript, components, state/data/forms, responsive implementation → `frontend-engineering`
- React hooks/components and Next.js App Router/RSC/Actions/Handlers/cache/rendering/hydration → `react-nextjs`
- Application module boundaries, dependency direction, architecture trade-offs/migration → `software-architecture`

## Typical routes
**Implement approved marketing page in Next.js:** `frontend-engineering` → `react-nextjs`; load Phase 01 only for unresolved design and Phase 10 only for material advanced visual/motion/3D implementation.

**Build a reusable React component system:** `frontend-engineering` + `react-nextjs`; `ux-ui-design` only when component behavior/design contract is unresolved.

**Advanced masks/layered responsive creative section:** `frontend-engineering` for semantic/component boundary + `creative-frontend` for the advanced surface when needed.

**GSAP/ScrollTrigger sequence:** `animation-engineering`; add `frontend-engineering`/framework owner when component lifecycle/state integration is material.

**Three.js canvas/scene:** `threejs-webgl`; add `frontend-engineering` for page/component shell and `react-nextjs` only for actual framework runtime concerns.

**Cookie disappears after reload:** `debugging` → `web-platform`; add `react-nextjs` only when framework request/runtime handling is part of the proven cause.

**Hydration mismatch:** `debugging` → `react-nextjs`; add Phase 10 only if a creative runtime is proven to cause the mismatch.

**Choose app module structure:** `software-architecture` → `task-planning`; add specialists for implementation only.

**CSS/layout/responsive bug:** `frontend-engineering` unless the failure is specifically in a Phase 10 advanced composition.

## Overlap prevention
- `web-platform` explains standards/browser mechanisms; it does not own application component architecture.
- `frontend-engineering` owns normal production frontend; it does not become a GSAP, Three.js, shader, DCC pipeline, or visual-regression specialist.
- `react-nextjs` owns framework behavior and preserves contracts established by frontend/domain owners.
- `software-architecture` decides structural boundaries; it does not become detailed implementation owner.
- Phase 01 owns experience/design intent; Phase 02 implements normal product UI; Phase 10 owns advanced creative implementation/evidence and returns unresolved intent conflicts rather than silently redesigning.

## Token rule
Do not load all frontend/creative skills. A normal page usually uses Phase 02 only. A GSAP-only implementation can use `animation-engineering` plus one framework/frontend owner if integration requires it. A Three.js page should not activate `realtime-shaders` or `three-d-asset-pipeline` unless those boundaries are actually present.
