# research-template

SS-Lab research project template (beginner-friendly).

This template is designed so that:
- students can run a demo with ONE command
- outputs are saved under `results/`
- `results/` is NOT committed to GitHub

## Folder structure

- `src/` : reusable source code (functions, models, utilities)
- `experiments/` : runnable scripts (entry points)
- `results/` : outputs (ignored by git)

## Quick start (students)

### 1) Create virtual environment (recommended)

```bash
python -m venv .venv
# mac / linux
source .venv/bin/activate
# windows (PowerShell)
# .venv\Scripts\Activate.ps1
