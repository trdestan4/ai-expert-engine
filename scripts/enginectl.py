#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,shutil,time
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[1];MANIFEST=".ai-expert-engine-install.json";START="<!-- AI-EXPERT-ENGINE:START -->";END="<!-- AI-EXPERT-ENGINE:END -->";DIRS=(".codex/skills",".cursor/agents","engine")
def ver():return json.loads((SOURCE/"engine/manifest.json").read_text())["version"]
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1048576),b""):h.update(c)
    return h.hexdigest()
def snap(t):
    o={}
    for r in DIRS:
        b=t/r
        if b.exists():
            for p in b.rglob("*"):
                if p.is_file():o[p.relative_to(t).as_posix()]=sha(p)
    return o
def agents(t):
    p=t/"AGENTS.md";block=f"{START}\n{(SOURCE/'AGENTS.md').read_text().strip()}\n{END}";text=p.read_text() if p.exists() else ""
    if START in text and END in text:
        before=text.split(START,1)[0].rstrip();after=text.split(END,1)[1].lstrip();text=(before+"\n\n" if before else "")+block+("\n\n"+after if after else "")+"\n"
    else:text=text.rstrip()+("\n\n" if text.strip() else "")+block+"\n"
    p.write_text(text)
def apply(t,force,update):
    t=t.resolve();t.mkdir(parents=True,exist_ok=True)
    if update and not (t/MANIFEST).exists():raise SystemExit("not an engine-managed install")
    if not (t/MANIFEST).exists():
        conf=[t/r for r in DIRS if (t/r).exists()]
        if conf and not force:raise SystemExit("managed paths already exist; use --force to back up")
        if conf:
            b=t/".ai-expert-engine-backup"/time.strftime("%Y%m%d-%H%M%S")
            for p in conf:
                d=b/p.relative_to(t);d.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(p),str(d))
    for r in DIRS:
        d=t/r;d.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(SOURCE/r,d,dirs_exist_ok=True)
    agents(t);(t/MANIFEST).write_text(json.dumps({"name":"ai-expert-engine","version":ver(),"managed_dirs":list(DIRS),"files":snap(t)},indent=2)+"\n");print(f"engine {ver()} {'updated' if update else 'installed'}")
def doctor(t):
    t=t.resolve();p=t/MANIFEST
    if not p.exists():print("missing install manifest");return 1
    d=json.loads(p.read_text());f=[]
    for r,h in d["files"].items():
        q=t/r
        if not q.exists():f.append("missing "+r)
        elif sha(q)!=h:f.append("modified "+r)
    a=(t/"AGENTS.md").read_text() if (t/"AGENTS.md").exists() else ""
    if START not in a or END not in a:f.append("AGENTS block missing")
    if f:[print(" -",x) for x in f];return 1
    print("engine doctor passed");return 0
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest="cmd",required=True)
    for c in("install","update"):
        p=sp.add_parser(c);p.add_argument("target",nargs="?",default=".");p.add_argument("--force",action="store_true")
    p=sp.add_parser("doctor");p.add_argument("target",nargs="?",default=".");n=ap.parse_args()
    if n.cmd=="install":apply(Path(n.target),n.force,False);return 0
    if n.cmd=="update":apply(Path(n.target),n.force,True);return 0
    return doctor(Path(n.target))
if __name__=="__main__":raise SystemExit(main())
