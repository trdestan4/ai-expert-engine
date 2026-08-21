# Decision Framework

Use this only for choices whose trade-offs materially affect the result.

## 1. Frame the decision

State the decision in one sentence and separate hard constraints from preferences.

## 2. Generate viable options

Include only options that satisfy hard constraints. Usually 2–3 are enough. Do not include a knowingly inferior option just to create symmetry.

## 3. Evaluate relevant dimensions

Select only dimensions that can change the choice:

- correctness / requirement fit;
- compatibility with existing architecture;
- security and privacy;
- data integrity / migration risk;
- implementation complexity;
- operational complexity;
- maintainability;
- performance / scalability;
- reversibility;
- user experience;
- delivery cost/time when actually constrained.

## 4. Weight by context

Not every dimension is equal. A payment/auth/data-integrity concern outranks cosmetic implementation convenience. Existing-repository compatibility generally outranks stylistic preference unless a migration is intentional.

## 5. Choose and record why

A decision should state:

- selected option;
- decisive reasons;
- meaningful downside accepted;
- condition that would justify revisiting it.

## Avoid

- choosing the newest technology by default;
- optimizing for hypothetical scale with no requirement;
- adding abstraction without a concrete change pressure;
- using familiarity as the sole reason when it conflicts with repository conventions;
- pretending uncertain estimates are facts.
