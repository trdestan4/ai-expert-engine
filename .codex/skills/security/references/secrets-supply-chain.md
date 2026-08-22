# Secrets and Supply-Chain Security

## Secret lifecycle

Classify secrets by privilege, environment and rotation/revocation mechanism. Prefer short-lived/workload identity or OIDC federation over long-lived static keys where supported. Production secrets never belong in client bundles, public env prefixes, source, fixtures, screenshots or logs.

A secret committed to history or exposed to an untrusted client must be treated as compromised: revoke/rotate first, then remove/redact history where justified. Deleting the line is not remediation.

Scope keys to least privilege and environment. Separate preview/staging/production provider accounts/IDs when feasible. Protect local developer secrets and CI outputs; mask values but remember derived/encoded variants can still leak.

## Dependency decisions

Before adding a dependency, assess maintenance activity, ownership, release history, transitive graph, install scripts/native code, permission/network surface, bundle/runtime cost and whether a small local implementation is safer. Pin/lock versions through the repository's ecosystem conventions and review surprising lockfile changes.

## Build and CI

Use least-privilege workflow permissions. Avoid executing untrusted fork code with write secrets. Pin third-party CI actions to immutable commits where policy requires it. Protect artifact provenance and ensure the released artifact traces to reviewed source.

Treat package-manager install scripts, Docker base images, downloaded binaries, code-generation tools and remote build plugins as executable supply-chain inputs. Verify checksums/signatures/provenance when risk warrants it.

## SBOM/provenance/scanning

SBOM, dependency scanners/SCA, secret scanners and provenance attestations are useful evidence, not guarantees. Triage vulnerabilities by reachable use, version, exploit prerequisites and exposure; do not ignore a critical vulnerable parser simply because the vulnerable function is “probably unused.” Conversely, avoid blocking on irrelevant CVEs with no reachable path unless policy requires patching.

## Typosquatting and dependency confusion

Use trusted registries/scopes and internal package namespace controls. Review new packages with names similar to popular libraries. Avoid build configurations that can prefer public packages over intended internal dependencies.

## Recovery

Document owner, rotation procedure, blast radius and dependent systems for high-privilege credentials. Test rotation where operationally critical. A recovery plan that requires discovering every consumer during an incident is not mature secret management.
