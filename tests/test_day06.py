import unittest
# from src.day06 import get_positions
from src.day06 import get_positions, get_num_visited_positions, Guard, get_visited_nodes

TEST_GRID = [
    '....#.....',
    '.........#',
    '..........',
    '..#.......',
    '.......#..',
    '..........',
    '.#..^.....',
    '........#.',
    '#.........',
    '......#...'
]


class TestDay06(unittest.TestCase):
    def test_get_positions(self):
        test_grid = [
            '.#..^.....',
            '........#.',
        ]
        obstacles, guard_position, guard_direction = get_positions(test_grid)
        expected_obstacles = set([
            (0, 1), (1, 8)
        ])
        self.assertEqual(set(obstacles), expected_obstacles)
        self.assertEqual(guard_position, (0, 4))
        self.assertEqual(guard_direction, 0)

    def test_get_num_visitied_positions(self):
        num_positions, _ = get_num_visited_positions(TEST_GRID)
        self.assertEqual(num_positions, 41)

    def test_get_num_visited_positions_loop(self):
        grid = [
            '.#......',
            '.......#',
            '.^......',
            '#.......',
            '......#.',
        ]
        obstacles_list, guard_position, guard_direction_index = get_positions(
            grid)
        obstacles = set(obstacles_list)
        guard = Guard(guard_position, guard_direction_index,
                      len(grid), len(grid[0]))
        _, has_loop = get_visited_nodes(guard, obstacles)
        self.assertTrue(has_loop)

    def test_get_num_visited_positions_loop_example(self):
        grid = [
            '....#.....',
            '.........#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#.#^.....',
            '........#.',
            '#.........',
            '......#...'
        ]
        obstacles_list, guard_position, guard_direction_index = get_positions(
            grid)
        obstacles = set(obstacles_list)
        guard = Guard(guard_position, guard_direction_index,
                      len(grid), len(grid[0]))
        _, has_loop = get_visited_nodes(guard, obstacles)
        self.assertTrue(has_loop)

    def test_get_num_visited_positions_no_loop(self):
        grid = [
            '....#.....',
            '.........#',
            '..........',
            '..#.......',
            '...#...#..',
            '..........',
            '.#..^.....',
            '........#.',
            '#.........',
            '......#...'
        ]
        obstacles_list, guard_position, guard_direction_index = get_positions(
            grid)
        obstacles = set(obstacles_list)
        guard = Guard(guard_position, guard_direction_index,
                      len(grid), len(grid[0]))
        _, has_loop = get_visited_nodes(guard, obstacles)
        self.assertFalse(has_loop)

    def test_num_loop_obstacles(self):
        _, num_loop_obstacles = get_num_visited_positions(TEST_GRID)
        self.assertEqual(num_loop_obstacles, 6)
