# Maintainability and Safe Refactoring

Good refactoring reduces cognitive load and change risk while preserving behavior. First identify responsibilities, invariants and callers; then improve names, boundaries, data flow and duplication. Avoid refactoring unfamiliar behavior based only on aesthetics.

Cohesion matters more than arbitrary file/function size. Group behavior that changes for the same reason and separate concepts with independent lifecycles. Reduce hidden global state and cross-module knowledge.

Use abstractions for stable shared behavior or important boundary isolation—not because two code blocks currently look similar. Premature generic layers often increase indirection and make future variation harder.

For risky legacy areas, add characterization/regression tests before structural changes. Prefer small reviewable steps, preserving public contracts until callers migrate. Separate broad refactors from unrelated feature changes when practical.

Delete dead code and obsolete compatibility paths once evidence shows they are no longer needed. A simpler explicit implementation is often safer than an elegant but over-general framework.