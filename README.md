# research-template

SS-Lab Research Project Template  
Beginner-Friendly / Safe / Minimal

This template is intentionally simple.

Goals:
- Students can run it immediately.
- Every experiment automatically saves outputs.
- The structure is hard to break.
- GitHub usage remains safe.

------------------------------------------------------------

PROJECT STRUCTURE

research-template/
- README.md
- requirements.txt
- .gitignore
- LICENSE
- src/                  reusable functions
- experiments/          runnable entry scripts
- results/              auto-created (NOT committed)

------------------------------------------------------------

WHAT GOES WHERE?

experiments/
- Entry scripts (things you run)
- Example: run_demo.py
- Example: run_train.py
- Example: run_ablation1.py

src/
- Reusable code
- Shared utilities
- Models
- Functions used by multiple experiments

results/
- All experiment outputs
- Automatically created
- Never committed to GitHub

------------------------------------------------------------

QUICK START (FOR STUDENTS)

Step 1: Create virtual environment

macOS / Linux:
python -m venv .venv
source .venv/bin/activate

Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

Step 2: Install dependencies

pip install -r requirements.txt

Step 3: Run demo

python experiments/run_demo.py

If successful, you will see:

[OK] Template works

A folder will be created automatically:

results/YYYYMMDD_HHMMSS_demo/

Inside it:
log.json

------------------------------------------------------------

HOW TO CREATE A NEW EXPERIMENT

1) Copy:
   experiments/run_demo.py

2) Rename:
   experiments/run_your_experiment.py

Examples:
- run_ablation1.py
- run_train.py
- run_eval.py

3) Modify main()

4) Run it:
   python experiments/run_your_experiment.py

5) Outputs automatically go to results/

------------------------------------------------------------

EXPERIMENT TEMPLATE (COPY THIS)

from src.main import make_run_dir, save_json

def main():
    run_dir = make_run_dir("my_experiment")

    # Your experiment code here
    x = 1 + 1

    save_json(run_dir / "result.json", {"x": x})

    print("[OK] saved to", run_dir)

if __name__ == "__main__":
    main()

------------------------------------------------------------

IMPORTANT RULES

DO NOT COMMIT:
- results/
- .venv/

ALWAYS:
- Put runnable scripts inside experiments/
- Put reusable code inside src/
- Save outputs inside results/

------------------------------------------------------------

DEVELOPMENT FLOW

1) Create a new branch
2) Make changes
3) Open a Pull Request
4) Merge into main

Direct commits to main are disabled for safety.

------------------------------------------------------------

COMMON MISTAKES

- Writing experiment code inside src/ and trying to run it directly
- Saving files outside results/
- Committing results/
- Forgetting to activate virtual environment

If something fails:
1) Activate .venv
2) Reinstall requirements
3) Run run_demo.py first

------------------------------------------------------------

DESIGN PHILOSOPHY

Simple > Smart  
Clear > Clever  
Safe > Fancy  

If students can run it without asking questions,
the template is successful.
