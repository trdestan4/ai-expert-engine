# Maintainability and Refactoring

Code quality optimizes future correctness/change cost, not aesthetic uniformity.

## Cohesion and boundaries

Keep code that changes for the same reason together. Make dependencies/side effects visible. Prefer modules around capability/domain behavior over generic `utils` dumping grounds. A clean folder tree cannot compensate for hidden coupling.

## Abstraction

Abstract a stable repeated concept or volatility boundary, not visual similarity. Duplicate a little before committing to a wrong abstraction. Warning signs: boolean-option explosion, one shared helper branching by caller/domain, base class with unrelated overrides, generic repository/service layers that hide useful database behavior.

Conversely, repeated validation/business invariants across multiple paths may deserve one authoritative implementation even before duplication becomes large.

## Refactoring strategy

Preserve behavior with tests/evidence, make small dependency-aware steps and keep migration/compatibility windows explicit. For risky refactors, separate mechanical moves/renames from semantic changes. Remove dead compatibility code after consumers migrate; permanent dual paths multiply defects.

## Complexity

Use complexity metrics as signals. Break functions/components when they contain multiple decisions/side-effect owners, not merely because line count is high. Sometimes a linear 100-line parser is clearer than ten indirections.

## Comments/docs

Comments explain why, invariants, non-obvious tradeoffs or external constraints. Delete comments that narrate syntax or contradict code. Public/shared APIs need usage/contracts/examples when types/tests are insufficient.

## Review

Prioritize correctness, security/data risk, compatibility and maintainability before naming/style. Formatters/linters should absorb subjective noise. A review comment should state consequence and acceptance condition, not “I prefer.”
