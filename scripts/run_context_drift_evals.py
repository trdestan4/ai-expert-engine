#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CASES=ROOT/'evals/context-drift/cases.json';OUT=ROOT/'.artifacts/context-drift.json'
def extract(t):
    t=str(t).strip();a=t.find('{');b=t.rfind('}')
    if a>=0 and b>a:return json.loads(t[a:b+1])
    raise ValueError('no JSON')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--validate-corpus',action='store_true');ap.add_argument('--model',default=os.environ.get('CURSOR_EVAL_MODEL','auto'));ap.add_argument('--output',type=Path,default=OUT);n=ap.parse_args();d=json.loads(CASES.read_text());cases=d.get('cases',[])
    if len(cases)<3 or any(len(x.get('distractors',[]))<5 for x in cases):raise SystemExit('context-drift corpus invalid')
    if n.validate_corpus:print(f'context-drift corpus valid: {len(cases)} cases');return 0
    if not os.environ.get('CURSOR_API_KEY'):raise SystemExit('CURSOR_API_KEY is required for live context-drift evals')
    from cursor_sdk import Agent,LocalAgentOptions
    results=[]
    for c in cases:
        with Agent.create(model=n.model,api_key=os.environ['CURSOR_API_KEY'],local=LocalAgentOptions(cwd=str(ROOT))) as agent:
            initial=f"READ ONLY. We are starting task {c['id']}. Goal: {c['goal']} Complexity {c['complexity']}, risk {c['risk']}, primary owner {c['primary']}. Hard constraint: {c['constraint']} Preserve these facts through the session. Reply ACK only."
            agent.send(initial).wait()
            for q in c['distractors']:agent.send('READ ONLY side discussion: '+q+' Do not replace the active task checkpoint.').wait()
            r=agent.send('Return exactly JSON with task_id, complexity, risk, primary_skill, constraint. Do not inspect files; recall the active task checkpoint.').wait();raw=r.result
            try:x=extract(raw);ok=x.get('task_id')==c['id'] and x.get('complexity')==c['complexity'] and x.get('risk')==c['risk'] and x.get('primary_skill')==c['primary'] and c['constraint'].lower() in str(x.get('constraint','')).lower()
            except Exception as ex:x={'error':repr(ex),'raw':str(raw)};ok=False
            u=getattr(r,'usage',None);results.append({'id':c['id'],'passed':ok,'response':x,'tokens':getattr(u,'total_tokens',None)});print(f"[{'PASS' if ok else 'FAIL'}] {c['id']}")
    out={'passed':sum(x['passed'] for x in results),'total':len(results),'results':results};n.output.parent.mkdir(parents=True,exist_ok=True);n.output.write_text(json.dumps(out,indent=2)+'\n');return 0 if out['passed']==out['total'] else 1
if __name__=='__main__':raise SystemExit(main())
