from day11 import num_stones


def run():
    with open('data/11.txt', 'r') as f:
        input_stones = f.read().strip()

    print(f'Part 1: {num_stones(input_stones, 25)}')
    print(f'Part 2: {num_stones(input_stones, 75)}')


if __name__ == "__main__":
    run()
