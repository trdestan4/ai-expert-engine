# Asset Consistency and Provenance

Treat asset families as versioned design-system outputs. Record the approved visual direction, master source, generation/edit notes, intended surfaces, variants and immutable traits that should not drift between generations or edits.

Use naming that reveals role rather than generation order: `hero-dental-chair-desktop-v2` is more useful than `final-7.png`. Keep source/master and delivery files in distinguishable locations or naming groups. Avoid overwriting the only editable source with compressed delivery output.

For generated imagery, store enough prompt/reference/seed/settings context when available to reproduce the family, but do not treat raw prompts as the design system. The invariant visual rules belong in creative/art-direction references so future tooling can reproduce the intent even if models change.

Track origin and usage constraints for source photos, fonts, stock elements, 3D models, music, footage, icons and externally generated assets. Generated does not automatically mean commercially unrestricted; provider terms/source rights can differ.

When client/user-supplied content is involved, preserve explicit editing constraints and do not silently use it as a broader reusable training/reference asset. Sensitive or private source material should follow storage/privacy rules.

For asset replacements, preserve stable identifiers or update every consumer deliberately. Remove orphaned variants only after usage is checked. A design system with five near-duplicate logos or icons because old versions were never retired creates implementation errors.

Release handoff should identify master, approved variant set, source/license status, intended crops/backgrounds, and any unresolved provenance risk.