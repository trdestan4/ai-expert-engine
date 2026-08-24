# AI Expert Engine v1.4 — Master Hardened + Creative Engineering Expansion

AI Expert Engine is a token-efficient, production-grade expert system for Cursor/Codex-style coding agents. It routes work to narrow domain owners, separates diagnosis/implementation/review/release authority, preserves evidence for high-risk work, and now includes a dedicated creative-engineering layer for high-fidelity motion, 3D, shader, reference-reconstruction and visual-QA work.

## System shape
- **50 discoverable skills** under `.codex/skills/`
- **6 isolated Cursor reviewers** under `.cursor/agents/`
- deterministic repository profiling, routing, runtime contracts, checkpoints, review evidence and release gates
- official-source freshness registry and offline behavioral/reviewer/repository eval corpora
- installer/update/migration flow with drift protection and production release guard

## Phases
- **Phase 00 — Core / AI Brain:** orchestration, repository intelligence, planning, debugging.
- **Phase 01 — Creative / Product Intelligence:** product strategy, creative direction, brand, anti-generic design, color, typography, visual art direction, motion direction, UX/UI.
- **Phase 02 — Web Engineering / Frontend:** browser platform, frontend engineering, React/Next.js, software architecture.
- **Phase 03 — Backend / API Engineering:** backend, APIs, identity/access, integrations, realtime/async.
- **Phase 04 — Data / Platform:** database/data, storage/media, SaaS platform.
- **Phase 05 — Quality Engineering:** testing/QA, security, performance, accessibility, privacy/compliance, code quality.
- **Phase 06 — Business / Growth:** ecommerce, SEO, content/conversion.
- **Phase 07 — Production Engineering:** DevOps/deployment, observability/SRE, Git delivery, documentation.
- **Phase 08 — AI / Asset Production:** AI engineering and production visual assets.
- **Phase 09 — Final Control:** multi-review, audit-review, release-readiness.
- **Phase 10 — Creative Engineering Expansion:** design reconstruction/Design DNA, advanced creative frontend, GSAP/ScrollTrigger and web-motion engineering, Three.js/WebGL runtime, realtime shaders, web 3D asset pipeline, and evidence-based visual/motion QA.

## Phase 10 ownership
`motion-direction` remains the motion designer; `animation-engineering` owns implementation. `frontend-engineering` remains ordinary semantic/component frontend owner; `creative-frontend` owns advanced visual composition. `threejs-webgl` owns the browser 3D runtime, `three-d-asset-pipeline` owns DCC→glTF delivery, and `realtime-shaders` owns custom GPU effect code. `design-reconstruction` turns references into evidence-tagged design grammar; `visual-qa` proves the implementation against that authority.

Material creative experiences can use `engine/schemas/creative-experience-plan.schema.json` and `scripts/creative_experience_checks.py` to ensure responsive modes, reduced motion, 3D fallback/disposal, budgets and QA evidence are not forgotten. Passing this completeness check is not a substitute for real performance, accessibility, functional or visual evidence.

## Install / update
```bash
python scripts/enginectl.py install /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
python scripts/enginectl.py update /path/to/target-project
```

Repository profiling:
```bash
python scripts/profile_repository.py /path/to/target-project
python scripts/resolve_stack_profile.py /path/to/target-project --all
```

Creative experience plan completeness:
```bash
python scripts/creative_experience_checks.py path/to/creative-experience-plan.json
```

## Validation
CI runs every `scripts/validate_*.py` validator plus offline corpus/freshness/release-enforcement checks. Phase 10 has its own validator and behavioral cases covering reference reconstruction, GSAP lifecycle, Three.js disposal/fallback, shader boundaries, glTF optimization, creative CSS, reduced-motion 3D and visual regression.

## Core rule
Load the smallest expert set that changes the next decision or proves required evidence. “Premium”, “cinematic”, “Awwwards”, or “3D” never means load every creative specialist by default. Production quality, accessibility, native scroll control, lifecycle cleanup, responsive art direction, graceful fallbacks and measured budgets remain mandatory.
