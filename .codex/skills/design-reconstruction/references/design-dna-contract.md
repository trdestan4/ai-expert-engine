# Design DNA Contract

The Design DNA is a compact, implementation-neutral description of the visual and interaction system recovered from evidence. It is not a dump of CSS values and not a claim that the original source code is known.

## Required sections

### Evidence
List each source with viewport/state and confidence. Keep unresolved discrepancies. The contract should make it possible for a reviewer to ask “which reference proves this rule?”

### Foundations
Describe canvas/surface model, density, grid/container strategy, spacing rhythm, shape language, border/shadow behavior, and depth/compositing rules. Prefer semantic constraints such as “content column caps while media bleeds to viewport edge” over coordinates.

### Color
Define semantic roles and mode behavior. Include transparency/overlay logic and media interactions. Hex values may be included when measured or approved, but semantic purpose is mandatory.

### Typography
Define roles for display, headings, body, labels, metadata, numeric/data, and controls as applicable. Record family only when known; otherwise specify measurable characteristics and a fallback plan. Include fluid scale, line-height, measure, tracking, weight range, and wrapping constraints.

### Components
For each repeated component record purpose, anatomy, variants, states, content limits, alignment, media behavior, and responsive transformation. Distinguish primitives from page-specific compositions so implementation does not over-componentize unique editorial moments.

### Responsive rules
Represent breakpoints as behavior transitions: reflow, reorder, hide/replace, crop change, navigation change, pin removal, density reduction, or control substitution. Identify which are observed versus proposed. Mobile must preserve the concept through recomposition rather than automatic stacking.

### Motion
Record motion jobs, trigger/state relationship, tempo/easing character, intensity level, scroll dependency, reduced-motion equivalent, and signature moments. Technology is chosen later by `animation-engineering` unless runtime evidence already proves it.

### Media and 3D
Document crop/focal/safe area, responsive sources, video poster/fallback, 3D camera framing, material/lighting look, or shader visual intent when present. Asset production details route to `asset-production` or `three-d-asset-pipeline`.

### Unknowns and decisions
Maintain a short decision log: unknown, impact, owner, proposed validation, and whether a reversible default is safe. Do not bury uncertainty in prose.

## Handoff contract
An implementation handoff should contain:
- approved DNA version and reference set;
- non-negotiable visual relationships;
- flexible ranges where adaptation is allowed;
- states and viewport matrix;
- asset inventory and missing assets;
- motion/3D escalation requirements;
- accessibility/performance constraints;
- visual QA acceptance criteria.

## Anti-patterns
Avoid “DNA” files that merely list colors and fonts, screenshots annotated with hundreds of absolute coordinates, invented breakpoint values presented as facts, or direct copies of proprietary assets. The contract is successful when another team can create a coherent extension that still feels like the same system without seeing the original screenshot.
