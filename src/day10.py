from typing import List

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_inside_grid(i_row: int, i_col: int, grid: List[List[int]]) -> bool:
    if i_row < 0 or i_col < 0:
        return False
    if i_row >= len(grid):
        return False
    if i_col >= len(grid[0]):
        return False
    return True


def reachable_summits(i_row: int, i_col: int, grid: List[List[int]]) -> int:
    if grid[i_row][i_col] == 9:
        return [(i_row, i_col)]
    if grid[i_row][i_col] is None:
        return None

    summits = []
    for direction in DIRECTIONS:
        i_row_next = i_row + direction[0]
        i_col_next = i_col + direction[1]
        if not is_inside_grid(i_row_next, i_col_next, grid):
            continue
        if grid[i_row_next][i_col_next] == grid[i_row][i_col] + 1:
            summits += reachable_summits(i_row_next, i_col_next, grid)
    return summits


def total_reachable_summits(grid_strings: List[str]) -> int:
    grid = []
    for row in grid_strings:
        grid += [[int(c) if c.isdigit() else None for c in row]]

    sum = 0
    rating = 0
    for i_row, row in enumerate(grid):
        for i_col, value in enumerate(row):
            if value is not None and value == 0:
                summits = reachable_summits(i_row, i_col, grid)
                sum += len(set(summits))
                rating += len(summits)
    return sum, rating
