# Senior Review and Technical Debt

Review findings should distinguish correctness/security/reliability blockers from maintainability concerns and personal style. Severity should reflect likely user/business impact, change difficulty and probability of failure—not reviewer preference.

Look for unclear ownership, duplicated domain rules, tight coupling, hidden side effects, weak error semantics, unsafe types, dead code, dependency sprawl and code that is difficult to test or observe. Prefer actionable findings with file/behavior context and a bounded fix.

Technical debt is useful only when tied to consequence. Record the current constraint, why it matters, what trigger makes remediation necessary, likely scope and an owner or review point. Avoid vague TODOs such as “refactor later.”

Do not demand architectural rewrites for small local problems. Conversely, repeated local workarounds around the same boundary are evidence that architecture may need review.

A quality review is complete when blockers are resolved or explicitly accepted, important debt is visible, tests protect risky behavior and the changed code remains understandable to another senior engineer.