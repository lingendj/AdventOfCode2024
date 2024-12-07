from day07 import sum_valid_operands


def run():
    with open('data/07.txt', 'r') as f:
        equations = f.readlines()
    print(f'Part 1: {sum_valid_operands(equations, False)}')
    print(f'Part 2: {sum_valid_operands(equations, True)}')


if __name__ == "__main__":
    run()
