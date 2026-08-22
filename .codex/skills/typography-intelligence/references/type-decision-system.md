# Typography Decision System

Typography carries hierarchy, brand voice, reading efficiency, data clarity and layout behavior. Select by job and measurable characteristics rather than serif/sans stereotypes.

## Evaluate families

Inspect x-height, width, stroke contrast, geometry/terminals, counters, punctuation, numerals, symbols, language coverage, diacritics, weights/axes, optical sizes, small-size clarity and loading footprint. Verify actual glyph coverage for target locales; a Latin demo does not prove Turkish, Arabic, Cyrillic or CJK support.

## Roles

Use only roles that add value: display, heading, body, UI/control, data/mono, metadata. One family can fill several roles. A second family must add meaningful expressive or functional contrast; “serif + sans = luxury” is not rationale.

## Hierarchy

Control size, weight, line-height, tracking, measure, case, optical size and surrounding spacing. Build a hierarchy that remains clear without color. Protect body measure and line height; design responsive display line breaks rather than only shrinking font-size.

Use fluid scaling only when it improves behavior across viewports; clamp extremes and test zoom. Avoid heading scales that create one spectacular hero but awkward H2/H3/product/table behavior.

## UI and data

Controls need stable metrics and legibility at compact sizes. Check numerals: proportional vs tabular, slashed zero, currency/percent alignment, minus sign, decimal and locale formatting. Tables/dashboards often benefit from tabular figures without requiring a monospaced face.

## Internationalization

Test expansion, bidirectional text, punctuation, numerals, fallback fonts and line breaking. Pairing a Latin display face with an unrelated fallback can destroy brand hierarchy in another language; define cross-script strategy intentionally.

## Performance and implementation

Load only used weights/styles/axes. Variable fonts can reduce payload/complexity but not always; inspect file size and browser needs. Use `font-display` strategy based on product priorities, metric-compatible fallbacks where layout shift matters and selective preload only for critical faces. Subsetting must not remove dynamically needed glyphs.

## Optical quality

Check real rendering at target OS/browser/device, not only design tool screenshots. Very thin strokes, tight tracking or extreme contrast can fail on low-density screens. Avoid faux bold/italic when real styles exist.

## Validation

Test: hero with long/short titles, body paragraphs, forms, buttons, tables, currency/data, mobile, 200% text/zoom, localization, dark mode and loading fallback. A type system is approved when it handles the boring screens as well as the hero.
