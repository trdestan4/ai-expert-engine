#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STALE=("future ","future `","once those skills exist","before those phases are implemented","before those skills are implemented","once implemented")
def known():
    s=set()
    for p in (ROOT/"engine/registry").glob("*.json"):s.update(i["name"] for i in json.loads(p.read_text()).get("skills",[]))
    return s
def main():
    k=known();e=[]
    for p in (ROOT/"engine/routing").glob("*.md"):
        for n,line in enumerate(p.read_text().splitlines(),1):
            refs=set(re.findall(r"`([a-z0-9-]+)`",line));exist=refs&k;low=line.lower()
            if exist and any(x in low for x in STALE):e.append(f"{p.relative_to(ROOT)}:{n}: existing skills described as future: {sorted(exist)}")
            for ref in refs:
                if "-" in ref and ref not in k:e.append(f"{p.relative_to(ROOT)}:{n}: unknown skill-like reference `{ref}`")
    if e:
        print("semantic routing validation failed:");[print(" -",x) for x in e];return 1
    print(f"semantic routing validation passed: {len(k)} skills");return 0
if __name__=="__main__":raise SystemExit(main())
