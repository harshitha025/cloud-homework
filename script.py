import csv
from collections import defaultdict

INPUT_FILE = "data.csv"
OUTPUT_FILE = "output.txt"

def process_data(file_path):
    totals = defaultdict(float)

    try:
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                key = row.get("category", "unknown")
                value = float(row.get("amount", 0))
                totals[key] += value

    except FileNotFoundError:
        print("Input file not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

    return totals


def write_output(results):
    if results is None:
        return

    with open(OUTPUT_FILE, "w") as f:
        for key, value in results.items():
            line = f"{key}: {value}\n"
            f.write(line)

    print(f"Results written to {OUTPUT_FILE}")


def main():
    print("Starting data processing...")

    results = process_data(INPUT_FILE)
    write_output(results)

    print("Done.")


if __name__ == "__main__":
    main()