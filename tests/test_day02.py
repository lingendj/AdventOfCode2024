import unittest
from src import day02


class TestDay02(unittest.TestCase):
    def test_is_safe_decreasing_safe(self):
        self.assertTrue(day02.is_safe([7, 6, 4, 2, 1]))

    def test_is_safe_increasing_safe(self):
        self.assertTrue(day02.is_safe([1, 3, 6, 7, 9]))

    def test_is_safe_unsafe_increase_too_large(self):
        self.assertFalse(day02.is_safe([1, 2, 7, 8, 9]))

    def test_is_safe_unsafe_decrease_too_large(self):
        self.assertFalse(day02.is_safe([9, 7, 6, 2, 1]))

    def test_is_safe_unsafe_non_monotonic(self):
        self.assertFalse(day02.is_safe([1, 3, 2, 4, 5]))

    def test_is_safe_unsafe_repeated_value(self):
        self.assertFalse(day02.is_safe([8, 6, 4, 4, 1]))

    def test_safe_count_example(self):
        reports = [[7, 6, 4, 2, 1],
                   [1, 3, 6, 7, 9],
                   [1, 2, 7, 8, 9],
                   [9, 7, 6, 2, 1],
                   [1, 3, 2, 4, 5],
                   [8, 6, 4, 4, 1]]
        self.assertEqual(day02.safe_count(reports), 2)

    def test_is_safe_dampener_decreasing_safe(self):
        self.assertTrue(day02.is_safe_with_dampener([7, 6, 4, 2, 1]))

    def test_is_safe_dampener_increasing_safe(self):
        self.assertTrue(day02.is_safe_with_dampener([1, 3, 6, 7, 9]))

    def test_is_safe_dampener_unsafe_increase_too_large(self):
        self.assertFalse(day02.is_safe_with_dampener([1, 2, 7, 8, 9]))

    def test_is_safe_dampener_unsafe_decrease_too_large(self):
        self.assertFalse(day02.is_safe_with_dampener([9, 7, 6, 2, 1]))

    def test_is_safe_dampener_safe_non_monotonic(self):
        self.assertTrue(day02.is_safe_with_dampener([1, 3, 2, 4, 5]))

    def test_is_safe_dampener_safe_repeated_value(self):
        self.assertTrue(day02.is_safe_with_dampener([8, 6, 4, 4, 1]))

    def test_safe_count_example(self):
        reports = [[7, 6, 4, 2, 1],
                   [1, 3, 6, 7, 9],
                   [1, 2, 7, 8, 9],
                   [9, 7, 6, 2, 1],
                   [1, 3, 2, 4, 5],
                   [8, 6, 4, 4, 1]]
        self.assertEqual(day02.safe_count_with_dampener(reports), 4)
