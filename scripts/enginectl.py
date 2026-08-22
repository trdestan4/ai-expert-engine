#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,shutil,time
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[1];MANIFEST='.ai-expert-engine-install.json';START='<!-- AI-EXPERT-ENGINE:START -->';END='<!-- AI-EXPERT-ENGINE:END -->'
DIRS=('.codex/skills','.cursor/agents','engine')
FILES=('scripts/enginectl.py','scripts/runtime_contract.py','scripts/engine_telemetry.py','scripts/review_store.py','scripts/release_gate.py','scripts/build_release_decision.py','scripts/session_checkpoint.py','scripts/check_release_enforcement.py','scripts/profile_repository.py','scripts/resolve_stack_profile.py','scripts/check_knowledge_freshness.py','.github/workflows/ai-expert-release-gate.yml')
def version():return json.loads((SOURCE/'engine/manifest.json').read_text())['version']
def digest(data):return hashlib.sha256(data).hexdigest()
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1048576),b''):h.update(c)
    return h.hexdigest()
def source_block():return f"{START}\n{(SOURCE/'AGENTS.md').read_text().strip()}\n{END}"
def current_block(t):
    p=t/'AGENTS.md'
    if not p.exists():return None
    text=p.read_text()
    if START not in text or END not in text:return None
    return START+text.split(START,1)[1].split(END,1)[0]+END
def managed_paths(t,old=None):
    rel=list(DIRS)+list(FILES)
    if old:rel+=old.get('managed_dirs',[])+old.get('managed_files',[])
    return [t/r for r in dict.fromkeys(rel)]
def snapshot(t):
    out={}
    for r in DIRS:
        b=t/r
        if b.exists():
            for p in b.rglob('*'):
                if p.is_file():out[p.relative_to(t).as_posix()]=sha(p)
    for r in FILES:
        p=t/r
        if p.exists():out[r]=sha(p)
    return out
def drift(t,d):
    f=[]
    for r,h in d.get('files',{}).items():
        p=t/r
        if not p.exists():f.append('missing '+r)
        elif sha(p)!=h:f.append('modified '+r)
    expected=d.get('agents_block_sha256');block=current_block(t)
    if expected and (block is None or digest(block.encode())!=expected):f.append('modified AGENTS managed block')
    return f
def backup(t,paths,include_agents=False,include_state=False):
    b=t/'.ai-expert-engine-backup'/(time.strftime('%Y%m%d-%H%M%S')+f'-{time.time_ns()%1000000:06d}')
    for p in paths:
        if not p.exists():continue
        d=b/p.relative_to(t);d.parent.mkdir(parents=True,exist_ok=True)
        if p.is_dir():shutil.copytree(p,d,dirs_exist_ok=True)
        else:shutil.copy2(p,d)
    if include_agents and (t/'AGENTS.md').exists():b.mkdir(parents=True,exist_ok=True);shutil.copy2(t/'AGENTS.md',b/'AGENTS.md')
    if include_state and (t/'.ai-expert-engine').exists():shutil.copytree(t/'.ai-expert-engine',b/'.ai-expert-engine-state',dirs_exist_ok=True)
    return b
def write_agents(t):
    p=t/'AGENTS.md';block=source_block();text=p.read_text() if p.exists() else ''
    if START in text and END in text:
        before=text.split(START,1)[0].rstrip();after=text.split(END,1)[1].lstrip();text=(before+'\n\n' if before else '')+block+('\n\n'+after if after else '')+'\n'
    else:text=text.rstrip()+('\n\n' if text.strip() else '')+block+'\n'
    p.write_text(text)
def clean_copy(t,old=None):
    for p in managed_paths(t,old):
        if p.is_dir():shutil.rmtree(p)
        elif p.exists():p.unlink()
    for r in DIRS:
        d=t/r;d.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(SOURCE/r,d)
    for r in FILES:
        s=SOURCE/r;d=t/r
        if not s.exists():raise SystemExit('engine source missing managed file: '+r)
        d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(s,d)
def run_migrations(t,oldv,newv):
    if oldv==newv:return []
    mf=json.loads((SOURCE/'engine/migrations/manifest.json').read_text());history=[];cur=oldv;guard=0
    while cur!=newv:
        guard+=1
        if guard>20:raise SystemExit('migration chain loop')
        step=next((x for x in mf.get('migrations',[]) if x.get('from')==cur),None)
        if not step:raise SystemExit(f'no engine migration path from {cur} to {newv}')
        path=SOURCE/'engine/migrations'/step['module'];spec=importlib.util.spec_from_file_location('ai_expert_migration',path)
        if not spec or not spec.loader:raise SystemExit('cannot load migration '+str(path))
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);result=mod.migrate(t,{'from':cur,'to':step['to'],'source':str(SOURCE)});history.append({'from':cur,'to':step['to'],'module':step['module'],'result':result});cur=step['to']
    return history
def apply(t,force,update):
    t=t.resolve();t.mkdir(parents=True,exist_ok=True)
    if t==SOURCE.resolve():raise SystemExit('refusing to install engine into its own source checkout')
    mp=t/MANIFEST;old=None;history=[]
    if update:
        if not mp.exists():raise SystemExit('not an engine-managed install')
        old=json.loads(mp.read_text());changes=drift(t,old)
        if changes and not force:raise SystemExit('managed install has local drift; run doctor or use --force to back up:\n - '+'\n - '.join(changes))
        if changes and force:backup(t,managed_paths(t,old),include_agents=True,include_state=True)
        if old.get('version')!=version():
            if not changes:backup(t,[],include_state=True)
            history=run_migrations(t,old.get('version','0.0.0'),version())
    elif not mp.exists():
        conflicts=[p for p in managed_paths(t) if p.exists()]
        if conflicts and not force:raise SystemExit('managed engine paths already exist; use --force to back up')
        if conflicts and force:backup(t,conflicts,include_agents=True)
    else:raise SystemExit('engine is already installed; use update')
    clean_copy(t,old);write_agents(t);block=current_block(t) or ''
    previous=(old or{}).get('migration_history',[]);mp.write_text(json.dumps({'name':'ai-expert-engine','version':version(),'managed_dirs':list(DIRS),'managed_files':list(FILES),'files':snapshot(t),'agents_block_sha256':digest(block.encode()),'migration_history':previous+history},indent=2)+'\n');print(f"engine {version()} {'updated' if update else 'installed'}")
def doctor(t):
    t=t.resolve();p=t/MANIFEST
    if not p.exists():print('missing install manifest');return 1
    d=json.loads(p.read_text());f=drift(t,d)
    if d.get('version')!=version():f.append(f"engine version outdated: installed={d.get('version')} source={version()}")
    if f:[print(' -',x) for x in f];return 1
    print(f"engine doctor passed: {d.get('version','unknown')}");return 0
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='cmd',required=True)
    for c in ('install','update'):
        p=sp.add_parser(c);p.add_argument('target',nargs='?',default='.');p.add_argument('--force',action='store_true')
    p=sp.add_parser('doctor');p.add_argument('target',nargs='?',default='.');n=ap.parse_args()
    if n.cmd=='install':apply(Path(n.target),n.force,False);return 0
    if n.cmd=='update':apply(Path(n.target),n.force,True);return 0
    return doctor(Path(n.target))
if __name__=='__main__':raise SystemExit(main())
