# Reliability, Security and Performance Tests

High-risk systems need failure-oriented tests beyond functional correctness. Exercise timeouts, retry exhaustion, partial dependency failure, duplicate delivery, out-of-order events, worker restart, transaction conflicts and recovery/rollback paths where the architecture allows them.

Security tests should cover unauthorized object/action access, cross-tenant isolation, malformed/oversized inputs, replay, webhook forgery, unsafe upload types and relevant injection/SSRF paths defined by the security specialist.

Performance tests need realistic traffic/data models and clear targets. Record latency percentiles, throughput, errors and saturation signals. Avoid one-off benchmark numbers without environment/context.

Flaky tests are engineering defects. Remove arbitrary sleeps, implicit shared state, nondeterministic clocks/randomness and uncontrolled external dependencies. Use deterministic clocks/IDs and bounded polling when appropriate. Quarantine a flaky test only temporarily with owner and expiry; retries must not become a permanent way to hide failures.