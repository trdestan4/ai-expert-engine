#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CONTRACTS=ROOT/"engine/runtime/contracts.json"
def typename(v):
    if v is None:return"null"
    if isinstance(v,bool):return"boolean"
    if isinstance(v,str):return"string"
    if isinstance(v,int) and not isinstance(v,bool):return"integer"
    if isinstance(v,(int,float)) and not isinstance(v,bool):return"number"
    if isinstance(v,list):return"array"
    if isinstance(v,dict):return"object"
    return"unknown"
def validate(s,v,p="$",e=None):
    e=e if e is not None else[];t=s.get("type")
    if t:
        ok=typename(v) in ([t] if isinstance(t,str) else t)
        if not ok:e.append(f"{p}: expected {t}, got {typename(v)}");return e
    if "enum" in s and v not in s["enum"]:e.append(f"{p}: not in enum")
    if isinstance(v,str):
        if len(v)<s.get("minLength",0):e.append(f"{p}: too short")
        if s.get("pattern") and not re.search(s["pattern"],v):e.append(f"{p}: pattern mismatch")
    if isinstance(v,(int,float)) and not isinstance(v,bool):
        if "minimum" in s and v<s["minimum"]:e.append(f"{p}: below minimum")
        if "maximum" in s and v>s["maximum"]:e.append(f"{p}: above maximum")
    if isinstance(v,list):
        if len(v)<s.get("minItems",0):e.append(f"{p}: too few items")
        if s.get("uniqueItems"):
            try:
                if len({json.dumps(x,sort_keys=True) for x in v})!=len(v):e.append(f"{p}: duplicate items")
            except Exception:pass
        if "items" in s:
            for i,x in enumerate(v):validate(s["items"],x,f"{p}[{i}]",e)
    if isinstance(v,dict):
        for k in s.get("required",[]):
            if k not in v:e.append(f"{p}: missing {k}")
        props=s.get("properties",{})
        for k,x in v.items():
            if k in props:validate(props[k],x,f"{p}.{k}",e)
            elif s.get("additionalProperties") is False:e.append(f"{p}: unexpected {k}")
    return e
def schema_for(name):
    m=json.loads(CONTRACTS.read_text());rel=m["contracts"].get(name)
    if not rel:raise SystemExit(f"unknown contract: {name}")
    return json.loads((ROOT/rel).read_text())
def main():
    ap=argparse.ArgumentParser();ap.add_argument("contract");ap.add_argument("file",type=Path);ap.add_argument("--quiet",action="store_true");n=ap.parse_args()
    try:data=json.loads(n.file.read_text())
    except Exception as ex:print(f"invalid JSON: {ex}");return 2
    errors=validate(schema_for(n.contract),data)
    if errors:
        if not n.quiet:[print(" -",x) for x in errors]
        return 1
    if not n.quiet:print(f"runtime contract passed: {n.contract}")
    return 0
if __name__=="__main__":raise SystemExit(main())
