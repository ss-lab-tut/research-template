"""
experiments/run_demo.py

Entry script example.
- Creates a results run folder
- Saves a simple log.json
"""

from src.main import make_run_dir, save_json


def main():
    print("Starting demo experiment...")

    run_dir = make_run_dir("demo")

    save_json(
        run_dir / "log.json",
        {
            "status": "success",
            "message": "Template works",
            "run_directory": str(run_dir),
        },
    )

    print("[OK] Template works")
    print(f"[OK] Output saved to: {run_dir}")


if __name__ == "__main__":
    main()
