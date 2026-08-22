# Install / Update

Normal Cursor use does **not** require a Cursor API key. The API key is only for optional automated live behavioral/context-drift/reviewer-calibration benchmarks.

From a checkout of this engine:
```bash
python scripts/enginectl.py install /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
```

The installer manages `.codex/skills/`, `.cursor/agents/`, `engine/`, selected `scripts/*`, the reusable AI Expert release-gate workflow, and a marked block in the target `AGENTS.md`. It does not take ownership of the target project's whole `scripts/` or `.github/` directories. Existing unmanaged managed-path collisions require `--force`, which backs them up first.

Update:
```bash
python scripts/enginectl.py update /path/to/target-project
python scripts/enginectl.py doctor /path/to/target-project
```

Updates refuse modified managed files unless `--force` is used. Version transitions run the migration chain in `engine/migrations/manifest.json`; state is backed up before migration. The install manifest records managed hashes and migration history.

Project profiling:
```bash
python scripts/profile_repository.py /path/to/target-project
python scripts/resolve_stack_profile.py /path/to/target-project --all
```

Runtime evidence tools inside an installed project include `runtime_contract.py`, `session_checkpoint.py`, `engine_telemetry.py`, `review_store.py`, `build_release_decision.py` and `release_gate.py`.

Optional live model benchmarks:
```bash
pip install cursor-sdk
export CURSOR_API_KEY=...
python scripts/run_behavioral_evals.py --repeat 3
python scripts/run_context_drift_evals.py
python scripts/run_reviewer_calibration.py
```
