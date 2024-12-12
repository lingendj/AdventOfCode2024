from day11 import num_stones
import time


def run():
    with open('data/11.txt', 'r') as f:
        input_stones = f.read().strip()

    print(f'Part 1: {num_stones(input_stones, 25)}')
    start_time = time.time()
    result = num_stones(input_stones, 75)
    end_time = time.time()
    print(f'Part 2: {result}')
    print(f'Part 2 time: {(end_time - start_time)*1000}ms')


if __name__ == "__main__":
    run()
