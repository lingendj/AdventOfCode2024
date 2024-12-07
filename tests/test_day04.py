import unittest
from src.day04 import word_matches, word_search_count, kernel_matches, num_kernel_matches


class TestDay04(unittest.TestCase):
    def test_word_matches_horizontal_forward_true(self):
        grid = ["XMAS"]
        result = word_matches("XMAS", 0, 0, 1, 0, grid)
        self.assertTrue(result)

    def test_word_matches_horizontal_forward_not_match(self):
        grid = ["XMAA"]
        result = word_matches("XMAS", 0, 0, 1, 0, grid)
        self.assertFalse(result)

    def test_word_matches_horizontal_forward_end(self):
        grid = ["XMA"]
        result = word_matches("XMAS", 0, 0, 1, 0, grid)
        self.assertFalse(result)

    def test_word_matches_horizontal_backward_true(self):
        grid = ["SAMX"]
        result = word_matches("XMAS", 0, 3, -1, 0, grid)
        self.assertTrue(result)

    def test_word_matches_horizontal_backward_false_end(self):
        grid = ["AMX"]
        result = word_matches("XMAS", 0, 2, -1, 0, grid)
        self.assertFalse(result)

    def test_word_search_count(self):
        grid = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"]
        self.assertEqual(word_search_count("XMAS", grid), 18)

    def test_kernel_matches_true(self):
        grid = ["MXS",
                "XAX",
                "MXS"]
        kernel = ["M.S",
                  ".A.",
                  "M.S"]
        self.assertTrue(kernel_matches(kernel, 0, 0, grid))

    def test_kernel_matches_false_no_match(self):
        grid = ["MXS",
                "XAX",
                "MXS"]
        kernel = ["M.S",
                  ".Y.",
                  "M.S"]
        self.assertFalse(kernel_matches(kernel, 0, 0, grid))

    def test_kernel_matches_false_edge(self):
        grid = ["MXS",
                "XAX",
                "MXS"]
        kernel = ["M.S",
                  ".A.",
                  "M.S"]
        self.assertFalse(kernel_matches(kernel, 1, 0, grid))

    def test_num_kernel_matches(self):
        grid = [".M.S......",
                "..A..MSMS.",
                ".M.S.MAA..",
                "..A.ASMSM.[]",
                ".M.S.M....",
                "..........",
                "S.S.S.S.S.",
                ".A.A.A.A..",
                "M.M.M.M.M.",
                ".........."]
        kernels = [["M.S",
                   ".A.",
                    "M.S"],
                   ["S.S",
                   ".A.",
                    "M.M"],
                   ["M.M",
                   ".A.",
                    "S.S"],
                   ["S.M",
                   ".A.",
                    "S.M"]]
        self.assertEqual(num_kernel_matches(kernels, grid), 9)
