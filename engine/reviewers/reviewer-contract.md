# Reviewer Contract

Reviewer profiles are independent, read-only review lenses, not discoverable implementation skills.

Each reviewer must:
1. inspect the actual candidate/change evidence relevant to its lens;
2. remain inside its ownership boundary;
3. reason independently and avoid another reviewer's verdict before its own result;
4. report only evidence-backed findings;
5. assign severity and confidence separately;
6. include candidate, affected surface, evidence, impact and acceptance condition;
7. identify owner and blocker state;
8. avoid implementing fixes unless separately routed to the owning skill;
9. state coverage gaps/evidence it could not verify.

Canonical persistent finding shape follows `engine/schemas/reviewer-finding.schema.json`. When persistence is available, the parent orchestration layer—not the read-only reviewer—normalizes and stores findings with `scripts/review_store.py`. Stored candidate identity must match the reviewed artifact. Accepted risk requires explicit disposition and expiry; silence never closes a finding.

Reviewers do not vote. Conflicts are resolved by evidence and the owning domain contract.
