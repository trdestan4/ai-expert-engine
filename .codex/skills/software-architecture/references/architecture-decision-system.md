# Architecture Decision System

Use this only when multiple structural options differ materially in long-term consequences.

## 1. State the decision

Write one sentence describing the boundary/structure that must be chosen. Do not start from a preferred pattern.

## 2. List drivers

Rank only relevant drivers such as:

- change frequency/ownership;
- independent deployment or runtime need;
- persistence/transaction boundary;
- compatibility/migration constraints;
- measured scale/latency;
- reliability/failure isolation;
- testability/substitution;
- team/repository organization.

## 3. Generate realistic options

Usually 2–4 options are enough, including the simplest acceptable option. Do not compare fantasy end-states that the project cannot realistically operate.

## 4. Compare decision-relevant dimensions

For each option assess:

- requirement fit;
- coupling/cohesion;
- implementation/migration cost;
- operational complexity;
- reversibility;
- maintenance/observability;
- performance/reliability only where evidence makes them material.

Avoid numeric scoring that disguises subjective assumptions. Use explicit trade-offs.

## 5. Prefer reversibility under uncertainty

When two options satisfy requirements similarly, prefer the one with lower irreversible cost and a clear evolution path.

## 6. Record consequences

Document both what becomes easier and what becomes harder. Every architecture decision has a cost.

## 7. Define revisit trigger

Examples: sustained workload threshold, second independent team, integration replacement, deployment cadence conflict, unacceptable build time, availability requirement, or compatibility deadline.

## Concise ADR template

**Context:** relevant facts/drivers only.  
**Decision:** chosen structure.  
**Alternatives:** material alternatives and why not now.  
**Consequences:** benefits + costs.  
**Revisit when:** observable trigger.

Do not create an ADR for ordinary implementation choices that can be changed locally at low cost.
