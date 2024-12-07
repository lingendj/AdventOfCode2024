from day05 import sum_middle_page_in_valid_rules, sum_middle_page_in_fixed_invalid_rules


def run():
    with open('data/05.txt', 'r') as f:
        lines = f.readlines()

    rule_specs = []
    update_specs = []
    for line in lines:
        if '|' in line:
            rule_specs += [line]
        elif ',' in line:
            update_specs += [line]

    sum = sum_middle_page_in_valid_rules(update_specs, rule_specs)
    print(f'Part 1: {sum}')
    sum_fixed = sum_middle_page_in_fixed_invalid_rules(
        update_specs, rule_specs)
    print(f'Part 2: {sum_fixed}')


if __name__ == "__main__":
    run()
