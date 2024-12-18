from typing import List, Tuple


def is_valid(operands: List[int], expected: int, previous_result: int, index: int, include_concat: bool) -> bool:
    if index == len(operands):
        return previous_result == expected
    if previous_result > expected:
        return False
    valid = (is_valid(operands, expected, previous_result + operands[index], index + 1, include_concat)
             or is_valid(operands, expected, previous_result * operands[index], index + 1, include_concat))
    if include_concat:
        valid = valid or is_valid(operands, expected, int(
            f'{previous_result}{operands[index]}'), index + 1, include_concat)
    return valid


def parse_equation(equation: str) -> Tuple[List[int], int]:
    expected_str, operands_str = equation.strip().split(':')
    expected = int(expected_str)
    operands = [int(s) for s in operands_str.strip().split()]
    return operands, expected


def sum_valid_operands(equations: List[str], include_concat: bool) -> int:
    sum = 0
    for equation in equations:
        operands, expected = parse_equation(equation)
        if is_valid(operands, expected, 0, 0, include_concat):
            sum += expected
    return sum
