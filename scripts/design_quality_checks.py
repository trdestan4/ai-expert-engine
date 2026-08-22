#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,re,sys
from pathlib import Path
HEX=re.compile(r'^#?([0-9a-fA-F]{6})$')
def rgb(raw:str):
    m=HEX.fullmatch(raw.strip())
    if not m:raise ValueError(f'invalid 6-digit hex color: {raw}')
    s=m.group(1);return tuple(int(s[i:i+2],16)/255 for i in (0,2,4))
def linear(c):return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def luminance(raw):
    r,g,b=rgb(raw);return 0.2126*linear(r)+0.7152*linear(g)+0.0722*linear(b)
def contrast(fg,bg):
    a,b=luminance(fg),luminance(bg);hi,lo=max(a,b),min(a,b);return (hi+0.05)/(lo+0.05)
def audit(spec):
    rows=[];failed=[]
    for item in spec.get('contrast_pairs',[]):
        name=str(item.get('name') or f"{item.get('foreground')}/{item.get('background')}");req=float(item.get('required_ratio',4.5));ratio=contrast(item['foreground'],item['background']);ok=ratio+1e-9>=req;row={'name':name,'foreground':item['foreground'],'background':item['background'],'ratio':round(ratio,3),'required_ratio':req,'passed':ok};rows.append(row)
        if not ok:failed.append(name)
    type_issues=[]
    for t in spec.get('typography',[]):
        name=str(t.get('name','type'));size=float(t.get('font_size_px',0));lh=float(t.get('line_height_px',0));measure=t.get('measure_ch')
        if size<=0:type_issues.append(f'{name}: font_size_px must be >0')
        if lh and size and lh<size:type_issues.append(f'{name}: line-height is smaller than font size')
        if measure is not None and (float(measure)<20 or float(measure)>100):type_issues.append(f'{name}: measure_ch={measure} is outside broad readability guardrail 20..100; justify or revise')
    tokens=spec.get('semantic_tokens',{}) or{};missing=[]
    required=spec.get('required_semantic_tokens',[]) or[]
    for name in required:
        if name not in tokens:missing.append(name)
    return {'contrast':rows,'failed_contrast':failed,'typography_issues':type_issues,'missing_semantic_tokens':missing,'passed':not(failed or type_issues or missing)}
def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='cmd',required=True)
    c=sp.add_parser('contrast');c.add_argument('foreground');c.add_argument('background');c.add_argument('--required',type=float,default=4.5)
    a=sp.add_parser('audit');a.add_argument('spec',type=Path);a.add_argument('--output',type=Path)
    n=ap.parse_args()
    if n.cmd=='contrast':
        try:r=contrast(n.foreground,n.background)
        except ValueError as ex:print(ex,file=sys.stderr);return 2
        ok=r+1e-9>=n.required;print(json.dumps({'foreground':n.foreground,'background':n.background,'ratio':round(r,3),'required_ratio':n.required,'passed':ok},indent=2));return 0 if ok else 1
    try:spec=json.loads(n.spec.read_text());out=audit(spec)
    except Exception as ex:print(f'design quality audit failed: {ex}',file=sys.stderr);return 2
    text=json.dumps(out,indent=2);n.output.write_text(text+'\n') if n.output else print(text);return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
