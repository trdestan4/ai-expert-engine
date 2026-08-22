#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(*args,cwd=ROOT):return subprocess.run([sys.executable,*map(str,args)],cwd=cwd,text=True,capture_output=True)
def finding(fid,candidate,status='open',expiry=None):
    return {'id':fid,'reviewer':'security-reviewer','candidate':candidate,'title':'Cross-tenant bypass','severity':'high','confidence':'verified','affected_surface':'policy','evidence':'negative test fails','impact':'tenant data exposure','acceptance_condition':'negative test denies access','owner':'identity-access','blocker':True,'status':status,'created_at':datetime.now(timezone.utc).isoformat(),'resolved_at':None,'resolution':None,'risk_expiry':expiry}
def main():
    e=[]
    with tempfile.TemporaryDirectory() as td:
        t=Path(td);state=t/'.ai-expert-engine';(state/'evidence').mkdir(parents=True);(state/'state').mkdir(parents=True)
        route=t/'route.json';route.write_text(json.dumps({'task_id':'T1','intent':'implement','complexity':'C2','risk':'R3','primary_skill':'identity-access','supporting_skills':['database-data'],'reviewers':['security-reviewer'],'loaded_references':[],'reason':'tenant boundary','release_required':False}))
        if run(ROOT/'scripts/runtime_contract.py','routing',route).returncode:e.append('routing contract smoke failed')
        cp=state/'state/checkpoint.json';r=run(ROOT/'scripts/session_checkpoint.py','init','--store',cp,'--task-id','T1','--goal','Preserve tenant isolation','--complexity','C3','--risk','R3','--primary','identity-access','--accept','Cross-tenant access remains denied')
        if r.returncode or run(ROOT/'scripts/session_checkpoint.py','verify','--store',cp,'--task-id','T1','--min-risk','R3').returncode:e.append('checkpoint smoke failed')
        candidate='abcdef1234567890';findingp=t/'finding.json';findingp.write_text(json.dumps(finding('SEC-1',candidate)));store=state/'evidence/reviews.jsonl'
        if run(ROOT/'scripts/review_store.py','add',findingp,'--store',store).returncode:e.append('review store add failed')
        if run(ROOT/'scripts/review_store.py','check-blockers','--store',store,'--candidate',candidate).returncode==0:e.append('open blocker did not block')
        if run(ROOT/'scripts/review_store.py','resolve','SEC-1','--resolution','fixed and negative-tested','--store',store).returncode:e.append('review resolve failed')
        evidence=t/'evidence.txt';evidence.write_text('tests passed for candidate '+candidate);decision=state/'evidence/release-decision.json'
        if run(ROOT/'scripts/build_release_decision.py','--candidate',candidate,'--environment','production','--risk','R3','--decision','GO','--evidence',evidence,'--reviews',store,'--ttl-hours','1','--output',decision,cwd=t).returncode:e.append('release decision build failed')
        if run(ROOT/'scripts/release_gate.py','--decision',decision,'--candidate',candidate,'--environment','production','--reviews',store,cwd=t).returncode:e.append('GO release gate failed')
        if run(ROOT/'scripts/release_gate.py','--decision',decision,'--candidate',candidate,'--environment','staging','--reviews',store,cwd=t).returncode==0:e.append('environment mismatch did not block')
        d=json.loads(decision.read_text());d['expires_at']=(datetime.now(timezone.utc)-timedelta(minutes=1)).isoformat();decision.write_text(json.dumps(d))
        if run(ROOT/'scripts/release_gate.py','--decision',decision,'--candidate',candidate,'--environment','production','--reviews',store,cwd=t).returncode==0:e.append('expired release decision did not block')
        expired=(datetime.now(timezone.utc)-timedelta(minutes=1)).isoformat();findingp.write_text(json.dumps(finding('SEC-2',candidate,'accepted',expired)))
        if run(ROOT/'scripts/review_store.py','add',findingp,'--store',store).returncode:e.append('accepted-risk finding add failed')
        if run(ROOT/'scripts/review_store.py','check-blockers','--store',store,'--candidate',candidate).returncode==0:e.append('expired accepted risk did not reactivate blocker')
        run(ROOT/'scripts/review_store.py','resolve','SEC-2','--resolution','expired risk remediated','--store',store)
        run(ROOT/'scripts/build_release_decision.py','--candidate',candidate,'--environment','production','--risk','R3','--decision','GO','--evidence',evidence,'--reviews',store,'--ttl-hours','1','--output',decision,cwd=t)
        evidence.write_text('tampered evidence')
        if run(ROOT/'scripts/release_gate.py','--decision',decision,'--candidate',candidate,'--environment','production','--reviews',store,cwd=t).returncode==0:e.append('release gate failed to detect evidence tamper')
        big=t/'big';big.mkdir()
        for i in range(4):(big/f'{i}.txt').write_text('x')
        prof=run(ROOT/'scripts/profile_repository.py',big,'--max-files','2')
        try:pd=json.loads(prof.stdout)
        except Exception:pd={}
        if not pd.get('truncated'):e.append('repository profiler failed to expose truncation')
    src=json.loads((ROOT/'engine/knowledge/sources.json').read_text());bench=json.loads((ROOT/'benchmarks/corpus.json').read_text());mig=json.loads((ROOT/'engine/migrations/manifest.json').read_text());profiles=json.loads((ROOT/'engine/profiles/profiles.json').read_text()).get('profiles',[])
    if len(src.get('sources',[]))<25:e.append('knowledge source registry too small')
    if len(bench.get('external',[]))<10 or any(len(x.get('commit',''))!=40 for x in bench.get('external',[])):e.append('benchmark corpus pins invalid or too small')
    if not any(x.get('from')=='1.2.0' and x.get('to')=='1.3.0' for x in mig.get('migrations',[])):e.append('migration chain missing 1.2.0 -> 1.3.0')
    if len(profiles)<20 or len({x.get('dimension') for x in profiles})<5:e.append('stack profile breadth/composition too small')
    if run(ROOT/'scripts/check_knowledge_freshness.py').returncode:e.append('offline knowledge freshness check failed')
    if run(ROOT/'scripts/check_release_enforcement.py','--root',ROOT).returncode:e.append('repository production workflow release enforcement check failed')
    if run(ROOT/'scripts/validate_semantics.py').returncode:e.append('semantic validation failed')
    if run(ROOT/'scripts/validate_master_depth.py').returncode:e.append('master depth validation failed')
    if e:print('runtime hardening validation FAILED');[print(' -',x) for x in e];return 1
    print('runtime hardening validation PASSED');return 0
if __name__=='__main__':raise SystemExit(main())
