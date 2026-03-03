import subprocess
from pathlib import Path


def main():
    config_dir = Path("configs")
    configs = sorted(config_dir.glob("*.json"))

    if not configs:
        print("[ERR] No config files found in configs/")
        return

    for cfg in configs:
        print("--------------------------------------------------")
        print("[RUN]", cfg)
        subprocess.run(["python", "experiments/run.py", str(cfg)], check=True)

    print("--------------------------------------------------")
    print("[OK] sweep finished")


if __name__ == "__main__":
    main()
