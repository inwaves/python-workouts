import json
import os

def print_scores(dirname: str) -> None:
    json_files = [os.path.join(dirname, file) for file in os.listdir(dirname) if "json" in file.split(".")[-1]]
    for filepath in json_files:
        with open(filepath) as fileobj:
            content = json.load(fileobj)
            print(filepath)
            print(compute_stats(content) + "\n")
    return None


def compute_stats(raw_results: list) -> str:
    results = {}
    for entry in raw_results:
        for key, value in entry.items():
            results[key] = results.get(key, []) + [value]
    stats = {k: (min(v), max(v), sum(v)/len(v)) for k, v in results.items()}
    return "\n".join(f"{k}: min={stats[k][0]}, max={stats[k][1]:.2f}, avg={stats[k][2]:.2f}" for k in stats)


def pwd_to_json(input_filename: str, output_filename: str) -> None:
    if not len(input_filename) or not len(output_filename):
        raise ValueError(f"Filename problem: {input_filename=}, {output_filename=}")

    KEYS = ("user", "password", "user_id", "group_id", "user_id_info", "home_directory", "shell")

    entries: list = []
    with open(input_filename) as fileobj:
        for line in fileobj:
            if not line.startswith("#"):
                entries += [dict(list(zip(KEYS, line.split(":"))))]

    with open(output_filename, "w", encoding="utf-8") as fileobj:
        json.dump(entries, fileobj)
