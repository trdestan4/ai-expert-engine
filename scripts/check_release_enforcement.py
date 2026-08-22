#!/usr/bin/env python3
from __future__ import annotations
import argparse,re
from pathlib import Path
DEPLOY=re.compile(r'(?i)(vercel\s+(deploy|--prod)|aws\s+.*deploy|kubectl\s+(apply|set image)|helm\s+(upgrade|install)|terraform\s+apply|tofu\s+apply|environment:\s*production|deploy[-_ ]?production|deploy[-_ ]?prod)')
GATE=re.compile(r'(?i)(ai-expert-release-gate\.yml|release_gate\.py|AI Expert Release Gate)')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',default='.');ap.add_argument('--soft',action='store_true');n=ap.parse_args();root=Path(n.root);wf=root/'.github/workflows';bad=[]
    if not wf.exists():print('release enforcement: no workflows');return 0
    for p in list(wf.glob('*.yml'))+list(wf.glob('*.yaml')):
        if p.name=='ai-expert-release-gate.yml':continue
        t=p.read_text(encoding='utf-8',errors='ignore')
        if DEPLOY.search(t) and not GATE.search(t):bad.append(p.relative_to(root).as_posix())
    if bad:
        print('production-like workflows missing AI Expert release gate:');[print(' -',x) for x in bad];return 0 if n.soft else 1
    print('release enforcement check passed');return 0
if __name__=='__main__':raise SystemExit(main())
