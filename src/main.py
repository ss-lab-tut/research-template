from pathlib import Path
from datetime import datetime
import json
import random
import numpy as np


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)


def make_run_dir(tag: str) -> Path:
    base = Path("results")
    base.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = base / f"{timestamp}_{tag}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def save_json(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_config(path: str):
    with open(path, "r") as f:
        return json.load(f)
