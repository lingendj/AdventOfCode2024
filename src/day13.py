from dataclasses import dataclass
from typing import List, Union
import re
import numpy as np

COST_A = 3
COST_B = 1


@dataclass
class Machine:
    ax: int
    ay: int
    bx: int
    by: int
    prize_x: int
    prize_y: int

    @staticmethod
    def from_string(lines: list[str]):
        a_coeff = None
        b_coeff = None
        prize_location = None
        for line in lines:
            if line.startswith("Button A"):
                a_coeff = [int(s) for s in re.findall(r'[0-9]+', line)]

            elif line.startswith("Button B"):
                b_coeff = [int(s) for s in re.findall(r'[0-9]+', line)]
            elif line.startswith("Prize"):
                prize_location = [int(s) for s in re.findall(r'[0-9]+', line)]
        if a_coeff is None or b_coeff is None or prize_location is None:
            raise ValueError(f'Could not parse machine lines {lines}')
        return Machine(a_coeff[0], a_coeff[1