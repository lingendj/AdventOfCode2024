from day12 import get_fencing_cost


def main():
    with open('data/12.txt', 'r') as f:
        grid = [l.strip() for l in f.readlines()]

    cost = get_fencing_cost(grid)
    print(f'Part 1: {cost}')


if __name__ == "__main__":
    main()
