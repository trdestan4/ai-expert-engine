#!/usr/bin/env python3
from __future__ import annotations
import argparse,re
from pathlib import Path
DEPLOY=re.compile(r'(?ix)(vercel\s+(deploy|--prod)|netlify\s+deploy.*--prod|flyctl\s+deploy|railway\s+(up|deploy)|render\s+deploy|gcloud\s+(run\s+deploy|app\s+deploy|functions\s+deploy)|az\s+(webapp|functionapp|containerapp).*?(deploy|up|create|update)|aws\s+.*(deploy|update-stack|create-stack|delete-stack)|kubectl\s+(apply|replace|create|delete|patch|scale|rollout|set\s+image)|helm\s+(upgrade|install|rollback|uninstall)|terraform\s+(apply|destroy)|tofu\s+(apply|destroy)|environment:\s*production|deploy[-_ ]?production|deploy[-_ ]?prod)')
GATE=re.compile(r'(?i)(ai-expert-release-gate\.yml|release_gate\.py|AI Expert Release Gate)')
ENV=re.compile(r'(?i)(--environment|environment:)')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',default='.');ap.add_argument('--soft',action='store_true');n=ap.parse_args();root=Path(n.root);wf=root/'.github/workflows';bad=[];weak=[]
    if not wf.exists():print('release enforcement: no workflows');return 0
    for p in list(wf.glob('*.yml'))+list(wf.glob('*.yaml')):
        if p.name=='ai-expert-release-gate.yml':continue
        t=p.read_text(encoding='utf-8',errors='ignore')
        if DEPLOY.search(t) and not GATE.search(t):bad.append(p.relative_to(root).as_posix())
        elif DEPLOY.search(t) and GATE.search(t) and not ENV.search(t):weak.append(p.relative_to(root).as_posix())
    if bad or weak:
        if bad:print('production-like workflows missing AI Expert release gate:');[print(' -',x) for x in bad]
        if weak:print('production-like workflows gate without explicit environment binding:');[print(' -',x) for x in weak]
        return 0 if n.soft else 1
    print('release enforcement check passed');return 0
if __name__=='__main__':raise SystemExit(main())
