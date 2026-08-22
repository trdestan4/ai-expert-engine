#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path);ns=ap.parse_args();s={}
    for rp in (ROOT/"engine/registry").glob("*.json"):
        d=json.loads(rp.read_text());ph=d.get("phase",rp.stem)
        for i in d.get("skills",[]):s[i["name"]]={"phase":ph,"path":i["path"],"routing_mentions":[]}
    for r in (ROOT/"engine/routing").glob("*.md"):
        t=r.read_text()
        for n in s:
            if re.search(rf"`{re.escape(n)}`",t):s[n]["routing_mentions"].append(r.name)
    txt=json.dumps({"skill_count":len(s),"skills":dict(sorted(s.items()))},indent=2);ns.output.write_text(txt+"\n") if ns.output else print(txt);return 0
if __name__=="__main__":raise SystemExit(main())
