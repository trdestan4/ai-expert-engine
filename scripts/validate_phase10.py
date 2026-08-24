#!/usr/bin/env python3
"""Validate Phase 10 Creative Engineering Expansion."""
from __future__ import annotations
import ast,json,re,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'engine/registry/phase-10-skills.json';ROUTE=ROOT/'engine/routing/phase-10-routing.md';POLICY=ROOT/'engine/policies/creative-engineering.md';SCHEMA=ROOT/'engine/schemas/creative-experience-plan.schema.json';EVAL=ROOT/'evals/phase-10-creative-engineering.md';TOOL=ROOT/'scripts/creative_experience_checks.py'
EXPECTED={'design-reconstruction','creative-frontend','animation-engineering','threejs-webgl','realtime-shaders','three-d-asset-pipeline','visual-qa'}
HEAD=['# Purpose','## Use when','## Do not use when','## Inputs','## Workflow','## Decision rules','## Reference routing','## Quality gates','## Failure handling','## Output contract']

def fm(t):
    if not t.startswith('---\n'):raise ValueError('missing YAML frontmatter')
    end=t.find('\n---\n',4)
    if end<0:raise ValueError('unterminated YAML frontmatter')
    d={}
    for raw in t[4:end].splitlines():
        if raw.strip() and not raw.lstrip().startswith('#'):
            if ':' not in raw:raise ValueError('invalid frontmatter')
            k,v=raw.split(':',1);d[k.strip()]=v.strip().strip("\"'")
    return d

def main():
    e=[]
    for p in (REG,ROUTE,POLICY,SCHEMA,EVAL,TOOL):
        if not p.exists():e.append('missing '+str(p.relative_to(ROOT)))
    if e:return fail(e)
    try:r=json.loads(REG.read_text());json.loads(SCHEMA.read_text());ast.parse(TOOL.read_text())
    except Exception as ex:return fail(['invalid phase artifact: '+str(ex)])
    seen=set()
    for item in r.get('skills',[]):
        n=item.get('name');p=ROOT/item.get('path','');seen.add(n)
        if not p.exists():e.append('missing skill '+str(p));continue
        t=p.read_text()
        try:m=fm(t)
        except Exception as ex:e.append(f'{n}: {ex}');continue
        if m.get('name')!=n:e.append(f'{n}: frontmatter mismatch')
        if not 12<=len(m.get('description','').split())<=80:e.append(f'{n}: description size')
        for h in HEAD:
            if h not in t:e.append(f'{n}: missing {h}')
        refs=item.get('references',[])
        if len(refs)!=2:e.append(f'{n}: expected exactly two deep references')
        for ref in refs:
            q=p.parent/ref
            if not q.exists():e.append(f'{n}: missing {ref}')
            elif len(q.read_text().split())<250:e.append(f'{n}: shallow {ref}')
    if seen!=EXPECTED:e.append(f'phase10 registry mismatch missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}')
    rt=ROUTE.read_text()
    for n in EXPECTED:
        if f'`{n}`' not in rt:e.append('routing missing '+n)
    motion=(ROOT/'.codex/skills/motion-direction/SKILL.md').read_text()
    if 'animation-engineering' not in motion or 'future frontend animation specialist' in motion:e.append('motion-direction not handed off to animation-engineering')
    profiles=json.loads((ROOT/'engine/profiles/profiles.json').read_text()).get('profiles',[]);ids={x.get('id') for x in profiles}
    if not {'creative-motion-site','threejs-experience'}<=ids:e.append('creative stack profiles missing')
    owners={o for s in json.loads((ROOT/'engine/knowledge/sources.json').read_text()).get('sources',[]) for o in s.get('owners',[])}
    if not EXPECTED<=owners:e.append('knowledge freshness owner coverage missing '+str(sorted(EXPECTED-owners)))
    bids={json.loads(x)['id'] for x in (ROOT/'evals/behavioral/cases.jsonl').read_text().splitlines() if x.strip()}
    req={'reference-reconstruction','gsap-scroll-production','threejs-product-hero','shader-distortion','gltf-heavy-assets','visual-regression','creative-css-art-direction','reduced-motion-pinned-3d'}
    if not req<=bids:e.append('creative behavioral cases missing '+str(sorted(req-bids)))
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'plan.json';p.write_text(json.dumps({'version':1,'experience':{'creative_thesis':'Product-led spatial narrative','signature_moments':['hero reveal']},'responsive':{'desktop':'pinned product stage','mobile':'normal flow short reveal'},'motion':{'technologies':['gsap'],'scroll_control':'native-with-triggers','reduced_motion':'static product plus immediate content'},'graphics3d':{'enabled':True,'fallback':'product poster','lifecycle_disposal':True,'asset_pipeline':'validated glb','dpr_cap':2},'performance':{'target_devices':['mid mobile','desktop'],'budgets':{'3d_asset_kb':3000},'measurement':'real-device trace and web vitals'},'fallbacks':{'javascript_failure':'content remains readable','advanced_effect_failure':'static media','no_webgl':'product poster'},'qa':{'viewports':['390x844','1440x900'],'states':['initial','hero-complete'],'visual_authority':'approved design dna','baseline_policy':'intentional changes require review'}}))
        run=subprocess.run([sys.executable,str(TOOL),str(p)],capture_output=True,text=True)
        if run.returncode:e.append('creative experience tool smoke failed: '+(run.stderr or run.stdout))
    for marker in ('routing positives','routing negatives','edge cases','quality assertions'):
        if marker not in EVAL.read_text().lower():e.append('phase10 eval missing '+marker)
    if e:return fail(e)
    print('Phase 10 validation PASSED: 7 specialist skills / creative contract / routing / profiles / freshness / behavioral coverage');return 0

def fail(e):
    print('Phase 10 validation FAILED');[print('-',x) for x in e];return 1
if __name__=='__main__':raise SystemExit(main())
