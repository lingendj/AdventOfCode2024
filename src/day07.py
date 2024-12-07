from typing import List, Tuple
"""
190 / 10 = 19
190 - 19 = 171


3267
divide by 81: 40 R 27
subtract 81 - 3816 / 40 95 R 16

             11
          +6   *6
         17     66
      *16 +16  *16 +16
     272  33   x .   82
    +20
   292

7290
                    6
               +8   *8    ||8
               14   48     68
"""


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
