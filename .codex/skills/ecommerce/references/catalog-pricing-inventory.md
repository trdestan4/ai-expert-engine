# Catalog / Pricing / Inventory

Separate marketing product data from sellable variants and stock-keeping units. Model options consistently, reject impossible combinations and preserve stable identifiers across copy/name changes. Bundles need explicit component/availability behavior.

Pricing needs an authoritative calculation path covering base price, sale windows, customer/market rules, coupons, taxes, shipping and rounding. Never trust a submitted browser total. Promotions require eligibility, stacking and expiry semantics.

Inventory needs a source of truth, reservation/decrement point, release/expiry behavior and oversell policy. Concurrent checkouts can race; use atomic/transactional guarantees or provider-supported reservations. For multi-location inventory, distinguish available-to-sell from physical on-hand and define reconciliation.