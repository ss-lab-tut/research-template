# research-template

SS-Lab Research Project Template  
Minimal / Reproducible / Paper-Ready

This template is designed for:

- Graduate students
- Research experiments
- Ablation studies
- SOTA comparisons
- Reproducible research

The philosophy is:

Simple > Smart  
Clear > Clever  
Reproducible > Fast  

------------------------------------------------------------

PROJECT STRUCTURE

research-template/
- README.md
- requirements.txt
- .gitignore
- LICENSE
- configs/               experiment configurations
- src/                   reusable code
- experiments/           runnable scripts
- results/               auto-created (NOT committed)

------------------------------------------------------------

WHAT GOES WHERE?

configs/
- JSON files defining experiment settings
- Each config = one experiment condition
- Example:
  - demo.json
  - ablation_gat_off.json
  - sota_baselineA.json

src/
- Reusable functions
- Utilities
- Shared logic
- No direct execution

experiments/
- Entry scripts (runnable)
- run.py        → run one config
- sweep.py      → run all configs
- summarize.py  → collect results

results/
- Automatically created
- Each run gets its own folder
- NEVER commit this folder

------------------------------------------------------------

QUICK START

1) Create virtual environment

macOS / Linux:
python -m venv .venv
source .venv/bin/activate

Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

2) Install dependencies

pip install -r requirements.txt

If installation fails:
python -m pip install --upgrade pip

3) Run a single experiment

python experiments/run.py configs/demo.json

4) Run all experiments (sweep)

python experiments/sweep.py

5) Summarize results

python experiments/summarize.py

Output:
results/summary.csv

------------------------------------------------------------

EXPERIMENT DESIGN (VERY IMPORTANT)

Each experiment is defined by:

- group
- variant
- seed

Example config:

{
  "experiment_name": "ablation_gat_off",
  "group": "ablation",
  "variant": "gat_off",
  "seed": 42
}

------------------------------------------------------------

GROUP MEANINGS

group = proposed
    Your main method

group = ablation
    Modified version of proposed
    (remove component / change parameter)

group = sota
    State-of-the-art comparison

group = baseline
    Simple or classical method

------------------------------------------------------------

WHAT IS ABLATION?

Ablation isolates components.

Examples:
- Remove attention
- Replace GAT with MLP
- Change penalty weight
- Remove constraint term

Goal:
Explain why your method works.

------------------------------------------------------------

WHAT IS SOTA COMPARISON?

SOTA comparison evaluates:

Your method vs existing methods.

Examples:
- Heuristic baseline
- Classical optimization
- Published RL method
- Public implementation

Goal:
Show performance advantage.

------------------------------------------------------------

REPRODUCIBILITY RULES

Every experiment must:

1) Use a config file
2) Fix random seed
3) Save config_used.json
4) Save metrics.json
5) Never modify results manually

If someone cannot reproduce your experiment,
it is considered incomplete.

------------------------------------------------------------

RESULT STRUCTURE

Each run creates:

results/YYYYMMDD_HHMMSS_<experiment_name>/

Inside:
- config_used.json
- metrics.json

Example metrics.json:

{
  "experiment_name": "demo",
  "group": "proposed",
  "variant": "default",
  "seed": 42,
  "metrics": {
    "accuracy": 0.95,
    "reward": 123.4
  }
}

------------------------------------------------------------

HOW TO ADD A NEW EXPERIMENT

1) Create a new config in configs/

Example:
configs/ablation_penalty_low.json

2) Run:

python experiments/run.py configs/ablation_penalty_low.json

3) Or run all:

python experiments/sweep.py

------------------------------------------------------------

HOW TO ADD A NEW METRIC

In experiments/run.py:

Modify run_experiment()

Return metrics as dict:

metrics = {
    "accuracy": value,
    "loss": value,
    "reward": value
}

summarize.py will automatically collect all metrics.

------------------------------------------------------------

COMMON MISTAKES

- Running code without activating .venv
- Editing results manually
- Forgetting to fix seed
- Mixing experiment logic inside src and experiments

------------------------------------------------------------

GITHUB RULES (FOR STUDENTS)

Never commit directly to main.

Workflow:

1) Create branch:
   feature/<short-name>

2) Make changes

3) Open Pull Request

4) Merge

Branch examples:
- feature/add-train
- fix/readme-typo

Before PR:
At least confirm demo runs.

------------------------------------------------------------

DESIGN PRINCIPLES

This template is intentionally:

- Not over-engineered
- Not production-oriented
- Not CI-heavy

It is built for:

- Academic reproducibility
- Clean experiment comparison
- Student safety
- Long-term maintainability

------------------------------------------------------------

FINAL NOTE

If experiments become messy,
the problem is usually:

- Missing config separation
- Inconsistent metric naming
- No seed control

Keep experiments simple.
Keep metrics consistent.
Keep structure stable.

That is how research scales.
