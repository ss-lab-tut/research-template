import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.main import load_config, make_run_dir, save_json, set_seed


def run_experiment(config: dict) -> dict:
    """
    Replace this body with your real experiment.

    Must return a dict of metrics that summarize the run.
    Example metrics:
    - accuracy
    - loss
    - reward
    - sla_violation
    - latency
    """
    # demo metrics (placeholder)
    metrics = {
        "metric_x": 1.0,
        "metric_y": 2.0,
    }
    return metrics


def main():
    if len(sys.argv) != 2:
        print("Usage: python experiments/run.py configs/<config>.json")
        sys.exit(1)

    config_path = sys.argv[1]
    config = load_config(config_path)

    set_seed(int(config.get("seed", 0)))

    tag = config.get("experiment_name", "run")
    run_dir = make_run_dir(tag)

    # save config copy for reproducibility
    save_json(run_dir / "config_used.json", config)

    # run
    metrics = run_experiment(config)

    # save metrics (standardized)
    result = {
        "experiment_name": config.get("experiment_name"),
        "group": config.get("group"),
        "variant": config.get("variant"),
        "seed": config.get("seed"),
        "metrics": metrics,
        "config_path": config_path,
        "run_dir": str(run_dir),
    }
    save_json(run_dir / "metrics.json", result)

    print("[OK] finished:", tag)
    print("[OK] saved to:", run_dir)


if __name__ == "__main__":
    main()
