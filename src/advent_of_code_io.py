from typing import List


def read_as_lists_of_integers(filename: str) -> List[List[int]]:
    with open(filename, 'r') as file:
        lines = file.readlines()

    rows = []
    for line in lines:
        rows += [[int(val) for val in line.strip().split()]]
    return rows
