from day08 import get_num_antinodes, get_num_antinodes_part_two


def run():
    with open('data/08.txt', 'r') as f:
        grid = f.readlines()

    print(f'Part 1: {get_num_antinodes(grid)}')
    print(f'Part 2: {get_num_antinodes_part_two(grid)}')


if __name__ == "__main__":
    run()
