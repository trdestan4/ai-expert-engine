#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CASES=ROOT/'evals/reviewer-calibration/cases.jsonl';OUT=ROOT/'.artifacts/reviewer-calibration.json'
DOMAIN={'code-reviewer':'code-quality','design-reviewer':'ux-ui-design','security-reviewer':'security','performance-reviewer':'performance','qa-reviewer':'testing-qa','release-reviewer':'release-readiness'}
def load():return [json.loads(x) for x in CASES.read_text().splitlines() if x.strip()]
def extract(t):
    t=str(t);a=t.find('{');b=t.rfind('}')
    if a>=0 and b>a:return json.loads(t[a:b+1])
    raise ValueError('no JSON')
def registry_item(name):
    for p in (ROOT/'engine/registry').glob('*.json'):
        for x in json.loads(p.read_text()).get('skills',[]):
            if x.get('name')==name:return x
    raise KeyError(name)
def skill_context(name):
    item=registry_item(name);skill=ROOT/item['path'];parts=[skill.read_text()]
    for rel in item.get('references',[]):parts.append((skill.parent/rel).read_text())
    return '\n\n'.join(parts)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--validate-corpus',action='store_true');ap.add_argument('--model',default=os.environ.get('CURSOR_EVAL_MODEL','auto'));ap.add_argument('--output',type=Path,default=OUT);n=ap.parse_args();cases=load();reviewers={x['reviewer'] for x in cases}
    if len(cases)<24 or len(reviewers)!=6:raise SystemExit('reviewer calibration corpus invalid')
    if n.validate_corpus:
        for c in cases:
            if c['reviewer'] not in DOMAIN:raise SystemExit('unknown reviewer '+c['reviewer'])
        print(f'reviewer calibration corpus valid: {len(cases)} cases / {len(reviewers)} reviewers');return 0
    if not os.environ.get('CURSOR_API_KEY'):raise SystemExit('CURSOR_API_KEY is required for live reviewer calibration')
    from cursor_sdk import Agent,AgentOptions,LocalAgentOptions
    rows=[];stats=defaultdict(lambda:{'tp':0,'fp':0,'tn':0,'fn':0,'blocker_correct':0,'n':0,'tokens':0});contract=(ROOT/'engine/reviewers/reviewer-contract.md').read_text();contexts={r:skill_context(DOMAIN[r]) for r in reviewers}
    for c in cases:
        profile=(ROOT/'.cursor/agents'/f"{c['reviewer']}.md").read_text();prompt=f"READ ONLY CALIBRATION. Apply this isolated reviewer contract/profile AND EXPERT DOMAIN CONTEXT to the supplied artifact only. Return exactly JSON {{\"finding\":boolean,\"blocker\":boolean,\"severity\":\"critical|high|medium|low|info\",\"reason\":string}}. Do not invent missing evidence. Distinguish a real defect from an intentional/tradeoff-safe pattern.\nCONTRACT:\n{contract}\nPROFILE:\n{profile}\nEXPERT DOMAIN CONTEXT:\n{contexts[c['reviewer']]}\nARTIFACT:\n{c['artifact']}"
        r=Agent.prompt(prompt,AgentOptions(model=n.model,tools=[],local=LocalAgentOptions(cwd=str(ROOT))));u=getattr(r,'usage',None)
        try:x=extract(r.result);finding=bool(x.get('finding'));blocker=bool(x.get('blocker'));sev=str(x.get('severity','')).lower();ok=finding==c['expect_finding'] and (not finding or sev in c['severity_any']) and blocker==c['expect_blocker']
        except Exception as ex:x={'error':repr(ex),'raw':str(getattr(r,'result',r))};finding=False;blocker=False;ok=False
        s=stats[c['reviewer']];s['n']+=1;s['tokens']+=getattr(u,'total_tokens',0) if u else 0
        if c['expect_finding'] and finding:s['tp']+=1
        elif c['expect_finding'] and not finding:s['fn']+=1
        elif not c['expect_finding'] and finding:s['fp']+=1
        else:s['tn']+=1
        if blocker==c['expect_blocker']:s['blocker_correct']+=1
        rows.append({'id':c['id'],'reviewer':c['reviewer'],'passed':ok,'response':x});print(f"[{'PASS' if ok else 'FAIL'}] {c['id']}")
    metrics={}
    for k,s in stats.items():
        precision=s['tp']/(s['tp']+s['fp']) if s['tp']+s['fp'] else 1.0;recall=s['tp']/(s['tp']+s['fn']) if s['tp']+s['fn'] else 1.0
        metrics[k]={**s,'precision':round(precision,3),'recall':round(recall,3),'blocker_accuracy':round(s['blocker_correct']/s['n'],3),'avg_tokens':round(s['tokens']/s['n'],1)}
    out={'passed':sum(x['passed'] for x in rows),'total':len(rows),'metrics':metrics,'results':rows};n.output.parent.mkdir(parents=True,exist_ok=True);n.output.write_text(json.dumps(out,indent=2)+'\n');return 0 if out['passed']==out['total'] else 1
if __name__=='__main__':raise SystemExit(main())
