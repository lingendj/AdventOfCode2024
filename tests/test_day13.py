import unittest
from src.day13 import tokens_to_win_all_prizes

class TestDay13(unittest.TestCase):
    def test_has_solution(self):
        lines = ['Button A: X+94, Y+34',
                 'Button B: X+22, Y+67',
                 'Prize: X=8400, Y=5400']
        self.assertEqual(tokens_to_win_all_prizes(lines, 0), 280)

    def test_example(self):
        lines = ['Button A: X+94, Y+34',
                'Button B: X+22, Y+67',
                'Prize: X=8400, Y=5400',
                '',
                'Button A: X+26, Y+66',
                'Button B: X+67, Y+21',
                'Prize: X=12748, Y=12176',
                '',
                'Button A: X+17, Y+86',
                'Button B: X+84, Y+37',
                'Prize: X=7870, Y=6450',
                '',
                'Button A: X+69, Y+23',
                'Button B: X+27, Y+71',
                'Prize: X=18641, Y=10279']
        self.assertEqual(tokens_to_win_all_prizes(lines, 0), 480)

    def test_has_solution_part_two(self):
        lines = ['Button A: X+26, Y+66',
                 'Button B: X+67, Y+21',
                 'Prize: X=12748, Y=12176']
        self.assertEqual(tokens_to_win_all_prizes(lines, 10000000000000), 459236326669)