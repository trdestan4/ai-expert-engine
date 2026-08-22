# Repository Governance

`engine/governance/github.json` defines the desired live protection state for `main`.

Verify:

```bash
python scripts/check_github_governance.py --repo trdestan4/ai-expert-engine
```

Apply with a GitHub Administration-write token:

```bash
export GITHUB_ADMIN_TOKEN=...
python scripts/apply_github_governance.py --repo trdestan4/ai-expert-engine
```

A green validator does not substitute for live branch protection.
