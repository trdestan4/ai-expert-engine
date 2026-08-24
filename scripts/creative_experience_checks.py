#!/usr/bin/env python3
"""Deterministically validate completeness of a creative-experience plan.

This proves contract completeness only. It does not claim visual quality, accessibility,
performance, or browser behavior without their real evidence.
"""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path

def validate(plan:dict)->tuple[list[str],list[str]]:
    e=[];w=[]
    req=("version","experience","responsive","motion","performance","fallbacks","qa")
    for k in req:
        if k not in plan:e.append(f"missing {k}")
    if e:return e,w
    if plan.get("version")!=1:e.append("version must be 1")
    exp=plan.get("experience") or{};mom=exp.get("signature_moments") or[]
    if not str(exp.get("creative_thesis","")).strip():e.append("experience.creative_thesis required")
    if len(mom)>3:e.append("signature_moments must be <=3")
    rsp=plan.get("responsive") or{}
    for k in ("desktop","mobile"):
        if not str(rsp.get(k,"")).strip():e.append(f"responsive.{k} required")
    motion=plan.get("motion") or{}
    if motion.get("scroll_control") not in {"native","native-with-triggers","not-applicable"}:e.append("motion.scroll_control invalid")
    if not str(motion.get("reduced_motion","")).strip():e.append("motion.reduced_motion required")
    perf=plan.get("performance") or{}
    if len(perf.get("target_devices") or[])<2:e.append("performance.target_devices needs >=2 representative classes")
    if not (perf.get("budgets") or{}):e.append("performance.budgets required")
    if not str(perf.get("measurement","")).strip():e.append("performance.measurement required")
    fb=plan.get("fallbacks") or{}
    for k in ("javascript_failure","advanced_effect_failure"):
        if not str(fb.get(k,"")).strip():e.append(f"fallbacks.{k} required")
    qa=plan.get("qa") or{}
    if len(qa.get("viewports") or[])<2:e.append("qa.viewports needs >=2 composition-relevant viewports")
    if len(qa.get("states") or[])<2:e.append("qa.states needs >=2 states")
    for k in ("visual_authority","baseline_policy"):
        if not str(qa.get(k,"")).strip():e.append(f"qa.{k} required")
    g=plan.get("graphics3d")
    if g and g.get("enabled"):
        if not g.get("lifecycle_disposal"):e.append("3D requires graphics3d.lifecycle_disposal=true")
        if not str(g.get("fallback","")).strip():e.append("3D requires graphics3d.fallback")
        if not str(fb.get("no_webgl","")).strip():e.append("3D requires fallbacks.no_webgl")
        if "dpr_cap" not in g:w.append("3D plan has no explicit dpr_cap; justify renderer resolution another way")
    tech={str(x).lower() for x in (motion.get("technologies") or[])}
    if any(x in tech for x in {"gsap","scrolltrigger"}) and motion.get("scroll_control")=="not-applicable":w.append("GSAP/ScrollTrigger listed while scroll_control is not-applicable; verify intent")
    return e,w

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("plan",type=Path);ap.add_argument("--output",type=Path);n=ap.parse_args()
    try:plan=json.loads(n.plan.read_text())
    except Exception as ex:print(f"creative experience check failed: {ex}",file=sys.stderr);return 2
    errors,warnings=validate(plan);out={"passed":not errors,"errors":errors,"warnings":warnings,"note":"Completeness check only; runtime/design/performance evidence remains required."};text=json.dumps(out,indent=2)
    if n.output:n.output.write_text(text+"\n")
    else:print(text)
    return 0 if not errors else 1
if __name__=="__main__":raise SystemExit(main())
