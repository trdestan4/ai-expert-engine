#!/usr/bin/env python3
"""Validate Phase 01 creative/product skill structure without third-party packages."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'engine/registry/phase-01-skills.json'
REQ=['# Purpose','## Use when','## Do not use when','## Inputs','## Workflow','## Decision rules','## Reference routing','## Quality gates','## Failure handling','## Output contract']
NAME=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
EXPECTED={'product-strategy','creative-director','brand-design','anti-generic-design','color-intelligence','typography-intelligence','visual-art-direction','motion-direction','ux-ui-design'}
def fm(text):
    if not text.startswith('---\n'): raise ValueError('missing frontmatter')
    end=text.find('\n---\n',4)
    if end<0: raise ValueError('unterminated frontmatter')
    out={}
    for line in text[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip().strip('"\'')
    return out
def main():
    errors=[]
    try: data=json.loads(REG.read_text())
    except Exception as e: print('FAILED:',e); return 1
    seen=set()
    descriptions=[]
    for item in data.get('skills',[]):
        name=item.get('name',''); path=ROOT/item.get('path','')
        if name in seen: errors.append(f'duplicate: {name}')
        seen.add(name)
        if not NAME.fullmatch(name): errors.append(f'invalid name: {name}')
        if path.parent.name!=name: errors.append(f'folder/name mismatch: {path.parent.name} != {name}')
        if not path.exists(): errors.append(f'missing skill: {path}'); continue
        text=path.read_text(); meta=fm(text)
        if meta.get('name')!=name: errors.append(f'{name}: frontmatter mismatch')
        desc=meta.get('description','')
        words=len(desc.split())
        if words<12 or words>80: errors.append(f'{name}: description routing budget {words}')
        descriptions.append((name,set(re.findall(r'[a-z]{4,}',desc.lower()))))
        for h in REQ:
            if h not in text: errors.append(f'{name}: missing {h}')
        if len(text.split())>2200: errors.append(f'{name}: SKILL too large')
        for ref in item.get('references',[]):
            if not (path.parent/ref).exists(): errors.append(f'{name}: missing ref {ref}')
    if seen!=EXPECTED: errors.append(f'registry set mismatch: missing={sorted(EXPECTED-seen)} extra={sorted(seen-EXPECTED)}')
    for i,(a,wa) in enumerate(descriptions):
        for b,wb in descriptions[i+1:]:
            union=wa|wb
            if union and len(wa&wb)/len(union)>0.72: errors.append(f'possible routing overlap: {a} / {b}')
    policy=(ROOT/'engine/policies/design-quality.md')
    if not policy.exists(): errors.append('missing design-quality policy')
    if errors:
        print('Phase 01 validation FAILED')
        for e in errors: print('-',e)
        return 1
    print('Phase 01 validation PASSED')
    return 0
if __name__=='__main__': sys.exit(main())