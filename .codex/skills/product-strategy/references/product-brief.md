# Product Brief Reference

Use this when downstream design/engineering decisions need a compact but evidence-aware product contract. The brief is not a fictional persona document and not a feature wishlist.

## Core brief

Capture:
- **Outcome:** observable user/business result, not “launch a website.”
- **Primary audience and context:** who arrives, what triggered the visit, what they already know, what risk/cost they perceive.
- **Primary job:** functional job plus the important emotional/social consequence when relevant.
- **Value proposition:** promise, supporting benefit, evidence/proof and meaningful differentiation.
- **Trust requirements:** proof needed before action: authority, quality, reversibility, privacy, price clarity, social proof, guarantees, credentials or operational evidence.
- **Core / supporting / optional / noise scope:** only capabilities tied to outcomes.
- **Constraints:** business, legal, operational, content, data, localization, accessibility, platform, performance and maintenance.
- **Experience principles:** 3–6 project-specific rules that resolve tradeoffs.
- **Success evidence:** leading/lagging metrics or observable behavior.
- **Assumptions and unknowns:** only those that can change product/design/engineering decisions.

## Research and evidence ladder

Prefer direct evidence over invented certainty:
1. observed user behavior, support/sales transcripts, analytics, search logs, churn/activation data;
2. customer interviews or usability evidence with concrete situations;
3. domain/operator knowledge and competitor/category evidence;
4. strong inference from multiple signals;
5. hypothesis requiring validation.

Do not convert demographics into needs without evidence. “35-year-old dentist” is weaker than “clinic owner comparing equipment after a supplier quote and needing installation/service confidence.”

## Jobs-to-be-done and opportunity framing

For high-consideration work, describe the situation → motivation → desired progress → obstacles → current workaround → success signal. Separate the job from the proposed solution. A user asking for “AI search” may actually need faster retrieval, confidence, or reduced support workload.

Map major opportunities by importance, current satisfaction/evidence and strategic fit. Avoid fake precision. Use scoring only when it changes prioritization; record uncertainty and sensitivity.

## Market and competitive context

Competitor research should answer decision questions: table stakes, overused category codes, trust conventions, pricing/packaging norms, switching barriers, underserved jobs and ownable differentiation. Do not produce a gallery of screenshots with no strategic consequence.

Market sizing is only needed when the decision depends on it. Distinguish TAM/SAM/SOM assumptions and avoid multiplying speculative numbers into false certainty.

## Metrics and product analytics

Build a metric tree from the outcome. Choose one or a few primary measures plus guardrails. Examples: activation completion, qualified lead rate, repeat purchase, successful task completion, retention, expansion, support deflection, time-to-value. Protect against optimizing a proxy that harms trust, accessibility, margin or long-term retention.

Define event semantics before tracking implementation: actor, object, trigger, state, timestamp and source. Do not create dozens of events with no question they answer.

## Experimentation

Use experiments when uncertainty is causal and traffic/time/cost justify them. State hypothesis, primary metric, guardrails, minimum meaningful effect or decision threshold, exposure unit and stopping rule. A/B testing is not mandatory for obvious correctness, accessibility, security or severe usability fixes.

For low traffic, use qualitative research, prototypes, staged rollout or interrupted time-series evidence instead of pretending an underpowered test is definitive.

## Roadmap and sequencing

Prefer dependency-aware outcome slices: smallest release that proves value safely, then expand. Sequence irreversible/data/model changes more carefully than reversible UI. Separate discovery risk, delivery risk and operational risk. Do not call speculative infrastructure “future-proofing” unless a near-term requirement makes it cheaper now.

## Quality checks

A strong brief:
- is shorter than the project conversation;
- can explain the product without visual adjectives;
- distinguishes evidence from hypothesis;
- names what is deliberately out of scope;
- gives design/engineering enough constraints to make choices without inventing product policy.

Treat “premium, modern, trustworthy, innovative, simple, fast, exclusive, luxurious” as unresolved criteria. Translate them into behavior/proof before creative direction.
