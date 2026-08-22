#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
SKIP={".git","node_modules",".next","dist","build",".venv","venv","coverage",".turbo"}
def read_json(p:Path)->dict[str,Any]:
    try:return json.loads(p.read_text(encoding="utf-8"))
    except Exception:return{}
def collect(root:Path)->dict[str,Any]:
    pkg=read_json(root/"package.json");deps={}
    for k in("dependencies","devDependencies","peerDependencies"):
        v=pkg.get(k,{})
        if isinstance(v,dict):deps.update({str(a):str(b) for a,b in v.items()})
    fs=[]
    for p in root.rglob("*"):
        rel=p.relative_to(root)
        if any(x in SKIP for x in rel.parts):continue
        if p.is_file():
            fs.append(rel.as_posix())
            if len(fs)>=8000:break
    return {"root":str(root.resolve()),"dependencies":sorted(deps),"dependency_versions":deps,"files":sorted(fs),"signals":{"python":(root/"pyproject.toml").exists() or (root/"requirements.txt").exists(),"supabase":(root/"supabase").exists(),"vercel":(root/"vercel.json").exists()}}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("root",nargs="?",default=".");ap.add_argument("--output");ns=ap.parse_args();txt=json.dumps(collect(Path(ns.root)),indent=2,ensure_ascii=False)
    Path(ns.output).write_text(txt+"\n",encoding="utf-8") if ns.output else print(txt);return 0
if __name__=="__main__":raise SystemExit(main())
