---
name: product-strategy
description: Defines the product intent, audience, value proposition, requirements priorities, business constraints, success criteria, and experience goals that should guide a web product before design or implementation; it does not own visual execution or code.
---

# Purpose

Turn vague business intent into a product direction strong enough to guide creative, UX, architecture, conversion, and implementation decisions without over-specifying the solution.

## Use when

- a new website, ecommerce experience, SaaS product, campaign site, dashboard, or major feature needs product framing;
- requirements are broad, conflicting, or mostly expressed as desired impressions such as “premium”, “modern”, “fast”, or “easy”;
- audience, primary job-to-be-done, conversion goal, or scope priority is unclear;
- design/engineering trade-offs require product context;
- another specialist needs a compact product brief rather than assumptions.

## Do not use when

- the product direction is already explicit and only visual execution is needed;
- the task is purely technical and product behavior is fixed;
- detailed brand identity is the primary question (`brand-design` owns it);
- layout/interaction usability is the primary question (`ux-ui-design` owns it).

## Inputs

Capture only decision-relevant information:

- business/organization type;
- audience and their primary intent;
- core offer/product/service;
- desired user action or success event;
- market/positioning constraints;
- must-have capabilities and exclusions;
- trust, legal, operational, content, and delivery constraints;
- known business model or conversion model.

## Workflow

### 1. Define the outcome

Translate the request into one primary product outcome and, when needed, secondary outcomes. Prefer observable behavior over adjectives.

Bad: “Make it premium.”

Better: “Create a high-trust product experience for buyers comparing high-value options, with clear proof, fast product discovery, and confident checkout.”

### 2. Identify the audience and context

Define:

- primary audience;
- their intent when arriving;
- what they already know;
- biggest uncertainty/friction;
- trust proof they need;
- device/context patterns when relevant.

Do not invent demographic detail that does not affect decisions.

### 3. Define value proposition hierarchy

Separate:

- core promise;
- supporting benefits;
- proof/evidence;
- differentiators;
- objections that must be resolved.

Do not treat slogans as strategy.

### 4. Define product jobs

Identify the smallest set of high-value user jobs, such as discover, compare, understand, configure, buy, book, contact, subscribe, manage, or return.

Rank by user/business importance.

### 5. Prioritize scope

Classify requested capabilities:

- **Core** — required for the primary outcome;
- **Supporting** — materially improves success;
- **Optional** — useful but deferrable;
- **Noise** — adds complexity without material value.

Avoid feature-count prestige.

### 6. Define experience principles

Produce 3–6 project-specific principles that constrain design and engineering, for example:

- proof before persuasion;
- comparison before checkout pressure;
- editorial confidence instead of decorative luxury;
- mobile purchase flow must remain one-handed and concise.

Avoid generic principles that could apply to every website.

### 7. Define measurable success

Choose metrics proportional to the project, such as:

- qualified lead completion;
- add-to-cart / checkout completion;
- product discovery success;
- onboarding completion;
- reduced support friction;
- relevant performance/accessibility quality gates.

Do not invent target numbers unless supplied or explicitly modeled as hypotheses.

### 8. Hand off decision context

Produce a compact brief usable by `creative-director`, `ux-ui-design`, architecture, ecommerce, conversion, and engineering specialists.

## Decision rules

- Business adjectives are inputs, not design instructions.
- One clear primary outcome beats several equal “goals.”
- Prefer user jobs over page lists.
- Prioritize trust and comprehension before persuasion when decision risk is high.
- Do not copy competitors merely because a convention is common; separate necessary convention from sameness.
- If a feature does not support a user job, business requirement, risk control, or measurement need, challenge it.
- When uncertainty is low-impact and reversible, state a working assumption rather than blocking progress.

## Reference routing

Load `references/product-brief.md` when a structured brief is needed.

Load `references/product-decisions.md` for prioritization or competing product directions.

Use `creative-director` after product intent is sufficiently clear to define visual/experiential direction.

## Quality gates

- Primary outcome is explicit.
- Audience intent is decision-relevant rather than fictional persona detail.
- Value proposition and proof are separated.
- Core jobs and scope priorities are clear.
- Experience principles are specific to this product.
- Success criteria are observable.
- No visual style has been selected merely from a prestige adjective.

## Failure handling

If critical business information is unavailable, infer only reversible defaults and label them. If multiple audiences have incompatible jobs, choose a primary audience or define distinct flows. If scope is too broad, protect the primary outcome and defer lower-value complexity.

## Output contract

Return a compact product direction containing:

- primary outcome;
- primary audience/context;
- value proposition hierarchy;
- core user jobs;
- prioritized scope;
- experience principles;
- material constraints;
- success criteria;
- assumptions requiring later validation.
