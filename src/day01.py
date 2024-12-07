from collections import defaultdict
from numpy.typing import NDArray
import numpy as np


def get_total_distance(first: NDArray[np.int64], second: NDArray[np.int64]) -> int:
    first_sorted = np.sort(first)
    second_sorted = np.sort(second)
    return int(np.linalg.norm(first_sorted - second_sorted, ord=1))


def get_frequency_distance(left: NDArray[np.int64], right: NDArray[np.int64]) -> int:
    right_frequencies = defaultdict(int)
    for right_value in right:
        right_frequencies[right_value] += 1

    score = 0
    for left_value in left:
        score += left_value * right_frequencies[left_value]

    return score
