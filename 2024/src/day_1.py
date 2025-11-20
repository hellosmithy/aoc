from collections import Counter
from pathlib import Path


def load_data(data_path):
    """Load data from the given path."""
    l_list = []
    r_list = []
    with open(data_path, newline="", encoding="utf-8") as f:
        for line in f:
            left, right = line.split("   ")
            l_list.append(int(left))
            r_list.append(int(right))
    return l_list, r_list


def count_occurrences(seq):
    """Return a dict mapping value -> count for seq. See: https://realpython.com/python-counter/"""
    return dict(Counter(seq))


def compute_total_distance(l_list, r_list):
    """Compute the total distance between two lists."""
    return sum(abs(l - r) for l, r in zip(sorted(l_list), sorted(r_list)))


def compute_total_similarity(l_list, r_list):
    """Compute the total similarity between two lists."""
    r_counts = count_occurrences(r_list)
    total_similarity = 0
    for l in l_list:
        total_similarity += l * r_counts.get(l, 0)
    return total_similarity


def main():
    l, r = load_data(Path(__file__).parent / "day_1_data.txt")
    total_distance = compute_total_distance(l, r)
    total_similarity = compute_total_similarity(l, r)
    print(
        f"""
        Total Distance: {total_distance}
        Total Similarity: {total_similarity}
        """
    )


if __name__ == "__main__":
    main()
