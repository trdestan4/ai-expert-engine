# Discovery, Merchandising and Commerce Analytics

## Discovery

Design category/navigation/search/filter around actual shopping decisions. Search should handle synonyms/typos/identifiers appropriate to catalog and expose useful no-result recovery. Ranking combines relevance with business rules only transparently enough to avoid hiding user intent.

Facets need controlled attributes, counts and reversible state. Very large dynamic combinations coordinate with SEO/crawl strategy.

## Merchandising

Collections, badges, featured products, bundles/cross-sell/upsell and recommendations need business ownership and eligibility rules. Avoid manual merchandising systems that cannot scale or automated recommendations that promote unavailable/incompatible items.

Recommendations should have fallback and explainable constraints (inventory, locale, margin, compatibility) where relevant. Personalization follows privacy/consent policy.

## Analytics model

Define product impression/view, search, filter, add/remove cart, begin checkout, payment/order and refund events with stable IDs and currency/value semantics. Deduplicate events across client/server/webhook paths. Separate revenue/order source of truth from analytics convenience.

Measure funnel plus downstream quality: conversion, AOV, margin, return/refund, repeat purchase, search success, zero-results and checkout errors. Do not optimize click/add-to-cart while payment failure/returns worsen.

## Experimentation

Test merchandising/ranking changes with guardrails for margin, inventory concentration, returns and customer trust. Ranking experiments require consistent exposure unit and avoid contamination across sessions/users where it matters.
