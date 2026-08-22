# Executable Behavioral Evals

These cases exercise the real Cursor agent against project instructions and skills. Each case launches a fresh Cursor SDK local-agent context and asks the engine to classify a request without modifying files.

Run:
```bash
pip install cursor-sdk==1.0.24
export CURSOR_API_KEY=...
python scripts/run_behavioral_evals.py --repeat 3
```

Use `--validate-corpus` for zero-cost structural validation.
