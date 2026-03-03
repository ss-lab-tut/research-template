from pathlib import Path
import json
import csv


def main():
    results_dir = Path("results")
    if not results_dir.exists():
        print("[ERR] results/ not found. Run experiments first.")
        return

    metric_files = sorted(results_dir.glob("*/metrics.json"))
    if not metric_files:
        print("[ERR] No metrics.json found under results/*/")
        return

    rows = []
    metric_keys = set()

    for mf in metric_files:
        data = json.loads(mf.read_text(encoding="utf-8"))
        metrics = data.get("metrics", {})
        metric_keys.update(metrics.keys())

        row = {
            "experiment_name": data.get("experiment_name"),
            "group": data.get("group"),
            "variant": data.get("variant"),
            "seed": data.get("seed"),
            "run_dir": data.get("run_dir"),
        }
        for k, v in metrics.items():
            row[k] = v
        rows.append(row)

    # stable column order
    metric_keys = sorted(metric_keys)
    fieldnames = ["experiment_name", "group", "variant", "seed"] + metric_keys + ["run_dir"]

    out_path = results_dir / "summary.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("[OK] Wrote:", out_path)
    print("[OK] Rows:", len(rows))


if __name__ == "__main__":
    main()
