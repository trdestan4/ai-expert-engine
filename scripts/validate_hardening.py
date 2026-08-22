#!/usr/bin/env python3
from __future__ import annotations
import ast,json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REV={'code-reviewer','design-reviewer','security-reviewer','performance-reviewer','qa-reviewer','release-reviewer'};REQ={'run_behavioral_evals.py','run_context_drift_evals.py','run_reviewer_calibration.py','runtime_contract.py','engine_telemetry.py','review_store.py','release_gate.py','build_release_decision.py','session_checkpoint.py','check_knowledge_freshness.py','run_repository_benchmarks.py','resolve_stack_profile.py','profile_repository.py','enginectl.py','check_release_enforcement.py','validate_semantics.py','validate_master_depth.py','design_quality_checks.py','check_github_governance.py','apply_github_governance.py','routing_report.py'}
def skills():
    s=set()
    for p in (ROOT/'engine/registry').glob('*.json'):s.update(i['name'] for i in json.loads(p.read_text()).get('skills',[]))
    return s
def run(*args,cwd=ROOT):return subprocess.run([sys.executable,*map(str,args)],cwd=cwd,text=True,capture_output=True)
def main():
    e=[];s=skills()
    if len(s)!=43:e.append('skill count changed')
    if {p.stem for p in (ROOT/'.cursor/agents').glob('*.md')}!=REV:e.append('reviewer set mismatch')
    ps=json.loads((ROOT/'engine/profiles/profiles.json').read_text())['profiles']
    if len(ps)<20 or len({x.get('dimension') for x in ps})<5:e.append('need >=20 profiles across five composable dimensions')
    for p in ps:
        for x in p['owners']+p['conditional']:
            if x not in s:e.append(f"profile {p['id']} unknown {x}")
    ids=[json.loads(x)['id'] for x in (ROOT/'evals/behavioral/cases.jsonl').read_text().splitlines() if x.strip()]
    if len(ids)<30 or len(ids)!=len(set(ids)):e.append('behavioral corpus invalid')
    drift=json.loads((ROOT/'evals/context-drift/cases.json').read_text()).get('cases',[])
    if len(drift)<3:e.append('context drift corpus invalid')
    cal=[json.loads(x) for x in (ROOT/'evals/reviewer-calibration/cases.jsonl').read_text().splitlines() if x.strip()]
    if len(cal)<24 or {x['reviewer'] for x in cal}!=REV:e.append('reviewer calibration corpus invalid')
    bench=json.loads((ROOT/'benchmarks/corpus.json').read_text()).get('external',[])
    if len(bench)<10 or any(len(x.get('commit',''))!=40 for x in bench):e.append('repository benchmark corpus invalid')
    for x in REQ:
        if not (ROOT/'scripts'/x).exists():e.append('missing '+x)
    for p in (ROOT/'scripts').glob('*.py'):
        try:ast.parse(p.read_text(),filename=str(p))
        except SyntaxError as ex:e.append(f'python syntax error {p.name}:{ex.lineno}: {ex.msg}')
    for cmd in ((ROOT/'scripts/run_behavioral_evals.py','--validate-corpus'),(ROOT/'scripts/run_context_drift_evals.py','--validate-corpus'),(ROOT/'scripts/run_reviewer_calibration.py','--validate-corpus'),(ROOT/'scripts/run_repository_benchmarks.py','--validate-corpus')):
        r=run(*cmd)
        if r.returncode:e.append('corpus validation failed: '+(r.stderr or r.stdout).strip())
    with tempfile.TemporaryDirectory() as td:
        t=Path(td)/'project';t.mkdir();(t/'AGENTS.md').write_text('# Project rules\n\nKeep this line.\n');(t/'package.json').write_text(json.dumps({'dependencies':{'next':'16.0.0','@supabase/supabase-js':'2.0.0'}}));(t/'app').mkdir();(t/'app/page.tsx').write_text('export default function Page(){return null}\n')
        prof=run(ROOT/'scripts/resolve_stack_profile.py',t,'--all')
        try:
            pdata=json.loads(prof.stdout);selected=(pdata.get('selected') or{}).get('id');dims={x.get('dimension') for x in pdata.get('selected_profiles',[])}
        except Exception:selected=None;dims=set()
        if selected!='next-supabase':e.append(f'stack profile smoke failed: {selected!r}')
        if 'application' not in dims or 'experience' not in dims:e.append('composable profile dimensions missing in smoke')
        if run(ROOT/'scripts/enginectl.py','install',t).returncode:e.append('engine install smoke failed')
        if run(ROOT/'scripts/enginectl.py','doctor',t).returncode:e.append('doctor after install failed')
        inst=t/'.ai-expert-engine-install.json';meta=json.loads(inst.read_text());meta['version']='1.1.0';inst.write_text(json.dumps(meta));legacy=t/'.ai-expert-engine/reviews.jsonl';legacy.parent.mkdir(parents=True,exist_ok=True);legacy.write_text('{"legacy":true}\n')
        up=run(ROOT/'scripts/enginectl.py','update',t)
        if up.returncode:e.append('migration update failed: '+(up.stderr or up.stdout).strip())
        meta=json.loads(inst.read_text()) if inst.exists() else{}
        if meta.get('version')!='1.3.0' or len(meta.get('migration_history',[]))<2:e.append('migration history/version not recorded through v1.3')
        if not (t/'.ai-expert-engine/evidence/reviews.jsonl').exists():e.append('legacy review store not migrated')
        managed=t/'.codex/skills/master-agent/SKILL.md';managed.write_text(managed.read_text()+'\nlocal drift\n');reject=run(ROOT/'scripts/enginectl.py','update',t)
        if reject.returncode==0:e.append('update failed to reject local drift')
        if run(ROOT/'scripts/enginectl.py','update',t,'--force').returncode:e.append('forced update failed')
        if run(ROOT/'scripts/enginectl.py','doctor',t).returncode:e.append('doctor after forced update failed')
        if 'Keep this line.' not in (t/'AGENTS.md').read_text():e.append('installer did not preserve project AGENTS content')
        for rel in ('scripts/release_gate.py','scripts/runtime_contract.py','scripts/design_quality_checks.py','scripts/routing_report.py','.github/workflows/ai-expert-release-gate.yml'):
            if not (t/rel).exists():e.append('installer missing runtime/tool file '+rel)
    if e:print('hardening validation failed:');[print(' -',x) for x in e];return 1
    print(f'hardening validation passed: 43 skills, 6 reviewers, {len(ids)} behavioral, {len(drift)} drift, {len(cal)} calibration, {len(bench)} repo benchmarks, {len(ps)} profiles');return 0
if __name__=='__main__':raise SystemExit(main())
