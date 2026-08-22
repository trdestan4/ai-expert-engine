# Contract, E2E and Visual Testing

Contract tests verify request/response/schema/event assumptions between consumers and providers without requiring every system to run together. Include compatibility rules for optional/required fields, enum evolution, error shapes and versioning.

E2E tests should focus on critical user journeys such as sign-in, checkout/payment, account recovery, admin-sensitive actions and primary product workflows. Keep them few, observable and deterministic. Seed data explicitly and avoid dependence on shared production-like accounts.

For web UI, combine browser automation with assertions on meaningful behavior, not brittle DOM implementation details. Cover supported browsers/devices where platform differences matter.

Visual regression is useful for design-system components, high-value landing pages and complex responsive layouts. Stabilize fonts/data/animations/time before snapshot comparison and use review thresholds that avoid constant noise.

Do not treat screenshot equality as accessibility or UX correctness; pair it with semantic/interaction assertions.