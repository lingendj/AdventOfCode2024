import unittest
import numpy as np
from src import day01


class TestDay01(unittest.TestCase):
    def test_get_total_distance_example(self):
        first = np.array([3, 4, 2, 1, 3, 3])
        second = np.array([4, 3, 5, 3, 9, 3])
        self.assertEqual(day01.get_total_distance(first, second), 11)

    def test_get_frequency_distance_example(self):
        first = np.array([3, 4, 2, 1, 3, 3])
        second = np.array([4, 3, 5, 3, 9, 3])
        self.assertEqual(day01.get_frequency_distance(first, second), 31)
