# research-template

SS-Lab Research Project Template (Beginner Friendly)

This template is intentionally simple.
Students should be able to run it immediately.

------------------------------------------------------------

PROJECT STRUCTURE

research-template/
- README.md
- requirements.txt
- .gitignore
- LICENSE
- src/
- experiments/
- results/  (auto-created, NOT committed)

------------------------------------------------------------

QUICK START (FOR STUDENTS)

1) Create virtual environment

macOS / Linux:
python -m venv .venv
source .venv/bin/activate

Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

2) Install dependencies

pip install -r requirements.txt

3) Run demo

python experiments/run_demo.py

If successful, you will see:

[OK] Template works

A folder will be created automatically:

results/YYYYMMDD_HHMMSS_demo/

Inside it:
log.json

------------------------------------------------------------

HOW TO START A NEW EXPERIMENT

1) Copy experiments/run_demo.py
2) Rename it (example: run_ablation1.py)
3) Modify it
4) Run it
5) Outputs automatically go to results/

------------------------------------------------------------

IMPORTANT RULES

DO NOT COMMIT:
- results/
- .venv/

ALWAYS:
- Put runnable scripts inside experiments/
- Put reusable code inside src/

------------------------------------------------------------

DEVELOPMENT FLOW

1) Create a new branch
2) Make changes
3) Open a Pull Request
4) Merge into main

Direct commits to main are disabled for safety.

------------------------------------------------------------

Design Philosophy:

Simple > Smart
Clear > Clever
Safe > Fancy
