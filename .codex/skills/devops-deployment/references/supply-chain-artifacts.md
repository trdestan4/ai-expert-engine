# Supply Chain, Build Artifacts and Provenance

## Inputs

Treat dependencies, lockfiles, package install scripts, container bases, CI actions, downloaded binaries, compilers/code generators and remote build plugins as executable supply-chain inputs.

## Integrity

Pin immutable versions/digests where risk/governance requires it; verify checksums/signatures/provenance for downloaded tools. Keep lockfile changes reviewable and avoid generated lockfile noise hiding new packages.

## Artifacts

Record source commit, build environment/toolchain and artifact digest. Prefer build-once/promote. Store artifacts in controlled registry with retention/access and avoid mutable `latest` as sole production identity.

## SBOM and attestations

SBOM/provenance attestations improve inventory/traceability but do not guarantee safety. Associate them with exact artifact and retain enough to investigate incidents. Vulnerability triage still needs reachability/exposure/context.

## Build isolation

Minimize secrets available during builds and separate untrusted PR/fork jobs. Network-restricted/hermetic builds may be appropriate for high assurance. Cache inputs must be scoped to prevent untrusted poisoning.

## Emergency dependency response

For compromised/vulnerable dependency: identify affected versions/artifacts, disable/contain if needed, update/replace, rebuild from trusted source, rotate secrets if exposure plausible, verify production artifact and document residual risk.
