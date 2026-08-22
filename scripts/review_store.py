#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DEFAULT=Path(".ai-expert-engine/evidence/reviews.jsonl")
def load(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.exists() else[]
def save(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in rows))
def valid(f):return subprocess.run([sys.executable,str(ROOT/"scripts/runtime_contract.py"),"reviewer-finding",str(f),"--quiet"]).returncode==0
def add(n):
    p=Path(n.store);x=json.loads(Path(n.finding).read_text());rows=load(p)
    if any(r["id"]==x["id"] for r in rows):raise SystemExit("duplicate finding id")
    if not valid(Path(n.finding)):raise SystemExit("finding contract failed")
    rows.append(x);save(p,rows);print(x["id"]);return 0
def update(n,status):
    p=Path(n.store);rows=load(p);found=False;now=datetime.now(timezone.utc).isoformat()
    for x in rows:
        if x["id"]==n.id:
            x["status"]=status;x["resolved_at"]=now;x["resolution"]=n.resolution
            if status=="accepted":x["risk_expiry"]=n.expiry
            found=True
    if not found:raise SystemExit("finding not found")
    tmp=p.parent/".finding-check.json"
    for x in rows:
        tmp.write_text(json.dumps(x));
        if not valid(tmp):tmp.unlink(missing_ok=True);raise SystemExit("updated finding contract failed")
    tmp.unlink(missing_ok=True);save(p,rows);return 0
def blockers(p,candidate=None):
    rows=load(Path(p));b=[x for x in rows if x.get("blocker") and x.get("status")=="open" and (not candidate or x.get("candidate")==candidate)]
    print(json.dumps(b,indent=2));return 1 if b else 0
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest="cmd",required=True)
    a=sp.add_parser("add");a.add_argument("finding");a.add_argument("--store",default=str(DEFAULT))
    for c in("resolve","accept"):
        x=sp.add_parser(c);x.add_argument("id");x.add_argument("--resolution",required=True);x.add_argument("--expiry");x.add_argument("--store",default=str(DEFAULT))
    l=sp.add_parser("list");l.add_argument("--store",default=str(DEFAULT));l.add_argument("--status")
    b=sp.add_parser("check-blockers");b.add_argument("--store",default=str(DEFAULT));b.add_argument("--candidate")
    n=ap.parse_args()
    if n.cmd=="add":return add(n)
    if n.cmd=="resolve":return update(n,"resolved")
    if n.cmd=="accept":
        if not n.expiry:raise SystemExit("accepted risk requires --expiry")
        return update(n,"accepted")
    if n.cmd=="check-blockers":return blockers(n.store,n.candidate)
    rows=load(Path(n.store));rows=[x for x in rows if not n.status or x.get("status")==n.status];print(json.dumps(rows,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
