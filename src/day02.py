from typing import List
import numpy as np


def is_safe(report: List[int]) -> bool:
    diff = np.diff(report)
    if not np.all(diff > 0) and not np.all(diff < 0):
        return False
    diff_magnitude = np.abs(diff)
    return np.all(np.logical_and(diff_magnitude >= 1, diff_magnitude <= 3))


def is_safe_with_dampener(report: List[int]) -> bool:
    if is_safe(report):
        return True
    # The reports are all very short, so use a brute force solution for simplicity.
    for i in range(len(report)):
        sublist = [report[j] for j in range(len(report)) if j != i]
        if is_safe(sublist):
            return True
    return False


def safe_count(reports: List[List[int]]) -> int:
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


def safe_count_with_dampener(reports: List[List[int]]) -> int:
    count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            count += 1
    return count
