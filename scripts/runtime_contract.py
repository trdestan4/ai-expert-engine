#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CONTRACTS=ROOT/'engine/runtime/contracts.json'
def typename(v):
    if v is None:return'null'
    if isinstance(v,bool):return'boolean'
    if isinstance(v,str):return'string'
    if isinstance(v,int) and not isinstance(v,bool):return'integer'
    if isinstance(v,(int,float)) and not isinstance(v,bool):return'number'
    if isinstance(v,list):return'array'
    if isinstance(v,dict):return'object'
    return'unknown'
def resolve_ref(ref,root):
    if not ref.startswith('#/'):raise ValueError('only local JSON Pointer refs are supported: '+ref)
    cur=root
    for part in ref[2:].split('/'):
        part=part.replace('~1','/').replace('~0','~');cur=cur[part]
    return cur
def fmt_ok(name,v):
    if name=='date-time':
        try:datetime.fromisoformat(v.replace('Z','+00:00'));return 'T' in v
        except Exception:return False
    if name=='date':
        try:datetime.fromisoformat(v).date();return True
        except Exception:return False
    return True
def validate(s,v,p='$',e=None,root=None):
    e=e if e is not None else[];root=s if root is None else root
    if '$ref' in s:
        try:return validate(resolve_ref(s['$ref'],root),v,p,e,root)
        except Exception as ex:e.append(f'{p}: invalid $ref {ex}');return e
    if 'allOf' in s:
        for q in s['allOf']:validate(q,v,p,e,root)
    if 'anyOf' in s:
        trials=[]
        for q in s['anyOf']:
            x=[];validate(q,v,p,x,root);trials.append(x)
        if all(trials):e.append(f'{p}: failed anyOf')
    if 'oneOf' in s:
        ok=0
        for q in s['oneOf']:
            x=[];validate(q,v,p,x,root);ok+=not x
        if ok!=1:e.append(f'{p}: expected exactly one oneOf match, got {ok}')
    cond=s.get('if')
    if cond is not None:
        x=[];validate(cond,v,p,x,root);branch='then' if not x else 'else'
        if branch in s:validate(s[branch],v,p,e,root)
    if 'const' in s and v!=s['const']:e.append(f'{p}: expected const {s["const"]!r}')
    t=s.get('type')
    if t:
        allowed=[t] if isinstance(t,str) else t
        if typename(v) not in allowed:e.append(f'{p}: expected {t}, got {typename(v)}');return e
    if 'enum' in s and v not in s['enum']:e.append(f'{p}: not in enum')
    if isinstance(v,str):
        if len(v)<s.get('minLength',0):e.append(f'{p}: too short')
        if 'maxLength' in s and len(v)>s['maxLength']:e.append(f'{p}: too long')
        if s.get('pattern') and not re.search(s['pattern'],v):e.append(f'{p}: pattern mismatch')
        if s.get('format') and not fmt_ok(s['format'],v):e.append(f'{p}: invalid format {s["format"]}')
    if isinstance(v,(int,float)) and not isinstance(v,bool):
        if 'minimum' in s and v<s['minimum']:e.append(f'{p}: below minimum')
        if 'maximum' in s and v>s['maximum']:e.append(f'{p}: above maximum')
        if 'exclusiveMinimum' in s and v<=s['exclusiveMinimum']:e.append(f'{p}: below exclusive minimum')
        if 'exclusiveMaximum' in s and v>=s['exclusiveMaximum']:e.append(f'{p}: above exclusive maximum')
    if isinstance(v,list):
        if len(v)<s.get('minItems',0):e.append(f'{p}: too few items')
        if 'maxItems' in s and len(v)>s['maxItems']:e.append(f'{p}: too many items')
        if s.get('uniqueItems'):
            if len({json.dumps(x,sort_keys=True) for x in v})!=len(v):e.append(f'{p}: duplicate items')
        if 'items' in s:
            for i,x in enumerate(v):validate(s['items'],x,f'{p}[{i}]',e,root)
    if isinstance(v,dict):
        if len(v)<s.get('minProperties',0):e.append(f'{p}: too few properties')
        if 'maxProperties' in s and len(v)>s['maxProperties']:e.append(f'{p}: too many properties')
        for k in s.get('required',[]):
            if k not in v:e.append(f'{p}: missing {k}')
        props=s.get('properties',{})
        for k,x in v.items():
            if k in props:validate(props[k],x,f'{p}.{k}',e,root)
            elif s.get('additionalProperties') is False:e.append(f'{p}: unexpected {k}')
            elif isinstance(s.get('additionalProperties'),dict):validate(s['additionalProperties'],x,f'{p}.{k}',e,root)
    return e
def schema_for(name):
    m=json.loads(CONTRACTS.read_text());rel=m['contracts'].get(name)
    if not rel:raise SystemExit(f'unknown contract: {name}')
    return json.loads((ROOT/rel).read_text())
def main():
    ap=argparse.ArgumentParser();ap.add_argument('contract');ap.add_argument('file',type=Path);ap.add_argument('--quiet',action='store_true');n=ap.parse_args()
    try:data=json.loads(n.file.read_text())
    except Exception as ex:print(f'invalid JSON: {ex}');return 2
    schema=schema_for(n.contract);errors=validate(schema,data,root=schema)
    if errors:
        if not n.quiet:[print(' -',x) for x in errors]
        return 1
    if not n.quiet:print(f'runtime contract passed: {n.contract}')
    return 0
if __name__=='__main__':raise SystemExit(main())
