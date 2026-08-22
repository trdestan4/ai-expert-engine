#!/usr/bin/env python3
from __future__ import annotations
import json,os,re,subprocess,sys
from pathlib import Path
PROD=re.compile(r'''(?ix)(
vercel(?:\s+deploy)?[^\n]*--prod|netlify\s+deploy[^\n]*--prod|flyctl\s+deploy|railway\s+(?:up|deploy)|render\s+deploy|gcloud\s+(?:run\s+deploy|app\s+deploy|functions\s+deploy)|az\s+(?:webapp|functionapp|containerapp)[^\n]*(?:deploy|up|create|update)|
kubectl\s+(?:apply|replace|create|delete|patch|scale|rollout|set\s+image)|helm\s+(?:upgrade|install|rollback|uninstall)|terraform\s+(?:apply|destroy|import)|tofu\s+(?:apply|destroy|import)|\bcdk\s+(?:deploy|destroy)\b|aws\s+[^\n]*\b(?:deploy|update-stack|create-stack|delete-stack)\b|(?:npm|pnpm|yarn)\s+(?:run\s+)?deploy(?::(?:prod|production))?\b
)''')
def main():
    try:data=json.load(sys.stdin)
    except Exception:return 0
    cmd=str(data.get('command') or data.get('shell_command') or '')
    if not PROD.search(cmd):return 0
    root=Path(os.environ.get('CURSOR_PROJECT_DIR') or os.getcwd()).resolve();gate=root/'scripts/release_gate.py'
    if not gate.exists():print('AI Expert Engine: production-like command blocked because release gate is missing.',file=sys.stderr);return 2
    g=subprocess.run(['git','rev-parse','HEAD'],cwd=root,text=True,capture_output=True);candidate=g.stdout.strip() if g.returncode==0 else None
    if not candidate:print('AI Expert Engine: production-like command blocked because candidate commit cannot be identified.',file=sys.stderr);return 2
    decision=root/'.ai-expert-engine/evidence/release-decision.json';reviews=root/'.ai-expert-engine/evidence/reviews.jsonl';env=os.environ.get('AI_EXPERT_RELEASE_ENVIRONMENT','production')
    r=subprocess.run([sys.executable,str(gate),'--decision',str(decision),'--candidate',candidate,'--environment',env,'--reviews',str(reviews)],cwd=root,text=True,capture_output=True)
    if r.returncode:
        msg=(r.stdout+r.stderr).strip();print('AI Expert Engine: production-like shell command BLOCKED. '+(msg or 'Release gate did not pass.'),file=sys.stderr);return 2
    return 0
if __name__=='__main__':raise SystemExit(main())
