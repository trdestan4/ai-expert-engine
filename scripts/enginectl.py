#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,shutil,time
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[1];MANIFEST=".ai-expert-engine-install.json";START="<!-- AI-EXPERT-ENGINE:START -->";END="<!-- AI-EXPERT-ENGINE:END -->";DIRS=(".codex/skills",".cursor/agents","engine")
def ver():return json.loads((SOURCE/"engine/manifest.json").read_text())["version"]
def digest(data:bytes):return hashlib.sha256(data).hexdigest()
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1048576),b""):h.update(c)
    return h.hexdigest()
def source_block():return f"{START}\n{(SOURCE/'AGENTS.md').read_text().strip()}\n{END}"
def current_block(t):
    p=t/"AGENTS.md"
    if not p.exists():return None
    text=p.read_text()
    if START not in text or END not in text:return None
    return START+text.split(START,1)[1].split(END,1)[0]+END
def snap(t):
    o={}
    for r in DIRS:
        b=t/r
        if b.exists():
            for p in b.rglob("*"):
                if p.is_file():o[p.relative_to(t).as_posix()]=sha(p)
    return o
def drift(t,d):
    f=[]
    for r,h in d.get("files",{}).items():
        p=t/r
        if not p.exists():f.append("missing "+r)
        elif sha(p)!=h:f.append("modified "+r)
    expected=d.get("agents_block_sha256");block=current_block(t)
    if expected and (block is None or digest(block.encode())!=expected):f.append("modified AGENTS managed block")
    return f
def backup(t,paths,include_agents=False):
    b=t/".ai-expert-engine-backup"/(time.strftime("%Y%m%d-%H%M%S")+f"-{time.time_ns()%1000000:06d}")
    for p in paths:
        if not p.exists():continue
        d=b/p.relative_to(t);d.parent.mkdir(parents=True,exist_ok=True)
        if p.is_dir():shutil.copytree(p,d)
        else:shutil.copy2(p,d)
    if include_agents and (t/"AGENTS.md").exists():
        b.mkdir(parents=True,exist_ok=True);shutil.copy2(t/"AGENTS.md",b/"AGENTS.md")
    return b
def write_agents(t):
    p=t/"AGENTS.md";block=source_block();text=p.read_text() if p.exists() else ""
    if START in text and END in text:
        before=text.split(START,1)[0].rstrip();after=text.split(END,1)[1].lstrip();text=(before+"\n\n" if before else "")+block+("\n\n"+after if after else "")+"\n"
    else:text=text.rstrip()+("\n\n" if text.strip() else "")+block+"\n"
    p.write_text(text)
def clean_copy(t):
    for r in DIRS:
        d=t/r
        if d.exists():shutil.rmtree(d)
        d.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(SOURCE/r,d)
def apply(t,force,update):
    t=t.resolve();t.mkdir(parents=True,exist_ok=True)
    if t==SOURCE.resolve():raise SystemExit("refusing to install engine into its own source checkout")
    mp=t/MANIFEST
    if update:
        if not mp.exists():raise SystemExit("not an engine-managed install")
        old=json.loads(mp.read_text());changes=drift(t,old)
        if changes and not force:raise SystemExit("managed install has local drift; run doctor or use --force to back up:\n - "+"\n - ".join(changes))
        if changes and force:backup(t,[t/r for r in DIRS],include_agents=True)
    elif not mp.exists():
        conf=[t/r for r in DIRS if (t/r).exists()]
        if conf and not force:raise SystemExit("managed paths already exist; use --force to back up")
        if conf and force:backup(t,conf,include_agents=True)
    else:raise SystemExit("engine is already installed; use update")
    clean_copy(t);write_agents(t);block=current_block(t) or ""
    mp.write_text(json.dumps({"name":"ai-expert-engine","version":ver(),"managed_dirs":list(DIRS),"files":snap(t),"agents_block_sha256":digest(block.encode())},indent=2)+"\n")
    print(f"engine {ver()} {'updated' if update else 'installed'}")
def doctor(t):
    t=t.resolve();p=t/MANIFEST
    if not p.exists():print("missing install manifest");return 1
    d=json.loads(p.read_text());f=drift(t,d)
    if f:[print(" -",x) for x in f];return 1
    print(f"engine doctor passed: {d.get('version','unknown')}");return 0
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest="cmd",required=True)
    for c in("install","update"):
        p=sp.add_parser(c);p.add_argument("target",nargs="?",default=".");p.add_argument("--force",action="store_true")
    p=sp.add_parser("doctor");p.add_argument("target",nargs="?",default=".");n=ap.parse_args()
    if n.cmd=="install":apply(Path(n.target),n.force,False);return 0
    if n.cmd=="update":apply(Path(n.target),n.force,True);return 0
    return doctor(Path(n.target))
if __name__=="__main__":raise SystemExit(main())
