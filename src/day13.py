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
        return Machine(a_coeff[0], a_coeff[1], b_coeff[0], b_coeff[1], prize_location[0], prize_location[1])

    def cost(self, prize_offset: int) -> int:
        A = np.array([[self.ax, self.bx],
                      [self.ay, self.by]])
        if np.linalg.matrix_rank(A) != 2:
            raise ValueError("Matrix {A} is not full rank")
        b = np.array([self.prize_x + prize_offset,
                     self.prize_y + prize_offset])
        pushes = [int(n) for n in np.round(np.linalg.solve(A, b))]
        pushes_a = pushes[0]
        pushes_b = pushes[1]
        if (pushes_a * self.ax + pushes_b * self.bx != self.prize_x + prize_offset
                or pushes_a * self.ay + pushes_b * self.by != self.prize_y + prize_offset):
            return None
        return COST_A * pushes_a + COST_B * pushes_b


def tokens_to_win_all_prizes(lines: List[str], prize_offset: int) -> Union[int, None]:
    machine_lines = []
    total_tokens = 0
    for line in lines:
        if len(line) > 0:
            machine_lines += [line]
        if len(machine_lines) == 3:
            machine = Machine.from_string(machine_lines)
            tokens = machine.cost(prize_offset)
            if tokens is not None:
                total_tokens += tokens
            machine_lines = []

    return total_tokens
