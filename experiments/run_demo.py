"""
run_demo.py

Purpose:
- Demonstrate how experiments should be structured.
- Automatically create a results folder.
- Save a simple log file.
"""

from pathlib import Path
from datetime import datetime
import json


def create_results_folder():
    """
    Create a timestamped results folder.

    Returns:
        Path: path to the created run directory
    """

    # Ensure base results directory exists
    base_dir = Path("results")
    base_dir.mkdir(exist_ok=True)

    # Create timestamped folder name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = base_dir / f"{timestamp}_demo"

    run_dir.mkdir(parents=True, exist_ok=True)

    return run_dir


def save_log(run_dir):
    """
    Save a simple log.json file inside the run directory.
    """

    log_data = {
        "status": "success",
        "message": "Template works",
        "run_directory": str(run_dir)
    }

    log_file = run_dir / "log.json"
    log_file.write_text(json.dumps(log_data, indent=2), encoding="utf-8")


def main():
    print("Starting demo experiment...")

    # 1) Create output folder
    run_dir = create_results_folder()

    # 2) Save log file
    save_log(run_dir)

    print("[OK] Template works")
    print(f"[OK] Output saved to: {run_dir}")


if __name__ == "__main__":
    main()
