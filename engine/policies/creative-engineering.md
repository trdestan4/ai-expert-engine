# Creative Engineering Policy

Creative ambition never waives production quality. Signature visuals are enhancements around a semantic, usable product surface.

## Required principles
1. **Intent before technique.** Creative direction and motion jobs exist before choosing GSAP, Three.js, shaders, or other runtimes.
2. **Evidence before fidelity claims.** Reference reconstruction labels observed/derived/hypothesis/unknown. “Pixel-perfect” requires authoritative assets/fonts/viewports and measurable criteria.
3. **Native-first escalation.** Use semantic HTML/CSS/browser capabilities when they express the same intent; introduce JS animation, canvas, WebGL, or shaders only for real value.
4. **One owner per runtime concern.** Avoid competing scroll authorities, animation loops, or multiple libraries writing the same properties.
5. **Lifecycle is correctness.** Timelines, listeners, render loops, GPU resources, render targets, decoders, and authored animation runtimes must be created/reverted/disposed by an explicit owner.
6. **Responsive art direction.** Mobile is allowed to recompose, shorten, substitute media, remove pins, and lower visual depth while preserving hierarchy and brand thesis.
7. **Reduced motion is designed.** Remove vestibular/spatial/perpetual motion while preserving content/state; also remove layout artifacts created only for the original sequence.
8. **Graceful failure.** Essential content/action survives failed video/3D/shader/animation initialization and unsupported capabilities.
9. **Measured budgets.** Network bytes, LCP/CLS/INP, CPU work, DPR, GPU fill, texture memory, draw calls, shader passes, and frame behavior are treated as different risks.
10. **Independent visual evidence.** High-fidelity/signature experiences receive reproducible visual QA in addition to functional, accessibility, and performance evidence.

## Creative experience contract
For C2+ creative implementation, or any material 3D/shader/pinned-scroll experience, produce a `creative-experience-plan` when project tooling supports it. It records signature moments, responsive/reduced-motion modes, runtime technologies, 3D lifecycle/fallback, budgets, and QA matrix. `scripts/creative_experience_checks.py` validates completeness; passing it is not subjective design approval or performance proof.

## Release blockers for creative surfaces
Treat the following as blockers proportional to scope: essential content inaccessible without the effect; scroll trapping/hijacking that blocks normal navigation; no reduced-motion path for material spatial motion; no fallback for required 3D initialization; repeated-route GPU/listener/timeline leaks; severe mobile performance failure; hidden content after animation failure; baseline updates that merely erase an unexplained regression; or unsupported fidelity claims presented as verified evidence.
