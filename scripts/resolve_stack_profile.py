#!/usr/bin/env python3
from __future__ import annotations
import argparse,fnmatch,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"scripts"))
from profile_repository import collect
def fm(files,pat):return any(fnmatch.fnmatch(f,pat) for f in files)
def score(p,f):
    m=p.get("match",{});deps=set(f["dependencies"]);files=f["files"];txt=f.get("text_signals","").lower();s=int(p.get("priority",0));why=[]
    a=m.get("dependencies_all",[])
    if a and not all(x in deps for x in a):return -1,[]
    if a:s+=30*len(a);why.append("dependencies_all")
    for key,weight in (("dependencies_any",15),("files_any",8),("text_signals_any",6)):
        a=m.get(key,[])
        if a:
            if key=="dependencies_any":h=[x for x in a if x in deps]
            elif key=="files_any":h=[x for x in a if fm(files,x)]
            else:h=[x for x in a if x.lower() in txt]
            if not h:return -1,[]
            s+=weight*len(h);why.append(key+":"+",".join(h[:4]))
    return s,why
def main():
    ap=argparse.ArgumentParser();ap.add_argument("root",nargs="?",default=".");ap.add_argument("--all",action="store_true");ns=ap.parse_args();ps=json.loads((ROOT/"engine/profiles/profiles.json").read_text())["profiles"];f=collect(Path(ns.root));r=[]
    for p in ps:
        s,w=score(p,f)
        if s>=0:r.append({"id":p["id"],"score":s,"reasons":w,"owners":p["owners"],"conditional":p["conditional"],"defaults":p["defaults"]})
    r.sort(key=lambda x:(-x["score"],x["id"]));print(json.dumps({"selected":r[0] if r else None,"candidates":r if ns.all else r[:5]},indent=2));return 0 if r else 2
if __name__=="__main__":raise SystemExit(main())
