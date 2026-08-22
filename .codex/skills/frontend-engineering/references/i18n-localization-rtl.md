# Internationalization, Localization, RTL and Locale Correctness

Treat internationalization as application behavior, not string replacement.

## Locale model
- Define supported BCP 47 locale identifiers and a canonical default.
- Decide whether locale is URL-owned, account-owned, device-derived or explicitly selected; avoid multiple competing authorities.
- Locale routing, persistence and fallback must be deterministic and testable.
- Do not infer language from country or currency.

## Messages and grammar
Use a real message-format system when plural/select/gender/number rules are non-trivial. Keep whole semantic messages together instead of concatenating translated fragments. Stable translation keys describe meaning, not current English wording. Missing-message fallback must be observable in development and safe in production.

## Numbers, money, dates and time
Use locale-aware formatting APIs/libraries. Store money and timestamps in authoritative domain forms; formatting is presentation. Timezone is separate from locale. Calendar, week-start and numbering system assumptions must be explicit when product behavior depends on them.

## Forms and validation
Localize labels, help, errors and confirmation text without changing authoritative validation rules. Allow local input conventions only when normalization is unambiguous. Names, addresses and phone numbers must not be forced into one-country shapes without a product requirement.

## RTL and bidi
Prefer logical CSS properties (`margin-inline`, `padding-inline`, `inset-inline`, logical borders) over physical left/right assumptions. Set document/region direction correctly and isolate mixed-direction user content when needed. Mirror spatial/navigation affordances only when meaning is directional; do not mirror logos, media controls, numerals or culturally fixed symbols blindly.

## Layout resilience
Test pseudo-localization, 30–50% text expansion, long compound words, CJK, RTL, narrow viewports and 200% text. Components must not encode English string length into width or truncation assumptions.

## Translation workflow
Define source locale, extraction, translator context, review, fallback, stale-key cleanup and release ownership. Machine translation may accelerate drafts but does not remove human/domain review for legal, medical, financial, marketing or brand-sensitive copy.

## SEO/accessibility integration
Coordinate locale URLs, `hreflang`, canonical behavior and localized metadata with `seo`. Ensure `lang`/`dir`, accessible names, alt text and validation messages match rendered language. Route formal accessibility review to `accessibility`.

## Quality checks
Verify locale switching without state loss, route reload/deep-link behavior, fallback behavior, date/currency/timezone correctness, plural/select cases, RTL keyboard/focus order, pseudo-localized overflow and localized error states.
