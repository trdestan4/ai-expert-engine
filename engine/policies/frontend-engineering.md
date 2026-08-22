# Frontend Engineering Policy

These rules apply whenever Phase 02 frontend skills participate.

1. **Version evidence first.** Framework/version-sensitive behavior must come from the repository or current authoritative docs, not memory.
2. **Semantics before styling.** Native HTML/browser behavior is the baseline; custom behavior must be justified.
3. **Design fidelity without brittleness.** Preserve Phase 01 creative intent using tokens, layout systems, reusable contracts, and responsive recomposition—not screenshot hacks.
4. **One state owner.** Do not mirror important state across URL, local state, store, cache, and form state without an explicit synchronization contract.
5. **Server/client boundary is deliberate.** Browser JavaScript is a cost and trust boundary; keep client-only scope as small as behavior requires.
6. **Complete product states.** Loading, empty, error, validation, success, permission, and recovery states are first-class where relevant.
7. **Responsive means behavior, not breakpoints.** Test content and interaction extremes, not only reference viewport sizes.
8. **No trust in the browser.** Client validation/UI visibility are usability controls, never authoritative validation or access control.
9. **Performance by structure first.** Avoid waterfalls, unnecessary client JS, oversized eager assets, and duplicate data before micro-optimizing.
10. **Verification is proportional.** Significant route/data/state changes require behavior evidence beyond type/build success.
11. **Do not silently redesign.** If implementation constraints conflict with UX/creative direction, return the conflict to the owning design skill.
12. **Route specialist depth.** Baseline accessibility/security/performance rules are mandatory, but formal audits belong to their later specialist phases.
