import unittest
# from src.day06 import get_positions
from src.day07 import is_valid, sum_valid_operands

EXAMPLE_INPUT = ['190: 10 19',
                 '3267: 81 40 27',
                 '83: 17 5',
                 '156: 15 6',
                 '7290: 6 8 6 15',
                 '161011: 16 10 13',
                 '192: 17 8 14',
                 '21037: 9 7 18 13',
                 '292: 11 6 16 20']


class TestDay07(unittest.TestCase):
    def test_is_valid_calibration_two(self):
        self.assertTrue(is_valid([10, 19], 190, 0, 0, False))

    def test_is_valid_calibration_three(self):
        self.assertTrue(is_valid([81, 40, 27], 3267, 0, 0, False))

    def test_is_valid_calibration_four_operands(self):
        self.assertTrue(is_valid([11, 6, 16, 20], 292, 0, 0, False))

    def test_is_valid_calibration_false(self):
        self.assertFalse(is_valid([9, 7, 18, 13], 21037, 0, 0, False))

    def test_sum_valid_operands(self):
        self.assertEqual(sum_valid_operands(EXAMPLE_INPUT, False), 3749)

    def test_is_valid_with_concat(self):
        self.assertTrue(is_valid([6, 8, 6, 15], 7290, 0, 0, True))

    def test_sum_valid_operands_with_concat(self):
        self.assertEqual(sum_valid_operands(EXAMPLE_INPUT, True), 11387)
