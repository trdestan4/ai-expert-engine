#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys,tempfile
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(*args,cwd=ROOT):return subprocess.run([sys.executable,*map(str,args)],cwd=cwd,text=True,capture_output=True)
def main():
    e=[]
    with tempfile.TemporaryDirectory() as td:
        t=Path(td);state=t/'.ai-expert-engine';(state/'evidence').mkdir(parents=True);(state/'state').mkdir(parents=True)
        route=t/'route.json';route.write_text(json.dumps({'task_id':'T1','intent':'implement','complexity':'C2','risk':'R3','primary_skill':'identity-access','supporting_skills':['database-data'],'reviewers':['security-reviewer'],'loaded_references':[],'reason':'tenant boundary','release_required':False}))
        if run(ROOT/'scripts/runtime_contract.py','routing',route).returncode:e.append('routing contract smoke failed')
        cp=state/'state/checkpoint.json';r=run(ROOT/'scripts/session_checkpoint.py','init','--store',cp,'--task-id','T1','--goal','Preserve tenant isolation','--complexity','C3','--risk','R3','--primary','identity-access','--accept','Cross-tenant access remains denied')
        if r.returncode or run(ROOT/'scripts/session_checkpoint.py','verify','--store',cp,'--task-id','T1','--min-risk','R3').returncode:e.append('checkpoint smoke failed')
        finding=t/'finding.json';finding.write_text(json.dumps({'id':'SEC-1','reviewer':'security-reviewer','candidate':'abcdef1234567890','title':'Cross-tenant bypass','severity':'high','confidence':'verified','affected_surface':'policy','evidence':'negative test fails','impact':'tenant data exposure','acceptance_condition':'negative test denies access','owner':'identity-access','blocker':True,'status':'open','created_at':datetime.now(timezone.utc).isoformat(),'resolved_at':None,'resolution':None,'risk_expiry':None}))
        store=state/'evidence/reviews.jsonl'
        if run(ROOT/'scripts/review_store.py','add',finding,'--store',store).returncode:e.append('review store add failed')
        if run(ROOT/'scripts/review_store.py','check-blockers','--store',store,'--candidate','abcdef1234567890').returncode==0:e.append('open blocker did not block')
        if run(ROOT/'scripts/review_store.py','resolve','SEC-1','--resolution','fixed and negative-tested','--store',store).returncode:e.append('review resolve failed')
        if run(ROOT/'scripts/review_store.py','check-blockers','--store',store,'--candidate','abcdef1234567890').returncode:e.append('resolved blocker still blocks')
        evidence=t/'evidence.txt';evidence.write_text('tests passed for candidate abcdef1234567890');decision=state/'evidence/release-decision.json'
        if run(ROOT/'scripts/build_release_decision.py','--candidate','abcdef1234567890','--environment','production','--risk','R3','--decision','GO','--evidence',evidence,'--reviews',store,'--output',decision,cwd=t).returncode:e.append('release decision build failed')
        if run(ROOT/'scripts/release_gate.py','--decision',decision,'--candidate','abcdef1234567890','--reviews',store,cwd=t).returncode:e.append('GO release gate failed')
        evidence.write_text('tampered evidence')
        if run(ROOT/'scripts/release_gate.py','--decision',decision,'--candidate','abcdef1234567890','--reviews',store,cwd=t).returncode==0:e.append('release gate failed to detect evidence tamper')
    src=json.loads((ROOT/'engine/knowledge/sources.json').read_text());bench=json.loads((ROOT/'benchmarks/corpus.json').read_text());mig=json.loads((ROOT/'engine/migrations/manifest.json').read_text());profiles=json.loads((ROOT/'engine/profiles/profiles.json').read_text()).get('profiles',[])
    if len(src.get('sources',[]))<10:e.append('knowledge source registry too small')
    if len(bench.get('external',[]))<4 or any(len(x.get('commit',''))!=40 for x in bench.get('external',[])):e.append('benchmark corpus pins invalid')
    if not any(x.get('from')=='1.1.0' and x.get('to')=='1.2.0' for x in mig.get('migrations',[])):e.append('migration chain missing 1.1.0 -> 1.2.0')
    if len(profiles)<20:e.append('stack profile breadth too small')
    if run(ROOT/'scripts/check_knowledge_freshness.py').returncode:e.append('offline knowledge freshness check failed')
    if run(ROOT/'scripts/check_release_enforcement.py','--root',ROOT).returncode:e.append('repository production workflow release enforcement check failed')
    if e:print('runtime hardening validation FAILED');[print(' -',x) for x in e];return 1
    print('runtime hardening validation PASSED');return 0
if __name__=='__main__':raise SystemExit(main())
