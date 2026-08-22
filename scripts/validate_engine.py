#!/usr/bin/env python3
"""Cross-phase structural, semantic, runtime-hardening and CI validation."""
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/'engine/manifest.json';SKILLS=ROOT/'.codex/skills';README=ROOT/'README.md'
HEADINGS=['# Purpose','## Use when','## Do not use when','## Inputs','## Workflow','## Decision rules','## Reference routing','## Quality gates','## Failure handling','## Output contract'];REF_RE=re.compile(r'references/[a-z0-9-]+\.md');SHA=re.compile(r'^[0-9a-f]{40}$');USES=re.compile(r'^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)',re.M)
def fm(t):
    if not t.startswith('---\n'):raise ValueError('missing YAML frontmatter')
    end=t.find('\n---\n',4)
    if end<0:raise ValueError('unterminated YAML frontmatter')
    d={}
    for raw in t[4:end].splitlines():
        line=raw.strip()
        if line and not line.startswith('#'):
            if ':' not in line:raise ValueError('invalid frontmatter line')
            k,v=line.split(':',1);d[k.strip()]=v.strip().strip("\"'")
    return d
def validate():
    e=[];required=[MANIFEST,SKILLS,README,ROOT/'.github/workflows/validate-skills.yml',ROOT/'evals/master-regression.md',ROOT/'evals/behavioral/cases.jsonl',ROOT/'evals/context-drift/cases.json',ROOT/'evals/reviewer-calibration/cases.jsonl',ROOT/'engine/reviewers/reviewer-contract.md',ROOT/'engine/profiles/profiles.json',ROOT/'engine/runtime/contracts.json',ROOT/'engine/knowledge/sources.json',ROOT/'benchmarks/corpus.json',ROOT/'engine/migrations/manifest.json',ROOT/'docs/INSTALL.md']
    for p in required:
        if not p.exists():e.append('missing engine artifact: '+str(p.relative_to(ROOT)))
    if e:return e
    try:m=json.loads(MANIFEST.read_text())
    except Exception as ex:return ['invalid engine manifest: '+str(ex)]
    if m.get('version')!='1.2.0' or m.get('status')!='hardened':e.append('manifest must declare v1.2.0 hardened')
    ids=[str(p.get('id')) for p in m.get('phases',[])]
    if ids!=[f'{i:02d}' for i in range(10)]:e.append('manifest phases must be 00..09 in order')
    registered={};total_refs=0
    for phase in m.get('phases',[]):
        rp=ROOT/phase.get('registry','')
        if not rp.exists():e.append('missing registry '+str(rp));continue
        try:r=json.loads(rp.read_text())
        except Exception as ex:e.append(f'invalid registry {rp}: {ex}');continue
        for item in r.get('skills',[]):
            name=item.get('name','');p=ROOT/item.get('path','')
            if name in registered:e.append('duplicate registered skill '+name);continue
            registered[name]=p
            if not p.exists():e.append('missing skill '+str(p));continue
            text=p.read_text()
            try:meta=fm(text)
            except ValueError as ex:e.append(f'{p.relative_to(ROOT)}: {ex}');continue
            if meta.get('name')!=name:e.append(f'{name}: frontmatter mismatch')
            for h in HEADINGS:
                if h not in text:e.append(f'{name}: missing {h}')
            refs=set(item.get('references',[]));called=set(REF_RE.findall(text));total_refs+=len(refs)
            if refs!=called:e.append(f'{name}: registered/called refs differ registered={sorted(refs)} called={sorted(called)}')
            for ref in refs:
                q=p.parent/ref
                if not q.exists():e.append(f'{name}: missing {ref}')
                elif not 80<=len(q.read_text().split())<=1800:e.append(f'{name}: reference size invalid {ref}')
    physical={p.name for p in SKILLS.iterdir() if p.is_dir() and (p/'SKILL.md').exists()}
    if physical!=set(registered):e.append('skill registry/physical mismatch')
    if len(registered)!=43 or m.get('expected_skill_count')!=43:e.append('discoverable skill count must remain 43')
    if total_refs<70:e.append(f'reference depth unexpectedly low: {total_refs}')
    jsons=list((ROOT/'engine/registry').glob('*.json'))+list((ROOT/'engine/schemas').glob('*.json'))+[MANIFEST,ROOT/'engine/profiles/profiles.json',ROOT/'engine/governance/github.json',ROOT/'engine/runtime/contracts.json',ROOT/'engine/knowledge/sources.json',ROOT/'benchmarks/corpus.json',ROOT/'engine/migrations/manifest.json']
    for p in jsons:
        try:json.loads(p.read_text())
        except Exception as ex:e.append(f'invalid JSON {p.relative_to(ROOT)}: {ex}')
    readme=README.read_text()
    for i in range(10):
        if f'Phase {i:02d}' not in readme:e.append(f'README missing Phase {i:02d}')
    if 'AI Expert Engine v1.2' not in readme:e.append('README missing v1.2 marker')
    required_validators={'validate_core.py','validate_engine.py','validate_hardening.py','validate_semantics.py','validate_runtime_hardening.py'}|{f'validate_phase{i:02d}.py' for i in range(1,10)};actual={p.name for p in (ROOT/'scripts').glob('validate_*.py')}
    if not required_validators<=actual:e.append('validator set missing '+str(sorted(required_validators-actual)))
    for wf in sorted((ROOT/'.github/workflows').glob('*.yml'))+sorted((ROOT/'.github/workflows').glob('*.yaml')):
        for action,version in USES.findall(wf.read_text()):
            if not action.startswith('./') and not SHA.fullmatch(version):e.append(f'{wf.relative_to(ROOT)} action not SHA-pinned: {action}@{version}')
    profiles=json.loads((ROOT/'engine/profiles/profiles.json').read_text()).get('profiles',[])
    if len(profiles)<20:e.append('need >=20 stack profiles')
    expected=set(m.get('reviewers',[]));actual_reviewers={p.stem for p in (ROOT/'.cursor/agents').glob('*.md')}
    if expected!=actual_reviewers:e.append('isolated reviewer set mismatch')
    accidental=[p.name for p in ROOT.iterdir() if p.name.lower().startswith(('noop','dummy','tmp'))]
    if accidental:e.append('accidental root artifacts '+str(accidental))
    return e
def main():
    e=validate()
    if e:print('Engine validation FAILED');[print('-',x) for x in e];return 1
    print('Engine validation PASSED');return 0
if __name__=='__main__':sys.exit(main())
