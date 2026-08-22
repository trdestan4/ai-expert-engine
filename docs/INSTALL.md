# Install / Update

Normal Cursor use does **not** require a Cursor API key. The API key is only for optional automated live behavioral/context-drift/reviewer-calibration benchmarks.

```bash
python scripts/enginectl.py install /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
```

The installer manages `.codex/skills/`, `.cursor/agents/`, `engine/`, selected runtime `scripts/*`, the AI Expert release-gate workflow, a marked block in `AGENTS.md`, and merges the AI Expert production-shell guard into an existing `.cursor/hooks.json` without taking ownership of unrelated hooks. The hook uses Cursor's `beforeShellExecution` control surface; production-like deploy/apply commands are blocked when candidate/evidence release validation fails.

Existing unmanaged collisions require `--force`, which backs them up first. Updates refuse modified managed files unless forced, run the migration chain in `engine/migrations/manifest.json`, back up state before migration and record migration history.

```bash
python scripts/enginectl.py update /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
```

Project profiling:
```bash
python scripts/profile_repository.py /path/to/target-project
python scripts/resolve_stack_profile.py /path/to/target-project --all
```

Optional live model benchmarks only:
```bash
pip install cursor-sdk
export CURSOR_API_KEY=...
python scripts/run_behavioral_evals.py --repeat 3
python scripts/run_context_drift_evals.py
python scripts/run_reviewer_calibration.py
```
