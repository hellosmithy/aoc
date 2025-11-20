from day_1 import compute_total_distance, compute_total_similarity


def test_compute_total_distance():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert compute_total_distance(left, right) == 11


def test_compute_total_similarity():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert compute_total_similarity(left, right) == 31
