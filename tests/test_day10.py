import unittest
from src.day10 import total_reachable_summits


class TestDay10(unittest.TestCase):
    def test_small_two_trails(self):
        grid = ['...0...',
                '...1...',
                '...2...',
                '6543456',
                '7.....7',
                '8.....8',
                '9.....9']
        self.assertEqual(total_reachable_summits(grid)[0], 2)

    def test_small_four_trailheads(self):
        grid = ['..90..9',
                '...1.98',
                '...2..7',
                '6543456',
                '765.987',
                '876....',
                '987....']
        self.assertEqual(total_reachable_summits(grid)[0], 4)

    def test_small_multiple_zeros(self):
        grid = ['10..9..',
                '2...8..',
                '3...7..',
                '4567654',
                '...8..3',
                '...9..2',
                '.....01']
        self.assertEqual(total_reachable_summits(grid)[0], 3)

    def test_example(self):
        grid = ['89010123',
                '78121874',
                '87430965',
                '96549874',
                '45678903',
                '32019012',
                '01329801',
                '10456732']
        self.assertEqual(total_reachable_summits(grid)[0], 36)

    def test_total_ratings(self):
        grid = ['89010123',
                '78121874',
                '87430965',
                '96549874',
                '45678903',
                '32019012',
                '01329801',
                '10456732']
        self.assertEqual(total_reachable_summits(grid)[1], 81)
