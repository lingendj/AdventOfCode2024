import re
from typing import List, Tuple
from functools import reduce

ENABLE_COMMAND = "do()"
DISABLE_COMMAND = "don't()"


def get_commands(s: str) -> List[str]:
    return re.findall(r'mul\(\d+,\d+\)', s)


def get_product(command: str) -> int:
    number_strings = re.findall(r'\d+', command)
    if len(number_strings) != 2:
        raise ValueError(f'Invalid command: {command}')
    operands = map(int, number_strings)
    return reduce(lambda n, m: n * m, operands)


def sum_of_product(text: str) -> int:
    mul_results = map(get_product, get_commands(text))
    return reduce(lambda x, y: x + y, mul_results)


def get_commands_and_instructions(s: str) -> List[str]:
    return re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', s)


def sum_of_product_with_instructions(text: str) -> int:
    enabled = True
    sum = 0
    for token in get_commands_and_instructions(text):
        if token == ENABLE_COMMAND:
            enabled = True
        elif token == DISABLE_COMMAND:
            enabled = False
        elif enabled:
            sum += get_product(token)
    return sum
