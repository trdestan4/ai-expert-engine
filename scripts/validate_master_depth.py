#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MIN={
'.codex/skills/product-strategy/references/product-brief.md':350,
'.codex/skills/brand-design/references/brand-system.md':300,
'.codex/skills/anti-generic-design/references/ai-design-cliches.md':300,
'.codex/skills/color-intelligence/references/color-decision-system.md':300,
'.codex/skills/typography-intelligence/references/type-decision-system.md':300,
'.codex/skills/visual-art-direction/references/art-direction-system.md':300,
'.codex/skills/motion-direction/references/motion-system.md':300,
'.codex/skills/ux-ui-design/references/ux-ui-system.md':300,
'.codex/skills/security/references/web-api-security.md':350,
'.codex/skills/performance/references/backend-data-load.md':300,
'.codex/skills/testing-qa/references/test-strategy-boundaries.md':300,
'.codex/skills/accessibility/references/accessibility-testing.md':250,
'.codex/skills/privacy-compliance/references/privacy-data-map.md':250,
'.codex/skills/ecommerce/references/cart-checkout-orders.md':250,
'.codex/skills/saas-platform/references/tenancy-membership-permissions.md':250,
'.codex/skills/seo/references/technical-crawl-index.md':250,
'.codex/skills/devops-deployment/references/cloud-iac-kubernetes.md':300,
'.codex/skills/observability-sre/references/sli-slo-alerting.md':200,
'.codex/skills/release-readiness/references/release-gates.md':300,
'.codex/skills/multi-review/references/reviewer-selection.md':300,
'.codex/skills/design-reconstruction/references/reference-analysis.md':250,
'.codex/skills/design-reconstruction/references/design-dna-contract.md':250,
'.codex/skills/creative-frontend/references/advanced-css-responsive-art-direction.md':250,
'.codex/skills/creative-frontend/references/scroll-experience-and-media.md':250,
'.codex/skills/animation-engineering/references/gsap-scrolltrigger-production.md':250,
'.codex/skills/animation-engineering/references/web-motion-runtimes.md':250,
'.codex/skills/threejs-webgl/references/scene-runtime-lifecycle.md':250,
'.codex/skills/threejs-webgl/references/loading-postprocessing-interaction.md':250,
'.codex/skills/realtime-shaders/references/shader-authoring.md':250,
'.codex/skills/realtime-shaders/references/gpu-effects-performance.md':250,
'.codex/skills/three-d-asset-pipeline/references/gltf-production-pipeline.md':250,
'.codex/skills/three-d-asset-pipeline/references/compression-textures-lod.md':250,
'.codex/skills/visual-qa/references/visual-regression-method.md':250,
'.codex/skills/visual-qa/references/motion-cross-device-qa.md':250,
}
REVIEW_DOMAIN={'code-reviewer':'code-quality','design-reviewer':'ux-ui-design','security-reviewer':'security','performance-reviewer':'performance','qa-reviewer':'testing-qa','release-reviewer':'release-readiness'}
def wc(p):return len(re.findall(r"\b[\w'-]+\b",p.read_text()))
def main():
    e=[]
    for rel,n in MIN.items():
        p=ROOT/rel
        if not p.exists():e.append('missing master reference '+rel)
        elif wc(p)<n:e.append(f'shallow master reference {rel}: {wc(p)}<{n} words')
    for rev,domain in REVIEW_DOMAIN.items():
        p=ROOT/'.cursor/agents'/f'{rev}.md';t=p.read_text() if p.exists() else''
        if f'.codex/skills/{domain}/SKILL.md' not in t:e.append(f'{rev} does not load owning expert skill {domain}')
    beh=[x for x in (ROOT/'evals/behavioral/cases.jsonl').read_text().splitlines() if x.strip()]
    cal=[x for x in (ROOT/'evals/reviewer-calibration/cases.jsonl').read_text().splitlines() if x.strip()]
    if len(beh)<40:e.append(f'behavioral corpus too small: {len(beh)}')
    if len(cal)<24:e.append(f'reviewer calibration corpus too small: {len(cal)}')
    src=json.loads((ROOT/'engine/knowledge/sources.json').read_text()).get('sources',[])
    if len(src)<40:e.append(f'knowledge sources too small: {len(src)}')
    bench=json.loads((ROOT/'benchmarks/corpus.json').read_text()).get('external',[])
    if len(bench)<10:e.append('repository benchmark corpus too small: '+str(len(bench)))
    ps=json.loads((ROOT/'engine/profiles/profiles.json').read_text()).get('profiles',[]);dims={x.get('dimension') for x in ps}
    if len(ps)<24:e.append(f'profile corpus too small: {len(ps)}')
    if not {'solution','application','data','infrastructure','experience'}<=dims:e.append('stack profiles are not composable across all dimensions')
    release=(ROOT/'scripts/release_gate.py').read_text();builder=(ROOT/'scripts/build_release_decision.py').read_text();prof=(ROOT/'scripts/profile_repository.py').read_text();runtime=(ROOT/'scripts/runtime_contract.py').read_text()
    for marker in ('environment','expires_at','candidate mismatch'):
        if marker not in release and marker not in builder:e.append('release hardening marker missing: '+marker)
    if 'truncated' not in prof:e.append('repository profiler lacks truncation evidence')
    for marker in ("'$ref'","'oneOf'","'if'"):
        if marker not in runtime:e.append('runtime schema composition marker missing '+marker)
    for tool in ('design_quality_checks.py','creative_experience_checks.py','routing_report.py'):
        if not (ROOT/'scripts'/tool).exists():e.append('deterministic tool missing '+tool)
    installer=(ROOT/'scripts/enginectl.py').read_text()
    for managed in ('scripts/design_quality_checks.py','scripts/creative_experience_checks.py','scripts/routing_report.py'):
        if managed not in installer:e.append('installer does not manage '+managed)
    phase10=(ROOT/'scripts/validate_phase10.py')
    if not phase10.exists():e.append('Phase 10 validator missing')
    if e:print('master depth validation FAILED');[print(' -',x) for x in e];return 1
    print(f'master depth validation PASSED: {len(MIN)} deep references, {len(beh)} behavioral, {len(cal)} reviewer, {len(bench)} repo benchmarks, {len(src)} freshness sources');return 0
if __name__=='__main__':sys.exit(main())
