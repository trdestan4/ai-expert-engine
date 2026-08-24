---
name: design-reconstruction
description: Reconstructs observable design systems from screenshots, recordings, reference sites, or design exports into evidence-tagged layout, token, typography, component, responsive, and motion rules without pretending hidden implementation details or unsupported pixel-perfect fidelity are known.
---

# Purpose
Turn visual references into an explicit, reusable design grammar that another specialist can implement and verify. Separate what is observed from what is inferred so reference-driven work does not devolve into guesswork or screenshot tracing.

## Use when
- a user provides screenshots, a reference site, video, or design export and wants the visual language understood;
- an existing product must be reconstructed from incomplete design artifacts;
- a team needs design tokens, layout rules, component grammar, responsive hypotheses, or state inventory extracted from evidence;
- fidelity must be measured across multiple viewports rather than judged from memory.

## Do not use when
- the project needs an original creative direction with no reference (`creative-director`);
- the design system is already documented and only implementation is needed (`frontend-engineering` or `creative-frontend`);
- the task is merely visual regression after implementation (`visual-qa`);
- copying protected brand assets, proprietary text, or distinctive expression is the goal rather than learning structural principles.

## Inputs
Collect the highest-quality available screenshots, viewport dimensions, recordings, URLs/design exports where authorized, brand/product constraints, real content, target breakpoints, known fonts/assets, interaction states, and fidelity expectations. Mark missing evidence instead of silently inventing it.

## Workflow
### 1. Build an evidence ledger
For every claim tag it as **observed**, **derived**, **hypothesis**, or **unknown**. Record viewport, state, source, and confidence. A single desktop screenshot cannot prove mobile behavior, hover logic, sticky thresholds, or exact type metrics.

### 2. Recover composition and geometry
Measure container behavior, columns, gutters, alignment anchors, section rhythm, whitespace ratios, overlap, crop rules, edge language, z-order, and likely fluid/fixed relationships. Prefer relationships such as `max-width`, min/max/clamp behavior, aspect ratio, and grid tracks over memorized pixels.

### 3. Recover visual tokens
Extract color roles, surface hierarchy, borders, radii, shadows, typography roles, scale relationships, icon treatment, image treatment, and spacing families. Distinguish semantic roles from one-off values.

### 4. Recover component grammar and states
Identify repeated primitives and composites, their variants, interaction states, content constraints, and responsive transformations. Include empty/loading/error/disabled/focus states only when evidenced or explicitly required; otherwise mark them as design work still needed.

### 5. Recover motion and spatial behavior
From recordings or runtime observation, identify trigger, start/end state, duration/easing character, scroll relation, pin/sticky behavior, depth, continuity, and reduced-motion needs. Motion implementation remains `animation-engineering`; this skill describes evidence and intent.

### 6. Produce a Design DNA contract
Create a compact structured record containing evidence, tokens, layout rules, components, responsive rules, media treatment, motion observations, unknowns, and confidence. Use `references/design-dna-contract.md` for the contract.

### 7. Hand off by boundary
Use `ux-ui-design` when missing states or interaction logic require design; `creative-frontend` for advanced visual implementation; `animation-engineering` for motion code; `threejs-webgl` for 3D runtime; `visual-qa` to measure the implemented result.

## Decision rules
- Never claim exactness that the evidence cannot support.
- Relationship fidelity matters more than blindly copying isolated pixel values.
- Multi-viewport evidence outranks a single screenshot.
- Hidden implementation technology is unknown until repository/runtime evidence proves it.
- Reference analysis may inspire principles; do not reproduce protected assets, text, or brand identity without permission.
- Preserve accessibility and product semantics even when the reference is weak in those areas.
- Responsive behavior is reconstructed from evidence or explicitly redesigned, never guessed and labeled as observed.

## Reference routing
Load `references/reference-analysis.md` for measurement, confidence, multi-viewport inference, and interaction evidence.
Load `references/design-dna-contract.md` for the structured design grammar, token, component, responsive, and handoff contract.

## Quality gates
- Every important claim has evidence/confidence status.
- Layout is described as relationships and constraints, not a bag of coordinates.
- Tokens are semantic enough to survive more than one page.
- Component/state inventory is explicit.
- Responsive behavior distinguishes observed rules from hypotheses.
- Motion observations include trigger and state, not only adjectives.
- Unknowns are visible and routed rather than fabricated.
- Implementation can be evaluated by `visual-qa` against the same evidence.

## Failure handling
If references conflict, preserve both observations and identify the condition that may explain the difference. If viewport or font evidence is missing, state the resulting uncertainty. If exact reproduction would require protected assets or inaccessible behavior, preserve the structural intent and create an original compliant implementation path.

## Output contract
Return evidence ledger, confidence map, design DNA, layout/token/component rules, responsive and motion observations, unknowns, implementation handoffs, and measurable fidelity criteria.
