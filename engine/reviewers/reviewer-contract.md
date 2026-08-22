# Reviewer Contract

Reviewer profiles are independent review lenses, not discoverable implementation skills.

Each reviewer must:
1. inspect the actual change/evidence relevant to its lens;
2. remain inside its ownership boundary;
3. report only evidence-backed findings;
4. assign severity and confidence separately;
5. include impact and an acceptance condition;
6. distinguish blockers from non-blockers;
7. avoid implementing fixes unless separately routed to the owning skill;
8. state coverage gaps and evidence it could not verify.

Common finding shape:
`{id, reviewer, title, severity, confidence, affected_surface, evidence, impact, acceptance_condition, owner, blocker}`.

Reviewers do not vote. Conflicts are resolved by evidence and the owning domain contract.