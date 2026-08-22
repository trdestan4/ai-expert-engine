#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STALE=("future skill","future `","once those skills exist","before those phases are implemented","before those skills are implemented","once implemented")
def known():
    s=set()
    for p in (ROOT/'engine/registry').glob('*.json'):s.update(i['name'] for i in json.loads(p.read_text()).get('skills',[]))
    return s
def files():
    out=list((ROOT/'engine/routing').glob('*.md'))+list((ROOT/'.codex/skills').glob('*/SKILL.md'))+list((ROOT/'engine/policies').glob('*.md'))+list((ROOT/'engine/reviewers').glob('*.md'))+[ROOT/'AGENTS.md']
    return [p for p in out if p.exists()]
def main():
    k=known();e=[]
    for p in files():
        for n,line in enumerate(p.read_text().splitlines(),1):
            refs=set(re.findall(r'`([a-z0-9-]+)`',line));exist=refs&k;low=line.lower()
            if exist and any(x in low for x in STALE):e.append(f'{p.relative_to(ROOT)}:{n}: existing skills described as future: {sorted(exist)}')
            if p.parent==ROOT/'engine/routing':
                for ref in refs:
                    if '-' in ref and ref not in k and not ref.startswith(('r','c')):e.append(f'{p.relative_to(ROOT)}:{n}: unknown skill-like reference `{ref}`')
    if e:print('semantic validation failed:');[print(' -',x) for x in e];return 1
    print(f'semantic validation passed: {len(k)} skills / {len(files())} semantic files');return 0
if __name__=='__main__':raise SystemExit(main())
