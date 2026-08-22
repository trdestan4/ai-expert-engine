#!/usr/bin/env python3
from __future__ import annotations
import argparse,fnmatch,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from profile_repository import collect
def fm(files,pat):return any(fnmatch.fnmatch(f,pat) for f in files)
def score(p,f):
    m=p.get('match',{});deps=set(f['dependencies']);files=f['files'];txt=f.get('text_signals','').lower();s=int(p.get('priority',0));why=[]
    a=m.get('dependencies_all',[])
    if a and not all(x in deps for x in a):return -1,[]
    if a:s+=30*len(a);why.append('dependencies_all')
    for key,weight in (('dependencies_any',15),('files_any',8),('text_signals_any',6)):
        a=m.get(key,[])
        if a:
            if key=='dependencies_any':h=[x for x in a if x in deps]
            elif key=='files_any':h=[x for x in a if fm(files,x)]
            else:h=[x for x in a if x.lower() in txt]
            if not h:return -1,[]
            s+=weight*len(h);why.append(key+':'+','.join(h[:4]))
    return s,why
def uniq(xs):return list(dict.fromkeys(xs))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',nargs='?',default='.');ap.add_argument('--all',action='store_true');ap.add_argument('--max-files',type=int,default=50000);ns=ap.parse_args();ps=json.loads((ROOT/'engine/profiles/profiles.json').read_text())['profiles'];f=collect(Path(ns.root),ns.max_files);r=[]
    for p in ps:
        s,w=score(p,f)
        if s>=0:r.append({'id':p['id'],'dimension':p['dimension'],'score':s,'reasons':w,'owners':p['owners'],'conditional':p['conditional'],'defaults':p['defaults']})
    r.sort(key=lambda x:(-x['score'],x['id']));by={}
    for x in r:by.setdefault(x['dimension'],x)
    selected_profiles=[by[k] for k in ('solution','application','data','infrastructure','experience') if k in by]
    owners=uniq([v for x in selected_profiles for v in x['owners']]);conditional=uniq([v for x in selected_profiles for v in x['conditional'] if v not in owners]);defaults={};conflicts=[]
    for x in selected_profiles:
        for k,v in x['defaults'].items():
            if k in defaults and defaults[k]!=v:conflicts.append({'key':k,'kept':defaults[k],'ignored':v,'profile':x['id']});continue
            defaults[k]=v
    warnings=[]
    if f.get('truncated'):warnings.append('repository profile is truncated; stack resolution confidence is partial')
    out={'selected':r[0] if r else None,'selected_profiles':selected_profiles,'selected_by_dimension':by,'merged':{'owners':owners,'conditional':conditional,'defaults':defaults,'default_conflicts':conflicts},'confidence':'partial' if f.get('truncated') else ('high' if selected_profiles else 'low'),'repository_truncated':bool(f.get('truncated')),'warnings':warnings,'candidates':r if ns.all else r[:10]};print(json.dumps(out,indent=2));return 0 if r else 2
if __name__=='__main__':raise SystemExit(main())
