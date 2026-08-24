# Phase 10 Routing — Creative Engineering Expansion

Phase 10 owns specialist implementation/evidence boundaries that are intentionally deeper than ordinary frontend or creative direction. Use the smallest set.

## Primary ownership
- Reference screenshots/sites/recordings → evidence-tagged reusable design grammar → `design-reconstruction`
- Advanced CSS, layered visual composition, responsive art direction, sticky/scroll DOM architecture, media treatment → `creative-frontend`
- GSAP/ScrollTrigger, CSS/WAAPI/View Transitions, Lottie/Rive/SVG timeline/runtime implementation → `animation-engineering`
- Three.js scene/renderer/camera/light/material/loaders/interaction/postprocessing/lifecycle → `threejs-webgl`
- GLSL/Three shader-node/custom realtime GPU effect math/pipelines → `realtime-shaders`
- Blender/DCC → glTF/GLB, PBR/UV/animation, KTX2/geometry compression/LOD web asset optimization → `three-d-asset-pipeline`
- Screenshot/reference/regression fidelity and motion/3D visual verification → `visual-qa`

## Typical routes
**Reference site, recreate the design language:** `design-reconstruction` → `creative-director` only if a new/adapted thesis is needed → `ux-ui-design` → `creative-frontend` → `visual-qa`.

**Awwwards-style scroll marketing page:** `creative-director` → `motion-direction` → `creative-frontend` + `animation-engineering` → `performance` + `accessibility` as material → `visual-qa`.

**3D product hero driven by scroll:** `visual-art-direction`/`motion-direction` as needed → `three-d-asset-pipeline` for source assets → `threejs-webgl` → `animation-engineering` for scroll timeline bridge → `realtime-shaders` only if custom GPU effects are required → `performance` + `visual-qa`.

**GSAP bug/duplicate ScrollTriggers:** `debugging` → `animation-engineering`; add `frontend-engineering` or framework owner only when component lifecycle/state is part of the proven cause.

**GLB is huge/slow before rendering:** `three-d-asset-pipeline`; add `threejs-webgl` only for runtime loader/decoder evidence.

**Three.js route leaks memory:** `debugging` → `threejs-webgl`; use `performance` for measured impact and `three-d-asset-pipeline` only if asset structure contributes.

**Custom distortion/shader:** `realtime-shaders` + `threejs-webgl` when integrated in a Three scene; do not activate shader expertise for normal PBR material tuning.

**Pixel-perfect request:** `design-reconstruction` defines evidence/authority → implementation owners → `visual-qa`; never promise pixel-perfect from incomplete assets/viewports/fonts.

## Overlap prevention
- `motion-direction` owns motion intent/choreography; `animation-engineering` owns code/runtime.
- `ux-ui-design` owns interaction/layout design; `creative-frontend` owns advanced visual frontend implementation.
- `frontend-engineering` remains owner of ordinary semantic/component/state work; Phase 10 activates only when specialist visual/runtime depth is material.
- `threejs-webgl` owns runtime; `three-d-asset-pipeline` owns the exported asset; `realtime-shaders` owns custom GPU math/effect code.
- `design-reconstruction` analyzes evidence; `visual-qa` verifies the implemented result.
- `visual-qa` never replaces functional `testing-qa`, `accessibility`, or `performance` evidence.

## Mandatory cross-checks
Material signature motion/3D/shader pages require explicit reduced-motion/fallback behavior. Production 3D must define lifecycle/disposal and mobile performance strategy. Reference-driven work must label observed vs inferred rules. Baseline updates in visual regression require intentional-change evidence.

## Token rule
Do not load all Phase 10 skills for a creative page. A GSAP-only page usually needs `animation-engineering` plus its intent owner. A standard marketing page may need none of Phase 10. The master should activate a Phase 10 owner only when that boundary changes the next decision or acceptance evidence.
