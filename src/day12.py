from typing import List, Tuple, Set
from dataclasses import dataclass, field

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def is_inside_grid(i_row: int, i_col: int, grid: List[str]) -> bool:
    if i_row < 0 or i_col < 0:
        return False
    if i_row >= len(grid):
        return False
    if i_col >= len(grid[0]):
        return False
    return True


@dataclass
class Region:
    perimeter: int = 0
    visited: Set[Tuple[int]] = field(default_factory=lambda: set())

    def area(self) -> int:
        return len(self.visited)


def get_region(i_row: int, i_col: int, plant_type: str, region: Region, grid: List[str]) -> Region:
    if not is_inside_grid(i_row, i_col, grid) or grid[i_row][i_col] != plant_type:
        region.perimeter += 1
        return region

    region.visited.add((i_row, i_col))
    for direction in DIRECTIONS:
        i_row_next = i_row + direction[0]
        i_col_next = i_col + direction[1]
        if (i_row_next, i_col_next) not in region.visited:
            region = get_region(i_row_next,
                                i_col_next,
                                plant_type,
                                region,
                                grid)
    return region


def get_fencing_cost(grid: List[str]) -> int:
    visited = set()
    cost = 0
    for i_row in range(len(grid)):
        for i_col in range(len(grid[i_row])):
            if (i_row, i_col) in visited:
                continue
            region = get_region(
                i_row, i_col, grid[i_row][i_col], Region(), grid)
            visited = visited.union(region.visited)
            cost += region.area() * region.perimeter
            # print(f'A region of {grid[i_row][i_col]} with price {region.area()} * {region.perimeter} = {region.area() * region.perimeter}')
    return cost
