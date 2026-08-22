#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess,sys,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORPUS=ROOT/'benchmarks/corpus.json'
SHA=re.compile(r'^[0-9a-f]{40}$')

def sh(args,cwd=None):
    return subprocess.run(args,cwd=cwd,text=True,capture_output=True)

def corpus():
    return json.loads(CORPUS.read_text())['external']

def validate(items):
    ids=set();errors=[]
    for x in items:
        if x.get('id') in ids: errors.append('duplicate '+str(x.get('id')))
        ids.add(x.get('id'))
        if not SHA.fullmatch(x.get('commit','')): errors.append('unpinned '+str(x.get('id')))
        if '/' not in x.get('repo',''): errors.append('bad repo '+str(x.get('id')))
        expected=x.get('expected_profiles') or x.get('expected_any_profile') or []
        if not expected: errors.append('missing expected profile '+str(x.get('id')))
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--limit',type=int)
    ap.add_argument('--output',default='.artifacts/repository-benchmarks.json')
    ap.add_argument('--validate-corpus',action='store_true')
    n=ap.parse_args()
    items=corpus();errors=validate(items)
    if errors:
        [print(' -',x) for x in errors]
        return 1
    if n.validate_corpus:
        print(f'repository benchmark corpus valid: {len(items)} pinned repos')
        return 0
    items=items[:n.limit] if n.limit else items
    results=[]
    with tempfile.TemporaryDirectory() as td:
        for x in items:
            p=Path(td)/x['id']
            r=sh(['git','clone','--filter=blob:none','--no-checkout',f"https://github.com/{x['repo']}.git",str(p)])
            if r.returncode:
                results.append({'id':x['id'],'passed':False,'error':r.stderr[-1000:]})
                continue
            r=sh(['git','checkout','--detach',x['commit']],p)
            if r.returncode:
                results.append({'id':x['id'],'passed':False,'error':r.stderr[-1000:]})
                continue
            prof=sh([sys.executable,str(ROOT/'scripts/profile_repository.py'),str(p)])
            res=sh([sys.executable,str(ROOT/'scripts/resolve_stack_profile.py'),str(p),'--all'])
            try:
                data=json.loads(res.stdout)
                selected_ids={z.get('id') for z in data.get('selected_profiles',[]) if isinstance(z,dict)}
                top=(data.get('selected') or{}).get('id')
                if top: selected_ids.add(top)
            except Exception:
                data={};selected_ids=set()
            expected=set(x.get('expected_profiles') or [])
            any_expected=set(x.get('expected_any_profile') or [])
            all_ok=(not expected or expected<=selected_ids)
            any_ok=(not any_expected or bool(any_expected & selected_ids))
            passed=prof.returncode==0 and res.returncode==0 and all_ok and any_ok
            results.append({'id':x['id'],'repo':x['repo'],'commit':x['commit'],'selected_profiles':sorted(selected_ids),'expected_profiles':sorted(expected),'expected_any_profile':sorted(any_expected),'confidence':data.get('confidence'),'repository_truncated':data.get('repository_truncated'),'passed':passed,'resolver_rc':res.returncode})
            print(f"[{'PASS' if passed else 'FAIL'}] {x['id']} -> {','.join(sorted(selected_ids)) or 'none'}")
    out={'passed':sum(r['passed'] for r in results),'total':len(results),'results':results}
    op=Path(n.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2)+'\n')
    return 0 if out['passed']==out['total'] else 1

if __name__=='__main__':
    raise SystemExit(main())
