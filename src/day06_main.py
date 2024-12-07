from day06 import get_num_visited_positions


def run():
    with open('data/06.txt', 'r') as f:
        grid = f.readlines()
    num_visited_positions, num_loop_obstacles = get_num_visited_positions(grid)
    print(f'Part 1: {num_visited_positions}')
    print(f'Part 2: {num_loop_obstacles}')


if __name__ == "__main__":
    run()
