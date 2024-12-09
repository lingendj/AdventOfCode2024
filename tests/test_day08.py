import unittest
from src.day08 import get_num_antinodes, get_num_antinodes_part_two

EXAMPLE_GRID = ['............',
                '........0...',
                '.....0......',
                '.......0....',
                '....0.......',
                '......A.....',
                '............',
                '............',
                '........A...',
                '.........A..',
                '............',
                '............']


class TestDay08(unittest.TestCase):
    def test_get_num_antinodes_example(self):
        self.assertEqual(get_num_antinodes(EXAMPLE_GRID), 14)

    def test_get_num_antinodes_part_two_example(self):
        self.assertEqual(get_num_antinodes_part_two(EXAMPLE_GRID), 34)
