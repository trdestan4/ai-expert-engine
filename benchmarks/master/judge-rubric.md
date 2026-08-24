# Master Benchmark Expert Judge Rubric

Expert judgment is deliberately subordinate to deterministic hard gates. A judge may score taste, architecture quality, reference fidelity, product coherence, maintainability and evidence interpretation; a judge may never turn a failed security, accessibility, functional, testing-integrity, release-integrity or hidden-leakage gate into a pass.

## Evidence protocol

Judge only artifacts tied to the scenario, candidate workspace/commit, environment fingerprint and run identifier. Distinguish **observed**, **derived**, **inferred** and **unknown** facts. Never convert an unmeasured claim into measured evidence. Candidate-authored score claims are advisory only.

Each domain receives 0–100 with a short rationale and evidence pointers. Use 90+ only when the result is production-credible for the scenario. Use 95+ only when failure paths, edge cases, cross-device behavior and maintenance quality are unusually strong. Missing evidence is not neutral; it is an evidence gap.

## Domain anchors

| Domain | 90–94 | 95–100 | Typical blocker |
| --- | --- | --- | --- |
| Functional correctness | Main and edge flows work with explicit error recovery | State transitions/retries survive adversarial sequences | Broken critical flow |
| Visual fidelity | Hierarchy, spacing and type are coherent/reference-aware | Multi-viewport fidelity with intentional art direction | Major structural mismatch |
| Responsive art direction | Layout adapts intentionally | Content priority/composition changes appropriately | Critical content clipped/hidden |
| Interaction quality | Focus, touch, keyboard and states are coherent | Interaction states are complete and resilient | Unusable control path |
| Motion quality | Purpose, cleanup and reduced-motion path exist | Choreography is deterministic and responsive | Motion blocks content/control |
| Graphics / 3D | Lifecycle, fallback and performance are handled | Asset/runtime/shader budgets are measured and robust | Leak or no fallback |
| Accessibility | Semantic/keyboard/AT fundamentals are evidenced | Complex states and motion/media are proven | Critical WCAG/keyboard blocker |
| Performance | Budgets and bottlenecks are measured | Device-aware quality tiers and runtime stability | Critical budget failure |
| Semantic HTML | Native semantics/document outline are correct | Semantics remain strong in dynamic states | Broken landmark/control semantics |
| SEO discoverability | Crawl/meta/content fundamentals are correct | Scalable canonical/entity/internal-link strategy | Indexability/canonical failure |
| Security | Trust boundaries and abuse paths are addressed | Threat model, tests and runtime controls align | Exploitable blocker |
| Privacy compliance | Collection/consent/retention are minimized | Product degrades safely under consent choices | Undisclosed unnecessary collection |
| Resilience / fallbacks | Failure states and retries are designed | Capability/network/service failures preserve core tasks | Single failure destroys core task |
| Browser compatibility | Key paths work across required engines | Enhancement boundaries are capability-aware | Critical engine-specific failure |
| Code quality | Clear, maintainable implementation | Small coherent abstractions and low accidental complexity | Fragile critical logic |
| Architecture | Boundaries match the problem | Evolution paths and ownership are explicit | Unsafe cross-boundary coupling |
| Data / API integrity | Validation and consistency rules are correct | Idempotency/concurrency/migration behavior is proven | Data corruption/contract break |
| Testing evidence | Meaningful deterministic tests cover risk | Adversarial/regression evidence is reproducible | Tests weakened/fabricated |
| Release discipline | Candidate/environment-specific evidence exists | Rollback, expiry and gate are technically enforced | Stale/wrong-environment evidence |
| Product originality | Solution fits the problem and avoids filler | Distinctive choices improve user value | Novelty damages usability |

## Judge output contract

Return JSON with `expert_scores` keyed by the 20 domain ids plus `rationales` keyed the same way. A domain not materially applicable may be scored only when the scenario defines how its absence is handled; otherwise mark it unknown and allow certification to fail on missing required coverage. Never emit hard-gate state from the subjective judge.
