#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
SKIP={".git","node_modules",".next","dist","build",".venv","venv","coverage",".turbo","vendor","target","bin","obj"}
def read_json(p:Path)->dict[str,Any]:
    try:return json.loads(p.read_text(encoding="utf-8"))
    except Exception:return{}
def collect(root:Path)->dict[str,Any]:
    root=root.resolve();deps={};dep_sources={};files=[];text_signals=[]
    for p in root.rglob("*"):
        rel=p.relative_to(root)
        if any(x in SKIP for x in rel.parts):continue
        if p.is_file():
            rp=rel.as_posix();files.append(rp)
            if p.name=="package.json" and len(rel.parts)<=5:
                pkg=read_json(p)
                for k in("dependencies","devDependencies","peerDependencies"):
                    v=pkg.get(k,{})
                    if isinstance(v,dict):
                        for a,b in v.items():deps[str(a)]=str(b);dep_sources[str(a)]=rp
            if p.suffix in {".tf",".xml",".gradle",".kts",".yaml",".yml"} or p.name in {"Gemfile","go.mod","pyproject.toml","requirements.txt"}:
                try:text_signals.append(p.read_text(encoding="utf-8",errors="ignore")[:20000])
                except Exception:pass
            if len(files)>=12000:break
    sig={"python":any(Path(f).name in("pyproject.toml","requirements.txt") for f in files),"supabase":any(f.startswith("supabase/") for f in files),"vercel":"vercel.json" in files,"go":any(f.endswith("go.mod") for f in files),"jvm":any(Path(f).name in("pom.xml","build.gradle","build.gradle.kts") for f in files),"dotnet":any(f.endswith((".csproj",".sln")) for f in files),"ruby":any(Path(f).name=="Gemfile" for f in files),"terraform":any(f.endswith(".tf") for f in files),"kubernetes":any(Path(f).name in("Chart.yaml","kustomization.yaml","kustomization.yml") for f in files)}
    return {"root":str(root),"dependencies":sorted(deps),"dependency_versions":deps,"dependency_sources":dep_sources,"files":sorted(files),"signals":sig,"text_signals":"\n".join(text_signals)[:300000]}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("root",nargs="?",default=".");ap.add_argument("--output");ns=ap.parse_args();txt=json.dumps(collect(Path(ns.root)),indent=2,ensure_ascii=False)
    Path(ns.output).write_text(txt+"\n",encoding="utf-8") if ns.output else print(txt);return 0
if __name__=="__main__":raise SystemExit(main())
