# Install / Update

From a checkout of this repository:

```bash
python scripts/enginectl.py install /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
```

The installer manages `.codex/skills/`, `.cursor/agents/`, `engine/`, and a marked block inside the target project's `AGENTS.md`. Existing unmanaged paths are never overwritten silently; `--force` backs them up first.

Update:

```bash
python scripts/enginectl.py update /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
```

Stack profile:

```bash
python scripts/profile_repository.py /path/to/target-project
python scripts/resolve_stack_profile.py /path/to/target-project --all
```

Live behavioral eval:

```bash
pip install cursor-sdk==1.0.24
export CURSOR_API_KEY=...
python scripts/run_behavioral_evals.py --repeat 3
```
