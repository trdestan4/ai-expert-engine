# Phase 02 Evals — Web Engineering / Frontend

These cases test routing boundaries and quality behavior. Expected routes are intentionally minimal.

## Routing positives

1. **“CORS preflight succeeds locally but browser blocks production response.”**  
   Expected: `debugging` → `web-platform`. Do not load React by default.

2. **“Implement this approved responsive landing page with semantic HTML/CSS/TypeScript.”**  
   Expected: `frontend-engineering`.

3. **“Next App Router page needs Server Action form mutation and revalidation.”**  
   Expected: `react-nextjs`; add `frontend-engineering` only if component/form structure is substantial.

4. **“Page hydrates with mismatch only after reading localStorage.”**  
   Expected: `debugging` → `react-nextjs`; `web-platform` is supporting evidence if storage/runtime semantics are material.

5. **“Should this large app become microservices or a modular monolith?”**  
   Expected: `software-architecture` after `repository-intelligence`/requirements evidence. Do not load frontend skills by default.

6. **“Filters must survive reload and be shareable.”**  
   Expected: `frontend-engineering` (URL state decision). `web-platform` only if history/URL mechanics are disputed.

## Routing negatives

7. **“Choose a premium color palette for a dental brand.”**  
   Must NOT trigger Phase 02 as primary. Route Phase 01 `creative-director`/`color-intelligence`.

8. **“Optimize PostgreSQL query indexes.”**  
   Must NOT trigger Phase 02.

9. **“Audit this site for OWASP vulnerabilities.”**  
   Baseline frontend hygiene is insufficient; route future security specialist, not `frontend-engineering` as primary.

10. **“Fix spelling in one static paragraph.”**  
    No Phase 02 orchestration needed unless code editing itself requires repository context.

## Edge cases

11. **Next.js unknown version**  
    Prompt: “Use middleware to read cookies and redirect.”  
    Expected behavior: `react-nextjs` verifies installed Next version/router before choosing middleware/proxy/request APIs. Fails if it asserts a version-sensitive convention from memory.

12. **Design conflict**  
    Prompt: “Implement fixed 900px card height but content can translate to German and mobile.”  
    Expected: `frontend-engineering` identifies content/responsive conflict and returns it to `ux-ui-design` rather than clipping content or silently redesigning.

13. **State duplication**  
    Prompt: “Keep filter in URL, global store, and component state so it’s always synced.”  
    Expected: `frontend-engineering` challenges multiple authorities and chooses one source of truth unless synchronization has an explicit requirement.

14. **Cache confusion**  
    Prompt: “Data is stale, disable every cache.”  
    Expected: determine cache owner first (`react-nextjs` or `web-platform` based on evidence); fails if global no-cache is the first action.

15. **RSC client spread**  
    Prompt: “Add `use client` to root layout because one button needs onClick.”  
    Expected: `react-nextjs` keeps client boundary narrow.

16. **Architecture overengineering**  
    Prompt: “Create five services for a small single-team app to be scalable.”  
    Expected: `software-architecture` demands drivers/evidence and prefers simpler process-local modules absent real independent deployment/scale needs.

## Quality assertions

A passing Phase 02 implementation should demonstrate:

- version-sensitive framework facts are verified;
- semantics/native behavior are preferred;
- design intent is preserved without brittle screenshot hacks;
- state ownership is explicit;
- loading/error/empty/recovery states exist where relevant;
- responsive behavior is tested against content/input extremes;
- baseline client security/performance/accessibility issues are not deferred;
- formal specialist audits are routed rather than impersonated;
- verification proves behavior, not only successful compilation.
