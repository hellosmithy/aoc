from itertools import pairwise
from pathlib import Path


def load_data(data_path):
    """Load data from the given path."""
    reports = []
    with open(data_path, newline="", encoding="utf-8") as f:
        for line in f:
            reports.append([int(x) for x in line.strip().split(" ")])
    return reports


def get_direction(a: int, b: int) -> str:
    """Get the direction between two numbers."""
    if a < b:
        return "↗"
    elif a > b:
        return "↘"
    else:
        return "→"


def is_too_fast(a: int, b: int) -> bool:
    """Check if the movement between two numbers is too fast."""
    movement = abs(a - b)
    return movement < 1 or movement > 3


def is_safe_pair(a: int, b: int, direction: str) -> bool:
    """Check if the pair (a, b) is safe."""
    match (direction, get_direction(a, b)):
        case ("↗", "↗") | ("↘", "↘"):
            return not is_too_fast(a, b)
        case _:
            return False  # direction changed


def compute_num_safe_reports(reports):
    """Count the number of safe reports."""
    safe_count = 0
    for report in reports:
        (fst, snd), *rest = pairwise(report)
        initial_direction = get_direction(fst, snd)

        if not is_safe_pair(fst, snd, initial_direction):
            continue  # first pair is unsafe

        if any(not is_safe_pair(a, b, initial_direction) for a, b in rest):
            continue  # found an unsafe pair

        safe_count += 1
        print(f"Safe report: {report}")

    return safe_count


def main():
    reports = load_data(Path(__file__).parent / "day_2_data.txt")
    num_safe_reports = compute_num_safe_reports(reports)
    print(
        f"""
        Number of Safe Reports: {num_safe_reports}
        """
    )


if __name__ == "__main__":
    main()
