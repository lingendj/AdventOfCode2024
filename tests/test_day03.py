import unittest
from src.day03 import get_commands, get_product, sum_of_product, get_commands_and_instructions, sum_of_product_with_instructions

TEST_INPUT = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
TEST_INPUT_PART_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


class TestDay03(unittest.TestCase):
    def test_get_commands(self):
        expected = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
        self.assertEqual(get_commands(TEST_INPUT), expected)

    def test_get_product_valid_command(self):
        self.assertEqual(get_product('mul(2,4)'), 8)

    def test_get_products_invalid_command(self):
        with self.assertRaises(ValueError):
            get_product('mul(2)')

    def test_total_product(self):
        self.assertEqual(sum_of_product(TEST_INPUT), 161)

    def test_get_commands_and_instructions(self):
        expected = ['mul(2,4)',
                    "don't()",
                    'mul(5,5)',
                    'mul(11,8)',
                    'do()',
                    'mul(8,5)']
        self.assertEqual(get_commands_and_instructions(
            TEST_INPUT_PART_2), expected)

    def test_sum_of_product_with_instructions(self):
        self.assertEqual(
            sum_of_product_with_instructions(TEST_INPUT_PART_2), 48)
