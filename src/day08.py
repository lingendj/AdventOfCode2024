from typing import Dict, List, Tuple
import re


def get_antenna_locations(grid: List[str]) -> Dict[str, List[Tuple[int]]]:
    antenna_locations = {}
    for i_row, row in enumerate(grid):
        for i_col, char in enumerate(row):
            if re.match(r'[a-zA-Z0-9]', char):
                if char not in antenna_locations:
                    antenna_locations[char] = [(i_row, i_col)]
                else:
                    antenna_locations[char] += [(i_row, i_col)]
    return antenna_locations


def antinode_is_valid(antinode: Tuple[int], grid: List[str]):
    if antinode[0] < 0 or antinode[1] < 0:
        return False
    if antinode[0] >= len(grid):
        return False
    if antinode[1] >= len(grid[0]):
        return False
    return True


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_num_antinodes(grid: List[str]) -> int:
    antinodes = set()
    grid = [row.strip() for row in grid]
    antennas = get_antenna_locations(grid)
    for _, antenna_locations in antennas.items():
        for i_first_antenna, first_antenna in enumerate(antenna_locations):
            for i_second_antenna in range(i_first_antenna + 1, len(antenna_locations)):
                second_antenna = antenna_locations[i_second_antenna]
                second_to_first = (first_antenna[0] - second_antenna[0],
                                   first_antenna[1] - second_antenna[1])
                first_antinode = (first_antenna[0] + second_to_first[0],
                                  first_antenna[1] + second_to_first[1])
                if antinode_is_valid(first_antinode, grid):
                    antinodes.add(first_antinode)
                second_antinode = (second_antenna[0] - second_to_first[0],
                                   second_antenna[1] - second_to_first[1])
                if antinode_is_valid(second_antinode, grid):
                    antinodes.add(second_antinode)
    return len(antinodes)


def get_num_antinodes_part_two(grid: List[str]) -> int:
    antinodes = set()
    grid = [row.strip() for row in grid]
    antennas = get_antenna_locations(grid)
    for _, antenna_locations in antennas.items():
        for i_first_antenna, first_antenna in enumerate(antenna_locations):
            for i_second_antenna in range(i_first_antenna + 1, len(antenna_locations)):
                second_antenna = antenna_locations[i_second_antenna]
                second_to_first = (first_antenna[0] - second_antenna[0],
                                   first_antenna[1] - second_antenna[1])
                first_antinode = first_antenna
                while antinode_is_valid(first_antinode, grid):
                    antinodes.add(first_antinode)
                    first_antinode = (first_antinode[0] + second_to_first[0],
                                      first_antinode[1] + second_to_first[1])
                second_antinode = second_antenna
                while antinode_is_valid(second_antinode, grid):
                    antinodes.add(second_antinode)
                    second_antinode = (second_antinode[0] - second_to_first[0],
                                       second_antinode[1] - second_to_first[1])
    return len(antinodes)
