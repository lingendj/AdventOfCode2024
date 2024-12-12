import unittest
from src.day11 import num_stones


class TestDay11(unittest.TestCase):
    def test_example_six_blinks(self):
        self.assertEqual(num_stones('125 17', 6), 22)

    def test_example_twenty_two_blinks(self):
        self.assertEqual(num_stones('125 17', 25), 55312)
