# Repository Profile Reference

Use this reference to keep repository discovery compact and evidence-based.

## Evidence strength

- **Verified** — directly observed in current source/config/manifests/tests.
- **Strong inference** — implied by multiple current signals but not directly proven.
- **Unknown** — insufficient evidence; must not be treated as fact.

Material decisions should rely on verified evidence whenever practical.

## Profile fields

### Stack

Record only relevant technologies and versions/signals:

- language/runtime;
- framework;
- package manager/workspace;
- UI/styling;
- backend/API;
- database/ORM/storage;
- auth/session;
- test/build/deploy.

### Architecture

Capture a short path-based flow, for example:

`app/login/page.tsx` → `lib/auth.ts` → provider SDK → middleware/session check.

Do not restate whole files.

### Conventions

Record only conventions likely to constrain the task: naming, module placement, validation, error handling, data access, test style, component composition.

### Change surface

- direct files/symbols;
- dependent consumers;
- contracts that could break;
- elevated-risk boundaries;
- explicitly unrelated areas.

### Unknowns

List only unknowns that could alter implementation, risk, or verification. Cosmetic uncertainty does not belong in the profile.

## Stop condition

Discovery is sufficient when the primary owner can choose an implementation path and verification strategy without relying on a material unverified assumption.
