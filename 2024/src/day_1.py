from pathlib import Path


def load_data(data_path):
    l_list = []
    r_list = []
    with open(data_path, newline="", encoding="utf-8") as f:
        for line in f:
            left, right = line.split("   ")
            l_list.append(int(left))
            r_list.append(int(right))
    return l_list, r_list


def compute_total_distance(l_list, r_list):
    return sum(abs(l - r) for l, r in zip(sorted(l_list), sorted(r_list)))


def main():
    l, r = load_data(Path(__file__).parent / "day_1_data.txt")
    result = compute_total_distance(l, r)
    print(result)


if __name__ == "__main__":
    main()
