from typing import List, Tuple, Set
import copy

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Guard:
    def __init__(self, position_in, direction_index_in, n_rows, n_cols):
        self._position = position_in
        self._direction_index = direction_index_in
        self._n_rows = n_rows
        self._n_cols = n_cols

    def next(self):
        direction = DIRECTIONS[self._direction_index]
        return (self._position[0] + direction[0],
                self._position[1] + direction[1])

    def right(self):
        direction = DIRECTIONS[(self._direction_index + 1) % len(DIRECTIONS)]
        return (self._position[0] + direction[0],
                self._position[1] + direction[1])

    def advance(self):
        self._position = self.next()

    def turn(self):
        self._direction_index = (self._direction_index + 1) % len(DIRECTIONS)

    def position(self):
        return self._position

    def direction_index(self):
        return self._direction_index

    def is_inside_grid(self):
        return (self.position()[0] >= 0
                and self.position()[1] >= 0
                and self.position()[0] < self._n_rows
                and self.position()[1] < self._n_cols)


def guard_direction_from_character(character: str) -> Tuple[int]:
    if character == '^':
        return 0
    if character == '>':
        return 1
    if character == 'v':
        return 2
    if character == '<':
        return 3
    return None


def get_positions(grid: List[str]):
    obstacles = []
    guard_direction_index = None
    guard_position = None
    for i_row, row in enumerate(grid):
        for i_col, char in enumerate(row):
            if char == '#':
                obstacles += [(i_row, i_col)]
            elif guard_direction_from_character(char) is not None:
                guard_direction_index = guard_direction_from_character(char)
                guard_position = (i_row, i_col)
    return obstacles, guard_position, guard_direction_index


def get_visited_nodes(guard: Guard, obstacles: Set[Tuple[int]]):
    visited = set()
    turn_nodes = set()
    has_loop = False
    while guard.is_inside_grid() and not has_loop:
        visited.add(guard.position())
        while guard.next() in obstacles:
            if (guard.position(), guard.direction_index()) in turn_nodes:
                # print(f'found loop at position: {guard.position()}')
                has_loop = True
                break
            turn_nodes.add((guard.position(), guard.direction_index()))
            guard.turn()
        guard.advance()
    return visited, has_loop


def get_num_visited_positions(grid: List[str]):
    obstacles_list, guard_position, guard_direction_index = get_positions(grid)
    obstacles = set(obstacles_list)
    guard = Guard(guard_position, guard_direction_index,
                  len(grid), len(grid[0]))
    visited, _ = get_visited_nodes(guard, obstacles)

    # print(f'visited: {visited}')

    loop_obstacles = set()
    for node in visited:
        if node == guard_position:
            continue
        guard = Guard(guard_position, guard_direction_index,
                      len(grid), len(grid[0]))
        # print(f'union:{obstacles.union(set([node]))}')
        _, has_loop = get_visited_nodes(guard, obstacles.union(set([node])))
        # print(f'Checking for loop with new obstacle {node}: {has_loop}')
        if has_loop:
            loop_obstacles.add(node)

    return len(visited), len(loop_obstacles)
