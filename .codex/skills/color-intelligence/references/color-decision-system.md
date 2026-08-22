# Color Decision System

Color is a semantic, perceptual and brand system—not a set of favorite hex codes.

## Build in layers

1. **Intent:** recognition, calm, energy, evidence focus, dense-app clarity, editorial warmth, material/product compatibility.
2. **Source palette:** controlled hue families and tonal/chroma steps; derive from brand/product/imagery/category evidence where useful.
3. **Semantic roles:** canvas, surface, raised surface, primary/muted text, borders, action, focus, link, selected and statuses.
4. **Interaction states:** hover, active, selected, disabled, destructive, visited where relevant.
5. **Modes/themes:** light/dark/high-contrast treated as perceptual systems, not inversion.

## Perceptual decisions

Check luminance hierarchy before hue novelty. Adjacent surfaces need enough perceptual separation on real displays. Highly saturated accents often require reduced area; dark mode commonly needs lower chroma and carefully raised surface luminance rather than brighter borders everywhere.

Use perceptual color spaces (e.g. OKLCH) when tooling supports them for predictable lightness/chroma scales, but verify browser/support/fallback requirements. Numerical uniformity does not replace visual testing.

## Accessibility

Meet applicable contrast requirements for text/UI/focus and never use color as the only signal. Test forced-colors/high-contrast behavior when product audience/platform warrants it. Status colors need icon/text/shape support and should remain distinguishable under common color-vision deficiencies.

## Brand and category fit

Evaluate category trust conventions, differentiation, emotional temperature, cultural meaning when material, imagery/product compatibility and print/offline constraints if relevant. Do not assert universal color psychology (“blue means trust”) without context.

## Product imagery

For ecommerce/portfolio/media-heavy work, test representative product cutouts and photography against surfaces. Dark products disappear on dark surfaces without tone/shadow/rim/background treatment; bright/transparent assets may need alternate art direction. Do not recolor evidence-critical products inaccurately for brand harmony.

## Data visualization

Separate categorical, sequential and diverging palettes. Reserve semantic red/green meanings deliberately. Keep series count bounded, label important values directly when possible and test grayscale/contrast. Do not reuse action accent as every chart series.

## Tokens

Prefer semantic tokens (`surface-canvas`, `text-muted`, `action-primary`) over component-specific hexes. Separate source tokens from semantic mapping so modes can change without rewriting components. Document allowed accent frequency and exceptions.

## Validation

Test: light/dark, common device brightness, long pages, disabled/selected/focus states, charts, forms/errors, product imagery, screenshots under compression and localization where line wrapping changes colored areas. A palette is approved because the system works, not because a swatch board looks premium.
