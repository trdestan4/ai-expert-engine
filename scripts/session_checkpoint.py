#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DEFAULT=Path('.ai-expert-engine/state/checkpoint.json')
def now():return datetime.now(timezone.utc).isoformat()
def check(p):return subprocess.run([sys.executable,str(ROOT/'scripts/runtime_contract.py'),'session-checkpoint',str(p),'--quiet']).returncode
def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');
    if check(p):raise SystemExit('checkpoint contract failed')
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='cmd',required=True)
    i=sp.add_parser('init');i.add_argument('--store',default=str(DEFAULT));i.add_argument('--task-id',required=True);i.add_argument('--goal',required=True);i.add_argument('--complexity',required=True,choices=['C0','C1','C2','C3','C4']);i.add_argument('--risk',required=True,choices=['R0','R1','R2','R3','R4']);i.add_argument('--primary',required=True);i.add_argument('--supporting',action='append');i.add_argument('--accept',action='append',required=True);i.add_argument('--constraint',action='append');i.add_argument('--phase',default='planned')
    u=sp.add_parser('update');u.add_argument('--store',default=str(DEFAULT));u.add_argument('--phase');u.add_argument('--decision',action='append');u.add_argument('--unresolved',action='append');u.add_argument('--clear-unresolved',action='store_true')
    s=sp.add_parser('show');s.add_argument('--store',default=str(DEFAULT))
    v=sp.add_parser('verify');v.add_argument('--store',default=str(DEFAULT));v.add_argument('--task-id');v.add_argument('--min-risk',choices=['R0','R1','R2','R3','R4'])
    n=ap.parse_args();p=Path(n.store)
    if n.cmd=='init':
        d={'version':1,'task_id':n.task_id,'goal':n.goal,'complexity':n.complexity,'risk':n.risk,'primary_skill':n.primary,'supporting_skills':n.supporting or[],'acceptance_criteria':n.accept,'constraints':n.constraint or[],'decisions':[],'unresolved':[],'phase':n.phase,'updated_at':now()};save(p,d);print(p);return 0
    if not p.exists():print('checkpoint missing');return 2
    d=json.loads(p.read_text())
    if n.cmd=='show':print(json.dumps(d,indent=2,ensure_ascii=False));return check(p)
    if n.cmd=='update':
        if n.phase:d['phase']=n.phase
        d['decisions']+=n.decision or[]
        if n.clear_unresolved:d['unresolved']=[]
        d['unresolved']+=n.unresolved or[];d['updated_at']=now();save(p,d);return 0
    if n.task_id and d['task_id']!=n.task_id:print('checkpoint task mismatch');return 3
    if n.min_risk and int(d['risk'][1])<int(n.min_risk[1]):print('checkpoint risk below required floor');return 4
    return check(p)
if __name__=='__main__':raise SystemExit(main())
