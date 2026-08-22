# Secrets, Dependencies, Supply Chain and Release Security

Keep secrets out of source control, browser bundles, public mobile artifacts, logs and analytics. Separate public identifiers from privileged credentials. Scope credentials to the minimum environment/resource/actions, rotate exposed or long-lived keys and make revocation possible.

Treat package installation and build tooling as code execution. Pin/lock dependencies, review unexpected lifecycle scripts, provenance and ownership, and investigate relevant advisories/transitive exposure. Dependency scanners inform risk; they do not replace exploitability and reachability analysis.

Protect CI/CD credentials and branch/release paths with least privilege. Production deployment should be reproducible from reviewed source and trusted artifacts where practical.

For abuse-sensitive endpoints, combine authentication/authorization with rate/velocity controls, idempotency/replay defense and monitoring. Do not create user-lockout mechanisms that attackers can weaponize trivially.

Before release, unresolved critical/high exploitable findings on exposed paths require remediation or explicit accountable risk acceptance with compensating controls, expiry and follow-up verification.