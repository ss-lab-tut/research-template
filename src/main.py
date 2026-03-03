"""
src/main.py

This file provides small reusable utilities for experiments.

Rule:
- Put "reusable code" here (functions used by many experiments).
- Put "runnable scripts" under experiments/ (entry points).

We keep it simple for beginners:
- create a results run folder
- save json logs
"""

from pathlib import Path
from datetime import datetime
import json


def make_run_dir(tag: str) -> Path:
    """
    Create a timestamped run directory under results/.

    Example:
        run_dir = make_run_dir("demo")
        -> results/20260303_123456_demo/

    Args:
        tag (str): short name for the run (e.g., "demo", "train", "ablation1")

    Returns:
        Path: created run directory
    """
    base = Path("results")
    base.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = base / f"{timestamp}_{tag}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def save_json(path: Path, data: dict) -> None:
    """
    Save dict to JSON file (UTF-8).

    Args:
        path (Path): output file path
        data (dict): JSON-serializable dict
    """
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
