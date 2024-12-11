from day10 import total_reachable_summits


def run():
    with open('data/10.txt', 'r') as f:
        grid = [l.strip() for l in f.readlines()]

    num_summits, ratings = total_reachable_summits(grid)
    print(f'Part 1: {num_summits}')
    print(f'Part 2: {ratings}')


if __name__ == "__main__":
    run()
