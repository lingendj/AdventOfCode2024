from typing import List, Dict
from math import log10
from collections import defaultdict


def apply_rules(value: int) -> List[int]:
    if value == 0:
        return [1]
    string_value = str(value)
    num_digits = int(log10(value)) + 1
    if int(num_digits) % 2 == 0:
        middle_index = num_digits // 2
        first_half = int(value // 10 ** (num_digits // 2))
        return [first_half,
                value - first_half * 10 ** (num_digits // 2)]
    return [value * 2024]


def blink_stones(stones_before: Dict[int, int]) -> Dict[int, int]:
    stones_after = {}
    for value, count in stones_before.items():
        values_after = apply_rules(value)
        for value_after in values_after:
            if value_after not in stones_after:
                stones_after[value_after] = count
            else:
                stones_after[value_after] += count
    return stones_after


def num_stones(serialized_stones: str, num_blinks: int) -> int:
    stone_values = [int(i) for i in serialized_stones.strip().split()]
    stones = {}
    for value in stone_values:
        if value not in stones:
            stones[value] = 1
        else:
            stones[value] += 1
    for i in range(num_blinks):
        stones = blink_stones(stones)
    sum = 0
    for count in stones.values():
        sum += count
    return sum
