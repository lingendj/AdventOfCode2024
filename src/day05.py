from typing import List


class OrderingRule:
    def __init__(self, rule_str: str):
        nums = rule_str.split('|')
        if len(nums) != 2:
            raise ValueError('Invalid Rule')
        self.first = int(nums[0])
        self.second = int(nums[1])


def is_valid_update(update: List[int], rules: List[OrderingRule]) -> bool:
    for rule in rules:
        if not rule.first in update or not rule.second in update:
            continue
        if update.index(rule.first) > update.index(rule.second):
            return False
    return True


def sum_middle_page_in_valid_rules(update_specs: List[str], rule_specs: List[str]) -> int:
    rules = [OrderingRule(spec) for spec in rule_specs]
    updates = map(lambda s: [int(n) for n in s.split(',')], update_specs)

    sum = 0
    for update in updates:
        if is_valid_update(update, rules):
            sum += update[len(update) // 2]

    return sum


def fix_update(update: List[int], rules: List[OrderingRule]) -> List[int]:
    while not is_valid_update(update, rules):
        for rule in rules:
            if not rule.first in update or not rule.second in update:
                continue
            if update.index(rule.first) > update.index(rule.second):
                first_index = update.index(rule.first)
                second_index = update.index(rule.second)
                tmp = update[first_index]
                update[first_index] = update[second_index]
                update[second_index] = tmp
    return update


def sum_middle_page_in_fixed_invalid_rules(update_specs: List[str], rule_specs: List[str]):
    rules = [OrderingRule(spec) for spec in rule_specs]
    updates = map(lambda s: [int(n) for n in s.split(',')], update_specs)

    sum = 0
    for update in updates:
        if not is_valid_update(update, rules):
            fixed_update = fix_update(update, rules)
            sum += fixed_update[len(fixed_update) // 2]

    return sum
