import unittest
from src.day09 import checksum, checksum_brute_force, checksum_part_two


class TestDay09(unittest.TestCase):
    def test_small_odd_length_incomplete(self):
        # 00...11 ->
        # 0011...
        self.assertEqual(checksum('232'), 5)

    def test_small_odd_length_complete(self):
        # 00..111
        # 00111..
        self.assertEqual(checksum('223'), 9)

    def test_checksum_example(self):
        self.assertEqual(checksum('2333133121414131402'), 1928)

    def test_checksum_brute_force_example(self):
        self.assertEqual(checksum_brute_force('2333133121414131402'), 1928)

    def test_checksum_part_two(self):
        self.assertEqual(checksum_part_two('2333133121414131402'), 2858)
