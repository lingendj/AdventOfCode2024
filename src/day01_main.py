import numpy as np
from day01 import GetTotalDistance, GetFrequencyDistance


def run():
    file_contents = np.genfromtxt(
        'data/01.txt', delimiter=None, dtype=np.int64)
    distance = get_total_distance(file_contents[:, 0], file_contents[:, 1])
    print(f'Part 1: Total Distance: {distance}')
    print(
        f'Part 2: Frequency Distance: {get_frequency_distance(file_contents[:,0], file_contents[:,1])}')


if __name__ == "__main__":
    run()
