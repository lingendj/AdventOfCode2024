import unittest
from src.day05 import sum_middle_page_in_valid_rules, fix_update, OrderingRule

rule_specs = ['47|53',
              '97|13',
              '97|61',
              '97|47',
              '75|29',
              '61|13',
              '75|53',
              '29|13',
              '97|29',
              '53|29',
              '61|53',
              '97|53',
              '61|29',
              '47|13',
              '75|47',
              '97|75',
              '47|61',
              '75|61',
              '47|29',
              '75|13',
              '53|13']


class TestDay05(unittest.TestCase):

    def test_sum_page_in_valid_rules_example_is_correct(self):

        update_specs = ['75,47,61,53,29',
                        '97,61,53,29,13',
                        '75,29,13',
                        '75,97,47,61,53',
                        '61,13,29',
                        '97,13,75,29,47']
        self.assertEqual(sum_middle_page_in_valid_rules(
            update_specs, rule_specs), 143)

    def test_fix_update(self):
        rules = [OrderingRule(spec) for spec in rule_specs]
        self.assertEqual(fix_update([75, 97, 47, 61, 53], rules), [
                         97, 75, 47, 61, 53])
        self.assertEqual(fix_update([61, 13, 29], rules), [61, 29, 13])
        self.assertEqual(fix_update([97, 13, 75, 29, 47], rules), [
                         97, 75, 47, 29, 13])
