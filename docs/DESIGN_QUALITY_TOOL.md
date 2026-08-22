# Deterministic Design Quality Checks

`python scripts/design_quality_checks.py` complements—not replaces—the design specialist skills.

## Contrast

```bash
python scripts/design_quality_checks.py contrast '#111827' '#ffffff' --required 4.5
```

It uses WCAG relative-luminance contrast math and returns a non-zero exit code when the requested ratio is not met. The caller chooses the applicable ratio based on current accessibility requirements and text/UI context.

## Audit spec

```json
{
  "contrast_pairs": [
    {"name":"body","foreground":"#111827","background":"#ffffff","required_ratio":4.5}
  ],
  "typography": [
    {"name":"body","font_size_px":16,"line_height_px":24,"measure_ch":68}
  ],
  "semantic_tokens":{"text-primary":"#111827"},
  "required_semantic_tokens":["text-primary"]
}
```

Run:

```bash
python scripts/design_quality_checks.py audit design-quality.json
```

The typography checks are intentionally broad deterministic guardrails, not aesthetic rules. Creative direction, brand fit, hierarchy, responsiveness and originality remain judgment tasks owned by their specialist skills.
