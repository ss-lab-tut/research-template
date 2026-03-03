from src.main import make_run_dir, save_json, load_config, set_seed


def main():
    config = load_config("configs/demo.json")

    set_seed(config["seed"])

    run_dir = make_run_dir(config["experiment_name"])

    # Save config copy for reproducibility
    save_json(run_dir / "config_used.json", config)

    # Example experiment
    x = 1 + 1

    save_json(
        run_dir / "result.json",
        {
            "x": x,
            "seed": config["seed"]
        }
    )

    print("[OK] Experiment finished")
    print(f"[OK] Output saved to: {run_dir}")


if __name__ == "__main__":
    main()
