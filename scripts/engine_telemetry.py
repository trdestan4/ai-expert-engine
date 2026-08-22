#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,statistics,subprocess,sys
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DEFAULT=Path(".ai-expert-engine/telemetry/events.jsonl")
def arr(v):return [x for x in (v or []) if x]
def record(n):
    event={"timestamp":datetime.now(timezone.utc).isoformat(),"session_id":n.session_id,"task_id":n.task_id,"event":n.event,"complexity":n.complexity,"risk":n.risk,"primary_skill":n.primary,"supporting_skills":arr(n.supporting),"reviewers":arr(n.reviewers),"loaded_references":arr(n.references),"activation_width":1+len(arr(n.supporting))+len(arr(n.reviewers)),"prompt_tokens":n.prompt_tokens,"completion_tokens":n.completion_tokens,"context_tokens":n.context_tokens,"duration_ms":n.duration_ms,"outcome":n.outcome,"notes":n.notes}
    tmp=Path(".ai-expert-engine/telemetry/.validate.json");tmp.parent.mkdir(parents=True,exist_ok=True);tmp.write_text(json.dumps(event))
    rc=subprocess.run([sys.executable,str(ROOT/"scripts/runtime_contract.py"),"runtime-telemetry",str(tmp),"--quiet"]).returncode;tmp.unlink(missing_ok=True)
    if rc:return rc
    p=Path(n.store);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("a",encoding="utf-8") as f:f.write(json.dumps(event,ensure_ascii=False)+"\n")
    print(json.dumps(event,indent=2));return 0
def summary(p):
    rows=[json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()] if Path(p).exists() else[]
    if not rows:print("no telemetry");return 0
    widths=[x["activation_width"] for x in rows];ctx=[x["context_tokens"] for x in rows if x.get("context_tokens") is not None];freq=Counter()
    for x in rows:
        for s in [x["primary_skill"]]+x.get("supporting_skills",[]):freq[s]+=1
    r3=[x for x in rows if x["risk"] in("R3","R4")];miss=[x["task_id"] for x in r3 if not x.get("reviewers")]
    out={"events":len(rows),"avg_activation_width":round(statistics.mean(widths),2),"max_activation_width":max(widths),"avg_context_tokens":round(statistics.mean(ctx),1) if ctx else None,"top_skills":freq.most_common(12),"r3_r4_events":len(r3),"r3_r4_without_reviewers":miss}
    print(json.dumps(out,indent=2));return 1 if miss else 0
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest="cmd",required=True)
    r=sp.add_parser("record");r.add_argument("--store",default=str(DEFAULT));r.add_argument("--session-id");r.add_argument("--task-id",required=True);r.add_argument("--event",choices=["route","review","verify","release","checkpoint","eval"],default="route");r.add_argument("--complexity",choices=["C0","C1","C2","C3","C4"],required=True);r.add_argument("--risk",choices=["R0","R1","R2","R3","R4"],required=True);r.add_argument("--primary",required=True);r.add_argument("--supporting",action="append");r.add_argument("--reviewers",action="append");r.add_argument("--references",action="append");r.add_argument("--prompt-tokens",type=int);r.add_argument("--completion-tokens",type=int);r.add_argument("--context-tokens",type=int);r.add_argument("--duration-ms",type=int);r.add_argument("--outcome",choices=["success","failure","hold","no-go","unknown"],default="unknown");r.add_argument("--notes")
    s=sp.add_parser("summary");s.add_argument("--store",default=str(DEFAULT));n=ap.parse_args();return record(n) if n.cmd=="record" else summary(n.store)
if __name__=="__main__":raise SystemExit(main())
